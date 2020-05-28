FROM autonaomi-base:latest

EXPOSE 7700

CMD python -m autonaomi.server run-server -h '0.0.0.0' -p 7700 'rabbitmq://127.0.0.1:5672/'