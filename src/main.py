import sqlite3

from fastapi import FastAPI
from pydantic import BaseModel


# model to validate article data
class ArticleModel(BaseModel):
    id: int
    author: str
    title: str
    description: str
    imageUrl: str
    publishedAt: str
    content: str


app = FastAPI()

# add new article


@app.post('/article/add')
def add_article(data: ArticleModel):

    article = {
        "id": data.id,
        "author": data.author,
        "title": data.title,
        "description": data.description,
        "imageUrl": data.imageUrl,
        "publishedAt": data.publishedAt,
        "content": data.content
    }
    with sqlite3.connect("articles.db") as conn:
        command = "insert into Articles " + \
            str(tuple(article.keys())) + " values" + \
            str(tuple(article.values())) + ";"
        conn.execute(command)
    conn.commit()


# list all the articles
@app.get('/articles')
def get_articles():
    with sqlite3.connect("articles.db") as conn:
        command = "SELECT * FROM Articles"
        cursor = conn.execute(command)
        # for row in cursor:
        #     print(row)
    return cursor.fetchall()


# show article detail
@app.get('/article/{id}')
def get_article(id):
    with sqlite3.connect("articles.db") as conn:
        command = "select * from Articles where id = " + id
        cursor = conn.execute(command)
    return cursor.fetchall()
