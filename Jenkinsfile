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
                # Add the Jenkins public GPG key to trusted keys
                curl -fsSL https://pkg.jenkins.io/keys/jenkins.io.key | sudo tee /etc/apt/trusted.gpg.d/jenkins.asc
                
                # Update the package list
                sudo apt-get update
                
                # Install necessary system dependencies
                sudo apt-get install -y \
                    unzip curl \
                    fonts-liberation libappindicator3-1 libasound2 libatk-bridge2.0-0 \
                    libnspr4 libnss3 libxss1 libxcomposite1 libxcursor1 libxdamage1 \
                    libxrandr2 xdg-utils \
                && sudo rm -rf /var/lib/apt/lists/*
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                # Install Python dependencies
                pip install --upgrade pip --break-system-packages
                pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                # Set the display environment variable for X11 (for running UI-based tests)
                export DISPLAY=:0
                
                # Ensure the user's local bin is in the path
                export PATH=$HOME/.local/bin:$PATH
                
                # Run the tests and generate a JUnit XML file
                pytest --junitxml=test-results.xml
                '''
            }
        }
    }

    post {
        always {
            // Archive test results
            junit '**/test-results.xml'
        }
    }
}
