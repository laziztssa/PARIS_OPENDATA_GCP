resource "google_bigquery_dataset" "bronze" {
    dataset_id = "bronze"
    project = var.project_id
    location = var.region
    delete_contents_on_destroy = true
}


resource "google_bigquery_dataset" "silver" {
    dataset_id = "silver"
    project = var.project_id
    location = var.region
    delete_contents_on_destroy = true
}

resource "google_bigquery_dataset" "gold" {
    dataset_id = "gold"
    project = var.project_id
    location = var.region
    delete_contents_on_destroy = true
}