from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def read_root():
    return {'Hello': 'World'}

@app.get('/greetings/{name}')
def greetings(name: str):
    message = f'Good morning {name}!'
    return {
        'status': 'OK',
        'message': message,
    }
