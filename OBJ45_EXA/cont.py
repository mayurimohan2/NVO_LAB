import docker

# Define the name of the container
container_name = "bgp"

# Define the name of the image
image_name = "bgp"

# Define the command to run in the container
command = "ryu-manager"

# Define the arguments to pass to the command
args = "--ofp-tcp-listen-port 6653 ryu.app.simple_switch"

# Create a Docker client object
client = docker.from_env()

# Pull the Docker image
#client.images.pull(image_name)

container_config = {
    'image': 'exabgp',
    'privileged': True,
    'tty': True,
    'stdin_open': True,
    'name': 'my-exa1'
    
}


# Create the Docker container
container = client.containers.create(**container_config)
#image_name, privileged: True, name=container_name, command=command, ports={'6653/tcp': 6653}, detach=True)

# Start the Docker container
container.start()

# Print the status of the container
print("Container status: ", container.status)

# Print the logs of the container
print(container.logs().decode())

# Stop and remove the container

