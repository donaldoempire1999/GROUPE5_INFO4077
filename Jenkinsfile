pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Apk test for debug..'
                sh './gradlew tasks'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
