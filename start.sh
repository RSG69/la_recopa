#!/bin/bash

# Instalar dependencias necesarias para Reflex
apt-get update && apt-get install -y unzip curl

# Railway asigna un puerto dinámico, lo usamos aquí:
export PORT=${PORT:-3000}

# Arrancamos Reflex escuchando en todas las interfaces (importante para WS)
reflex run --env prod --backend-host 0.0.0.0 --port $PORT


