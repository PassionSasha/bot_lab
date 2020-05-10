pipeline{
    agent {
        label 'master'
        }
        stages {
        stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
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
