# Usar la imagen base de Python
FROM python:3.8

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias
RUN pip install -r requirements.txt

# Copiar el resto de los archivos al contenedor
COPY . .

# Exponer el puerto en el que corre la aplicación Flask
EXPOSE 5000

# Para poder ejecutar app.py entramos dentro de app/api
WORKDIR /app/api

# Comando para ejecutar la aplicación cuando el contenedor inicie
CMD ["python", "app.py"]

