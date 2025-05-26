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

variable "env_parameters" {
  type        = string
  description = "JSON string contenant les paramètres d'environnement"
}