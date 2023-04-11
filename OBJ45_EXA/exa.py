#!/usr/bin/env python

import os

# Define the base image
base_image = "ubuntu:latest"

# Define the packages required for Ryu Controller
packages = ["git", "python-pip"]

# Define the Ryu Controller repository URL
ryu_repo = "https://github.com/osrg/ryu.git"

# Define the working directory for the Ryu Controller
working_dir = "/home/ryu"

# Define the command to start the Ryu Controller
entry_point = "/bin/bash"

# Define the ports to expose
ports = ["6633"]

# Create the Dockerfile contents
dockerfile_contents = f"""FROM ubuntu:20.04

# Update the package list and install dependencies
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    libssl-dev \
    libffi-dev \
    libpcre3-dev \
    libdumbnet-dev \
    python3-pip \
    exabgp \
    && rm -rf /var/lib/apt/lists/*

# Clone ExaBGP repository
RUN git clone https://github.com/Exa-Networks/exabgp.git /tmp/exabgp

# Install ExaBGP
RUN cd /tmp/exabgp && python3 setup.py install

# Clean up
RUN rm -rf /tmp/exabgp
"""

# Write the Dockerfile contents to a file
with open("Dockerfile", "w") as f:
    f.write(dockerfile_contents)

print("Dockerfile created successfully!")
