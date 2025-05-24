resource "google_dataproc_cluster" "cluster" {
  name = var.cluster
  project = var.project_id
  region = var.region


    cluster_config {
        master_config {
        num_instances = 1
        machine_type  = "n1-standard-2"
        }

    worker_config {
      num_instances = 2
      machine_type  = "n1-standard-2"
    }

    gce_cluster_config {
      zone = var.zone
      service_account =  var.dataproc_service_account
    }
  }
}
