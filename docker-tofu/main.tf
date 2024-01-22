resource "docker_image" "tofu-monitoring" {
	name   = "tofu-monitoring"
	keep_locally = true
	build {
	  context = "./app"
	  dockerfile = "Dockerfile"
	}
}

resource "docker_container" "monitoring-container" {
	name = "monitoring-container"
	image = docker_image.tofu-monitoring.image_id
	ports {
	  internal = "5000"
	  external = "5000"
	}
}