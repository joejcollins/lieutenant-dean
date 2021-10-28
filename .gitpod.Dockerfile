FROM gitpod/workspace-full

# Redis
RUN sudo apt-get -q update \
 && sudo apt-get install -yq redis-server
 