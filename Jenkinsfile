pipeline {
    agent {
        docker {
            image 'python:3.10-slim'
            args '-u root'
        }
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Shravani3001/mlops-project.git'
            }
        }

        stage('Verify Environment') {
            steps {
                sh '''
                python --version
                pip --version
                '''
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                python -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
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

        stage('Run DVC Pipeline') {
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
            echo "✅ End-to-end MLOps pipeline completed successfully"
        }
        failure {
            echo "❌ MLOps pipeline failed"
        }
    }
}