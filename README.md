# Docker Workflow Automation Script

[![Licence](https://img.shields.io/github/license/Ileriayo/markdown-badges?style=for-the-badge)](./LICENSE)

## Overview

This is a Docker **workflow automation script** build with Python that automates the start and stop of specific tasks like:

- Start the Docker (Portainer) containers *
- Launches Chrome in incognito mode with two URLs
- Opens the Slack app
- Open the PhpStorm app
- Loading Ubuntu terminal and SSH login to the remote server.

**Note:** For this automation script to work is requred to use [Docker Local Web Server](https://github.com/mnestorov/docker-local-web-server) and [Docker Project Container with PHP 8+ and Apache](https://github.com/mnestorov/docker-poject-container)

## Prerequisites

- Docker
- Python 3.x
- Chrome browser
- Slack app
- PhpStorm
- sshpass

## Installation

1. Clone the repository to your local machine.
2. Install Docker, Python 3.x, and the Chrome browser.
3. Install the Slack app and PhpStorm on your machine.
4. Open a terminal and navigate to the directory containing the cloned repository.

**Run the following command to start the automation script:**

```
python3 start_services.py
```

Also we need to install the python3-pip package.

**Open a terminal and run the following command:**

```
sudo apt update
sudo apt install python3-pip
```

Also make sure you have Selenium and the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) installed.

**To install Selenium, run this command:**

```
pip3 install selenium
```

If you want to execute the `ssh` command with a `password`, you can use `sshpass`.

**You'll need to install it first using the following command in your terminal:**

```
sudo apt-get install sshpass
```

## Usage

When you run the Python script, it will automatically start the Docker containers listed in the **container_names** array, launch Chrome in incognito mode with the URLs specified in **url_1** and **url_2**, and open the Slack app.

To stop the automation, simply press `CTRL+C` in the terminal.

# Bash Automation Script

This is a Bash script that automates the start of the Python automation script. 

**We need to make the Bash script executable by running:**

```
chmod +x start_services.sh
```

## Usage

### **Start Script**

**To start the automation script, simply run the following command in the terminal:**

```
./start_services.sh
```

The Python automation script will start running, and you can use `CTRL+C` to stop it.

### **Stop Script**

**To stop the automation script, simply run the following command in the terminal:**

```
./stop_services.sh
```

The Python automation script will start running, and you can use `CTRL+C` to stop it.

## Run the script at startup

To run the script at startup on Ubuntu 22.04, you have a few options.

**One common approach is to add an entry to the "Startup Applications" tool:**

- Open the "Startup Applications" tool by searching for it in the Activities overview or running `gnome-session-properties` in the terminal.
- Click the "Add" button.
- Fill in the "Name" field (e.g., "Start Services").
- In the "Command" field, enter the full path to the start_services.sh script (e.g., `/home/YOUR_USERNAME/path/to/script/start_services.sh`).
- Click "Add" and close the "Startup Applications" tool.

Now, the bash script will run automatically when you log in to your Ubuntu system, starting the Python script that start Docker containers, start Slack and PhpStorm apps and opens the browser and loading two web pages, specified at the `config.py` file.

Please note that this approach will only work when you log in with a graphical environment, as it relies on the GNOME startup applications feature. If you need to run the script in a non-GUI environment or before user login, you may need to use a different method, such as a systemd service or a cron job.

## Troubleshooting

**If you encounter any issues while running the script, check the following:**

- Ensure that Docker, Python 3.x, the Chrome browser, the Slack app, and the PhpStorm are installed correctly.
- Check that the Docker containers specified in **container_names** are correct and running.
- Check that the URLs specified in **url_1** and **url_2** are correct.
- If Slack does not open, check that the path to the Slack app is correct.

## TODOs

- Add functionality to check if the required Docker images are available, and if not, download them.
- Add a feature to automatically download and install the required versions of Chrome and ChromeDriver.
- Add the ability to start and stop the Docker containers with a single command, instead of running separate Python scripts for each.
- Add support for more web browsers, such as Firefox or Edge.
- Implement error handling and logging to make it easier to debug issues.
- Create a command-line interface to make it more user-friendly and configurable.
- Add the ability to run tests or automated tasks on the loaded web pages.
- Add the ability to configure and use multiple profiles in the web browsers.
- Integrate with a Continuous Integration (CI) tool, such as Jenkins or Travis CI, to automate testing and deployment.
- Implement a scheduling feature to automatically run the script at specified intervals.

## Docker Server and Project Container Repositories

- [Docker Local Web Server](https://github.com/mnestorov/docker-local-web-server)
- [Docker Project Container with PHP 8+ and Apache](https://github.com/mnestorov/docker-poject-container)

## License

This project is licensed under the MIT License.
