pipeline {
    agent {
        docker {
            image 'selenium/standalone-chrome:latest'  // pre-built image with Chrome & chromedriver
            args '-u root:root'  // run as root to install Python packages
        }
    }

    environment {
        PATH = "/usr/local/bin:$PATH"
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
                    python3 -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    export DISPLAY=:99
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

