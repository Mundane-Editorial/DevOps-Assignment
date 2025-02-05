<h3>1. Update system</h3>
<code>sudo apt-get update</code>
<p>this updates th package lists on the system</p>
<hr>
<h3>2. installing NGINX</h3>
<code>sudo apt install nginx -y</code>
<p>this command updaets nginx on your system</p>
<hr>
<h3>3. installing Git</h3>
<code>sudo apt install git -y</code>
<p>this command installs git for managing repository</p>
<hr>
<h3>4. installing Nodejs, npm</h3>
<code>udo apt install nodejs npm -y</code>
<p>installs nodejs for running jscript on server and npm for managing dependencies</p>
<hr>
<h3>5. installing Nodejs, npm</h3>
<code>
sudo apt install ufw -y
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
sudo ufw enable
</code>
<p>installs ufw for setting up firewall, opens port 22 for ssh and port 80 and 443 for http and https, and then enables it</p>
<hr>
<h3>6. start nginx server </h3>
<code>
sudo systemctl start nginx
sudo systemctl enable nginx
</code>
<p>it starts nginx server and ensures automatically starts after a system reboot</p>
<hr>
<h3>7. verify nginx status</h3>
<code>
sudo systemctl status nginx
</code>
<p>verifies running status of nginx server</p>
<hr>
<h3>8. copying server configuration file</h3>
<code>
if [ -f "/path/of/server_config.js" ]; then
    sudo cp /path/of/server_config.js /var/www/html/server_config.js
    echo "server_config.js copied successfully."
else
    echo "Error: server_config.js not found at /path/of/server_config.js"
fi
</code>
<p>using conditional status, it copies server_config.js to /var/www/html directory and provides acknowledgement of task completion.</p>
<hr>