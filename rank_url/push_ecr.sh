#!/bin/bash


aws ecr get-login-password --region ap-northeast-2 | docker login --username AWS --password-stdin 593634833876.dkr.ecr.ap-northeast-2.amazonaws.com
docker build -t rank_url .
docker tag rank_url:latest 593634833876.dkr.ecr.ap-northeast-2.amazonaws.com/lambda-function:rank_url
docker push 593634833876.dkr.ecr.ap-northeast-2.amazonaws.com/lambda-function:rank_url
