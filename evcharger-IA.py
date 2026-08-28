import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

# importações novas para o FastAPI
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

load_dotenv()

#configuração client IA
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

#configuração do comportamento da IA
configuracao_ia = types.GenerateContentConfig(
    system_instruction=(
        "Você é o assistente virtual oficial e especialista técnico da GoodWe "
        "focado em eletromobilidade e carregadores de veículos elétricos (EV Chargers). "
        "Sua única função é tirar dúvidas sobre carregadores GoodWe, potências (AC/DC), "
        "instalação, compatibilidade com carros elétricos, tarifas e agendamentos de recarga. "
        "Se o usuário fizer uma pergunta sobre qualquer outro assunto (como receitas, "
        "política, esportes ou outras marcas que não tenham relação direta), recuse "
        "educadamente a resposta informando que você só pode ajudar com assuntos referentes "
        "à GoodWe e carregadores elétricos."
    ),
    temperature=0.3,
)


#servidor FastAPI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PerguntaRequest(BaseModel):
    pergunta: str

@app.post("/api/chat")
async def responder_chat(dados: PerguntaRequest):
    if not dados.pergunta.strip():
         raise HTTPException(status_code=400, detail="A pergunta não pode estar vazia.")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=dados.pergunta,
            config=configuracao_ia,
        )
        return {"resposta": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno no servidor da IA.")


#chat no terminal

if __name__ == '__main__':
    print("--- Chatbot GoodWe & Carregadores Iniciado ---")
    print("Digite 'sair' para encerrar.\n")

#loop de perguntas e respostas
    while True:
        pergunta_usuario = input("Você: ")

        if pergunta_usuario.lower() in ["sair", "exit", "quit"]:
            print("Encerrando chat...")
            break

        if not pergunta_usuario.strip():
            continue

        try:
#chamada com instruções de restrição
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=pergunta_usuario,
                config=configuracao_ia,
            )

            print(f"\nIA GoodWe: {response.text}\n")

        except Exception as e:
            print(f"\nErro ao comunicar com a IA: {e}\n")