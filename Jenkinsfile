pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'compose.yaml'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: '5f98fae6-a885-4ec8-85d6-55222cd53cb9', url: 'https://github.com/dessisdakova/Automated-Testing-of-Mock-API-Database-and-Web-UI'
            }
        }

        stage('Build Docker Containers') {
            steps {
                script {
                    sh 'docker-compose up -d --build'
                }
            }
        }

        stage('Run All Tests') {
            steps {
                script {
                    sh 'docker-compose run tests'
                }
            }
        }

        stage('Tear Down') {
            steps {
                script {
                    sh 'docker-compose down'
                }
            }
        }
    }
}