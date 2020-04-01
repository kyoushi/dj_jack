from gmusicapi import Mobileclient


def ask_for_song(song):
    api = Mobileclient()
    # mm.perform_oauth('C:\\Users\\mitsu\\Documents\\Python\\projects\\gmusicapi-develop\\oauth.cred')
    api.oauth_login(Mobileclient.FROM_MAC_ADDRESS,
                    'oauth.cred')
    api.login

    songs = api.search(song, 2)

    # print(json.dumps((library), indent=4))

    title = songs['song_hits'][0]['track']['title']
    artist = songs['song_hits'][0]['track']['artist']
    song_id = songs['song_hits'][0]['track']['storeId']
    stream_url = api.get_stream_url(song_id)

    track = [title, artist, stream_url]

    api.logout()

    return track


# print(ask_for_song('toto')[2])
