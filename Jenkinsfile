pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests in Docker') {
            steps {
                sh '''
                # Pull python image
                docker pull python:3.12-slim

                # Run tests inside container
                docker run --rm -v $PWD:/app -w /app python:3.12-slim /bin/bash -c "
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    pytest --junitxml=test-results.xml
                "
                '''
            }
        }
    }

    post {
        always {
            junit '**/test-results.xml'
        }
    }
}
