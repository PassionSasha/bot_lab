pipeline{
    agent {
        dockerfile true
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
