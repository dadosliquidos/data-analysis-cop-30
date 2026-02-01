from LeIA import SentimentIntensityAnalyzer


class Analyzer:
    def __init__(self):
        pass


    @staticmethod
    def analyze_sentiment(text):
        analyzer =  SentimentIntensityAnalyzer()
        '''Função que recebe um texto como entrada, analisa seu sentimento e interpreta o resultado'''
        sentiment = analyzer.polarity_scores(text)
        compound_score = sentiment['compound']
        if compound_score >= 0.05:
            return "Positivo"
        elif compound_score <= -0.05:
            return "Negativo"
        else:
            return "Neutro"