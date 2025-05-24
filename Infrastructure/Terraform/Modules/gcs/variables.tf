variable "project_id" {
    type = string
}

variable "region" {
    type = string
    default ="europe-west1"
}

variable "structure" {
    type = map(list(string))
    description = "structure des repertoire à créer dans le buckets"
}

variable "env" {
  type = string
}
