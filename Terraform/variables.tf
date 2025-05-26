variable "project_id" {
    type = string
}

variable "region" {
    type = string
    default ="us-east1"
}

variable "env" {
  type = string
}

variable "zone" {
    type = string
    default ="us-east1-b"
}

variable "cluster" {
  type = string
}

variable "dataproc_service_account" {
  type = string
}
