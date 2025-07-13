from bs4 import BeautifulSoup
import requests
# importing vlc module
import vlc
import time
# importing pafy module
import pafy

def findInDictionary(text):

	
	#Create a youtube video link 
	youtube_link = "https://www.youtube.com/watch?v=LbxSV8unB9M"
	
	# creating pafy object of the video
	video = pafy.new(youtube_link)
	
	# getting best stream
	best = video.getbest()
	media = vlc.MediaPlayer(best.url)
	media.play()
	'''playurl = best.url
	print('playurl')
	# creating vlc media player object
	Instance = vlc.Instance()
	print('Instance')
	player = Instance.media_player_new()
	Media = Instance.media_new(playurl)
	print('play')
	Media.get_mrl()
	player.set_media(Media)
	# start playing video
	player.play()
	print('actual play')
	time.sleep(5)

	Instance.vlm_stop_media(playurl)'''

findInDictionary('afternoon')