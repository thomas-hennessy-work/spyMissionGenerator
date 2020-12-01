# spyMissionGenerator
The spy mission generator is a flask application used to generate missions for a spy. The main application consists of three services. Two services produce random lists, one of chars, the other of numbers, and the third service combines the two to produce a mission.

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