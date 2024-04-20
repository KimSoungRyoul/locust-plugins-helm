TAG=3
IMAGE_NAME=sky5367/locust-grafana:$(TAG)

# --builder cloud-sky5367-locust-plugin-builder
build:
	docker buildx build --platform linux/amd64,linux/arm64 --progress plain . -t $(IMAGE_NAME)

push:
	docker push $(IMAGE_NAME)

run:
	docker run -p 3000:3000 $(IMAGE_NAME)

shell:
	docker run -p 3000:3000 -it --entrypoint=/bin/bash $(IMAGE_NAME)