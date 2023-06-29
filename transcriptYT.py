#pip install youtube_transcript_api
#import youtube-transcript-api

from youtube_transcript_api import YouTubeTranscriptApi

YouTubeTranscriptApi.get_transcript("Z6nkEZyS9nA")
a =YouTubeTranscriptApi.get_transcript('Z6nkEZyS9nA')
message=""
def trans():
    for i in a:
        #b=(i['text'])
        print(i['text'])
    

trans()
#print("HEllo")
#print(a)