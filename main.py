from typing import Union
import html
from pydantic import BaseModel
from fastapi import FastAPI, Request,Form
from fastapi.templating import Jinja2Templates
from transcriptYT import trans
from youtube_transcript_api import YouTubeTranscriptApi
from typing import Annotated

import time

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/youtube")
async def read_root(request: Request ):
    a=time.time()
    a=YouTubeTranscriptApi.get_transcript('Z6nkEZyS9nA')
    c=time.time()
    ch=" "
    for i in a:
        ch=ch+i['text']
    b=time.time()
    return {"Transcript":ch,"Time":b-c}
    

 