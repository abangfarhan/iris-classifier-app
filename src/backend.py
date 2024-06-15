from fastapi import FastAPI, Response, status, Request
import joblib
import pandas as pd

app = FastAPI()
MODEL_PATH = './model/classifier.pkl'

@app.get('/')
def read_root():
    return {
        'status': 'ok',
        'message': 'Your API is UP'
    }

@app.get('/check-model')
def check_model(response: Response):
    try:
        _ = joblib.load(MODEL_PATH)
        return {
            'status': 'ok',
            'message': 'model is ready to use'
        }
    except Exception:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status': 'error', 'message': 'failed to load model'}

@app.post('/predict')
async def predict(response: Response, request: Request):
    try:
        data = await request.json()
        model = joblib.load(MODEL_PATH)
        labels = ['Iris Setosa', 'Iris Versicolor', 'Iris Virginica']
        cols_map = {
            'SepalLengthCm': 'sepal_length',
            'SepalWidthCm': 'sepal_width',
            'PetalLengthCm': 'petal_length',
            'PetalWidthCm': 'petal_width',
        }
        cols_original = list(cols_map.keys())
        cols_request = list(cols_map.values())
        df = pd.DataFrame([data])[cols_request]
        df.columns = cols_original
        result_num = model.predict(df)[0]
        result = labels[result_num]
        return {
            'status': 'ok',
            'message': 'return prediction',
            'result': result
        }
    except Exception as exc:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {
            'status': 'error',
            'message': 'failed to make prediction',
            'detail_error': str(exc)
        }
