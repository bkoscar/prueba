# Prueba


# Dockers

Docker es una plataforma abierta para desarrollar, enviar y ejecutar aplicaciones. Docker te permite separar tus aplicaciones de tu infraestructura para que puedas entregar software rápidamente. Con Docker, puedes gestionar tu infraestructura de la misma manera en que gestionas tus aplicaciones. Al aprovechar las metodologías de Docker para el envío, prueba e implementación de código, puedes reducir significativamente la demora entre escribir código y ejecutarlo en producción.
Instalar Docker

A continuación, se presentan los enlaces para instalar Docker en diferentes sistemas operativos:

    MacBook: https://docs.docker.com/desktop/install/mac-install/
    Windows: https://docs.docker.com/desktop/install/windows-install/
    Linux:   https://docs.docker.com/desktop/install/linux-install/

# Ejecutar la API utilizando Docker

Una vez que hayas instalado Docker, puedes ejecutar el siguiente comando para levantar el contenedor con la API en Flask:

    ``` docker-compose up --build
    ```

# Realizar pruebas

Después de que el servicio esté en funcionamiento, puedes realizar pruebas utilizando el archivo de Python testing.py con el siguiente comando:


    ```python3 testing.py
    ```