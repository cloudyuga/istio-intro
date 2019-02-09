IMAGE = "teamcloudyuga/istio-flask-backend"
TAG = "v0.1"
CONTAINER = "istio-flask-backend1"


build:
	docker build -t $(IMAGE):$(TAG) .

build-push: build
	docker push $(IMAGE):$(TAG)

clean:
	docker stop $(CONTAINER)
	docker rm $(CONTAINER)

exec:
	docker exec -it $(CONTAINER) bash

logs:
	docker logs $(CONTAINER)

run:
	docker run -p 9999:9090 --name $(CONTAINER) -d $(IMAGE):$(TAG)


