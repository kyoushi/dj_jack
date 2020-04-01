from flask import Flask, request, Response
import getSong
import playVLC
import json

app = Flask(__name__)  # create the Flask app


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for playing Google Music.</p>'''


@app.route('/api/v1/play_music', methods=['POST'])
def play_song():
    content = request.json
    try:
        print(json.dumps(content, indent=4))
        content = content['queryResult']['parameters']['action'].strip('"')
        print(content)
        if content == 'stop':
            print(content)
            playVLC.stop_song(playVLC.player)
            response_text = "{'payload':{'google':{'expectUserResponse':false,'richResponse':{'items':[{'simpleResponse':{'textToSpeech':'OK! music stopped'}}]}}}}"
    except:
        song = content['queryResult']['parameters']['song'][0].strip('"')
        print(song)
        track = getSong.ask_for_song(song)
        stream_url = track[2]
        player = playVLC.play_song(stream_url)
        response_text = "{'payload':{'google':{'expectUserResponse':true,'richResponse':{'items':[{'simpleResponse':{'textToSpeech':'OK! playing "+track[0]+" by "+track[1]+"'}}]}}}}"

        print(response_text)

    # song = json.dumps((content['queryResult']['parameters']['song'][0]), indent=4)
    # print(song)
    # print(content['queryResult'])
    # song = content['song']

    # song = song.replace('"', '')
    # stream_url = getSong.ask_for_song(song)
    # player = playVLC.play_song(stream_url)

    return Response(response_text, status=201, mimetype='application/json')


@app.route('/api/v1/action', methods=['POST'])
def player_action():
    content = request.json

    playVLC.stop_song(playVLC.player)

    return Response("{'Status':'Success'}", status=201, mimetype='application/json')


app.run(debug=True, port=80)  # run app in debug mode on port 5000
