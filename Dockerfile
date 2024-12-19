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
    iputils-ping \
    netcat \
    dnsutils \
    iproute2 \
    traceroute \
    tcpdump \
    net-tools \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Python libraries
COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r /tmp/requirements.txt \
    && rm /tmp/requirements.txt

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
