pipeline {
    agent none
    
    stages {
        stage('Préparation des données de test') {
            agent {
                docker {
                    image 'python:3.9-slim'
                    label 'docker-agent'  // Nécessite un agent avec Docker installé
                    args '-v /tmp:/tmp'  // Montage de volume optionnel
                }
            }
            steps {
                checkout scm
                sh """
                pip install -r requirements.txt
                python data_generation/generate_test_data.py
                """
                stash name: 'test-data', includes: 'data_generation/output/*.json'
            }
        }
        
        stage('Exécution des tests API') {
            agent {
                docker {
                    image 'ppodgorsek/robot-framework:latest'
                    label 'docker-agent'
                    args '-v /tmp:/tmp'
                }
            }
            steps {
                checkout scm
                unstash 'test-data'
                sh """
                pip install -r requirements.txt
                robot -d results tests/api_tests.robot
                """
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