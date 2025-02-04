<h1> Steps to Deploy application using azure cloud infrastructure</h1>

<p>Instead of traditional architecture, we'll use Docker containers deployed on an AWS EC2 instance to ensure a scalable, 
portable, and efficient deployment. The application will be containerized and pushed to Docker Hub, allowing for easy 
distribution and version control. On the EC2 instance, we'll pull the container image from Docker Hub and run it, 
ensuring a consistent environment across deployments. This approach eliminates dependency conflicts, simplifies updates 
by pulling new images when needed, and enhances maintainability. Additionally, we can automate the deployment process 
using a CI/CD pipeline and configure reverse proxy (e.g., Nginx) or a load balancer for better performance and availability.<p>

<hr>

<h2>Steps to write single stage dockerfile</h2>
<ol>
    <li>Create a file inside the root directory of project and name it as 'Dockerfile'</li>
    <li>define base image
        <p><code>FROM node:16</code>   ::  it sets the base image as node versioon 16.0 ensuring node is preinstalled</p>
    </li>
    <li>setting up the working directory
        <p><code>WORKDIR /usr/src/apa</code>   :: it works as a working directory inside the container. Commands below this will be ececuted inside this directory</p>
    </li>
    <li>copy json packages to install all dependencies inside the container
        <p><code>COPY package*.json ./</code>   :: this line copies package*.json means it will copy file starting with package, * means anything and ending with .json to the root folder</p>
        <p><code>RUN npm install</code>  ::  RUN command is used to execute a command inside the container, here 'npm install' is executed in order to install all dependencies written in json</p>
    </li>
    <li>Copy App files to the container
        <p><code>COPY . .</code>  :: ".  ." copies all files from project directory to the container</p>
    </li>
    <li>Expose your desired port
        <p><code>EXPOSE 5000</code>   ::  this command exposes port 5000 for application</p>
    </li>
    <li>Start Applicaiton
        <p><code>CMD ["node", "index.js"]</code>  :: it specifies the default command to run when the container starts. where, index.js is the entry point of the application</p>
    </li>
</ol>


<hr>

<h2>Steps to Push Docker Image to Docker Hub</h2>
<ol>
    <li>Go to the root directory of the application</li>
    <li>Build the Docker image:
        <p><code>docker build -t your-dockerhub-username/node-app .</code>   :: this command builds a Docker image named 'node-app' from the current directory where, -t is used to assign a name to the image</p>
    </li>
    <li>Login to Docker Hub:
        <p><code>docker login</code>  :: use your docker login credentials</p>
    </li>
    <li>Tag the Docker image:
        <p><code>docker tag your-dockerhub-username/node-app your-dockerhub-username/node-app:v1</code>  :: this command tags the built image as 'node-app:v1'</p>
    </li>
    <li>Push the image to Docker Hub:
        <p><code>docker push your-dockerhub-username/node-app:v1</code>  :: this command pushes the tagged image to Docker Hub</p>
    </li>
</ol>

<hr>

<h2>Setting up AWS EC2</h2>
<ol>
    <li>Create an account on AWS and sign in.</li>
    <li>Go to the AWS console and create an EC2 instance.</li>
    <li>Name your instance</li>
    <li>choose your AMI from several option. I'm going for "Ubuntu server", select your instance type depending on needs</li>
    <li>Generate a new key pair that will you access your EC2 instance.</li>
    <li>Inside network setting, click on Allow SSH, HTTP and HTTPS for inbound traffic on ports 22, 80 and 443 to enable remote access and remote server access.</li>
    <li> Click "launch instance"</li>
    <li>Go to instance summary, click on "connect"
    <p> we'll be working with "ssh" so click on "SSH client", copy ssh code.
    </p></li>
</ol>

<hr>

<h2>SSH into AWS EC2 and setting up the server</h2>
<ol>
    <li>Open terminal, paste ssh code and press enter
    <p> <code> ssh -i "location-of-your-key.pem" username@public-ip.your-region.compute.amazonaws.com</code>
    </p></li>
    <li>once logged in, update the system using <code>sudo apt-get update</code></li>
    <li>install docker using <code>sudo apt-get install docker.io</code></li>
    <li>start and run docker using <code>sudo systemctl docker start</code> and enable it using <code>sudo systemctl enable docker</li>
    <li>once installed, add your USER to docker group using <code>sudo usermod -aG docker $USER</code> and reboot your system using <code>sudo reboot</code></li>
    <li>ssh into your EC2 instance</li>
    <li>verify docker installation using <code>docker --version</code></li>
    <li>pull the image from docker hub using <code>docker pull your-dockerhub-username/node-app:version</code>
    <p>Verify using image<code>docker images</code></p></li>
    <li>Now Spin up the container using <code>docker run -d -p 3000:3000 your-dockerhub-username/node-app:version</code>
    <p><code> -d -p </code> :: -d for detached mode and -p for port mapping</p>
    </li>
    <li>Verify using <code>docker ps</code></li>
</ol>

<hr>

<h2>Access node application</h2>
<ol>
    <li>copy your EC2 public IP</li>
    <li>paste the link into your local browser</li>
</o>

<h3>Congo : your node application is successfully deployed</h3>