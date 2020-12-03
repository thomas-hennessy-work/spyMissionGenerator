#!/bin/bash
docker build -f ./service_4/tests/Dockerfile -t thomashennessy/service_4_unittest:spy-app .
docker run -it -d --name service_4_tests thomashennessy/service_4_unittest:spy-app
docker exec service_4_tests pytest ./service_4 --cov ./service_4