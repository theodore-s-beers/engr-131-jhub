#! /usr/bin/env bash

set -Eeuo pipefail

docker buildx build \
	--build-arg CACHE_BUSTER=$(date +%s) \
	--platform linux/amd64,linux/arm64 \
	-t katomyomachia/engr-131-jhub:latest \
	-f Dockerfile \
	. --push

docker buildx build \
	--platform linux/amd64,linux/arm64 \
	-t katomyomachia/engr-131-jhub-exams:latest \
	-f exams.Dockerfile \
	. --push
