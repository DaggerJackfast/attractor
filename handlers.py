import os
from settings import database
from tempate_engine import render
from response import Response
from parse import *

from settings import TEMPLATES_DIR


def open_html(template):
    file = open(os.path.join(TEMPLATES_DIR, template))
    html = file.readlines()
    return ''.join(html)

class Article():
    def __init__(self,author,content,date):
        self.author=author
        self.content=content
        self.date=date

def index(request):
    articles=database.get_all_articles()
    context = {'articles': articles}
    rendered_body = render(os.path.join(TEMPLATES_DIR, 'index.html'), context).encode()
    response = Response(request, body=rendered_body)

    response.set_header(b'Content-Type', b'text/html')
    response.set_code(b'200')
    response.set_status(b'OK')
    return response


def about(request):
    pass


def contacts(request):
    pass

