sudo docker container rm -f er
sudo docker build -t er .

#sudo docker run -p 5000:5000 --name er er &
#sudo docker run -d restart-always -p 5000:5000 --name easyrecipe er &
sudo docker run --restart=always -p 5000:5000 --name er er &

#sudo docker container prune -f
#sudo docker image prune -a -f
#sudo docker volume prune -f 

