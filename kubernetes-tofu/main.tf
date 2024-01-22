resource "kubernetes_manifest" "deployment_tofu_monitoring" {
  manifest = {
    "apiVersion" = "apps/v1"
    "kind" = "Deployment"
    "metadata" = {
      "annotations" = {
        "prometheus.io/path" = "/metrics"
        "prometheus.io/port" = "roboport"
        "prometheus.io/scrape" = "true"
      }
      "labels" = {
        "name" = "tofu-monitoring"
        "release" = "prometheus"
      }
      "name" = "tofu-monitoring"
      "namespace" = "default"
    }
    "spec" = {
      "replicas" = 1
      "selector" = {
        "matchLabels" = {
          "app" = "tofu-monitoring"
        }
      }
      "template" = {
        "metadata" = {
          "labels" = {
            "app" = "tofu-monitoring"
          }
        }
        "spec" = {
          "containers" = [
            {
              "image" = "linuxrobotgeek/tofu-monitoring:latest"
              "imagePullPolicy" = "Always"
              "name" = "tofu-monitoring"
              "ports" = [
                {
                  "containerPort" = 5000
                  "name" = "roboport"
                  "protocol" = "TCP"
                },
              ]
            },
          ]
        }
      }
    }
  }
}

resource "kubernetes_manifest" "service_tofu_monitoring" {
  manifest = {
    "apiVersion" = "v1"
    "kind" = "Service"
    "metadata" = {
      "labels" = {
        "app" = "tofu-monitoring"
      }
      "name" = "tofu-monitoring"
      "namespace" = "default"
    }
    "spec" = {
      "ports" = [
        {
          "name" = "tofu-monitoring"
          "port" = 5000
          "protocol" = "TCP"
          "targetPort" = "roboport"
        },
      ]
      "selector" = {
        "app" = "tofu-monitoring"
      }
      "type" = "LoadBalancer"
    }
  }
}

resource "kubernetes_manifest" "servicemonitor_monitoring_tofu_monitoring" {
  manifest = {
    "apiVersion" = "monitoring.coreos.com/v1"
    "kind" = "ServiceMonitor"
    "metadata" = {
      "labels" = {
        "app" = "tofu-monitoring"
        "release" = "prometheus"
      }
      "name" = "tofu-monitoring"
      "namespace" = "monitoring"
    }
    "spec" = {
      "endpoints" = [
        {
          "interval" = "15s"
          "path" = "/metrics"
          "port" = "tofu-monitoring"
        },
      ]
      "namespaceSelector" = {
        "matchNames" = [
          "default",
        ]
      }
      "selector" = {
        "matchLabels" = {
          "app" = "tofu-monitoring"
        }
      }
    }
  }
}