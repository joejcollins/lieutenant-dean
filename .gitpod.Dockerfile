FROM gitpod/workspace-full:latest

# Redis and RabbitMQ
RUN sudo apt-get update \
 && sudo apt-get install redis-server -y \
 && sudo apt-get install rabbitmq-server -y --fix-missing

USER gitpod

RUN git -C /home/gitpod/.pyenv pull \
 && pyenv install 3.9.15 --skip-existing 
