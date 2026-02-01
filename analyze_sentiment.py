from src.database.database import DB
from src.classes.process.pnl import Pnl
from src.classes.process.analyze_sentiment import Analyzer
from src.classes.Instagram.scrapy import Scrape
from src.LLM.classificator import Chat
import pandas as pd
from dotenv import load_dotenv
import os



load_dotenv()



comentarios = DB.read_table(os.getenv('TABLE_C'))

for index,comentario in enumerate(comentarios): 
    sentimento = Chat.classificator(comment=comentario[1])
    DB.insert_comment_w_sentiment(comentario[1],sentimento)


