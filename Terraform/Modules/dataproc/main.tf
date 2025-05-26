resource "google_dataproc_cluster" "cluster" {
  name    = var.cluster
  project = var.project_id
  region  = var.region

  cluster_config {
    master_config {
      num_instances = 1
      machine_type  = "n1-standard-2"
      disk_config {
        boot_disk_size_gb = 50  # Taille réduite pour le disque du master
      }
    }

    worker_config {
      num_instances = 2
      machine_type  = "n1-standard-2"
      disk_config {
        boot_disk_size_gb = 50  # Taille réduite pour les disques des workers
      }
    }

    gce_cluster_config {
      zone            = var.zone
      service_account = var.dataproc_service_account
    }

    software_config {
      optional_components = ["JUPYTER"]
    }

    endpoint_config {
      enable_http_port_access = true
    }
  }
}
