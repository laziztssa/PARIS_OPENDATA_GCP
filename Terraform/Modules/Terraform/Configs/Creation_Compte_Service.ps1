gcloud iam service-accounts create terraform-admin --description="Service account for Terraform" --display-name="Terraform Admin"

gcloud projects add-iam-policy-binding paris_opendata-gcp --member="serviceAccount:terraform-admin@paris_opendata-gcp.iam.gserviceaccount.com" --role="roles/owner"

gcloud iam service-accounts keys create terraform-key.json --iam-account=terraform-admin@paris-opendata-gcp.iam.gserviceaccount.com
