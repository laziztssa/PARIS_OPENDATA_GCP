variable "project_id" {
    type = string
}

variable "region" {
    type = string
    default ="us-east1"
}

variable "structure" {
    type = map(list(string))
    description = "structure des repertoire à créer dans le buckets"
}

variable "env" {
  type = string
}
