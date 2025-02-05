#!/bin/bash

# Update system
echo "Updating system..."
sudo apt update -y

# Nginx
echo "Installing Nginx..."
sudo apt install nginx -y

# Install Git
echo "Installing Git..."
sudo apt install git -y

# Install Node.js (and npm)
echo "Installing Node.js and npm..."
sudo apt install nodejs npm -y

# Install uhncooplicated firewall and allow Nginx HTTP/HTTPS
echo "Setting up firewall..."
sudo apt install ufw -y
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable

# Start Nginx and enable it to start on boot
echo "Starting Nginx..."
sudo systemctl start nginx
sudo systemctl enable nginx

# Check the status of Nginx service
echo "Verifying Nginx status..."
sudo systemctl status nginx

# Check if server_config.js exists before copying
SERVER_CONFIG_PATH="/path/of/server_config.js"
NGINX_DIR="/var/www/html"

if [ -f "$SERVER_CONFIG_PATH" ]; then
    sudo cp "$SERVER_CONFIG_PATH" "$NGINX_DIR/server_config.js"
    echo "server_config.js copied successfully."
else
    echo "Error: server_config.js not found at $SERVER_CONFIG_PATH"
fi

# Print completion message
echo "Server setup complete! You can now access the server configuration at http://localhpost:PORT/server_config.js"

# End
