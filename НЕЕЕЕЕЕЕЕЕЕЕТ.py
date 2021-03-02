from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return 'Миссия Колонизация Марса'


@app.route('/index')
def index():
    return 'И на Марсе будут яблони цвести!'


@app.route('/promotion')
def promotion():
    s = ['Человечество вырастает из детства.', 'Человечеству мала одна планета.',
         'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
         'Присоединяйся!']
    return '<br>'.join(s)


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                </html>
                <img src="{url_for('static', filename='img/mars.jpg')}" 
                   alt="image not found">
                <body>
                    </br>Вот она какая, красная планета</h1>
                </body>'''


@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/styles.css')}" />
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                  </body>
                </html>
                <img src="img/mars.jpg" alt="image not found">
                <body>
                    <div class="alert-dark" role="alert">
                        <h2>Человечество вырастает из детства.<h2>
                    </div>
                    <div class="alert-success" role="alert">
                        <h2>Человечеству мала одна планета.<h2>
                    </div>
                    <div class="alert-secondary" role="alert">
                        <h2>Мы сделаем обитаемыми безжизненные пока планеты.<h2>
                    </div>
                    <div class="alert-warning" role="alert">
                        <h2>И начнем с Марса!<h2>
                    </div>
                    <div class="alert-danger" role="alert">
                        <h2>Присоединяйся!<h2>
                    </div>
                </body>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
