from fastapi import FastAPI

app = FastAPI()

#creating new Routes:
@app.get('/')
def index():
    return {'data':{'name' : 'Mayuri'}}


@app.get('/about')
def about():
    return {'data':{'about page test'}}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id : int):
    return {'data': id}