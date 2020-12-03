#!/bin/bash

docker build -f ./service_1/tests/Dockerfile -t thomashennessy/service_1_unittest:spy-app .
docker run -it -d --name service_1_tests thomashennessy/service_1_unittest:spy-app
docker exec service_1_tests pytest ./service_1 --cov ./service_1