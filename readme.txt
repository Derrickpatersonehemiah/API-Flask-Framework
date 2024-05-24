Pre-req:

Python needs to be installed.
Node.js needs to be installed.
Flask needs to be installed, - pip install flask
newman needs to be installed, npm install -g newman 
html extra reporter needs to be installed - npm install -g newman-reporter-htmlextra 

1)For Task 4.1 run: python API_ini.py
Result: http://127.0.0.1:5000/Task4.1

2)For Task 4.2 run: 
--> To run tesst cases in flask framework - python Test_cases_API.py
--> To run tesst cases with newman - start the server/host with - python API_Test.py then trigger - newman run PM.json