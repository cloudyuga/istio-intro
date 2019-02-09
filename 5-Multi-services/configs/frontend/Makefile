apply-k8s-v1:
	kubectl apply -f v1/k8s.yaml

apply-k8s-v2:
	kubectl apply -f v2/k8s.yaml

build-v1:
	cd v1/app; make build-push

build-v2:
	cd v2/app; make build-push

delete-k8s-v1:
	kubectl delete -f v1/k8s.yaml

delete-k8s-v2:
	kubectl delete -f v2/k8s.yaml

exec-k8s-v1:
	kubectl logs $(shell kubectl get pods -l app=frontend,version=v1 -o=jsonpath='{.items[*].metadata.name}')  flask-frontend-app -f

exec-k8s-v2:
	kubectl logs $(shell kubectl get pods -l app=frontend,version=v2 -o=jsonpath='{.items[*].metadata.name}') flask-frontend-app -f

logs-k8s-v1:
	kubectl logs $(shell kubectl get pods -l app=frontend,version=v1 -o=jsonpath='{.items[*].metadata.name}') flask-frontend-app -f

logs-k8s-v2:
	kubectl logs $(shell kubectl get pods -l app=frontend,version=v2 -o=jsonpath='{.items[*].metadata.name}') flask-frontend-app -f

istio:
	kubectl apply -f istio.yaml

istio-delete:
	kubectl delete -f istio.yaml

toggle-v1: delete-k8s-v1 apply-k8s-v1
toggle-v2: delete-k8s-v2 apply-k8s-v2

