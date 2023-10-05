from flask import Flask, request, jsonify, render_template
from chatterbot import ChatBot
from difflib import SequenceMatcher

CONFIANCA_MINIMA = 0.65

app = Flask(__name__)
robo = None

def comparar_mensagens(mensagem_digitada, mensagem_possivel):
    confianca = 0.0

    digitada = mensagem_digitada.text
    candidata = mensagem_possivel.text
    if digitada and candidata:
        confianca = SequenceMatcher(None,
                                    digitada,
                                    candidata)
        confianca = round(confianca.ratio(), 2)

    return confianca


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resposta', methods=['POST'])
def obter_resposta():
    data = request.get_json()
    mensagem = data['message']
    
    resposta = robo.get_response(mensagem.lower())
    confidence = resposta.confidence

    if confidence >= CONFIANCA_MINIMA:
        response = {
            'response': resposta.text,
            'confidence': confidence
        }
    else:
        response = {
            'response': "Ainda não sei responder isso. Tente escrever outra coisa: ",
            'confidence': confidence
        }
    
    return jsonify(response)


if __name__ == "__main__":
    robo = ChatBot("Robo Nata",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])

    app.run()
