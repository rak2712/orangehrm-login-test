pipeline {
    agent {
        docker {
            image 'python:3.10'
        }
    }

    environment {
        PYTHONUNBUFFERED = 1
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        always {
            junit '**/test-results.xml'
        }
    }
}
