#!/bin/bash

SERVER="localhost"

curl -s http://${SERVER}:8000/getall | jq . > /dev/null 2>&1
[[ $? == 0 ]] && { echo "API Test Passed .."; } || { echo "API test failed .."; exit 1; } 

curl -s http://${SERVER}:8000/doNotExist | jq . > /dev/null 2>&1
[[ $? == 4 ]] && { echo "API Negative Test Passed .."; } || { echo "API Negative test failed .."; exit 1; }

