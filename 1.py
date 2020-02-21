from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def default():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    message = [
        'Человечество вырастает из детства.', 'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '</br>'.join(message)


@app.route('/image_mars')
def image_mars():
    return """<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{}" alt="здесь должна была быть картинка, 
                        но не нашлась" width="450" height="450"/>
                        <p>Вот она такая, красная планета.</p>
                  </body>
                </html>""".format(url_for('static', filename='img/mars.png'))


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
