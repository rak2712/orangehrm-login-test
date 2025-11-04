pipeline {
    agent any

    environment {
        PATH = "$HOME/.local/bin:$PATH" // Ensure pip installed scripts are available
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
                # Make sure Python3 and pip3 are installed
                which python3 || sudo apt update && sudo apt install -y python3 python3-pip
                python3 --version
                pip3 --version

                # Upgrade pip and install requirements
                pip3 install --upgrade pip --break-system-packages
                pip3 install -r requirements.txt --break-system-packages
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
            // Publish JUnit test results
            junit '**/test-results.xml'
        }
    }
}
