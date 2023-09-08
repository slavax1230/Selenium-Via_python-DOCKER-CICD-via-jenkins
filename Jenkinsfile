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
                pip install fire       
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''     
                pip install fire              
                python3 hello.py
                python3 hello.py --name=my-name-is
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