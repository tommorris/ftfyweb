import ftfy
from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return '<!DOCTYPE html>\n<html><head><title>FTFY on the web</title><body><form method="POST" action="/"><textarea name="text"></textarea><br /><input type="submit" /></body></html>'

@app.route("/", methods=["POST"])
def translate():
    data = unicode(request.form['text'])
    headers = {"Content-Type": "text/plain; charset=UTF-8"}
    return Response(ftfy.fix_text(data), 200, headers=headers)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
