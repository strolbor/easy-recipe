sudo docker container rm -f docker.ursb.de/easyrecipe
sudo docker build -t docker.ursb.de/easyrecipe .
sudo docker run --restart=always -p 5000:5000 --name er docker.ursb.de/easyrecipe &

sudo docker rmi -f $(docker images --filter "dangling=true" -q --no-trunc)
sudo docker container prune -f
sudo docker volume prune -f 

