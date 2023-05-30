# Utiliza la imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala las dependencias de tu aplicación
RUN pip install -r requirements.txt

# Copia el contenido de tu aplicación al contenedor
COPY . .

# Expone el puerto en el que se ejecuta tu aplicación
EXPOSE 8000

# Comando para iniciar tu aplicación cuando se ejecute el contenedor
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
