#!/bin/bash
docker build -t onion ./tor_server
docker run -p 8000:80 -p 2222:22 onion