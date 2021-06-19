# Part3 - Docker
## Build
docker build --tag <image_name> .

## Check COntainer running
sudo docker ps

## Run
sudo docker run --name test_ctn -d --rm -p 1000:5000 -it test
