pipeline{
    agent {
        dockerfile true
        }
        stages {
            stage("robotay"){
                steps{
                    echo 'hi'
                     sh 'docker image build -t docker_file .'
                     sh 'docker run -it -p 81:80  docker_file'
                 }
             }
        }
     }
