# ok: gcp-sub-network-logging-enabled
resource "google_compute_subnetwork" "enabled" {
  name          = "example"
  ip_cidr_range = "10.0.0.0/16"
  network       = "google_compute_network.vpc.self_link"

  log_config {
    aggregation_interval = "INTERVAL_10_MIN"
    flow_sampling        = 0.5
    metadata             = "INCLUDE_ALL_METADATA"
  }
}

# fail
# ruleid: gcp-sub-network-logging-enabled
resource "google_compute_subnetwork" "default" {
  name          = "example"
  ip_cidr_range = "10.0.0.0/16"
  network       = "google_compute_network.vpc.id"
}
