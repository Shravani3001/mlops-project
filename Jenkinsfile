pipeline {

    agent any
 
    stages {
 
        stage('Checkout') {

            steps {

                git branch: 'main',

                    url: 'https://github.com/Shravani3001/mlops-project.git'

            }

        }
 
        stage('Setup Environment') {

            steps {

                sh '''

                python -m venv venv

                . venv/bin/activate

                pip install -r requirements.txt

                pip install dvc

                '''

            }

        }
 
        stage('DVC Pull') {

            steps {

                sh '''

                . venv/bin/activate

                dvc pull

                '''

            }

        }
 
        stage('Run Pipeline') {

            steps {

                sh '''

                . venv/bin/activate

                dvc repro

                '''

            }

        }
 
        stage('Metrics Check') {

            steps {

                sh '''

                . venv/bin/activate

                dvc metrics diff || true

                '''

            }

        }
 
        stage('DVC Push') {

            steps {

                sh '''

                . venv/bin/activate

                dvc push

                '''

            }

        }

    }
 
    post {

        success {

            echo "✅ MLOps pipeline completed successfully"

        }

        failure {

            echo "❌ MLOps pipeline failed"

        }

    }

}

 
