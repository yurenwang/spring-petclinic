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


	stage('Deploy to Web Server') {
    	    steps {
        	ansiblePlaybook(
                    playbook: 'ansible-playbook/web_server.yml',
                    inventory: 'localhost,', // Use 'localhost' to target the Jenkins server
                    installation: 'ansible',
                    extraVars: [
                	'ansible_port': '2222' // Specify the SSH port for the web_server container
            	    ]
        	)
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