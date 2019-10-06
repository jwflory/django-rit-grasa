git checkout remotes/origin/$1
git pull
sudo docker-compose stop -t 1 $2
sudo docker-compose build $2
sudo docker-compose create $2
sudo docker-compose start $2

sudo docker ps | grep $2
