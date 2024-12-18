#! /bin/bash
# Boilerplate
# find . -mindepth 2 -maxdepth 2 | grep -v "./venv"| grep -v "./.ctf/" | awk '{print substr($1,3); }' | awk '{print "pushd " $1 "\n\tsudo docker compose up -d" "\npopd\n"}'

pushd jail/ChriSHmaSH
    sudo docker compose up -d
popd

pushd crypto/booleanWonderland
    sudo docker build -t booleanwonderland .
    sudo docker run -d -p 2222:22 --name booleanwonderland booleanwonderland
popd

pushd web/opain
    sudo docker compose up -d
popd

pushd web/SantaVision
    sudo docker compose up -d
popd

pushd web/santa_recipe_processor
    sudo docker compose up -d
popd

pushd web/succ
    sudo docker compose up -d
popd

pushd pwn/sleigh_ride
    sudo docker compose up -d
popd

pushd web/WinterBoot
    sudo docker compose up -d
popd

pushd web/custom_tshirts
    docker build -t flask-app .
    docker run -d -p 15685:15685 flask-app
popd

pushd web/christmas_RESTored
    docker rmi christmas-restored
    docker image build -t christmas-restored .
    docker container run -d -p 34340:5000 --rm christmas-restored
popd

pushd web/FENtastic/deployment
    sudo docker compose up -d
popd
