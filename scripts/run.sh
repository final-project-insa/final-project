#/bin/bash

git pull origin main

docker-compose -f ./local.yml up --build -d
