apt-get install build-essential
apt-get install net-tools
vim
adduser code
sudo code

npm install -g sequelize-cli


docker run -it --net=host -v ~/MARCELO/CODE/jsfonetico/code_homonimia:/home/code -p 4001:4001 homonimia:node


https://stackoverflow.com/questions/40746453/how-to-connect-to-docker-host-from-container-on-windows-10-docker-for-windowshttps://stackoverflow.com/questions/40746453/how-to-connect-to-docker-host-from-container-on-windows-10-docker-for-windows
docker run -it --net="host" container_name
Then from container, you can connect to service on host using:
localhost:port
But in this case, you will not be able to link more containers using --link parameter.
