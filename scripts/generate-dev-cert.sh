#!/usr/bin/env bash
set -euo pipefail

mkdir -p certs

openssl req -x509 -newkey rsa:2048 -nodes -days 365 \
  -keyout certs/localhost.key \
  -out certs/localhost.crt \
  -subj "/CN=localhost"

echo "Generated certs/localhost.crt and certs/localhost.key"
