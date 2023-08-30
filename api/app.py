from flask import Flask, request, jsonify
from model import NERProcessor
import os

# Configuración del entorno Flask a producción
os.environ['FLASK_ENV'] = 'production'

# Creación de una instancia de la aplicación Flask
app = Flask(__name__)

@app.route('/process_sentences', methods=['POST'])
def process_sentences():
    """
    Procesa las oraciones proporcionadas a través de una solicitud POST y devuelve las entidades con nombre (NER) encontradas.

    Returns:
        jsonify: Un objeto JSON que contiene el resultado del procesamiento de las oraciones en el siguiente formato:
        {
            "resultado": [
                {
                    "oración": "Ejemplo de oración.",
                    "entidades": {
                        "entidad1": "TIPO1",
                        "entidad2": "TIPO2"
                    }
                },
                ...
            ]
        }

        En caso de error, devuelve un objeto JSON con el mensaje de error y el código de estado correspondiente.
    """
    try:
        data = request.json
        oraciones = data.get('oraciones', [])

        if not oraciones:
            return jsonify({"error": "No se proporcionaron oraciones"}), 400
        
        ner_processor = NERProcessor(oraciones)
        resultados = ner_processor.process_sentences()
        
        return jsonify({"resultado": resultados})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Inicia la aplicación Flask en el host 0.0.0.0 para que sea accesible externamente
    app.run(host='0.0.0.0')
