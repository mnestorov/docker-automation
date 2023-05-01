import subprocess
import time
from config import (YELLOW, BLUE, GREEN, RED, RESET, container_names)

# Check if containers are already running
running_containers = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True).stdout.strip().split('\n')

# Check if containers are stopped
stopped_containers = subprocess.run(["docker", "ps", "-a", "--filter", "status=exited", "--format", "{{.Names}}"], capture_output=True, text=True).stdout.strip().split('\n')

# Stop specific containers using the command line
for container_name in container_names:
    if container_name in stopped_containers:
        print(f"{RED}Container {container_name} is already stopped...{RESET}")
    elif container_name in running_containers:
        print(f"{YELLOW}Stopping container {container_name}...{RESET}")
        subprocess.run(["docker", "stop", container_name])
        time.sleep(1)
        print(f"{BLUE}Container {container_name} stopped successfully!{RESET}")
    else:
        print(f"{RED}Container {container_name} not found!{RESET}")

# Print a success message
print(f"{GREEN}All containers was stopped successfully!{RESET}")