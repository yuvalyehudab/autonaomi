echo "let's start"
echo "The autonaomious project"
docker run -d -p 5672:5672 --name mqueue rabbitmq
docker run -d -p 27017:27017 --name dbyuv mongo

echo "images running, wait a minute"
docker build -t autonaomi-base .
docker volume create --name naomemory
docker build -t auto-server autonaomi/server
docker build -t auto-saver autonaomi/saver
docker build -t auto-parser autonaomi/parsers
docker build -t auto-api autonaomi/api
docker build -t auto-gui autonaomi/gui

echo "waiting 30 sec"
sleep 30s

docker run -d -v naomemory:/root/autonaomi_data --network=host auto-server:latest

docker run -d -e PARSER='color_image' --network=host -v naomemory:/root/autonaomi_data auto-parser:latest
docker run -d -e PARSER='depth_image' --network=host -v naomemory:/root/autonaomi_data auto-parser:latest
docker run -d -e PARSER='feelings' --network=host auto-parser:latest
docker run -d -e PARSER='pose' --network=host auto-parser:latest

docker run -d -v naomemory:/root/autonaomi_data --network=host auto-saver:latest

docker run -d -v naomemory:/root/autonaomi_data --network=host auto-gui:latest

docker run -d -v naomemory:/root/autonaomi_data --network=host auto-api:latest
