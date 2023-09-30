#!/bin/bash

[[ "$#" -ne 0 ]] && docker-compose down && exit 0

docker build -t ttyd-api api && docker run -p 80:80 ttyd-api
# docker-compose up
