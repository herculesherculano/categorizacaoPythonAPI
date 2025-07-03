from fastapi import FastAPI
from pydantic import BaseModel
import joblib

#Carrega o modelo
modelo = joblib.load("modelo_categorias.joblib")

#Inicializa a API
app = FastAPI(title ="API de Categorização de Itens")

#Define o formato de entrada
class ItemEntrada(BaseModel):
    item: str

#Rota de predição
@app.post("/prever/")
def prever_categoria(dado: ItemEntrada):
    texto=[dado.item]
    categoria_prevista=modelo.predict(texto)[0]
    return {"categoria":categoria_prevista}