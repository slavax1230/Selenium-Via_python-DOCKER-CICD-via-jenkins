pipeline {
    agent { 
        node {
            label 'B'
            }
      }
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                echo "Building.."
                sh '''
                pip install -r requirements.txt       
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''                   
                python3 hello.py
                python3 hello.py --num1=2 --num2=2
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}