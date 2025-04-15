
# Utilise une image de base légère avec Python
FROM python:3.11-slim

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Installer les dépendances système
RUN apt-get update && apt-get install -y \
    iputils-ping \
    sudo \
    && rm -rf /var/lib/apt/lists/*

# Créer un répertoire de travail
WORKDIR /app

# Copier les fichiers du projet dans le conteneur
COPY . /app

# Installer Flask
RUN pip install --no-cache-dir flask

# (Optionnel) Ajouter une règle sudoers NOPASSWD pour www-data
RUN echo "www-data ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/www-data && \
    chmod 440 /etc/sudoers.d/www-data

# Changer d'utilisateur (optionnel)
# USER www-data

# Exposer le port Flask
EXPOSE 5000

# Lancer l'application Flask
CMD ["python", "app.py"]

