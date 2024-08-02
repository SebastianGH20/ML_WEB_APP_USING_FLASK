#!/bin/bash
# Actualiza pip
pip install --upgrade pip
# Instala las dependencias
pip install -r requirements.txt
# Inicia la aplicación (cambia `src.app:app` según sea necesario)
gunicorn src.app:app
