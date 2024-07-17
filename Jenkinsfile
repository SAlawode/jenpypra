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
            slackSend(channel: 'jenkins', color: '#00FF00', message: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' succeeded")
        }
        failure {
            echo 'Pipeline failed!'
            slackSend(channel: 'jenkins', color: '#FF0000', message: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' failed")
        }
        unstable {
            echo 'Pipeline is unstable!'
            slackSend(channel: 'jenkins', color: '#FFFF00', message: "Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' is unstable")
        }
        always {
            echo 'Pipeline finished!'
        }
    }
}
