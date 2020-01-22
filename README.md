# Deployement of application using Docker-compose                                                   
                                                                                  
## "Hello, World" using Python and Flask                                                                           
Create minimal "Hello, World" API with endpoint and keyword arguments

## Dockerize application in two ways with Docker-compose. 

### With local machine ###
   *Used Linux machine here(CentOS7)*
   
   **To install Docker**
   - Log into the system with SUDO priviledges. 
   - Update the system: sudo yum update -y
   - Install Docker: sudo yum install docker-engine -y
   - Start Docker: sudo service docker start   
   - verify: sudo docker run hello-world
   
   **To install Docker-compose**
   - sudo curl -L --fail https://github.com/docker/compose/releases/download/1.25.1/run.sh -o /usr/local/bin/docker-compose
   - To set permission: sudo chmod +x /usr/local/bin/docker-compose  
   
   **To Dockerize the application**
   - Make project directory and work into that directory
   - Create the file "app.py" and include the python code into this file
   - Create another file "requirements.txt" 
   - Create Dockerfile with the Alpine image
   - Create docker-compose.yml file 
   - To start up the application:**$ docker-compose up**
   - Go to the localhost:8080 and the web browser will be opened with the "Hello, World!" message
   
### With AWS cloud server ###
   - Launch EC2 instance with RHEL AMI and define security groups.    
     [make sure to allow all traffic for all ports in all range along with SSH port(22) and HTTP port(80).]
   - Used Mobaxterm for the SSH connection (works similar like PuTTY).
   - Install docker and docker-compose as mentioned in above steps. 
  
   **To Dockerize the application**
   - Make project directory and work into that directory
   - Create the file "app.py" and include the python code into this file
   - Create another file "requirements.txt" 
   - Create Dockerfile with the Alpine image
   - Create docker-compose.yml file 
   - To start up the application:**$ docker-compose up**
   - Go to the EC2 public IP address:8080 and the web browser will be opened with the "Hello, World!" message
   
   ![](https://vmfarms.com/f05fd8da2dbe5a63a66609dbedb80f65.svg)
   








