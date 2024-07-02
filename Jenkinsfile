pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                // Install Python and necessary dependencies
                sh 'python --version' // Check if Python is installed
                sh 'pip install --upgrade pip' // Upgrade pip
            }
        }

        stage('Run Script') {
            steps {
                // Run the palindrome-finding script
                sh 'python palindrome_finder.py'
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
