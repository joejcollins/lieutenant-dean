FROM gitpod/workspace-postgres

# Redis and RabbitMQ
RUN sudo apt-get update \
 && sudo apt-get install redis-server -y \
 && sudo apt-get install rabbitmq-server -y --fix-missing

RUN (cd ~/.pyenv; git pull)  \
 && pyenv install 3.9.15 --skip-existing 
