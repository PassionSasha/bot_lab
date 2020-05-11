pipeline{
    agent {
        label 'master'
        }
        stages {
            stage("robotay"){
                steps{
                     dir('docker') {
                     sh 'docker image build -t lab6 . '

                        }
                     dir('docker') {
                     sh 'docker run -p 80:81 lab6' }
                 }
             }
        }
     }
