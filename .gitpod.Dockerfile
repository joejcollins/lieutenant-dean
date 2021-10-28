FROM gitpod/workspace-full

# Redis
RUN sudo apt-get update \
 && sudo apt-get install -y redis-server \
 && sudo rm -rf /var/lib/apt/lists/* \
 && sudo apt install npm \
 && sudo npm install -g n \
 && sudo n stable \
 && sudo npm install -g redis-commander \
 && curl -fsSL https://starship.rs/install.sh | bash -s -- --yes
