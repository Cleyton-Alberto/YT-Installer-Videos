import os
import yt_dlp
import asyncio

async def downloadVideo(url_fic, status_text_fic, progress_bar_fic, page_fic):
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')

    def progress_hook(ytdlp_info):
        if ytdlp_info['status'] == 'downloading':
            total = ytdlp_info.get('total_bytes') or ytdlp_info.get("total_bytes_estimate")
            downloaded = ytdlp_info.get("downloaded_bytes", 0)
        
            if total:
                progress = downloaded / total
                progress_bar_fic.value = progress
                status_text_fic.value = 'Loading...'
                page_fic.update()

    options = {
        'progress_hooks': [progress_hook],
        'format': 'bestvideo',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'sleep_interval': 5,
        'max_sleep_interval': 10,
        'concurrent_fragment_downloads': 1,
    }

    await asyncio.to_thread(lambda: yt_dlp.YoutubeDL(options).download([url_fic]))



async def downloadAudio(url_fic, status_text_fic, progress_bar_fic, page_fic):
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    def progress_hook(ytdlp_info):
        if ytdlp_info['status'] == 'downloading':
            total = ytdlp_info.get('total_bytes') or ytdlp_info.get("total_bytes_estimate")
            downloaded = ytdlp_info.get("downloaded_bytes", 0)
        
            if total:
                progress = downloaded / total
                progress_bar_fic.value = progress
                status_text_fic.value = 'Loading...'
                page_fic.update()
    
    options = {
        'progress_hooks': [progress_hook],
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'sleep_interval': 5,
        'max_sleep_interval': 10,
        'concurrent_fragment_downloads': 1,
    }
    
    await asyncio.to_thread(lambda: yt_dlp.YoutubeDL(options).download([url_fic]))



async def downloadVideoAudio(url_fic, status_text_fic, progress_bar_fic, page_fic):
    download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    
    def progress_hook(ytdlp_info):
        if ytdlp_info['status'] == 'downloading':
            total = ytdlp_info.get('total_bytes') or ytdlp_info.get("total_bytes_estimate")
            downloaded = ytdlp_info.get("downloaded_bytes", 0)
        
            if total:
                progress = downloaded / total
                progress_bar_fic.value = progress
                status_text_fic.value = 'Loading...'
                page_fic.update()
    
    options = {
        'progress_hooks': [progress_hook],
        'format': 'bestvideo+bestaudio',
        'merge_output_format': 'mp4',
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        'noplaylist': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
        'sleep_interval': 5,
        'max_sleep_interval': 10,
        'concurrent_fragment_downloads': 1,
    }
    
    await asyncio.to_thread(lambda: yt_dlp.YoutubeDL(options).download([url_fic]))