FROM gitpod/workspace-postgres

# Redis
RUN sudo apt-get update \
 && sudo apt-get install -y redis-server \
 && sudo rm -rf /var/lib/apt/lists/*
