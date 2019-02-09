apply-k8s-v1:
	kubectl apply -f v1/k8s.yaml

apply-k8s-v2:
	kubectl apply -f v2/k8s.yaml

delete-k8s-v1:
	kubectl delete -f v1/k8s.yaml

delete-k8s-v2:
	kubectl delete -f v2/k8s.yaml

logs-k8s-v1:
	kubectl logs $(shell kubectl get pods -l app=paytm-app,version=v1 -o=jsonpath='{.items[*].metadata.name}') paytm -f

logs-k8s-v2:
	kubectl logs $(shell kubectl get pods -l app=paytm-app,version=v2 -o=jsonpath='{.items[*].metadata.name}') paytm -f

istio:
	kubectl apply -f istio.yaml

istio-delete:
	kubectl delete -f istio.yaml

toggle-v1: delete-k8s-v1 apply-k8s-v1
toggle-v2: delete-k8s-v2 apply-k8s-v2
