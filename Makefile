HOST_PATH ?= $(shell pwd)

REPO_ORG ?= $(shell basename $(HOST_PATH))
REPO = $(shell echo $(REPO_ORG) | tr A-Z a-z)

TAG = 'develop'

GUEST_PATH = '/tmp/$(REPO)'

CMD_DEV = 'cd $(GUEST_PATH) && /bin/bash start-service.sh && /bin/bash'
CMD_TEST = 'cd $(GUEST_PATH) && /bin/bash run-test.sh'

HOST_PORT ?= 80

# -------------------------                                                     
# golang path                                                        
# -------------------------
GOPARDIR = "/tmp"                                                         
GOROOT = "$(GOPARDIR)/go"                                                        
GOPATH = "/tmp/golang" 

# -------------------------
# Main
# -------------------------
build: Dockerfile
	docker build \
	  --build-arg ARG_GOPARDIR=$(GOPARDIR) \
	  --build-arg ARG_GOROOT=$(GOROOT) \
	  --build-arg ARG_GOPATH=$(GOPATH) \
	  -t $(REPO):$(TAG) \
      -f Dockerfile .

run:
	docker run --rm \
	  -v $(HOST_PATH):$(GUEST_PATH) \
	  -p $(HOST_PORT):80 \
	  -e GOROOT=$(GOROOT) \
	  -e GOPATH=$(GOPATH) \
	  $(DOCKER_OPTIONS) -it $(REPO):$(TAG) /bin/bash -c $(CMD_DEV)

test:
	docker run --rm \
	  -v $(HOST_PATH):$(GUEST_PATH) \
	  $(DOCKER_OPTIONS) -it $(REPO):$(TAG) /bin/bash -c $(CMD_TEST)

