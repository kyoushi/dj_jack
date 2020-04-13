import time
import os

if os.name == 'nt':
    os.add_dll_directory(r'C:\\Program Files (x86)\\VideoLAN\\VLC')
import vlc


class Song:

    def __init__(self):
        self.player = vlc.MediaPlayer()

    def play_song(self, stream_url):
        self.player = vlc.MediaPlayer(stream_url)
        self.player.play()

    def play_mp3(file_name):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        p = vlc.MediaPlayer(dir_path + '/' + file_name)
        p.play()

    def pause_song(self):
        self.player.pause()

    def stop_song(self):
        self.player.stop()

    # player = play_song('https://r4---sn-vgqsknez.c.doc-0-0-sj.sj.googleusercontent.com/videoplayback?id=37514c1acb1662b2&itag=25&source=skyjam&begin=0&ei=10SBXrTHItmAir4PqtKX-AE&o=03115231551108786426&cmbypass=yes&ratebypass=yes&cpn=hCNL6LhddZHQpag997CHlw&ip=0.0.0.0&ipbits=0&expire=1585530161&sparams=cmbypass,ei,expire,id,initcwndbps,ip,ipbits,itag,mh,mip,mm,mn,ms,mv,mvi,o,pl,ratebypass,source&signature=18F9E9BCE519EEC66331C5A88FD97A3D66DAD31B.2BF3F7A3F39FE575736311AF1E752973ED4D2BEA&key=cms1&initcwndbps=15330&mh=Mb&mip=97.70.1.38&mm=31&mn=sn-vgqsknez&ms=au&mt=1585529964&mv=m&mvi=3&pl=16')
    # time.sleep(10)
    # pause_song(player)
    # time.sleep(10)
    # pause_song(player)
    # time.sleep(10)
    # stop_song(player)
