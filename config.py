# SSH connection details
ssh_host = "USER@YOUR_SERVER_IP_ADDRESS"
ssh_password = "YOUR_USER_PASSWORD"

# Set the Slack app path
slack_app = '/snap/bin/slack'

# Set the PhpStorm path
phpstorm_path = '/snap/bin/phpstorm'

# Set the URLs you want to open
url_1 = 'https://YOUR_WEBSITE_1.com/'
url_2 = 'https://YOUR_WEBSITE_2.com/'

# Define ANSI escape sequences for color formatting
YELLOW = '\033[93m'
BLUE = '\033[94m'
GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

# Replace with the names of the containers you want to start
container_names = [
    'elasticsearch-main', 
    'kb-container', 
    'mailhog', 
    'mariadb', 
    'phpmyadmin', 
    'portainer', 
    'traefik', 
    
    'another_app'
]