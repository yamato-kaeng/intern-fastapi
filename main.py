from fastapi import FastAPI

app = FastAPI()

@app.get('/bmi')
def bmi(h:int=170, w:int=50):

    h = (h/100) ** 2
    bmi = w/h

    return {'bmi':bmi}