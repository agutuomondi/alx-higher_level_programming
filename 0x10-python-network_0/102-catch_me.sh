#!/bin/bash
#script makes request to 0.0.0.0:5000/catch_me
curl -s -X PUT -d "user_id=98" -L -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
