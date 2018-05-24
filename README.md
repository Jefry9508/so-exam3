# Sistemas Operacionales - Parcial 3  

**Nombre:** Jefry Cardona Chilito  
**Código:** A00320232  
**Correo:** jefry.cardona@correo.icesi.edu.co  
**Profesor:** Daniel Barragan  
**Url repositorio:** https://github.com/Jefry9508/so-exam3  

## Implemetación de un servicio web en flask

Se aprovisionó el ambiente virtual con las dependencias necesarias para poder dar solución a este parcial, se utilizarón los archivos requirements_dev.txt y requirements.txt que ya se encontraban disponibles en los repositorios del curso.

Proseguimos con la creación de los scripts que contendrán los metodos que nos permitirán acceder a los porcentajes de uso de la cpu, memoria RAM y espacio en disco. Estos métodos los podemos ver a continuación:

![](capturas/stats.png)

Luego se creó otro script, cuya función es la de llamar los métodos descritos anteriormente y poderlos exponer como servicios web y poder así ser consumidos a través de una petición de un navegador. Este script es el siguiente:

![](capturas/app.png)

Ya con los dos scripts, ejecutamos el comando el ```python app.py``` para ejecutar el script y poderlo consultar a través de la herramienta Postman obteniendo los siguientes resultados:

![](capturas/postman_cpu.png)

![](capturas/postman_ram.png)

![](capturas/postman_disk.png)


## Implementación de las pruebas unitarias para los servicios empleando Fixtures y Mocks

Se crea un script cuyo nombre siempre deberá empezar por test ya que el comando de pytest lo buscará para poderlo ejecutar. Este script realizará las pruebas unitarias de los resultados de los servicio web que anteriormente habia mencionado. El script es el siguiente:

![](capturas/test_stats.png)

Luego ejecutamos el comando ```pytest -v```, el cual buscará todos los archivos .py que comiencen con la palabra test para ser ejecutados. Obtenemos el siguiente resultado:

![](capturas/test_passed.png)
