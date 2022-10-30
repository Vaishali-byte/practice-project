pipeline {
    agent any 
    stages {
        stage('Tests') {
            steps {
                dir('flask-app'){
                    sh "echo this is a test"
                    // sh "rm application/test/test_int*"
                    // sh "bash test.sh"
                }
            }
        }

        stage('docker-compose build and run') {
            steps {                         
               
                sh "sudo -s docker-compose up -d"
            }
        }

    }
}
