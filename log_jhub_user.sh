#! /usr/bin/env bash

set -Eeuo pipefail

LOG_FILE="/var/log/jhub_user.log"

if [ -z "$JUPYTERHUB_USER" ]; then
	echo "JUPYTERHUB_USER is not set" >&2
	exit 1
fi

echo "$JUPYTERHUB_USER" >>"$LOG_FILE"
