DOCKER_TAG ?= my-little-blog

.PHONY: run
run: build
	docker run -d -p 127.0.0.1:27000:8888 --name $(DOCKER_TAG)-container $(DOCKER_TAG)

.PHONY: run-dev
run-dev: build
	docker run -it --rm -p 27000:8888 --name $(DOCKER_TAG)-container $(DOCKER_TAG)

.PHONY: build
build:
	docker build -t $(DOCKER_TAG) .
