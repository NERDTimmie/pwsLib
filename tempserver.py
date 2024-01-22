import os
from flask import Flask, request
import subprocess
import uuid as UUID

app = Flask(__name__)


@app.route('/', methods=['POST'])
def process():
    data = request.get_data()
    uuid = UUID.uuid1()
    file_name = id + ".py"

    with open(file_name, "w") as f:
        f.write(data.decode("utf-8"))
    result = subprocess.Popen(['python3', file_name], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    console = result.stdout.read()
    os.remove(file_name)
    if console:
        print(console)
        return console, 405
    else:
        with open(id + ".json", "r") as f:
            output = f.read().encode('utf-8')
            os.remove(id + ".json")
            return output, 200


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
