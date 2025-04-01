pipeline {
    agent none
    
    stages {
        stage('Préparation des données') {
            agent {
                docker {
                    image 'python:3.9-slim'
                    args '-v $WORKSPACE:/workspace -w /workspace'
                }
            }
            steps {
                checkout scm
                sh 'pip install -r requirements.txt'
                sh 'python data_generation/generate_test_data.py'
                stash name: 'test-data', includes: 'data_generation/output/*.json'
            }
        }
        
        stage('Tests API') {
            agent {
                docker {
                    image 'ppodgorsek/robot-framework:latest'
                    args '-v $WORKSPACE:/workspace -w /workspace'
                }
            }
            steps {
                checkout scm
                unstash 'test-data'
                sh 'robot -d results tests/api_tests.robot'
            }
            post {
                always {
                    archiveArtifacts 'results/**/*'
                    junit 'results/output.xml'
                }
            }
        }
    }
}