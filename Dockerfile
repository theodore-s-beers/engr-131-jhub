FROM jupyter/base-notebook:latest

LABEL maintainer="Theo Beers <theo.beers@drexel.edu>"

# Switch to root user to install dependencies
USER root

# Install system-level dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    build-essential \
    wget \
    curl \
    portaudio19-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python libraries
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

# Copy key files
COPY .client_private_key.bin .server_public_key.bin /opt/dotfiles/
RUN chmod -R a+r /opt/dotfiles

# Create JHub username log file, set permissions
RUN touch /var/log/jhub_user.log \
    && chmod 640 /var/log/jhub_user.log

# Copy logging script into container
COPY log_jhub_user_arm64 /usr/local/bin/log_jhub_user_arm64
RUN chmod 4755 /usr/local/bin/log_jhub_user_arm64

# Invalidate cache for following steps
ARG CACHE_BUSTER=latest

# Install PyKubeGrader (frequently updated)
RUN pip install --no-cache-dir --upgrade pykubegrader

# Set permissions for default JupyterHub user
RUN fix-permissions /home/jovyan

# Switch back to default notebook user
USER ${NB_UID}

# Expose Jupyter port
EXPOSE 8888

# Start single-user notebook server
CMD ["start-notebook.sh", "--NotebookApp.token=''"]
