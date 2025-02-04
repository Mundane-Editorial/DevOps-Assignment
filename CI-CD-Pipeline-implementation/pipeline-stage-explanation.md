<h1>Code clone</h1>
<p>This stage handles the process of cloning the repository and checking out the required directory for further steps.</p>
<ol>
    <li><code>rm -rf workspace </code> : remove any existing workspace directory.</li>
    <li><code>git clone --no-checkout $REPO_URL workspace </code> : clones the repository without checking out any files at all.</li>
    <li><code>cd workspace </code> : </li>
    <li><code>git sparse-checkout init --cone </code> : Initializes sparse-checkout to allow fetching only parts of the repository</li>
    <li><code>git sparse-checkout set $TARGET_DIR </code> : pull the specific directory</li>
    <li><code>git checkout master </code> : switch to master brach</li>
</ol>

<hr>

<h1>Building Docker image</h1>
<p>This stage builds the Docker image for the node application from the directory that was cloned earlier</p>
<ol>
    <li><code>dir("workspace/$TARGET_DIR") </code> : changes directory to one with applicaiton files.</li>
    <li><code>sh "docker build -t ${DOCKER_IMAGE} ." </code> : it builds a Docker image using the Dockerfile in the current directory (.) and tags it with the name specified in the DOCKER_IMAGE variable</li>
    <li><code>cd workspace </code> : </li>
    <li><code>git sparse-checkout init --cone </code> : Initializes sparse-checkout to allow fetching only parts of the repository</li>
    <li><code>git sparse-checkout set $TARGET_DIR </code> : pull the specific directory</li>
    <li><code>git checkout master </code> : switch to master brach</li>
</ol>

<hr>

<h1>Push To Docker Hub</h1>
<p>This stage logs into Docker Hub and pushes the built Docker image to the registry.</p>
<ol>
    <li><code>withCredentials([usernamePassword(credentialsId: 'DockerHUB', usernameVariable: 'userName', passwordVariable: 'userPass')]) </code> : It retrieves Docker login credentials using DockerHUB credentials ID stored in jenkins.</li>
    <li><code>echo "Docker Login" </code> : for validation purpose nothing else</li>
    <li><code>sh "docker login -u $userName -p $userPass" </code> : logs into Docker hub using the credentials provided.</li>
    <li><code>sh "docker push ${DOCKER_IMAGE}" </code> : pushes docker image to docker hub</li>
</ol>

<hr>

<h1>Deploy</h1>
<p>This stage deploys the application using Docker Compose.</p>
<ol>
    <li><code>sh "docker-compose down && docker-compose up -d" </code> : "docker-compose down" stops and removes the container defined in docker-compose.yml file && ""docker-compose up -d" rebuild and starts the container in detached mode.</li>
</ol>

