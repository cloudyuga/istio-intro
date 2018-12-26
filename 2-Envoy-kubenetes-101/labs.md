### Envoy in kubernetes

In this application with will be running container http-echo with envoy as sidecar.

Envoy config

```yaml
admin:
  access_log_path: "/dev/null"
  address:
    socket_address: { address: 0.0.0.0, port_value: 8001 }
stats_flush_interval:
  seconds: 5
static_resources:
  listeners:
  - name: envoy_101_listener_0
    address:
      socket_address: { address: 0.0.0.0, port_value: 8080 }
    filter_chains:
    - filters:
      - name: envoy.http_connection_manager
        config:
          codec_type: http1
          stat_prefix: envoy_101
          server_name: envoy_101
          route_config:
            name: local_app_route
            virtual_hosts:
            - name: local_app
              domains: ["*"]
              routes:
              - match: { prefix: "/" }
                route: { cluster: local }
          http_filters:
          - name: envoy.router
  clusters:
  - name: local
    type: static
    connect_timeout: 10s
    lb_policy: round_robin
    hosts:
    - socket_address:
        address: 127.0.0.1
        port_value: 9090
        protocol: tcp
```

To run the configmap envoy: 

```command
kubectl apply -f envoy-configmap.yaml
```


## K8s Deployment spec

```yaml
volumes:
- name: envoy-config
  configMap:
    name: envoy-config
containers:
- name: http-echo
  args: ["-listen", ":9090", "-text", "Hello from main app"]
  image: hashicorp/http-echo:0.2.3
- name: envoy-sidecar
  image: envoyproxy/envoy-alpine:v1.8.0
  command:
    - "/usr/local/bin/envoy"
  args:
    - "--config-path /etc/envoy/envoy.yaml"
    - "--mode serve"
    - "--service-cluster flask-app"
    - "--v2-config-only"
  ports:
    - containerPort: 8080
      protocol: TCP
      name: app
    - containerPort: 8001
      protocol: TCP
      name: metrics
  volumeMounts:
    - name: envoy-config
      mountPath: /etc/envoy
```


To run deployment and service of server with envoy as sidecar.
```command
kubectl apply -f app-deployment-with-envoy.yaml
```

### K8s servic spec

All our traffic to come to envoy sidecar then then routed to our http-echo server and we will back response in similar order.


```yaml
kind: Service
apiVersion: v1
metadata:
  name: k8s-envoy-101
  labels:
    app: k8s-envoy-101
spec:
  type: NodePort
  selector:
    app: k8s-envoy-101
  ports:
  - protocol: TCP
    name: app
    port: 8080
    nodePort: 31009
    targetPort: 8080
```


To check if working fine

```command
curl -I node-ip:31009
```
