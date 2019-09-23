#Stop any currently running versions of the app
sudo docker-compose down
#Build the container, and if successful, start the container
sudo docker-compose build && sudo docker-compose up -d
#Display the list of runnng containers for verification
sudo docker ps

