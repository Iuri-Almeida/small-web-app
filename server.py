"""
    Projeto: Small Web App
    Autor: Iuri Lopes Almeida
    GitHub: https://github.com/Iuri-Almeida
    Objetivo: Aprender como criar um web app sem usar framework
    Dependência:
        - gunicorn -> pip install gunicorn (https://gunicorn.org/)
    Ajuda: https://www.youtube.com/watch?v=fe9t9DGPBuE

    Obs.:
        - gunicorn -> Web Server Gateway Interface (WSGI)
        - WSGI -> cuida dos requests e procura a funcão para renderizar a página
"""
from typing import List


def render_template(template: str = 'index.html', context: dict = None) -> str:

    with open(f'pages/{template}', 'r') as file:
        html = file.read()
        html = html.format(**context or {})

    return html


def home(context: dict = None) -> str:
    return render_template('index.html', context or {})


def contact(context: dict = None) -> str:
    return render_template('contact.html', context or {})


def not_found(context: dict = None) -> str:
    return render_template('404.html', context or {})


def app(environ: dict, start_response) -> List[bytes]:

    path = environ.get('PATH_INFO')

    if path.endswith('/'):
        path = path[:-1]

    if path == '':  # index
        data = home()
    elif path == '/contact':  # contact

        name = 'Iuri'
        age = 22
        email = 'iurilopesalmeida@gmail.com'
        cpf = '178.240.817-70'

        data = contact({
            'name': name,
            'age': age,
            'email': email,
            'cpf': cpf
        })
    else:  # other pages
        data = not_found({'path': path})

    data = data.encode('utf-8')

    status = '200 OK'
    headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(data)))
    ]
    start_response(status, headers)

    return [data]
