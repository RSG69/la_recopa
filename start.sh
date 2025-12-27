#!/bin/bash
apt-get update && apt-get install -y unzip curl
export PORT=${PORT:-3000}
reflex run --env prod --backend-host 0.0.0.0 --single-port
