pipeline {
    agent any

    stages {
	stage('Build') {
	    steps {
		echo 'Building ...'
		sh "virtualenv venv -p python3"
		sh "cp conf/config.cfg.sample conf/config.cfg"
		sh "source venv/bin/activate && python -m pip install --upgrade pip setuptools"
		sh "source venv/bin/activate && python -m pip install -r requirements.txt"
	    }
	}
	stage('Test') {
	    steps {
		echo 'Testing ...'
		sh "source venv/bin/activate && python main.py"
	    }
	}
	stage('Deploy') {
	    steps {
		echo 'Deploying ...'
	    }
	}
    }
}
