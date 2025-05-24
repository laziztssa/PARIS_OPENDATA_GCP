# ressource google cloud storage

resource "google_storage_bucket" "data" {
    name = "${var.project_id}-data"
    location = var.region
    project = var.project_id
    force_destroy = true
}


## reccuperation des arboresnce des dossier à créer dans le bucket à partir du fichier structure.json

locals {
  folders = flatten([
    for zone , sources in var.structure : [
        for source in sources : "${zone}/${source}/" #
    ]
  ])
}


### rajout de ressource objet bucket

resource "google_storage_bucket_object" "folders" {
  for_each = toset(local.folders)
  name     = each.value
  bucket   = google_storage_bucket.data.name
  content  = " "
}
