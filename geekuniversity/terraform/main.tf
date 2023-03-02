terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.20.3"
    }
  }
}

provider "docker" {
  host     = "ssh://root@45.65.222.182:4022"
  ssh_opts = ["-o", "StrictHostKeyChecking=no", "-o", "UserKnownHostsFile=/dev/null"]
}

# Pulls the image
resource "docker_image" "nginx" {
  name = "nginx:latest"
  keep_locally = false
}

# Create a container
resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name  = "nginx"
  ports {
    internal = 80
    external = 6081
  }
}