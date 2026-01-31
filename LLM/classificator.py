from ollama import chat
from ollama import ChatResponse




print()
# or access fields directly from the response object



class Chat:
    def __init__(self):
        pass
    
    @classmethod
    def classificator(cls,comment):
        
        promt = '''Classifique o sentimento da seguinte frase em e retorne  apenas se é "Positivo", "Negativo" ou "Neutro", sendo que será um comentario de um Post do instagram  em caso de incertezas, classifique como Neutra. 
              Caso  haja conteúdo visíve, classifique como "Neutro.
              Não justifique a sua classificação. 
              avalie emojis também e retorne  apenas se é "Positivo", "Negativo" ou "Neutro".
              A  seguir frase: {}  '''.format(comment)
        
        response: ChatResponse = chat(model='llama3', messages=[
                  {
                    'role': 'user',
                    'content': promt,
                  },
                ])
        return response['message']['content']
