import vlc

if __name__ == '__main__':

    instance = vlc.Instance()

Python 2.7.10 (default, May 23 2015, 09:40:32) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> imoprt os
SyntaxError: invalid syntax
>>> import os
>>> import vlc
>>> os.chdir(r'N:\HR-ITS4-Documents\Projects\PyCharmProjects\Live-Rack\assets')
>>> filename = 'test_music.mp3')
SyntaxError: invalid syntax
>>> filename = 'test_music.mp3'
>>> inst = vlc.Instance()
>>> inst.media_player_new(filename)
<vlc.MediaPlayer object at 0x03696430>
>>> player = inst.media_player_new(filename)
>>> player.play()
0
>>> player.audio_get_volume()
100
>>> player.audio_set_volume(50)
0
>>> player.audio_set_volume(100)
0
>>> from time import sleep
>>> for i in range(100, 50, step=-10):
	print i



Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    for i in range(100, 50, step=-10):
TypeError: range() takes no keyword arguments
>>> for i in range(100, 50, -10):
	print i


100
90
80
70
60
>>> for i in range(100, 50, -10):
	player.audio_set_volume(i)
	sleep(0.5)


0
0
0
0
0
>>> for i in range(100, 50, -10):
	player.audio_set_volume(i)
	sleep(0.5)


0
0
0
0
0
>>> for i in range(100, 50, -5):
	player.audio_set_volume(i)
	sleep(0.25)


0
0
0
0
0
0
0
0
0
0
>>> for i in range(50, 100, 5):
	player.audio_set_volume(i)
	sleep(0.25)


0
0
0
0
0
0
0
0
0
0
>>> player.has_vout
<bound method MediaPlayer.has_vout of <vlc.MediaPlayer object at 0x03696330>>
>>> player.has_vout()
0L
>>> player.play()
0
>>> player.play()
0
>>> player.stop()
>>> player.play()
0
>>> player.get_length()
140835L
>>> player.set_time(70835)
>>> player.set_time(70835)
>>> player.play()
0
>>> player.stop()
>>> player.play()
0
>>> i2 = vlc.Instance()
>>> p2 = inst.media_player_new(filename)
>>> p2.play()
0
>>> player.pause()
>>> player.play()
0
>>> player.audio_set_volume(50)
0
>>>