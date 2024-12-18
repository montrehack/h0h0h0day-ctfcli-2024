#!/bin/bash

docker rmi christmas-restored
docker image build -t christmas-restored .
docker container run -p 34340:5000 --rm christmas-restored
