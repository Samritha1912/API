from fastapi import FastAPI,Request
from youtube_transcript_api import YouTubeTranscriptApi
from datetime import datetime
import uvicorn
import time
#app = FastAPI()

"""
@app.get("/transcript")
def get_transcript(url: str):
    video_id = get_video_id(url)
    method=GET
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        a=time.time()
        text = " ".join([t['text'] for t in transcript])
        b=time.time()
        return {"transcript": text,"time":b-a}
    except Exception as e:
        return {"error": str(e)}


def get_video_id(url):
    # Extract video ID from YouTube URL
    video_id = None
    if "youtube.com/watch?v=" in url:
        video_id = url.split("youtube.com/watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
    return video_id

"""
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def read_form(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/process-url")
async def process_url(request: Request):
    data = await request.json()
    url = data["url"]
    # Process the URL and obtain the transcript of the video
    # ...
    video_id = get_video_id(url)
    #method=GET
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
      
        text = " ".join([t['text'] for t in transcript])
       
        return {"transcript": text}
    except Exception as e:
        return {"error": str(e)}

def get_video_id(url):
    # Extract video ID from YouTube URL
    video_id = None
    if "youtube.com/watch?v=" in url:
        video_id = url.split("youtube.com/watch?v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        video_id = url.split("youtu.be/")[1].split("?")[0]
    return video_id
    