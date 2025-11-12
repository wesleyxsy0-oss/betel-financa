import openai

# Configure sua chave aqui depois
openai.api_key = "COLE_SUA_CHAVE_OPENAI_AQUI"

def responder_com_ia(mensagem):
    try:
        prompt = f"""
        Você é betel financa, um assistente financeiro pessoal amigável, claro e prático.
        O usuário disse: "{mensagem}"
        Dê uma resposta útil, com dicas simples, sem jargões.
        Se for sobre gastos, calcule porcentagens.
        Se for sobre investimentos, sugira opções seguras.
        """
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )
        return resposta.choices[0].message['content']
    except Exception as e:
        return "Desculpe, estou com problemas técnicos. Tente novamente mais tarde."
