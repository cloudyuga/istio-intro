In this application with will be running container http-echo with envoy as sidecar.

All our traffic to come to envoy sidecar then then routed to our http-echo server and we will back response in similar order.

To run the configmap envoy: 

```command
kubectl apply -f envoy-configmap.yaml
```

To run deployment and service of server with envoy as sidecar.

```command
kubectl apply -f pp-deployment-with-envoy.yaml
```

To check if working fine

```command
curl -I $(minikube ip):31009
```
