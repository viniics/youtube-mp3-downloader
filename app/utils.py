import yt_dlp
import os
from dotenv import load_dotenv
load_dotenv()

caminho_ffmpeg = os.getenv('FFMPEG_LOCATION')
if not caminho_ffmpeg:
    raise EnvironmentError("Configure o caminho do FFmpeg no arquivo .env")


def baixar_video_youtube(url, pasta_destino="./audioTest"):
    try:
        opcoes_do_download = {
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
            'format' : 'bestaudio',
            'ffmpeg_location': caminho_ffmpeg,
            'postprocessors':[{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec': 'mp3'
            }]
        }
        
        with yt_dlp.YoutubeDL(opcoes_do_download) as ydl:
            info = ydl.extract_info(url, download=True)
            caminho_arquivo = ydl.prepare_filename(info)
            print(f"Download concluído: {caminho_arquivo}")
            return caminho_arquivo
    except Exception as e:
        print(f"{e}")
