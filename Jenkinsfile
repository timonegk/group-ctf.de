// vim: set filetype=groovy:
library changelog: false, identifier: 'github.com/ftsell/jenkins-pipeline-library@main', retriever: modernSCM([$class: 'GitSCMSource', credentialsId: '', remote: 'https://github.com/ftsell/jenkins-pipeline-library.git', traits: [gitBranchDiscovery()]])

def image_name = "registry.finn-thorben.me/group-ctf-de"

pipeline {
    agent {
        kubernetes {
            yaml genPodYaml(true, true)
        }
    }
    options {
        skipDefaultCheckout(true)
    }
    stages {
        stage("Checkout SCM") {
            steps {
                checkout scm
            }
        }
        stage("Validate K8S") {
            steps {
                container("kustomize") {
                    checkKustomize()
                }
            }
        }
        stage("Container") {
            steps  {
                container("podman") {
                    buildContainer(image_name)
                    script {
                        if (env.BRANCH_IS_PRIMARY == "true") {
                            uploadContainer(image_name, "registry.finn-thorben.me", "registry-credentials")
                        }
                    }
                }
            }
        }
    }
}


