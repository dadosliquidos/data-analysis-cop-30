from wordcloud import WordCloud
import matplotlib.pyplot as plt
from pathlib import Path
import matplotlib
matplotlib.use('Agg') # or 'SVG'


ROOT_PATH = Path(__file__).parent.parent.parent

class Plot_word_cloud:
    def __init__(self):
        pass


    @classmethod
    def plot(cls,lista_comentarios:list):
        unica_string = ('').join(lista_comentarios)

        nuvem_de_palavras = WordCloud().generate(unica_string)
        plt.imshow(nuvem_de_palavras,interpolation='bilinear')
        plt.savefig(ROOT_PATH / 'app' / 'static' / 'imagem' / 'wordCloud.png')
        plt.close()
