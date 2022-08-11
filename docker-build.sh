sudo docker container rm -f er
sudo docker build -t er .
sudo docker run --restart=always -p 5000:5000 --name er er &

sudo docker rmi -f $(docker images --filter "dangling=true" -q --no-trunc)
sudo docker container prune -f
sudo docker volume prune -f 

