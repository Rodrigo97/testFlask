pipeline {
agent any
stages {
	stage('Build') {
	parallel {
		stage('Build') {
		steps {
			sh 'echo "Ejecutando Build desde Repositorio"'
		}
		}
	}
	}

	stage('Prueba') {
	steps {
		sh 'python3 app_test.py'
		input(id: "Deploy Gate", message: "Deploy ${params.project_name}?", ok: 'Deploy')
	}
	}

	stage('Despliegue')
	{
	steps {
		echo "Desplegando aplicación"
		sh "sudo nohup python3 app.py > log.txt 2>&1 &"
	}
	}
}

post {
		always {
			echo 'Pipeline completado'
			junit allowEmptyResults: true, testResults:'**/test_reports/*.xml'
		}
		success {				
			echo "Aplicación ejecutandose"
		}
		failure {
			echo 'Build ha fallado'
			error('Stopping early…')
		}
	}
}
