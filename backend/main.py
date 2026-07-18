import os
import glob
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

# Cria a instância principal da aplicação FastAPI
app = FastAPI()

# Configure o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define caminhos absolutos para a pasta de imagens
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Garante que o diretório de imagens exista
if not os.path.exists(PASTA_IMAGENS):
    os.makedirs(PASTA_IMAGENS)

# Lista completa de figurinhas (30 figurinhas)
# Deixamos ativas apenas as que possuem imagens correspondentes na pasta.
# A figurinha de ID 30 não possui imagem correspondente e por isso está comentada.
figurinhas = [
    {
        "id": 1,
        "nome": "Alan Turing",
        "categoria": "IA",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": 2,
        "nome": "John McCarthy",
        "categoria": "IA",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
        "id": 3,
        "nome": "Sam Altman",
        "categoria": "IA",
        "imagem_url": "/figurinhas/3/imagem"
    },
    {
        "id": 4,
        "nome": "Geoffrey Hinton",
        "categoria": "IA",
        "imagem_url": "/figurinhas/4/imagem"
    },
    {
        "id": 5,
        "nome": "Yann LeCun",
        "categoria": "IA",
        "imagem_url": "/figurinhas/5/imagem"
    },
    {
        "id": 6,
        "nome": "Guido van Rossum",
        "categoria": "Programação",
        "imagem_url": "/figurinhas/6/imagem"
    },
    {
        "id": 7,
        "nome": "Tim Berners-Lee",
        "categoria": "Web",
        "imagem_url": "/figurinhas/7/imagem"
    },
    {
        "id": 8,
        "nome": "Ray Kurzweil",
        "categoria": "IA",
        "imagem_url": "/figurinhas/8/imagem"
    },
    {
        "id": 9,
        "nome": "Travis Oliphant",
        "categoria": "Programação",
        "imagem_url": "/figurinhas/9/imagem"
    },
    {
        "id": 10,
        "nome": "Wes McKinney",
        "categoria": "Programação",
        "imagem_url": "/figurinhas/10/imagem"
    },
    {
        "id": 11,
        "nome": "Edgar Codd",
        "categoria": "Banco de Dados",
        "imagem_url": "/figurinhas/11/imagem"
    },
    {
        "id": 12,
        "nome": "Larry Page",
        "categoria": "Web",
        "imagem_url": "/figurinhas/12/imagem"
    },
    {
        "id": 13,
        "nome": "Michael Stonebraker",
        "categoria": "Banco de Dados",
        "imagem_url": "/figurinhas/13/imagem"
    },
    {
        "id": 14,
        "nome": "Salvatore Sanfilippo",
        "categoria": "Banco de Dados",
        "imagem_url": "/figurinhas/14/imagem"
    },
    {
        "id": 15,
        "nome": "Eliot Horowitz",
        "categoria": "Banco de Dados",
        "imagem_url": "/figurinhas/15/imagem"
    },
    {
        "id": 16,
        "nome": "Linus Torvalds",
        "categoria": "Sistemas Operacionais",
        "imagem_url": "/figurinhas/16/imagem"
    },
    {
        "id": 17,
        "nome": "Dennis Ritchie",
        "categoria": "Sistemas Operacionais",
        "imagem_url": "/figurinhas/17/imagem"
    },
    {
        "id": 18,
        "nome": "Richard Stallman",
        "categoria": "Sistemas Operacionais",
        "imagem_url": "/figurinhas/18/imagem"
    },
    {
        "id": 19,
        "nome": "Bill Gates",
        "categoria": "Sistemas Operacionais",
        "imagem_url": "/figurinhas/19/imagem"
    },
    {
        "id": 20,
        "nome": "Steve Jobs",
        "categoria": "Sistemas Operacionais",
        "imagem_url": "/figurinhas/20/imagem"
    },
    {
        "id": 21,
        "nome": "Paulo Silveira",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/21/imagem"
    },
    {
        "id": 22,
        "nome": "Guilherme Silveira",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/22/imagem"
    },
    {
        "id": 23,
        "nome": "Gustavo Guanabara",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/23/imagem"
    },
    {
        "id": 24,
        "nome": "Maurício Aniche",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/24/imagem"
    },
    {
        "id": 25,
        "nome": "André Silva",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/25/imagem"
    },
    {
        "id": 26,
        "nome": "Guilherme Lima",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/26/imagem"
    },
    {
        "id": 27,
        "nome": "Gisele Souza",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/27/imagem"
    },
    {
        "id": 28,
        "nome": "Vinicius Dias",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/28/imagem"
    },
    {
        "id": 29,
        "nome": "Rafaella Ballerini",
        "categoria": "Alura",
        "imagem_url": "/figurinhas/29/imagem"
    },
    {
        "id": 30,
        "nome": "Alex Pinheiro",
        "categoria": "Você",
        "imagem_url": "/figurinhas/30/imagem"
    }
]

# Rota GET "/figurinhas" para listar todas as figurinhas ativas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Rota GET "/figurinhas/{id}/imagem" para obter a imagem correspondente usando glob
@app.get("/figurinhas/{id}/imagem")
def obter_imagem(id: int):
    # Usa o formato com dois dígitos e o padrão para achar a imagem
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    if not arquivos:
        raise HTTPException(status_code=404, detail="Figurinha não encontrada")
    
    # Retorna o primeiro arquivo correspondente encontrado
    return FileResponse(arquivos[0])

# Define o caminho para a pasta frontend (pasta raiz do projeto)
PASTA_FRONTEND = os.path.abspath(os.path.join(PASTA_BASE, ".."))

# Serve os arquivos estáticos do frontend (HTML, CSS, JS) na raiz
app.mount("/", StaticFiles(directory=PASTA_FRONTEND, html=True), name="frontend")
