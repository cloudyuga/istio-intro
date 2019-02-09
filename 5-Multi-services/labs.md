
Jaeger is Distributed Tracing System. Here we will track a single request through our internal systems to see how time is spent.


Apply : 

Export the jaeger endpoint: 

```command
kubectl port-forward -n istio-system $(kubectl get pod -n istio-system -l app=jaeger -o jsonpath='{.items[0].metadata.name}') 16686:16686
```

Visit : <a href="localhost:16686"> localhost:16686 </a> to see jaeger dashboard.

Apply k8s config and istio config

```command
kubectl apply -f k8s.yaml
kubectl apply -f istio-0.yaml
```

Try making some request


Expose HOST and PORT
* `export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].nodePort}')`
* `export INGRESS_HOST=$(minikube ip)`

Output: we will see one of following message while making requests.

```
$ > curl http://${INGRESS_HOST}:$INGRESS_PORT/
We are on v4
```

```
 $ > curl http://${INGRESS_HOST}:$INGRESS_PORT/
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>503 Service Unavailable</title>
<h1>Service Unavailable</h1>
<p>The server is temporarily unable to service your request due to maintenance downtime or capacity problems.  Please try again later.</p>
```

Now go to dashboard [localhost:16686](http://localhost:16686) and see the trace of request.


---
Reference:
    * https://istio.io/docs/tasks/traffic-management/ingress/#determining-the-ingress-ip-and-ports
