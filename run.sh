## when I add the predictions volume, I run into permission errors as I am not allowed to read/write to that folder with the default user. That is why I omitted that volume here.
docker run -v "$(pwd)"/data/test:/data/test -it --entrypoint /bin/bash  stss-eval

# docker run -v "$(pwd)"/data/test:/data/test -v "$(pwd)"/predictions:/predictions -it stss-eval

# docker run -v "$(pwd)"/data/test:/data/test -v "$(pwd)"/predictions:/predictions -it --entrypoint /bin/bash stss-eval
