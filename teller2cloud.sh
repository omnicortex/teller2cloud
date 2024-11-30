#! /bin/bash

containerid=teller2cloud-$(id -u)

set -xe

podman run --rm \
    --name $containerid \
    -v ${PWD}/tokens.csv:/teller/tokens.csv \
    -v ${PWD}/client_secrets.json:/teller/client_secrets.json \
    -v ${PWD}/credentials.json:/teller/credentials.json \
    -v ${PWD}/settings.yaml:/teller/settings.yaml \
    -v ${PWD}/teller_zip:/teller/teller \
    -v ${PWD}/.env:/teller/.env \
    -v ${PWD}/export:/teller/export \
    ghcr.io/omnicortex/teller2cloud:latest
