import subprocess
import time
from selenium import webdriver
from config import (ssh_host, ssh_password, slack_app, phpstorm_path, url_1, url_2, YELLOW, BLUE, GREEN, RED, RESET, container_names)

# Check if containers are already running
running_containers = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True).stdout.strip().split('\n')

# Start specific containers using the command line
for container_name in container_names:
    if container_name in running_containers:
        print(f"{RED}Container {container_name} is already running...{RESET}")
    else: # Set up WebDriver (e.g., Chrome)
        print(f"{YELLOW}Starting container {container_name}...{RESET}")
        subprocess.run(["docker", "start", container_name])
        time.sleep(1)
        print(f"{BLUE}Container {container_name} started successfully!{RESET}")
    
# Print a success message after all containers have started
print(f"{GREEN}All containers started successfully!{RESET}")

# Set up ChromeOptions to launch Chrome in incognito mode
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
time.sleep(1)
print(f"{YELLOW}Starting the browser...{RESET}")

# Set up WebDriver (e.g., Chrome)
driver = webdriver.Chrome(options=chrome_options)

# Load the first page
driver.get(url_1)   

# Maximize the window
driver.maximize_window()

# Open a new tab and switch to it
driver.execute_script("window.open();")
driver.switch_to.window(driver.window_handles[1])

# Load the second page
driver.get(url_2)

# Maximize the window
driver.maximize_window()

# Switch to the second window if it exists
if len(driver.window_handles) > 2:
    driver.switch_to.window(driver.window_handles[2])
    driver.close()
    
# Print a success message
print(f"{GREEN}{url_1} and {url_2} loaded successfully in the browser!{RESET}")

# Start Slack
time.sleep(1)
print(f"{YELLOW}Starting the Slack app...{RESET}")
subprocess.run([slack_app])  

# Print a success message
print(f"{GREEN}Slack loaded successfully!{RESET}")

# Start Ubuntu terminal and connect via SSH
print(f"{YELLOW}Starting Ubuntu terminal and connecting via SSH to {ssh_host}...{RESET}")
subprocess.Popen(["gnome-terminal", "--", "bash", "-c", f"sshpass -p {ssh_password} ssh {ssh_host}; exec bash"])
print(f"{GREEN}SSH connection to {ssh_host} established successfully!{RESET}")

# Start PhpStorm
time.sleep(1)
print(f"{YELLOW}Starting PhpStorm...{RESET}")
subprocess.Popen([phpstorm_path])
print(f"{GREEN}PhpStorm started successfully!{RESET}")


# The browser will now stay open until you manually stop the script
while True:
    try:
        time.sleep(1)
    except KeyboardInterrupt:
        driver.quit()
        break