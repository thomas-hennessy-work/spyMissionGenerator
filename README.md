# spyMissionGenerator
The spy mission generator is a flask application used to generate missions for a spy. The main application consists of three services. Two services produce random lists, one of chars, the other of numbers, and the third service combines the two to produce a mission.

## Tools
### Application Dependencies
The application requires the following dependencies to run. The dependencies can be found in the requierments.txt files in the application.

- Flask==1.1.2
- PyMySQL==0.10.1
- Flask-SQLAlchemy==2.4.4
- SQLAlchemy==1.3.18
- pytest==6.1.2
- Flask-Testing==0.8.0
- pytest-cov==2.10.1
- gunicorn==20.0.4

The dependencies required for the application can be installed using [pip](https://pip.pypa.io/en/stable/) with the command:
`pip install -r requierments.txt` 
Python3 will additionally need to be installed.

### Build server
- **Jenkins**:
The build server.
- **Ansible**:
Used by the build server to configure the virtual machines running the application

### Docker
 - **Docker**:
Used to create images and run containers.
- **Docker swarm**:
Used to deploy, manage and configure a group of containers simultaneously.
- **Docker hub**:
Repository for pushing to and storing built images.

### Misc tools
 - **Google cloud platform**:
Hosts the virtual machines used for the build server and the virtual machines hosting the application.
- **Visual studio code**:
Code editor used for creating the application and its configuration files.

## Documentation
### ERD
The database used in the application is very simple consisting of one table. The database stores information regarding the dossier number, the missions target and the mission objective.

![Image of the systems ERD](images/erd.jpg)

### Application structure
The application consists of 4 services and a database. The user accesses the system via Nginx, which will load balance incoming traffic. The user is directed to service 1. Service 1, will obtain the number half of the mission dossier from service 2 and the letter half of the mission dossier from service 3. With these two halves of the mission dossier created, the system will send them to service 4 which will decide what the task and target are and return them to service 1. Service 1 will then store the information about the mission in the database and present the dossier to the user.
![Image of the system structure](images/appstructure.jpg)

### Risk assessment
![Image of the risk assessment](images/riskassesmentpt1.jpg)
![Image of the risk assessment](images/riskassesmentpt2.jpg)

## Testing
All 4 of the services are unit tested, reaching a total coverage of 95%
### Service 1
98% coverage
![Image of service 1's unit tests](images/unit_tests/service_1_tests.jpg)
### Service 2
92% coverage
![Image of service 1's unit tests](images/unit_tests/service_2_tests.jpg)
### Service 3
93% coverage
![Image of service 1's unit tests](images/unit_tests/service_3_tests.jpg)
### Service 4
97% coverage
![Image of service 1's unit tests](images/unit_tests/service_4_tests.jpg)