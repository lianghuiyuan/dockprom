# dockprom

一套通过Docker容器部署prometheus监控的方案，本方案包括： [Prometheus](https://prometheus.io/), [Grafana](http://grafana.org/), [cAdvisor](https://github.com/google/cadvisor),
[NodeExporter](https://github.com/prometheus/node_exporter) and 告警组件 [AlertManager](https://github.com/prometheus/alertmanager).

### 文件
./
├── LICENSE
├── README-cn.md
├── README.md
├── alertmanager
│   └── config.yml
├── caddy
│   └── Caddyfile
├── config
├── docker-compose.exporters.yml
├── docker-compose.yml
├── grafana
│   └── provisioning
│       ├── dashboards
│       │   ├── dashboard.yml
│       │   ├── docker_containers.json
│       │   ├── docker_host.json
│       │   ├── monitor_services.json
│       │   └── nginx_container.json
│       └── datasources
│           └── datasource.yml
├── helpers
│   └── aws
│       ├── README.md
│       ├── cadvisor_ecs_task_definition.json
│       ├── node_exporter_task_definition.json
│       └── prometheus.yml
├── homework
│   ├── Dockerfile
│   ├── Grafana_Docker_Containers.png
│   ├── imService.py
│   ├── pic.jpg
│   ├── server.log
│   └── server.py
├── prometheus
│   ├── alert.rules
│   └── prometheus.yml
└── screens
    ├── Grafana_Docker_Containers.png
    ├── Grafana_Docker_Host.png
    ├── Grafana_Prometheus.png
    └── Slack_Notifications.png

