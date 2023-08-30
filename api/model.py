import spacy
import es_core_news_sm

class NERProcessor:
    """
    Clase para el procesamiento de extracción de entidades con nombre (NER) en un conjunto de oraciones.
    Utiliza el modelo es_core_news_sm de Spacy para el procesamiento del lenguaje natural en español.
    """
    def __init__(self, sentences):
        """
        Inicializa una instancia de NERProcessor.

        Args:
            sentences (list): Una lista de oraciones en español para procesar.
        """
        self.sentences = sentences
        self.nlp = es_core_news_sm.load()
    
    def process_sentences(self):
        """
        Procesa cada una de las oraciones proporcionadas y extrae las entidades con nombre (NER).

        Returns:
            list: Una lista de diccionarios donde cada diccionario contiene la oración original y las entidades NER encontradas.
                Ejemplo:
                [
                    {
                        "oración": "La capital de Francia es París.",
                        "entidades": {
                            "Francia": "LOC",
                            "París": "LOC"
                        }
                    },
                    ...
                ]
        """
        results = []
        for sentence in self.sentences:
            doc = self.nlp(sentence)
            entities = {}
            for ent in doc.ents:
                entities[ent.text] = ent.label_
            
            results.append({
                "oración": sentence,
                "entidades": entities
            })
        return results
