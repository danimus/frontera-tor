#!/bin/bash

export FRONTERA_DIR=$(pwd)

SEED_FILE="seed.txt"

declare -A commands

commands=(
["broker"]="python -m frontera.contrib.messagebus.zeromq.broker"
["worker"]="python -m frontera.worker.db --config tor.settings"
["spider0"]="scrapy crawl general -L INFO -s SEEDS_SOURCE=$SEED_FILE -s SPIDER_PARTITION_ID=0s"
["spider1"]="scrapy crawl general -L INFO -s FRONTERA_SETTINGS=tor.settings -s SPIDER_PARTITION_ID=1"
)

for key in ${!commands[@]}; do
   echo "Starting ${key}"
   screen -d -m -S ${key} bash -c "${commands[${key}]}"
done