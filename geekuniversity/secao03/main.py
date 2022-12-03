from fastapi import FastAPI


app = FastAPI()


# dictionary example without database server
curses = {
    1: {
        "title": "Developer fo dummy's",
        "class": 112,
        "hours": 58
    },
    2: {
        "title": "Algorithm",
        "class": 87,
        "hours": 67
    }
}


@app.get('/')
async def default():
    return {"api": "API is running"}


@app.get('/curses')
async def get_curses():
    return curses


if __name__ == "__main__":
    import uvicorn as uvicorn

    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level='info', reload=True)
