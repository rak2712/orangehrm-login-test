pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install System Dependencies') {
            steps {
                sh '''
                apt-get update && apt-get install -y \
                    unzip curl \
                    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
                    libnspr4 libnss3 libxss1 libxcomposite1 libxcursor1 libxdamage1 \
                    libxrandr2 xdg-utils \
                && rm -rf /var/lib/apt/lists/*
                '''
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
                export DISPLAY=:0
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
