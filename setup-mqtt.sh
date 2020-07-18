#!/usr/bin/env bash
docker pull eclipse-mosquitto

docker run -it -p 1883:1883 -p 2221:9001 -p 8883:8883 --restart always -d -v mosquitto.conf:/mosquitto/config/mosquitto.conf --name mqtt eclipse-mosquitto
docker run -it -p 1883:1883 -p 2221:9001 -p 8883:8883 -v /home/qt/Downloads/iot/conf/mosquitto.conf:/mosquitto/config/mosquitto.conf --name mqtt eclipse-mosquitto