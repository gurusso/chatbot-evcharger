# EV Charger & GoodWe Assistant ⚡🚗

Plataforma web para gerenciamento e agendamento de recarga de veículos elétricos, equipada com um assistente virtual inteligente especializado em eletromobilidade e produtos GoodWe.

## 🚀 Funcionalidades
* **Mapa e Localização:** Interface para encontrar pontos de recarga disponíveis.
* **Agendamento e Simulação:** Ferramentas de suporte ao usuário para gestão de carregamento e pagamentos simulados.
* **Chatbot Especializado:** Assistente baseado em IA (Google Gemini) restrito estritamente a tirar dúvidas técnicas sobre carregadores GoodWe, potências AC/DC, instalação e compatibilidade.

---

## 🛠️ Tecnologias Utilizadas
* **Front-end:** HTML5, JavaScript, TailwindCSS.
* **Back-end:** Python, FastAPI, Uvicorn.
* **Inteligência Artificial:** Google GenAI SDK (`google-genai`), modelo Gemini 2.5 Flash com System Instructions.

---

## 📦 Como Rodar o Projeto e Acessar a Documentação

1. **Clone o repositório:**
   TERMINAL
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   cd seu-repositorio
## Instale as dependências:

TERMINAL
pip install fastapi uvicorn pydantic google-genai python-dotenv
## Configure as variáveis de ambiente:

Crie um arquivo chamado .env na raiz do projeto.

Adicione sua chave de API do Google AI Studio:


GEMINI_API_KEY=sua_chave_aqui
Inicie o Servidor FastAPI e acesse a documentação:

## No terminal do seu projeto, execute o comando para iniciar o servidor:

TERMINAL
uvicorn evcharger-IA:app --reload
Aguarde a mensagem de confirmação Application startup complete aparecer no terminal.

## Com o servidor rodando, abra o seu navegador e acesse a documentação interativa da API em http://127.0.0.1:8000/docs.

Abra o arquivo index.html no seu navegador para utilizar o site e interagir com o chatbot flutuante conectado à API.
