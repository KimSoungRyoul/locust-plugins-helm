TAG=6
IMAGE_NAME=sky5367/locust-timescale:$(TAG)

build:
	docker buildx build --platform linux/amd64,linux/arm64 --progress plain . -t $(IMAGE_NAME)

push:
	docker push $(IMAGE_NAME)

run:
	@echo no this doesnt work any more, use docker-compose file or locust-compose

shell:
	docker run -p 3000:3000 -it --entrypoint=/bin/bash $(IMAGE_NAME)