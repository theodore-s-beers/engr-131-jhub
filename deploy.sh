#! /usr/bin/env bash

set -Eeuo pipefail

if [[ -f .env ]]; then
	source .env
fi

envsubst <config.yml >config_rendered.yml

helm upgrade --cleanup-on-fail \
	--install engr-131-jhub jupyterhub/jupyterhub \
	--namespace jhub \
	--create-namespace \
	--version=3.3.8 \
	--timeout=10m \
	--values config_rendered.yml

envsubst <config_exams.yml >config_exams_rendered.yml

helm upgrade --cleanup-on-fail \
	--install engr-131-jhub-exams jupyterhub/jupyterhub \
	--namespace jhub-exams \
	--create-namespace \
	--version=3.3.8 \
	--timeout=10m \
	--values config_exams_rendered.yml
