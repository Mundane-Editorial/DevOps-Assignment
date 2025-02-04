<h2>Managing Environment variables and Secrets</h2>
<p>Environment variables are used to store sensitive information that should not be exposed to the public. They can be used to configure the application or other services. Whereas, Secrets are used to store sensitive information that should not be exposed to the public. They can be used to configure the application or other services.</p>
<p>jenkins provides multiple ways to manage environment variables and secrets securely ensuring the security.</p>
<p>methods as follows, </p>

<h4>1. Defining Environment Variables in pipeline</h4>
<code>
    pipeline {
    agent any

    environment {
        REPO_URL = "https://github.com/Mundane-Editorial/DevOps-Assignment.git"
        TARGET_DIR = "Cloud-Infrastructure-and-Deployment/node-application"
        DOCKER_IMAGE = "mundaneeditorial/node-application:lts"
    }

    stages {
        stage("Code Clone") {
            ..
        ..
    ..    
</code>
<p>we can define environment variables globally in the pipeline itself. Although it's not recommended as everything is visible and the values can be printed but it's easy to use </p>

<hr>

<h4>2. Storing Secrets Securely Using Jenkins Credentials Plugin</h4>
<code>
pipeline {
    agent any

    environment {
        REPO_URL = "https://github.com/Mundane-Editorial/DevOps-Assignment.git"
        TARGET_DIR = "Cloud-Infrastructure-and-Deployment/node-application"
        DOCKER_IMAGE = "mundaneeditorial/node-application:lts"
    }

    stages {
        stage("Code Clone") {
            steps {
                ...
            }
        }

        stage("Building Docker Image") {
            steps {
                ...
            }
        }

        stage("Push to Docker Hub") {
            steps {
                withCredentials([usernamePassword(credentialsId: 'DockerHUB', usernameVariable: 'userName', passwordVariable: 'userPass')]) {
                    echo "Docker Login"
                    sh "docker login -u $userName -p $userPass"
                    echo "Pushing Docker image to Hub"
                    sh "docker push ${DOCKER_IMAGE}"
                }
                echo "successfully pushed to Dockerhub"
            }
        }
...
</code>
<p>This is the recommended way to store secrets in jenkins. Highly secure and prevents secrets from being exposed in logs.</p>

<hr>