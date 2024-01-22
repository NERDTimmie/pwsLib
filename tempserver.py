from flask import Flask, request
import subprocess

app = Flask(__name__)


@app.route('/', methods=['POST'])
def process():
    data = request.get_data()

    with open("temp.py", "w") as f:
        f.write(data.decode("utf-8"))
    result = subprocess.Popen(['python', 'temp.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    console = result.stdout.read()

    if console:
        print(console)
        return console, 405
    else:
        with open("output.json", "r") as f:
            return f.read().encode('utf-8'), 200


if __name__ == '__main__':
    app.run()
