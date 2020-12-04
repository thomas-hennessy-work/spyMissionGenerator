  
pipeline{
    agent any
    stages{
        stage('unit test service 1'){
            steps{
                sh ". scripts/service_1_unittests.sh" 
            }
        }
        stage('unit test service 2'){
            steps{
                sh ". scripts/service_2_unittests.sh" 
            }
        }
        stage('unit test service 3'){
            steps{
                sh ". scripts/service_3_unittests.sh" 
            }
        }
        stage('unit test service 4'){
            steps{
                sh ". scripts/service_4_unittests.sh" 
            }
        }
        stage('build stage'){
            steps{
                sh ". scripts/buildImages.sh"
            }
        }
        stage('push builds'){
            steps{
                sh ". scripts/pushBuilds.sh"
            }
        }
        stage('run ansible'){
            steps{
                sh ". scripts/runAnsible.sh"
            }
        }
        stage('run application'){
            steps{
                withCredentials([sshUserPrivateKey(credentialsId: 'jenkins-ssh-manager', keyFileVariable: 'PRIVATE_KEY', passphraseVariable: '', usernameVariable: 'USER')]) {
                    sh'''ssh ${USER}@swarm-manager
                    [ ! -d spyMissionGenerator ] && git clone https://github.com/thomas-hennessy-work/spyMissionGenerator.git 
                    cd spyMissionGenerator
                    git pull
                    . scripts/buildImages.sh
                    . scripts/launchSwarm.sh
                    '''
                }
            }
        }
    }
}