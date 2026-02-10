import os
import yt_dlp

def downloadVideo(url_fic):
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        options = {
            'format': 'bestvideo',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'sleep_interval': 5,
            'max_sleep_interval': 10,
            'concurrent_fragment_downloads': 1,
        }
        
        with yt_dlp.YoutubeDL(options) as ytdl:
            ytdl.download([url_fic])
            
            
def downloadAudio(url_fic):
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        options = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'sleep_interval': 5,
            'max_sleep_interval': 10,
            'concurrent_fragment_downloads': 1,
        }
        
        with yt_dlp.YoutubeDL(options) as ytdl:
            ytdl.download([url_fic])
            
def downloadVideoAudio(url_fic):
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        
        options = {
            'format': 'bestvideo+bestaudio',
            'merge_output_format': 'mp4',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'noplaylist': True,
            'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)',
            'sleep_interval': 5,
            'max_sleep_interval': 10,
            'concurrent_fragment_downloads': 1,
        }
        
        with yt_dlp.YoutubeDL(options) as ytdl:
            ytdl.download([url_fic])