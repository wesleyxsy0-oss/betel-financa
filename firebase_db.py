import firebase_admin
from firebase_admin import credentials, firestore

# Baixe o arquivo JSON do Firebase e coloque o caminho aqui
try:
    cred = credentials.Certificate("betel-financa-firebase-adminsdk.json")
    firebase_admin.initialize_app(cred)
except:
    firebase_admin.initialize_app()

db = firestore.client()

def salvar_mensagem(usuario, mensagem):
    doc = {
        'numero': usuario,
        'mensagem': mensagem,
        'timestamp': firestore.SERVER_TIMESTAMP
    }
    db.collection('mensagens').add(doc)
