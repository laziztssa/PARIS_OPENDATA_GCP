resource "google_composer_environment" "composer" {
  name = var.composer_name
  project = var.project_id
  region = var.region
  
  
    config {
      software_config {
        image_version = "composer-3-airflow-2.10.5-build.3"
        } 

      node_config {
        network = var.network
        subnetwork = var.subnetwork
        service_account = var.service_account
      } 

    }
}