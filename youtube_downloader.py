import yt_dlp
import os

def download_video(url):
    output_path = "videos"

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{output_path}/%(title)s.%(ext)s'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info)

    return video_path