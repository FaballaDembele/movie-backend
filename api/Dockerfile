FROM python:3.12-slim

#definit le repertoire de travail dans le conteneur
WORKDIR /app

#copie le fichier des dependances dans le conteneur
COPY requirements.txt .

#installe les dependances python sans mise en cache
RUN pip install --no-cache-dir --upgrade -r requirements.txt

#copie tous les fichiers .py et le fichier .db dans le conteneur
COPY . .

# lance le serveur unicorn pour executer l'api fastapi
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","80"]