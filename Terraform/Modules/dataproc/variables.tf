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

variable "cluster" {
  type = string
}


variable "zone" {
    type = string
    default ="us-east1-c"
}

variable "dataproc_service_account" {
  type = string
}