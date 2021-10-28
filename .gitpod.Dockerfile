FROM gitpod/workspace-full:latest

# Redis
RUN sudo apt-get update \
 && sudo apt-get install -y redis-server \
 && sudo rm -rf /var/lib/apt/lists/*

# Nodejs
RUN sudo apt-get install -y npm \
 && sudo npm install -g n \
 && sudo n stable \
 && sudo npm install -g redis-commander
