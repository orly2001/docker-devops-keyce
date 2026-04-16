pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials')
        IMAGE_NAME = "jokers577/tchoudjidombouyvanjunior-flask-app"
    }

    stages {

        stage('Clonage') {
            steps {
                echo 'Clonage du depot GitHub...'
                git branch: 'main',
                    url: 'https://github.com/orly2001/docker-devops-keyce.git'
            }
        }

        stage('Image') {
            steps {
                echo 'Construction de l image Docker...'
                sh 'docker build -t ${IMAGE_NAME}:latest .'
            }
        }

        stage('Publication') {
            steps {
                echo 'Publication sur DockerHub...'
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push ${IMAGE_NAME}:latest'
            }
        }
    }

    post {
        success {
            echo 'Pipeline execute avec succes !'
        }
        failure {
            echo 'Echec du pipeline.'
        }
    }
}
