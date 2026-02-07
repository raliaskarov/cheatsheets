

Burn, restore
```
docker stop $(docker ps -a -q --filter "name=nextcloud-aio")
docker rm $(docker ps -a -q --filter "name=nextcloud-aio")
docker volume rm nextcloud_aio_nextcloud nextcloud_aio_database nextcloud_aio_database_dump nextcloud_aio_apache nextcloud_aio_redis
sudo rm -rf /mnt/ncdata/*
sudo chown 33:0 /mnt/ncdata
sudo chmod 750 /mnt/ncdata
docker compose up -d
```
