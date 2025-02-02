
### steps to deploy and config Kafka Monitoring :

1-create monitoring directory and docker compose file:

```
mkdir -p /opt/monitoring 
sudo chown moein:moein /opt/monitoring
cd /opt/monitoring
mkdir  grafana && sudo chown -R 472:472 grafana/



tree /opt/monitoring
.
├── docker-compose.yml
├── grafana
├── grafana_password.txt
├── grafana_user.txt
└── prometheus.yml

```

2- Run Docker compose file:
```
docker compose up -d


```