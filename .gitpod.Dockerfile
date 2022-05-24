FROM gitpod/workspace-postgres

# Redis and RabbitMQ
RUN sudo apt-get update \
 && sudo apt-get install redis-server -y \
 && sudo apt-get install rabbitmq-server -y --fix-missing
