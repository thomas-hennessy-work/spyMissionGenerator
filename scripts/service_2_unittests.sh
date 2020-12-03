#!/bin/bash
docker build -f ./service_2/tests/Dockerfile -t thomashennessy/service_2_unittest:spy-app .
docker run -it -d --name service_2_tests thomashennessy/service_2_unittest:spy-app
docker exec service_2_tests pytest ./service_2 --cov ./service_2
