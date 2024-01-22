# Open-Tofu-Monitoring
This project is exactly the same as my Terraform Monitoring Project but uses the open source Open Tofu instead of Terraform. Open Tofu is open source IaaS (Infrastructure as Code) which is used for infrastructure provisioning. I decided to switch to Open Tofu to test compatibility and the fact that Terraform was switching to a different license.

## Getting Started

To get started, the following applications must be installed on a local machine or on the cloud.

* [Docker](https://docs.docker.com/engine/install/)
* [Terraform](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli): This is required to install Open Tofu and as a backup in case Open Tofu fails.
* [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html): Ansible cannot be installed on Windows without enabling WSL.
* [Open Tofu](https://opentofu.org/docs/intro/install/): Note that Open Tofu has not released its first stable release so be sure to report any issues to their GitHub issues section.

## The Structure of the Project

This project is divided into multiple directories:

* `argocd-nodeport-tofu`: This contains the required HCL files to create a Node Port service`.
* `argocd-tofu`: This contains the required HCL files to deploy the Kubernetes cluster into Argo CD.
* `docker-tofu`: This contains the main application code and has the required HCL files to build and run the docker image.
* `grafana`: Contains the dashboard JSON file to build the Grafana dashboard. When accessing Grafana be sure to Import this dashboard rather than building a new one.
* `images`: Contains images
* `kubernetes-tofu`: Contains required HCL files to build the test Kubernetes cluster
* `kubernetes`: Contains the main manifest required by Argo CD to deploy the application.
* `playbooks`: Contains the required Ansible playbooks to install or deploy services.

## How to run Project

To run this project, you can test the main code first in the `docker-tofu` diectory and go into the `app` sub directory. Then run with `python3 app.py`. Be sure to go to `localhost:5000` or `external-ip:5000`. Be sure you enable Remote GPIO access with `sudo pigpiod` before running the application. You can extend the code to add more robots. The `docker-tofu`, `kubernetes-tofu`, and the `argocd-tofu` directories are used to test the application. You can run the HCL files by first running `tofu init`, validate with `tofu validate` and then `tofu apply`. Then the infrastructure should be created depending on which directory you are testing. You can remove the infrastructure with `tofu destroy`. The Ansible playbooks in the `playbooks` directory can be run with `ansible-playbook <directory>/<playbook>`. 

If you want to build the dashboard to monitor the robots, here are the steps to follow:

* If you haven't already, first build the Docker image in the `docker-tofu` directory. Run `tofu init`, test with `tofu validate` and then `tofu apply`. Make sure the Docker image was created with `docker images` and that the image is running with `docker ps`. Go to `localhost:5000` or `external-ip:5000`. You can clean things up with `tofu destroy`. Tag and push by going into the `playbooks` directory and then running `ansible-playbook docker/docker-push.yml`.

* Next, test that Kubernetes works by going into the `kubernetes-tofu` directory. Run the same commands as in the `docker-tofu` directory. You can optionally port forward the application by going into the `playbooks` directory again and then run `ansible-playbook kubernetes/port-forward.yml`. You can clean things up again with `tofu destroy`.
* Finally, go into the `argocd-tofu` directory. Make sure you have Argo CD installed first, created the Node Port and that you port forwarded the node port by running the command `ansible-playbook argocd/argocd-port.yml`. Log into Argo CD and then running the same commands as in the previous steps. Go to the Argo CD UI and Sync the cluster. Then it should work. You can check that Prometheus is scraping the application with `ansible-playbook prometheus/prometheus.yml` and go to `localhost:9090` or `external-ip:9090`. Then go to Status and then targets. It should appear in the bottom.
* Then go to the `playbooks` directory and make sure you opened another terminal window. In fact you will need to open extra terminal tabs for each playbook. Port forward the application with `ansible-playbook kubernetes/port-forward.yml`, then go to another terminal tab and then run `ansible-playbook grafana/grafana.yml` to access grafana. Run the application in another tab in your browser using `localhost:5000` or `external-ip:5000` and test it out. Then open another tab in your browser and then go to `localhost:3000` or `external-ip:3000` to access Grafana. Log in with `admin` and password `prom-operator`. Be sure to change the password to be more secure. Then go to Dashboards and click on New Dashboard and Import. Select the Dashboard in the `grafana` directory and then it should appear. Run the application a few times to see the charts update.

## Using Open Tofu on Other Cloud Environments

Open Tofu, Like Terraform should work in your Azure, AWS or Google Cloud Services. My [Terraform](https://github.com/sentairanger/Terraform-Monitoring) Repository has a section on how to do that. It should work with Open Tofu as well. If any issue arises be sure to report it to the GitHub issues section of Open Tofu.

## Compatibility in other Web Frameworks

Like with my Terraform Monitoring application, this should work with other frameworks as well. As long as the code supports Remote GPIO access, then it should work. This has been tested in Python, Node.js, Java, and Perl, for example.

## Images

* Main application
![App](https://github.com/sentairanger/Open-Tofu-Monitoring/blob/main/images/app.png)

* Argo CD UI
![Argo CD](https://github.com/sentairanger/Open-Tofu-Monitoring/blob/main/images/argocd.png)

* Prometheus UI
![prometheus](https://github.com/sentairanger/Open-Tofu-Monitoring/blob/main/images/prometheus.png)

* Grafana Dashboard For The Application
![opentofu](https://github.com/sentairanger/Open-Tofu-Monitoring/blob/main/images/dashboard.png)
