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
                    def sonarScannerHome = tool 'SonarQube Scanner'

                    // Set the location of the compiled Java classes using sonar.java.binaries
                    def binariesDir = 'target/classes'
                    
                    def projectName = "petclinic" 
                    def projectVersion = "1.0" 
                    def sonarHostUrl = "http://sonarqube:9000"

                    sh "${sonarScannerHome}/bin/sonar-scanner -Dsonar.projectKey=${projectName} -Dsonar.projectName=${projectName} -Dsonar.projectVersion=${projectVersion} -Dsonar.host.url=${sonarHostUrl} -Dsonar.login=sqa_3498eac4d96e05521d51345e64cb441db6ad0e63 -Dsonar.java.binaries=${binariesDir} -X"
                    
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
                	"ansible_port=2222" // Specify the SSH port for the web_server container
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