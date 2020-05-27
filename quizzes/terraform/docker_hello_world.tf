# Simple config for Terraform to run "Hello World container on docker"

# Define a Docker provider
provider "docker" {
}

#Run docker container with exposes ports
resource "docker_container" "hello_world" {
  name  = "hello_world"
  image = "${docker_image.hello_world.latest}"
  start = true
  ports {
    internal = "80"
    external = "8080"
  }
}

# Define an image for container
resource "docker_image" "hello_world" {
  name = "karthequian/helloworld"
}
