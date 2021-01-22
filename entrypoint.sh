#!/usr/bin/env bash

cd server
PYTHONPATH=. python wsgi.py &

cd ../client

npm install
HOST=0.0.0.0 npm run serve -D