from flask import Flask, render_template, request, jsonify
from utils import baixar_musica  # Importando a função de download
import webbrowser
# Criando o aplicativo Flask
app = Flask(__name__)

# exibir o formulário
@app.route('/')
def index():
    return render_template('index.html')

# Rota para processar o download de áudio
@app.route('/baixar_audio', methods=['POST'])
def baixar_audio():
    # Receber a URL do formulário
    url = request.form.get('url')
    
    if not url:
        return jsonify({'error': 'URL não fornecida'}), 400
    
    try:
        # Chamar a função de download
        caminho_arquivo = baixar_musica(url)
        return jsonify({'success': True, 'caminho': caminho_arquivo})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def abrir_navegador():
    webbrowser.open_new("http://127.0.0.1:5000")

if __name__ == '__main__':
    abrir_navegador()
    app.run(debug=True)
