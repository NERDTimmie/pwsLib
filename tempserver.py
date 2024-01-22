from flask import Flask, request
import subprocess
import uuid

app = Flask(__name__)


@app.route('/', methods=['POST'])
def process():
    data = request.get_data()
    id = uuid.uuid1()
    fileName = str(id) + ".py"


    with open("temp" + id + ".py", "w") as f:
        f.write(data.decode("utf-8"))
    result = subprocess.Popen(['python3', fileName], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    console = result.stdout.read()

    if console:
        print(console)
        return console, 405
    else:
        with open(id + ".json", "r") as f:
            return f.read().encode('utf-8'), 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
