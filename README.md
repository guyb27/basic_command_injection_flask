# basic_command_injection_flask
run 
```cd pods1 && docker build -t flask-ping-app .```
```kind load docker-image flask-ping-app```
```kubectl apply -f ./pods1/pods1.yml ```
```docker build -t ssh-ubuntu-low-password -f ./pods2/Dockerfile .```
```kind load docker-image ssh-ubuntu-low-password```
```kubectl apply -f ./pods2/pods2.yml ```


