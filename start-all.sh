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
