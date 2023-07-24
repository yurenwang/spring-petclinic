pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the repository
                checkout scm
            }
        }

        stage('Build') {
            steps {
                // Use Gradle to build the petclinic application
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                // Run tests (if applicable)
                sh 'mvn test'
            }
        }

        stage('Archive') {
            steps {
                // Archive the JAR artifact
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
            }
        }
    }
}