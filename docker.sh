#!/bin/bash
docker  run -it  --gpus  all  -v /home/songyi:/home/songyi -w /home/songyi/worker/123/forklift/darknet3  daisukekobayashi/darknet  bash