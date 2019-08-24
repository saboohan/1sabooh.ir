#!/usr/bin/python3
import requests
from flask import Flask, redirect, request, render_template, make_response

app = Flask(__name__)


def get_poem(poet):
    try:
        poemr = requests.get(
            'http://c.ganjoor.net/beyt-json.php?p=' + poet,
            timeout=2
        )
        if poemr.status_code == 200:
            return poemr.json()
        else:
            return False
    except Exception:
        return False


@app.route('/')
def static_page():
    poet = request.cookies.get('sabooh_poet') or '1'
    poem = get_poem(poet)
    if poem:
        resp = make_response(render_template('index.html', poem=poem))
        return resp
    else:
        return render_template(
            'error.html'
        )


@app.route('/setcookie', methods=['POST'])
def setcookie():
    try:
        poet = request.form['poet']
    except Exception:
        poet = '1'

    response = make_response(redirect('/'))
    response.set_cookie('sabooh_poet', poet)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8090')
