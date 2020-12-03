  
pipeline{
    agent any
    stages{
        stage('unit test service 1'){
            steps{
                sh "bash scripts/service_1_unittests.sh" 
            }
        }
        stage('unit test service 2'){
            steps{
                sh "bash scripts/service_2_unittests.sh" 
            }
        }
        stage('unit test service 3'){
            steps{
                sh "bash scripts/service_3_unittests.sh" 
            }
        }
        stage('unit test service 4'){
            steps{
                sh "bash scripts/service_4_unittests.sh" 
            }
        }
        stage('build stage'){
            steps{
                sh "bash scripts/buildImages.sh"
            }
        }
        stage('push builds'){
            steps{
                sh "bash scripts/pushBuilds.sh"
            }
        }
        stage('run application'){
            steps{
                sh "bash scripts/launchSwarm.sh"
            }
        }
    }
}