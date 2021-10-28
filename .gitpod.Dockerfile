FROM gitpod/workspace-full
USER gitpod

# Redis
RUN sudo apt-get update \
 && sudo apt-get install -y redis-server \
 && sudo rm -rf /var/lib/apt/lists/* \
 && curl -fsSL https://starship.rs/install.sh | bash -s -- --yes
