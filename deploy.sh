#! /usr/bin/env bash

set -Eeuo pipefail

helm upgrade --cleanup-on-fail \
	--install engr-131-jhub jupyterhub/jupyterhub \
	--create-namespace \
	--version=3.3.8 \
	--timeout=10m \
	--values config.yml
