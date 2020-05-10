pipeline{
    agent {
        label 'master'
        }
        stages {
        stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "/var/lib/docker"
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
