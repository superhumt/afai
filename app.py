from fastapi import FastAPI, HTTPException
import yt_dlp

app = FastAPI()

@app.get("/download")
def get_video_link(url: str):
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
        # Google block se bachne ke liye naye headers
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            video_url = info.get('url')
            title = info.get('title')
            
            return {
                "status": "success",
                "title": title,
                "download_link": video_url
            }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/")
def home():
    return {"message": "YouTube Bot API is Running!"}
