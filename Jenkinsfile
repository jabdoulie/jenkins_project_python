pipeline {
    agent {
        label 'python-agent' // Utilise l'agent 'test' spécifié
    }

    stages {
        stage('Continuous integration') {
            steps {
                // Cloner le projet depuis GitHub
                git branch: 'main', url: 'https://github.com/jabdoulie/jenkins_project_python.git'
                
                // Lancer l'analyse SonarQube
                sh '''
                sonar-scanner \
                    -Dsonar.projectKey=html-project \
                    -Dsonar.sources=. \
                    -Dsonar.host.url=http://192.168.8.10:9000 \
                    -Dsonar.token=sqp_226bfbcdbfbd416851c4066e53240b8035b98fa0
                '''
            }
        }

	stage('Test Unitaire') {
            steps {
                script {
                    //
                    sh 'python3 -m unittest test_current_time.py'
                }
            }
        }
	stage('Build le dockerfile') {
            steps {
                script {
                    //Builder le dockerfile
                    sh 'docker build -t py-project .'
                }
            }
        }

    }

    post {
        always {
            // Nettoyage des ressources après exécution
            echo 'Pipeline terminé'
        }
    }
}
