pipeline{
    agent {
        label 'master
        '
        }
        stages {
            stage("robotay"){
                steps{
                     dir('docker') {
                     sh 'docker build . '
                     sh 'docker run . '
                        }
                 }
             }
        }
     }
