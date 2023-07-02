# Establecer la imagen base
FROM python:3.11

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instalar las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente de la aplicación al contenedor
COPY . .

# Exponer el puerto en el que se ejecuta la aplicación
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "source/Main.py"]
