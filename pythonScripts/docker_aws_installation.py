import subprocess
import re

def docker_aws_installation():
    try:
        #updating the ubuntu packages 
        subprocess.run(['sudo', 'apt', 'update'])
        
        #checking if the docker is installed or not
        check_docker()

        #installing the AWS CLI
        check_aws()


        
    except subprocess.CalledProcessError as e:
        print("\n<------------------SOMETHING WENT WRONG :< ------------------------------------>\n\n")

def check_docker():
    try:
        #checking if the docker executable is present or not
        subprocess.run(["which", "docker"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("<-------------------------- DOCKER ALREADY INSATLLED------------------------------->\n\n")

    except subprocess.CalledProcessError as e:
        try:
            #installing docker now
            print("<----------------Couldn't find Docker! trying to install Docker!---------------------->") 
            
            #install a few prerequisite packages which let apt use packages over HTTPS
            subprocess.run(["sudo", "apt", "install", "apt-transport-https", "ca-certificates", "curl", "software-properties-common"])
            
            #adding the GPG key for the official Docker repository to your system
            subprocess.run(["curl", "-fsSL", "https://download.docker.com/linux/ubuntu/gpg", "|", "sudo", "apt-key", "add", "-"])
            
            #Add the Docker repository to APT sources
            #also updates our package database with the Docker packages from the newly added repo
            subprocess.run(["sudo", "add-apt-repository", "deb", "[arch=amd64]", "https://download.docker.com/linux/ubuntu", "focal", "stable"])

            #installing from the Docker repo instead of the default Ubuntu repo
            #Note that docker-ce is not installed, but the candidate for installation is from the Docker repository for Ubuntu 20.04 (focal)
            subprocess.run(["apt-cache", "policy", "docker-ce"])

            #installing docker
            subprocess.run(["sudo", "apt", "install", "docker-ce"])

            #checking if docker is up and running
            subprocess.run(["sudo", "systemctl", "status", "docker"])

            
        except subprocess.CalledProcessError as e:
            print("\n<------------------SOMETHING WENT WRONG :< ------------------------------------>\n\n")

def check_aws():
    try:
        print()
        
    except subprocess.CalledProcessorError as e:
        print(e)
if __name__ == "__main__":
    docker_aws_installation()
