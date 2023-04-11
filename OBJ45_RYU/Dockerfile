FROM python:3.9-slim

# Install required packages
RUN apt-get update && apt-get install -y     git     libffi-dev     libssl-dev     libxml2-dev     libxslt1-dev     libz-dev     python3-dev

# Clone Ryu repository
RUN git clone https://github.com/osrg/ryu.git /ryu

# Install Ryu
RUN cd /ryu && python3 -m pip install .

# Expose the necessary ports
EXPOSE 6633 6653

# Start the Ryu controller
CMD [ "ryu-manager" ]

