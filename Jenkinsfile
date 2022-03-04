pipeline {

  agent none

  options {
    disableConcurrentBuilds()
    skipDefaultCheckout()
  }

  environment {
    PRODUCT = "pyKVStore"
    VER = "1.0"
  }

  stages {
    
    stage('buildImage') {
      agent{
        label 'dev-server'
      }
      when {
        branch 'develop'
      }
      steps {
          checkout scm
          script{
            def BUILD_HASH = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
            env.VERSION = "${VER}-${BUILD_HASH}"
            env.TAG ="${PRODUCT}:$VERSION"
            currentBuild.displayName = "$VERSION"
          }
          sh 'docker build -t "$TAG" .'
      }
    }

    stage('unitTest') {
      agent{
        label 'dev-server'
      }
      when {
        branch 'develop'
      }
      steps {
          sh 'docker run $TAG python /app/tests/unitTest.py'
      }
    }

    stage('Deploy-Dev') {
      agent{
        label 'dev-server'
      }
      when {
        branch 'develop'
      }
      steps {
          sh 'docker rm -f $(docker ps -a -f name=pyKVStore-dev -q) 2> /dev/null || true'
          sh 'docker run --name pyKVStore-dev -d -p 8000:8000 $TAG'
      }
    }

    stage('Smoke-Test') {
      agent{
        docker 'dwdraju/alpine-curl-jq:latest'
      }
      when {
        branch 'develop'
      }
      steps {
          checkout scm
          sh './tests/smoke-test-dev.sh'
      }
    }
  }
}
