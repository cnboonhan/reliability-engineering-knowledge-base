# psql-tuning

## Pre-Requisites
```
# Install Openshift Local and Setup on Bare Metal Laptop
https://developers.redhat.com/products/openshift-local/overview
https://access.redhat.com/documentation/en-us/red_hat_openshift_local/2.5/html/getting_started_guide/installation_gsg

crc start

# Create Project
oc new-project psql-tuning

# Deploy 
oc apply -f onboarding.yaml
 oc process psql-tuning-onboarding | oc apply -f -
```
