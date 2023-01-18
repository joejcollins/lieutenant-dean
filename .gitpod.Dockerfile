FROM gitpod/workspace-python:latest

# Redis and RabbitMQ
RUN sudo apt-get update \
 && sudo apt-get install redis-server -y \
 && sudo apt-get install rabbitmq-server -y --fix-missing

USER gitpod

ENV PATH="$HOME/.pyenv/bin:$HOME/.pyenv/shims:$PATH"
ENV PIPENV_VENV_IN_PROJECT=true
ENV PYENV_ROOT="$HOME/.pyenv"

RUN pyenv install 3.9.15 --skip-existing 
