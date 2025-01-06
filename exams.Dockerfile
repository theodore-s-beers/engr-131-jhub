# Use our primary JupyterHub image as base
FROM katomyomachia/engr-131-jhub:latest

LABEL maintainer="Theo Beers <theo.beers@drexel.edu>"

# Switch to root to copy files and set permissions
USER root

# Copy any notebooks into default user's home directory
COPY notebooks/ /home/jovyan/

RUN fix-permissions /home/jovyan

# Switch back to default JupyterHub user
USER ${NB_UID}
