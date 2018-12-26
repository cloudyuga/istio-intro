IMAGE = "library/envoy-101-flask-app"
TAG = "v0.1"
CONTAINER = "envoy-101-flask-app"
APP_PORT=9090 
HOST_PORT=9999

build:
	docker build -t $(IMAGE):$(TAG) .

clean:
	docker stop $(CONTAINER)
	docker rm $(CONTAINER)

exec:
	docker exec -it $(CONTAINER) bash

logs:
	docker logs $(CONTAINER)

run:
	@echo "Port forwarding set to $(HOST_PORT)"
	docker run -p $(HOST_PORT):$(APP_PORT) --name $(CONTAINER) $(IMAGE):$(TAG)

