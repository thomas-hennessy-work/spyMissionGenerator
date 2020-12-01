#!/bin/bash
docker build -f service_1/Dockerfile -t thomashennessy/app:mission service_1/
docker build -f service_2/Dockerfile -t thomashennessy/dossiernumgen:mission service_2/
docker build -f service_3/Dockerfile -t thomashennessy/dossierchargen:mission service_3/