import streamlit as st
import requests

st.set_page_config(
    page_title='Iris Classifier App'
)
st.image('./assets/Image20240525091902.png')
st.title('Iris Classifier App')
st.markdown('**Created by Abang Farhan | Batch May 2024**')
st.divider()

st.markdown('Just type the value, and get the result.')

with st.form(key='iris-form'):
    sepal_length = st.number_input(label='Sepal Length', min_value=0, help='Input the numerical sepal length')
    sepal_width = st.number_input(label='Sepal Width', min_value=0, help='Input the numerical sepal width')
    petal_length = st.number_input(label='Petal Length', min_value=0, help='Input the numerical petal length')
    petal_width = st.number_input(label='Petal Width', min_value=0, help='Input the numerical petal width')
    submit_button = st.form_submit_button('Predict')

    if submit_button:
        data = {
            'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width,
        }

        with st.spinner('Wait for it...'):
            response = requests.post('http://backend:8000/predict', json=data)
            result = response.json()
            if response.status_code == 200:
                st.success(f'Prediction: {result["result"]}')
                st.balloons()
            else:
                st.error(result['detail_error'])
