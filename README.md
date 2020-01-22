# "Hello, World" using Python and Flask
Create minimal "Hello, World" API with endpoint and keyword arguments

# Dockerized application in two ways with Docker-compose. 
1) With local machine 
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
   - Create another file "need.txt" 
   - Create Dockerfile with the Alpine image
   - Create docker-compose.yml file 
   - To start up the application:**$ docker-compose up**
   - Go to the localhost:5000 and the web browser will be opened with the "Hello, World!" message
   
   2) With EC2 instance
   - Launch EC2 instance with RHEL AMI and define security groups:    
     * make sure to allow all traffic for all ports in all range along with SSH port(22) and HTTP port(80).
   - Used Mobaxterm for the SSH connection (works similar like PuTTY)
   - Install docker and docker-compose as mentioned in above steps. 
   **To Dockerize the application**
   - Make project directory and work into that directory
   - Create the file "app.py" and include the python code into this file
   - Create another file "need.txt" 
   - Create Dockerfile with the Alpine image
   - Create docker-compose.yml file 
   - To start up the application:**$ docker-compose up**
   - Go to the public IP of EC2 server:5000 and the web browser will be opened with the "Hello, World!" message
   
