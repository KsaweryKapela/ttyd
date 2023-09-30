#!/bin/bash

docker build -t ttyd . && docker run -p 80:80 ttyd

echo Api is running on:
echo "http://localhost:80"

