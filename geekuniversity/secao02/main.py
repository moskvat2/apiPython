from fastapi import FastAPI


app = FastAPI()


@app.get('/msg')
async def mensagem():
    return {"msg": "FastAPI com Geek University"}


if __name__ == "__main__":
    import uvicorn as uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level='info', reload=True)
