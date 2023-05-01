import subprocess
import time

# Define ANSI escape sequences for color formatting
YELLOW = "\033[93m"
BLUE = "\033[94m"
GREEN = '\033[32m'
RED = '\033[31m'
RESET = "\033[0m"

# Replace with the names of the containers you want to stop
container_names = ['elasticsearch-main', 'kb-container', 'mailhog', 'mariadb', 'phpmyadmin', 'portainer', 'traefik']

# Stop specific containers using the command line
for container_name in container_names:
    print(f"{YELLOW}Stopping container {container_name}......{RESET}")
    subprocess.run(["docker", "stop", container_name])
    time.sleep(1)
    print(f"{RED}Container {container_name} stopped successfully!{RESET}")
    
# Print a success message
print(f"{GREEN}All Docker containers stopped successfully!{RESET}")