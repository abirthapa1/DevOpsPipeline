# backend.tf
terraform {
  backend "s3" {
    bucket = "devops-pipeline-atjt"
    key    = "terraform-statefile/terraform.tfstate"
    region = "us-east-1"
  }
}
