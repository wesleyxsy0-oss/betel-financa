from flask import Flask, request, jsonify
import whatsapp_api
import ia_resposta
import firebase_db
import funcoes_financeiras

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    mensagem = data['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    numero_usuario = data['entry'][0]['changes'][0]['value']['messages'][0]['from']

    # Salvar mensagem no Firebase
    firebase_db.salvar_mensagem(numero_usuario, mensagem)

    # Verificar tipo de mensagem
    if "gastei" in mensagem.lower():
        resposta = funcoes_financeiras.calcular_gastos(mensagem)
    elif "investir" in mensagem.lower():
        resposta = funcoes_financeiras.sugerir_investimento(mensagem)
    elif "dica" in mensagem.lower():
        resposta = funcoes_financeiras.dica_do_dia()
    else:
        resposta = ia_resposta.responder_com_ia(mensagem)

    # Enviar resposta
    whatsapp_api.enviar_mensagem(numero_usuario, resposta)

    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True)
