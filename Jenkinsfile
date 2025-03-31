pipeline {
    agent none
    
    stages {
        stage('Préparation des données de test') {
            agent {
                label 'python-agent'
            }
            steps {
                checkout scm
                sh 'pip install -r requirements.txt'
                sh 'python data_generation/generate_test_data.py'
                stash name: 'test-data', includes: 'data_generation/output/*.json'
            }
        }
        
        stage('Exécution des tests API') {
            agent {
                label 'robot-agent'
            }
            steps {
                checkout scm
                unstash 'test-data'
                sh 'pip install -r requirements.txt'
                sh 'robot -d results tests/api_tests.robot'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'results/**/*'
                    junit 'results/output.xml'
                }
            }
        }
    }
}