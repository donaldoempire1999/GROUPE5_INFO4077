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
            }

            steps{
                echo "send build image to browerstack fpr appium testing"
                sh 'curl -u "donaldfotso1:r8aTdQab2LMpakRtw3CG" -X POST "https://api-cloud.browserstack.com/app-automate/upload" -F "file=@/path/to/app/file/Application-debug.apk"'
            }
        }
        
        
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
