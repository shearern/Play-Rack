import vlc
import os
from ctypes import CFUNCTYPE, c_char, c_void_p, c_uint, c_long
from time import sleep

callbackmethod = vlc.callbackmethod

class MyPlayback(vlc.AudioPlayCb):
    def data(self):
        print "HERE"


def callbck(a,b,c,d):
    print 'aa'
    print a
    print b
    print c
    print d
    return 'a'


if __name__ == '__main__':
    os.chdir(r'N:\HR-ITS4-Documents\Projects\PyCharmProjects\Live-Rack\assets')
    filename = 'test_music.mp3'
    inst = vlc.Instance()
    player = inst.media_player_new(filename)

#    CMPFUNC = CFUNCTYPE(c_char, c_void_p, c_void_p, c_uint, c_long)
#    player.audio_set_callbacks(CMPFUNC(callbck),None,None,None,None,None)

#    player.audio_set_callbacks(MyPlayback(),None,None,None,None,None)

    player.play()

    sleep(5)

    print "Closing"