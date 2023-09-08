from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

#creating new Routes:
@app.get('/')
def index():
    return {'data':{'name' : 'Mayuri'}}


@app.get('/about')
def about():
    return {'data':{'about page test'}}


@app.get('/blog')
def index(limit=10, published: bool = True, sort: Optional[str] = None):
    if published:
    #list al blogs
        return {'data': f'{limit} blog from db'}
    else:
        return {'data': f'{limit} blogs from the db'}


@app.get('/blog/unpublished')
def unpublished():
    return {'data': 'all unpublished blogs'}

@app.get('/blog/{id}')
def show(id : int):
    return {'data': id}

#posts
class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post('/blog')
def create_post(request: Blog):
    return request
    return {'data': 'post created'}