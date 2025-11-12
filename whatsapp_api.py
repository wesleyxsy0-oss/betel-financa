import requests

def enviar_mensagem(numero, mensagem):
    url = "https://graph.facebook.com/v18.0/SEU_ID_DO_NEGOCIO/messages"
    headers = {
        "Authorization": "Bearer SEU_TOKEN_AQUI",
        "Content-Type": "application/json"
    }
    payload = {
        "messaging_product": "whatsapp",
        "to": numero,
        "type": "text",
        "text": {"body": mensagem}
    }
    try:
        response = requests.post(url, headers=headers, json=payload)
        print(response.json())
    except Exception as e:
        print("Erro ao enviar:", e)
