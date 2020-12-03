#!/bin/bash
docker build -f ./service_2/tests/Dockerfile -t thomashennessy/service_3_unittest:spy-app .
docker run -it -d --name service_3_tests thomashennessy/service_3_unittest:spy-app
docker exec service_3_tests pytest ./service_3 --cov ./service_3