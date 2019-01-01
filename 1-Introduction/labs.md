# Envoy Introduction
Envoy is an L7 proxy and communication bus designed for complex microservice architectures. Envoy proxy is designed to run alongside of the every application. All these Envoys deployed alongside with applications create transperent service mesh. Alll communications of these applications take place through this service mesh.  Envoy can easily run with any application independent of the language in which applications have written. So in microservice architecture, Envoy motivates to use multiple application frameworks and languages as Envoy transparently bridges the gap.  Envoy can be deployed and upgraded quickly across an entire infrastructure transparently.

## Sample envoy configuration.

- Take a look at `envoy-0.yaml`, which contains simple envoy configuration.

```command
cat envoy-0.yaml
```
```yaml
admin:
  access_log_path: /tmp/admin_access.log
  address:
    socket_address: { address: 0.0.0.0, port_value: 9876 }
```

- Build the envoy docker image with simple configuration.

```command
docker build -t envoy-course-101:v.0.1 -f Dockerfile-envoy-0 .
```

- Run the docker image.
```command
docker run -p 8888:9876 --name envoy-course-101 envoy-course-101:v.0.1
```

- Check if it's working fine: go to browser and try `http://localhost:8888/` you will admin pannel of envoy is coming.

## Envoy configurations with listeners

- Take a look at another envoy configuration. In which we have added the listener port.

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
In this configuration we have added listener `listener_0` such that if any request comes to `0.0.0.0:9877` then it will be forwarded to `www.google.com`.

- Build the docker image with above envoy configurations.

```command
docker build -t envoy-course-101:v.0.2 -f Dockerfile-envoy-1 .
```

- Run the docker image:

```command
docker run -p 8888:9876 -p 8899:9877 --name envoy-course-101 envoy-course-101:v.0.2
```

- Check if it's working fine: go to browser and try `http://localhost:8888/` you will admin pannel of envoy is coming. In which you can check the information about the envoy. 

- If you try to access `http://localhost:8899/` in browser then you will be redirected to the `www.google.com`



