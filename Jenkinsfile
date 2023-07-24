pipeline {
    agent any

    environment {
        JAVA_HOME= '/usr/lib/jvm/java-17-openjdk-arm64'
        PATH= '/opt/java/openjdk/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
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
                // Use Maven to build the petclinic application
                withMaven (maven: 'maven-3.9.3') {
                    sh "mvn clean package"
                }
            }
        }

        stage('Test') {
            steps {
                // Run tests (if applicable)
                withMaven (maven: 'maven-3.9.3') {
                    sh 'mvn test'
                }
            }
        }

        stage('Static Analysis') {
            steps {
                script {
                    // Run static code analysis with SonarQube Scanner
                    def projectName = "petclinic" 
                    def projectVersion = "1.0" 
                    def sonarHostUrl = "http://localhost:9000"

                    sh "sonar-scanner -Dsonar.projectKey=${projectName} -Dsonar.projectName=${projectName} -Dsonar.projectVersion=${projectVersion} -Dsonar.host.url=${sonarHostUrl}"
                }
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