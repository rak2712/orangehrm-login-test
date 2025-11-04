pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:$PATH"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies & Run Tests') {
            steps {
                sh '''
                    docker run --rm -u root:root \
                        -v $PWD:/app -w /app \
                        selenium/standalone-chrome:latest \
                        bash -c "python3 -m pip install --upgrade pip && pip install -r requirements.txt && export DISPLAY=:99 && pytest --junitxml=test-results.xml"
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
