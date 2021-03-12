from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f'''<!doctype html>
                <html lang="en">
                  <head>    
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                  </body>
                    <h2>Эта планета близка к Земле;<h2>
                    <div class="alert-dark" role="alert">
                        <h2>На ней много необходимых ресурсов;<h2>
                    </div>
                    <div class="alert-success" role="alert">
                        <h2>На ней есть вода и атмосфера;<h2>
                    </div>
                    <div class="alert-secondary" role="alert">
                        <h2>На ней есть небольшое магнитное поле;<h2>
                    </div>
                    <div class="alert-warning" role="alert">
                        <h2>Наконец, она просто красива!<h2>
                    </div>
                  </body>
                </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
