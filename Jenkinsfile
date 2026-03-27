pipeline {
    agent any

    stages {
        stage('Run Ansible') {
            steps {
                sh '''
                cd simple-role
                ansible-playbook -i inventory.ini playbook.yml
                '''
            }
        }
    }
}
