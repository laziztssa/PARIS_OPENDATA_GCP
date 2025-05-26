# Create a Google Cloud Secret Manager secret to store environment parameters
resource "google_secret_manager_secret" "env" {
  project   = var.project_id
  secret_id = "env-parameters"

  replication {
    auto {
    } 
  }
}


resource "google_secret_manager_secret_version" "env" {
    secret = google_secret_manager_secret.env.id
    secret_data = var.env_parameters
}