import requests

# URL del servidor Flask donde se realizará la solicitud POST
url = "http://172.20.0.2:5000/process_sentences"  

# Datos a enviar en la solicitud POST
data = {
    "oraciones": [
        "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
        "San Francisco considera prohibir los robots de entrega en la acera."
    ]
}

# Realiza una solicitud POST al servidor Flask
response = requests.post(url, json=data)

# Verifica el código de estado de la respuesta
if response.status_code == 200:
    # Si la respuesta es exitosa (código 200), procesa y muestra el resultado
    result = response.json()
    print(result)
else:
    # Si hay un error en la respuesta, muestra el código de estado
    print("Error:", response.status_code)
