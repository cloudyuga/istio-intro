

# Envoy Introduction

## Sample envoy config

## Envoy config with listeners



* To build the image: `make build`

* To run the image: `make run`

* Check if it's working fine: 
    * Check headers only : `curl -I localhost:9001`
    * Or while running on local system go to browser and try : `localhost:9001`

* Cleanup entire setup: `make clean`


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
