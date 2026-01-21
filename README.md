# MQTT-Status-Analytics-Platform
**- Project Description:**

I have Developed a client-server script in Python that handles MQTT messages via RabbitMQ. The client script emits MQTT messages every second containing a field "status" with a random value in the range of 0-6. The server processes these messages and store them in MongoDB. Additionally, I have also developed an API using Django which accepts start and end times and return the count of each status during the specified time range.
  
**- Myassignment directory consists of files for MQTT Usage for messaging and caching in MongoDB**

**- assignment directory consists of files for Django API to get data from MongoDB**


- Technologies Used:
  1. Python
  2. MongoDB
  3. RabbitMQ
  4. Git
  5. Django



**-Required Python Libraries:**

1. pip install paho-mqtt
2. pip install pymongo
3. pip install django





**-MONGO Installation:**

Go to the MongoDB official website: https://www.mongodb.com/try/download/community and download MongoDB Community Server.
Mongo Installation using Homebrew- 
- brew tap mongodb/brew
- brew install mongodb-community

Start MongoDB- 

- brew services start mongodb/brew/mongodb-community

Check Mongo Shell Installation:
- mongosh —-version

To Use MongoShell to Interact with Database
- mongosh

Start Mongo Server:
- mongod

Check version of Mongod:
- mongod --version







**-RabbitMQ Installation:**

- Installation using Homebrew -> brew install rabbitmq
- To Start RMQ Server -> brew services start rabbitmq
- To Stop RMQ Server -> brew services stop rabbitmq





**-Commands To run MyAssignment:**

- server.py  -> python server.py
- client.py  -> python client.py

**-Commands To run assignment:**
- python3 manage.py runserver (To start Django server)
  




**-POSTMAN API CURL:**

curl --location 'localhost:8000/dataretrieval/startTime=2024-11-01T00:00:00&endTime=2024-11-30T23:59:59/' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json'

- Sample Response for API--

{
    "count": 6
}






**-Screenshots:**

<img width="431" alt="image" src="https://github.com/user-attachments/assets/8b2e43ba-c632-4794-9e15-5df3a98bb018">
<img width="1193" alt="image" src="https://github.com/user-attachments/assets/6135be2e-b6e4-4a16-981c-1cb97d0e250f">
<img width="897" alt="image" src="https://github.com/user-attachments/assets/446de7f7-3315-4758-8462-13e5474eb1a3">







**-NOTE:**
This setup was done on MacOS.

This is a project created for basic publishing/consuming data via RabbitMQ MQTT protocol and an API used for fetching data based on timestamp from MongoDB by Shardul Powale.
