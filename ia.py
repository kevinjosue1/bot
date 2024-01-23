import openai
from bd import get_data_chroma


def bot( question):
         
        from langchain.llms import OpenAI
        
       
          # search de data.
        context = get_data_chroma(question)
        prompt = """actua como un venderor experto, responder la pregunta basándote en el contexto de abajo. Si la
        pregunta no puede ser respondida usando la información proporcionada,
        responder con "No tengo la informacion solicitada".
        Contexto: """ + context + """
        Pregunta: """ + question + """
        Respuesta (escribe formal): """
          
        # initialize the models
        openai = OpenAI(
              model_name = "text-davinci-003",
              openai_api_key = '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'
        )
        return(openai(prompt))
    #bot