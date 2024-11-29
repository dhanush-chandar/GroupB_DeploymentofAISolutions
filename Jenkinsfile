pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/dhanush-chandar/GroupB_DeploymentofAISolutions'
            }
        }
        stage('Setup Environment') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Notebook') {
            steps {
                sh '''
                source venv/bin/activate
                python run_notebook.py
                '''
            }
        }
        stage('Convert Notebook to HTML') {
            steps {
                sh '''
                source venv/bin/activate
                jupyter nbconvert --to html executed_model.ipynb
                '''
            }
        }
    }
    post {
        always {
            archiveArtifacts artifacts: 'executed_model.html', allowEmptyArchive: true
        }
    }
}
