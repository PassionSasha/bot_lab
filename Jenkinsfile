pipeline{
    agent {
        dockerfile true
        }
        stages {
            stage("robotay"){
                steps{


                     sh 'docker build .'
                     sh 'docker run -it -p 81:80  docker_file'
                 }
             }
        }
     }
