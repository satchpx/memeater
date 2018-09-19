# Memory eater application
- This application simulates an application that exceeds its memory limits over time and gets OOM killed.
- In the same thread, it also has active IO against its persistent volume (a portworx volume)
- This is to test if an application using px getting OOM-killed has any impact to portworx.

## To build the container
```
docker build -t <container_name> .
```

A prebuilt container can be used from `satchpx/memeater:latest`

## To deploy the application on K8s
```
kubectl apply -f memeater-deployment.yaml
```

## Note:
```
1. The resource limits are set to 512MiB. To simulate an OOM faster or slower, adjust the resource limit accordingly
```
