IMAGE = "envoy-course-101"
TAG = "v0.1"
CONTAINER = "envoy-course-101-container"
#APP_PORT = 9877
APP_PORT = 9876
HOST_PORT = 9001


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
	docker run -p $(HOST_PORT):$(APP_PORT) --name $(CONTAINER) $(IMAGE):$(TAG)

