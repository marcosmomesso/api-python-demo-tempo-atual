from flask import Flask, jsonify
from datetime import datetime
import pytz
import sys

app = Flask(__name__)

@app.route("/")
def index():
    tz = pytz.timezone("America/Sao_Paulo")
    now = datetime.now(tz)
    return jsonify({
        "pais": "Brasil",
        "data_hora": now.strftime("%Y-%m-%d %H:%M:%S"),
        "tecnologia": "Python",
        "versao": sys.version.split()[0]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
