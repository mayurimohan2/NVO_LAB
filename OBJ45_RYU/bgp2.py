import os
import subprocess




dockerfile_path = "/home/nvo/Desktop"

# Define the name of the Docker image
image_name = "bgp20"

# Build the Docker image
result = subprocess.run(["docker", "build", "-t", image_name, dockerfile_path], capture_output=True)
print(result)
# Print the output of the build command
print(result.stdout.decode())
print(result.stderr.decode())