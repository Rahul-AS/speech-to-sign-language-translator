import mysql.connector as con
import getpass
import datetime 
import pafy
import vlc
import time


mycon= con.connect(host='localhost',user='root', passwd="Password123",database='sign_language')

cur=mycon.cursor(buffered=True)

def findInDictionary(word):
    query ='SELECT link FROM sign WHERE word = %s' 
    cur.execute(query,(word,))

    count = 1
    for x in cur:
        count = 0
        youtube_link = x[0]
        
        video = pafy.new(youtube_link)

        # getting best stream
        best = video.getbest()
        playurl = best.url

        # creating vlc media player object
        Instance = vlc.Instance()
        player = Instance.media_player_new()
        Media = Instance.media_new(playurl)
        
        Media.get_mrl()
        player.set_media(Media)

        # start playing video
        player.play()
        time.sleep(8)
        

        #Instance.vlm_stop_media(playurl)
    if count:
        return 1