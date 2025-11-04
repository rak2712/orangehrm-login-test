pipeline {
    agent {
        docker {
            image 'python:3.12' // official Python image
            args '-v $HOME/.cache/pip:/root/.cache/pip'
        }
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
                python --version
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=test-results.xml'
            }
        }
    }

    post {
        always {
            junit '**/test-results.xml'
        }
    }
}
