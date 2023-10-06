variable "cluster_name" {
  default = "testeks"
}

variable "region" {
  default = "eastus"
}

variable "enable_karpenter" {
  default = "True"
}

variable "enable_external_dns" {
  default = "True"
}

variable "enable_argocd" {
  default = "True"
}

variable "enable_ingress_nginx" {
  default = "True"
}

variable "enable_velero" {
  default = "True"
}

variable "enable_cert_manager" {
  default = "True"
}

