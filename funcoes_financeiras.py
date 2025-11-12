import re
import random

def calcular_gastos(mensagem):
    numeros = re.findall(r'\d+', mensagem)
    if numeros:
        valor = int(numeros[0])
        renda_media = 3000
        porcentagem = (valor / renda_media) * 100
        return f"Você gastou R${valor}. Isso representa {porcentagem:.1f}% da sua renda média. 💡 Dica: tente separar 10% para investir."
    return "Me diga quanto você gastou. Ex: 'Gastei R$800'."

def sugerir_investimento(mensagem):
    return "Com esse valor, você pode começar com: 1️⃣ Tesouro Selic (seguro), 2️⃣ CDB de banco grande, 3️⃣ Fundos DI. Quer ajuda para escolher?"

def dica_do_dia():
    dicas = [
        "Pague a si mesmo primeiro: transfira 10% da sua renda para investimento antes de pagar qualquer conta.",
        "Evite usar cartão de crédito para compras por impulso. Espere 24h antes de comprar.",
        "Se tiver dívida com juros acima de 5% ao mês, pague antes de investir.",
        "Crie uma reserva de emergência com pelo menos 6 meses de despesas."
    ]
    return random.choice(dicas)
