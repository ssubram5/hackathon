provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "my-vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "my-vpc"
  }
}

resource "aws_subnet" "my-subnet-1" {
  vpc_id     = aws_vpc.my-vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "us-west-2a"
  tags = {
    Name = "my-subnet-1"
  }
}

resource "aws_subnet" "my-subnet-2" {
  vpc_id     = aws_vpc.my-vpc.id
  cidr_block = "10.0.2.0/24"
  availability_zone = "us-west-2b"
  tags = {
    Name = "my-subnet-2"
  }
}

resource "aws_subnet" "my-subnet-3" {
  vpc_id     = aws_vpc.my-vpc.id
  cidr_block = "10.0.3.0/24"
  availability_zone = "us-west-2c"
  tags = {
    Name = "my-subnet-3"
  }
}

module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 19.0"

  cluster_name    = var.cluster_name
  cluster_version = "1.27"

  cluster_endpoint_public_access  = true

  vpc_id                   = aws_vpc.my-vpc.id
  subnet_ids               = [aws_subnet.y-subnet-1.id]
  control_plane_subnet_ids = [aws_subnet.y-subnet-2.id]
}

module "eks_blueprints_addons" {
  source = "aws-ia/eks-blueprints-addons/aws"
  version = "~> 1.0" #ensure to update this to the latest/desired version

  cluster_name      = module.eks.cluster_name
  cluster_endpoint  = module.eks.cluster_endpoint
  cluster_version   = module.eks.cluster_version
  oidc_provider_arn = module.eks.oidc_provider_arn

  eks_addons = {
    aws-ebs-csi-driver = {
      most_recent = true
    }
    coredns = {
      most_recent = true
    }
    vpc-cni = {
      most_recent = true
    }
    kube-proxy = {
      most_recent = true
    }
  }

  enable_aws_load_balancer_controller    = false
  enable_cluster_proportional_autoscaler = false
  enable_karpenter                       = var.enable_karpenter
  enable_kube_prometheus_stack           = false
  enable_external_dns                    = var.enable_external_dns
  enable_argocd                          = var.enable_argocd
  enable_ingress_nginx                  = var.enable_ingress_nginx
  enable_velero                         = var.enable_velero
  enable_cert_manager                  = var.enable_cert_manager

  tags = {
    Environment = "dev"
  }
}