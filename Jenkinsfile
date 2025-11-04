pipeline {
    agent any

    environment {
        PATH = "$HOME/.local/bin:/usr/local/bin:$PATH"
        DISPLAY = ":0"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python Dependencies') {
            steps {
                sh '''
                    python3 -m pip install --upgrade pip --break-system-packages
                    pip install -r requirements.txt --break-system-packages
                '''
            }
        }

        stage('Install Chrome & ChromeDriver') {
            steps {
                sh '''
                    # --- Install Google Chrome if missing ---
                    if ! command -v google-chrome &> /dev/null; then
                        echo "Google Chrome not found. Installing..."
                        wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
                        sudo dpkg -i google-chrome-stable_current_amd64.deb || sudo apt-get install -f -y
                        rm google-chrome-stable_current_amd64.deb
                    else
                        echo "Google Chrome is already installed"
                    fi

                    # --- Install ChromeDriver if missing ---
                    if ! command -v chromedriver &> /dev/null; then
                        echo "ChromeDriver not found. Installing..."
                        CHROME_VERSION=$(google-chrome --version | grep -oP '\\d+\\.\\d+\\.\\d+')
                        wget -N https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip
                        unzip chromedriver_linux64.zip
                        sudo mv chromedriver /usr/local/bin/
                        sudo chmod +x /usr/local/bin/chromedriver
                        rm chromedriver_linux64.zip
                    else
                        echo "ChromeDriver is already installed"
                    fi
                '''
            }
        }

        stage('Run Selenium Tests with GUI') {
            steps {
                sh '''
                    echo "Running Selenium tests with DISPLAY=$DISPLAY"
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
