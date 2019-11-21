#!/usr/bin/python3
import requests
from flask import Flask, request, render_template, make_response

app = Flask(__name__)

poets = {
    '1': 'همه شاعران',
    '2': 'حافظ',
    '3': 'خیام',
    '5': 'مولوی',
    '7': 'سعدی',
    '19': 'اوحدی',
    '20': 'خواجو',
    '21': 'عراقی',
    '22': 'صائب',
    '25': 'هاتف اصفهانی',
    '26': 'ابوالسعید ابوالخیر',
    '28': 'باباطاهر',
    '29': 'محتشم کاشانی',
    '31': 'سیف فرغانی',
    '32': 'فروغی بسطامی',
    '33': 'عبید زاکانی',
    '34': 'امیرخسرو دهلوی',
    '35': 'شهریار',
    '40': 'سلمان ساوجی',
    '41': 'رهی معیری'
}


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


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        poet = request.form['poet'] or '1'
    else:
        poet = request.cookies.get('sabooh_poet') or '1'
    poem = get_poem(poet)
    if poem:
        resp = make_response(
            render_template(
                'index.html',
                poem=poem,
                fav_poet=poet,
                poets=poets
            )
        )
        resp.set_cookie('sabooh_poet', poet)
        return resp
    else:
        return render_template(
            'error.html'
        )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='80')
