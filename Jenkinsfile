pipeline {
    agent any

    environment {
        // If your using the official maven image, these are probably where it puts it
        MAVEN_HOME = '/usr/share/maven'
        JAVA_HOME= '/usr/local/openjdk-20'
    }


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
                withMaven(maven: 'mvn') {
                    sh "mvn clean package"
                }
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