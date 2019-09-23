Steps for testing development

When you are at a point when you would like to test the project run the following commands:

sudo docker-compose build #This will build the docker image

If the container builds with no issues, run the following

sudo docker-compose up -d #This will run the container in detached mode

You should then be able to access the app in the browser from localhost:8000


When you are done testing, run sudo docker-compose down
