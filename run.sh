#!/bin/bash
docker run -v "$(pwd)"/data/test:/data/test -it --entrypoint /bin/bash  stss-eval