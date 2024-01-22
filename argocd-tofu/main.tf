resource "kubernetes_manifest" "application_argocd_terraform_monitoring" {
  manifest = {
    "apiVersion" = "argoproj.io/v1alpha1"
    "kind" = "Application"
    "metadata" = {
      "name" = "tofu-monitoring"
      "namespace" = "argocd"
    }
    "spec" = {
      "destination" = {
        "namespace" = "default"
        "server" = "https://kubernetes.default.svc"
      }
      "project" = "default"
      "source" = {
        "path" = "kubernetes"
        "repoURL" = "https://github.com/sentairanger/Open-Tofu-Monitoring"
        "targetRevision" = "HEAD"
      }
      "syncPolicy" = {}
    }
  }
}