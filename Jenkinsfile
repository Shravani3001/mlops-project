pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Shravani3001/mlops-project.git'
            }
        }

        stage('Ensure Python Installed') {
            steps {
                sh '''
                if ! command -v python3 >/dev/null 2>&1; then
                    echo "Python not found. Installing..."
                    sudo apt-get update
                    sudo apt-get install -y python3 python3-venv python3-pip
                else
                    echo "Python already installed"
                fi
                python3 --version
                '''
            }
        }

        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
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
