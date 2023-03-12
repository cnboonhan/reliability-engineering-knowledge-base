# psql-tuning

## Pre-Requisites
```
# Install Openshift Local and Setup on Bare Metal Laptop
https://developers.redhat.com/products/openshift-local/overview
https://access.redhat.com/documentation/en-us/red_hat_openshift_local/2.5/html/getting_started_guide/installation_gsg

# Start Openshift Local
crc config set enable-cluster-monitoring true
crc config set memory 14500
crc config set disk-size 100
crc start

# Get credentials and login
crc console --credentials

# Create Project
oc new-project psql-tuning

# Deploy 
oc apply -f onboarding.openshift.yaml
oc process psql-tuning-onboarding | oc apply -f -
oc apply -f jupyter.openshift.yaml

# Build lab image and deploy
oc start-build psql-tuning-build  --from-dir=.

# Access labs at http://jupyter-route-psql-tuning.apps-crc.testing/lab
```
