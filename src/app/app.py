from flask import Flask
from flask import render_template, request, redirect, url_for
from classes.Instagram.login import Login
from classes.Instagram.scrapy import Scrape
from classes.process.pnl import Pnl
from classes.visualization.plot_word_cloud import Plot_word_cloud
from classes.visualization.plot_bar import Plot_bar
from pathlib import Path
import time
ROOT_PATH = Path(__file__).parent.parent

app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def processamento():
    url = request.form['url']


    login = Login.inicializarNavegador(url)

    Scrape.scroll_comments(login)

    html_page = Scrape.Scraping(login)

    list_comments = Scrape.get_comments(html_page)



    with open(ROOT_PATH / 'database' / 'comentarios.csv', 'w',encoding='utf-8') as arquivo:
        
        for comment in list_comments:
            arquivo.write(comment+'\n')


    df = Pnl.get_comment('comentarios.csv')


    Plot_word_cloud.plot(Pnl.apply_stop_word(df))


    time.sleep(3)

    Plot_bar.plot(df)

    return redirect(url_for('homepage'))


def run():
    app.run()



