from flask import Flask, render_template, request, jsonify, send_file
from utils import baixar_musica
import webbrowser
app = Flask(__name__)
initalized = False
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/baixar_audio', methods=['POST'])
def baixar_audio():
    url = request.form.get('url')
    
    try:
        caminho_arquivo = baixar_musica(url)
        print(f"Arquivo gerado: {caminho_arquivo}")
        return send_file(caminho_arquivo,as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def abrir_navegador():
    webbrowser.open_new("http://127.0.0.1:5000")
    
def initialize():
    abrir_navegador()


if __name__ == '__main__':
    initialize()
    app.run(debug=True)