# Envoy Introduction

## Sample envoy config

```yaml
admin:
  access_log_path: /tmp/admin_access.log
  address:
    socket_address: { address: 0.0.0.0, port_value: 9876 }
```

Build the docker image: 

```command
docker build -t envoy-course-101:v.0.1 -f Dockerfile-envoy-0
```

Run the docker image: 
```command
docker run -p 8888:9876 --name envoy-course-101 envoy-course-101:v.0.1
```


## Envoy config with listeners

```yaml
admin:
  access_log_path: /tmp/admin_access.log
  address:
    socket_address: { address: 0.0.0.0, port_value: 9876 }
static_resources:
  listeners:
  - name: listener_0
    address:
      socket_address: { address: 0.0.0.0, port_value: 9877 }
    filter_chains:
    - filters:
      - name: envoy.http_connection_manager
        config:
          stat_prefix: envoy-docker
          server_name: envoy-101-example
          route_config:
            name: simple_route
            virtual_hosts:
            - name: google_redirect
              domains: ["*"]
              routes:
              - match: { prefix: "/" }
                route: { host_rewrite: www.google.com, cluster: google_cluster}
          http_filters:
          - name: envoy.router
  clusters:
  - name: google_cluster
    connect_timeout: 0.25s
    type: LOGICAL_DNS
    dns_lookup_family: V4_ONLY
    lb_policy: ROUND_ROBIN
    hosts: [{ socket_address: { address: google.com, port_value: 443 }}]
    tls_context: { sni: www.google.com }
```

* Build the docker image: 

```command
docker build -t envoy-course-101:v.0.2 -f Dockerfile-envoy-0
```

* Run the docker image: 
```command
docker run -p 8888:9876 --name envoy-course-101 envoy-course-101:v.0.2
```

* Check if it's working fine: 
    * Check headers only : 
    ```command
    curl -I localhost:9001
    ```
    * Or while running on local system go to browser and try : 
    ```command
    localhost:9001
    ```
