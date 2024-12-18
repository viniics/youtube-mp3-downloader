import yt_dlp
import os
from dotenv import load_dotenv
load_dotenv()

#Busca o caminho para o FFMpeg, que deve ser configurado nas variáveis de ambiente ou num arquivo .env
# No segundo caso, esse arquivo deve ser criado no diretório raíz desse projeto
caminho_ffmpeg = os.getenv('FFMPEG_LOCATION')
if not caminho_ffmpeg:
    raise EnvironmentError("Configure o caminho do FFmpeg no arquivo .env")

# Define onde sera a pasta de destino dos Downloads
# Por padrao: './audio-downloads'
pasta_destino="./audio-downloads"

def baixar_musica(url):
    try:
        # Configuracoes para baixar audio no formato mp3
        # Conforme o projeto for evoluindo, serao adicionadas outras configuracoes 
        # que serao obtidas via requisicao web 
        opcoes_do_download = {
            'outtmpl': f'{pasta_destino}/%(title)s.%(ext)s',
            'format' : 'bestaudio/best',
            'ffmpeg_location': caminho_ffmpeg,
            'postprocessors':[{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality' : '192'
            }]
        }
        
        with yt_dlp.YoutubeDL(opcoes_do_download) as ydl:
            info = ydl.extract_info(url, download=True)
            caminho_arquivo = ydl.prepare_filename(info)
            return caminho_arquivo
    except Exception as e:
        print(f"{e}")
