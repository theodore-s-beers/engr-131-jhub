# Use our primary JupyterHub image as base
FROM katomyomachia/engr-131-jhub:latest

LABEL maintainer="Theo Beers <theo.beers@drexel.edu>"

# Switch to root to copy files and set permissions
USER root

# Copy any notebooks into /opt/notebooks and set permissions
COPY notebooks/ /opt/notebooks/
RUN chown -R jovyan:users /opt/notebooks && chmod -R 755 /opt/notebooks

# Switch back to default JupyterHub user
USER ${NB_UID}
