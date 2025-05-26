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

variable "composer_name" {
  type = string
}


variable "network" {
  type = string
}


variable "subnetwork" {
  type = string
}


variable "service_account" {
  type = string
}