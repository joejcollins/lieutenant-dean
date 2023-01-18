FROM gitpod/workspace-full:latest

# Redis and RabbitMQ
RUN sudo apt-get update \
 && sudo apt-get install redis-server -y \
 && sudo apt-get install rabbitmq-server -y --fix-missing

USER gitpod

RUN cd /home/gitpod/.pyenv \
 && git pull \
 && pyenv install 3.9.15 --skip-existing 
