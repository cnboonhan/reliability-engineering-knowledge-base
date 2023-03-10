# psql-tuning

## Pre-Requisites
```
# Install Openshift Local and Setup on Bare Metal Laptop
https://developers.redhat.com/products/openshift-local/overview
https://access.redhat.com/documentation/en-us/red_hat_openshift_local/2.5/html/getting_started_guide/installation_gsg

# Start Openshift Local
crc start

# Get credentials and login
crc console --credentials

# Create Project
oc new-project psql-tuning

# Deploy 
oc apply -f onboarding.yaml
oc process psql-tuning-onboarding | oc apply -f -
```

## Experiments
```
# Configure database(TODO)

# Run pgbench to run benchmark and profile performance
oc apply -f pgbench.yaml

# Run jupyter to run interactive Experiments
oc apply -f jupyter.yaml

# Port forward pods to localhost to access them
oc port-forward POD_NAME PORT
```
