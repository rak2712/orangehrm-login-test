pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                pip install --upgrade pip --break-system-packages
                pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                export PATH=$HOME/.local/bin:$PATH
                pytest --junitxml=test-results.xml
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
