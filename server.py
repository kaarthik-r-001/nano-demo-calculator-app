from flask import Flask

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'hello world'

@app.route("/calculator/add", methods=['POST'])
def add():
    return '1+2'

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    return ''

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
