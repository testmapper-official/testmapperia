from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def start():
    return 'добавьте в URL /training/<prof>'
@app.route('/training/<prof>')
def index(prof):
    return render_template('trainings.html', title=prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')