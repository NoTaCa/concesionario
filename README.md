# Mi Aplicación Django

Este proyecto es una aplicación Django desarrollada para [describir brevemente el propósito de tu aplicación].

## Instrucciones de Docker

### 1. Construcción de la imagen

Para construir la imagen de Docker de la aplicación, ejecuta el siguiente comando:

`docker build -t nombre_imagen .`

Asegúrate de reemplazar `nombre_imagen` por el nombre que deseas darle a tu imagen de Docker.

### 2. Ejecución del contenedor

Una vez que la imagen se haya construido correctamente, puedes ejecutar un contenedor basado en esa imagen utilizando el siguiente comando:

`docker run -p 8000:8000 nombre_imagen`

Esto mapeará el puerto 8000 del contenedor al puerto 8000 de tu máquina local.

### 3. Acceso a la aplicación

Una vez que el contenedor esté en ejecución, podrás acceder a tu aplicación Django en tu navegador web utilizando la siguiente URL:

[http://localhost:8000/admin/](http://localhost:8000/admin/)

¡Listo! Ahora deberías poder ver y utilizar tu aplicación Django en tu entorno local utilizando Docker.

## Notas adicionales

- Asegúrate de tener instalado Docker en tu máquina antes de ejecutar los comandos anteriores.
- Si deseas detener el contenedor en cualquier momento, puedes presionar `Ctrl + C` en la terminal.
- Si necesitas realizar cambios en tu código o en los archivos de configuración de tu aplicación, deberás reconstruir la imagen y ejecutar un nuevo contenedor.

