pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building Apk test for debug..'
                sh './gradlew assembleDebug'
            }
        }
        stage('Test') {
            steps {
                echo 'Enhance test with Brower Testing..'
                echo "send build image to browerstack fpr appium testing"
            }
        }
        
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
