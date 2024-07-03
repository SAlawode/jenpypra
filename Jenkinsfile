pipeline {
    agent any

    stages {
        stage('Setup Python') {
            steps {
                script {
                    def pythonVersion = sh(returnStdout: true, script: 'python --version || python3 --version').trim()
                    echo "Python version: ${pythonVersion}"

                    def pipVersion = sh(returnStdout: true, script: 'pip --version || pip3 --version').trim()
                    echo "Pip version: ${pipVersion}"

                    sh 'pip install --upgrade pip || pip3 install --upgrade pip'
                }
            }
        }

        stage('Run Script') {
            steps {
                script {
                    try {
                        sh 'python palindrome_finder.py || python3 palindrome_finder.py'
                        echo 'The palindrome script ran successfully!'
                    } catch (Exception e) {
                        echo "Failed to run palindrome script: ${e.message}"
                        currentBuild.result = 'FAILURE'
                        throw e
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
