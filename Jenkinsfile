  
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
    }
}