variable "project_id" {
    type = string
}

variable "region" {
    type = string
    default ="europe-west1"
}

variable "env" {
  type = string
}

variable "cluster" {
  type = string
}


variable "zone" {
    type = string
    default ="europe-west1-b"
}

variable "dataproc_service_account" {
  type = string
}