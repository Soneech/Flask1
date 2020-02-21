from flask import Flask

app = Flask(__name__)


@app.route('/')
def default():
    return ''


@app.route('/promotion')
def promotion():
    message = [
        'Человечество вырастает из детства.', 'Человечеству мала одна планета.',
        'Мы сделаем обитаемыми безжизненные пока планеты.', 'И начнем с Марса!',
        'Присоединяйся!'
    ]
    return '</br>'.join(message)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
