#!/bin/bash

# Instalar dependencias necesarias
apt-get update && apt-get install -y unzip curl

# Railway asigna un puerto dinámico. Si no está, usamos 3000.
export PORT=${PORT:-3000}

# Iniciar Reflex usando un solo puerto (frontend + backend + websocket)
reflex run --env prod --backend-host 0.0.0.0 --single-port $PORT



