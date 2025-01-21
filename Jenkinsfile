pipeline {
    agent any

    environment {
        COMPOSE_FILE = 'compose.yaml'
    }

    stages {
        stage('Checkout') {
            steps {
                git credentialsId: '688dc148-0b71-4853-a39d-9f8dfc606d1c', url: 'https://github.com/dessisdakova/Automated-Testing-of-Mock-API-Database-and-Web-UI'
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