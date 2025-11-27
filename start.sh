#!/bin/bash
apt-get update && apt-get install -y unzip
reflex run --env prod
