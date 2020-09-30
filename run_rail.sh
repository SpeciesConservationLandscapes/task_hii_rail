#!/bin/bash

docker run -it -v $PWD/.config:/root/.config scl3/task_hii_rail python hii_rail.py -r 'Afrotropic'
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_rail python hii_rail.py -r 'Australasia'
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_rail python hii_rail.py -r 'Indomalayan'
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_rail python hii_rail.py -r 'Nearctic'
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_rail python hii_rail.py -r 'Neotropic'
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_rail python hii_rail.py -r 'Oceania'
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_rail python hii_rail.py -r 'Palearctic'
docker run -it -v $PWD/.config:/root/.config scl3/task_hii_rail python hii_rail.py -r 'HighArctic'
