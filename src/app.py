from utils import db_connect
engine = db_connect()

# your code here
from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get('/elevar_cuadrado')
async def get_cuadrado(numero):
    try:
        numero = int(numero)
    except:
        raise: HTTPException(status_code=400, detail='Debes proporcionar un numero')
    else:
        return f'Resultado: {numero**2}'


    