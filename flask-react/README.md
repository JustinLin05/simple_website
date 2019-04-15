# flask-react
This is a project for creating a light web application easily. 

## Installation (with docker)
* Clone the repository
```
git clone https://github.com/JustinLin05/simple_website.git
```
* Enter the project folder
```
cd flask-react
```
* Build the images
```
docker-compose build
```
* Run the container
```
docker-compose up
```
* check your docker ip and you can access the web server at ```<your docker ip>:5000/upload```
* If you see the "hello flask", it works~~~~
* Find the <your docker ip>
```
docker-machine ip
```
* Ubuntu ```<your docker ip> is localhost```
* Ask for the number(only for 0-9) you paint, and the website will predict it.
## Development

* Back-end code is in ```app.py```
* Front-end code is under ```/templates```
