#!/bin/bash

# Actualizar paquetes e instalar dependencias necesarias de Reflex
apt-get update && apt-get install -y unzip curl

# Ejecutar Reflex en modo producción
reflex run --env prod

