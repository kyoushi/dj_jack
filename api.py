from flask import Flask, request, Response
import getSong
import playVLC
import json

from playVLC import Song

app = Flask(__name__)  # create the Flask app
stream_song = Song()


# RaspberryPI
# https://0lt6bbtf0hbp2knmhts63g.webrelay.io/api/v1/play_music

# Windows10
# https://thbdqxnhzjqwpp432sgi2k.us-west.webrelay.io/api/v1/play_music

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for playing Google Music.</p>'''


@app.route('/api/v1/play_music', methods=['POST'])
def play_song():
    content = request.json
    try:
        print('LOOK! 1')
        print(json.dumps(content, indent=4))
        content = content['queryResult']['parameters']['action'].strip('"')
        if content == 'stop':
            response_text = "{'payload':{'google':{'expectUserResponse':false,'richResponse':{'items':[{'simpleResponse':{'textToSpeech':'OK! music stopped'}}]}}}}"
            stream_song.stop_song()
    except:
        song = content['queryResult']['parameters']['song'][0].strip('"')
        print(song)
        track = getSong.ask_for_song(song)
        stream_url = track[2]
        stream_song.play_song(stream_url)
        response_text = "{'payload':{'google':{'expectUserResponse':true,'richResponse':{'items':[{'simpleResponse':{'textToSpeech':'OK! playing " + \
                        track[0] + " by " + track[1] + "'}}]}}}}"
        print(response_text)

    return Response(response_text, status=201, mimetype='application/json')


app.run(debug=True, port=80)  # run app in debug mode on port 5000
