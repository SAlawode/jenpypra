pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Clone the repository containing the palindrome-finding script
                git 'https://your-repository-url.git'
            }
        }

        stage('Setup Python') {
            steps {
                // Check if Python is installed and print the version
                sh 'python --version || python3 --version' // Check for python or python3 and print the version
                // Upgrade pip and print the version
                sh 'pip --version || pip3 --version'
                sh 'pip install --upgrade pip || pip3 install --upgrade pip'
            }
        }

        stage('Run Script') {
            steps {
                // Run the palindrome-finding script
                sh 'python palindrome_finder.py || python3 palindrome_finder.py' // Ensure the script path is correct
            }
        }
    }

    post {
        success {
            echo 'The palindrome script ran successfully!'
        }
        failure {
            echo 'The palindrome script failed.'
        }
    }
}
