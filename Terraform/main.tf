locals {
  folders_structure = jsondecode(file("Modules/gcs/bucket_structure.json"))
}

module "gcs" {
  source     = "./Modules/gcs"
  project_id = var.project_id
  region     = var.region
  env        = var.env
  structure  = local.folders_structure
}



module "dataproc" {
  source = "./Modules/dataproc"
  project_id = var.project_id
  region = var.region
  env = var.env
  zone = var.zone
  cluster = var.cluster
  dataproc_service_account = var.dataproc_service_account
}


module "bigquery" {
  source = "./Modules/bigquery"
  project_id =  var.project_id
  region = var.region
  env = var.env
}