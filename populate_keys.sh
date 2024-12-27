#! /bin/bash

set -Eeuo pipefail

TARGET_DIR=/home/jovyan
FILES=("client_private_key.bin" "server_public_key.bin")

for file in "${FILES[@]}"; do
	if [ ! -f "${TARGET_DIR}/.${file}" ]; then
		cp "/opt/dotfiles/.${file}" "${TARGET_DIR}/.${file}"
		chown jovyan:users "${TARGET_DIR}/.${file}"
	fi
done
