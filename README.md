# locust-plugins-helm ![Version: 0.31.5](https://img.shields.io/badge/Version-0.31.5-informational?style=flat-square) ![AppVersion: 2.15.1](https://img.shields.io/badge/AppVersion-2.15.1-informational?style=flat-square)


* based-on deliveryhero/locust
* Alternative: [Locust-Swarm](https://github.com/SvenskaSpel/locust-swarm)

~~~
minikube start
kubectl create ns locust-plugins
helm repo add locust-plugins https://kimsoungryoul.github.io/locust-plugins-helm

kubectl create configmap loadtest-lib --from-file locustfiles/example/lib -n locust-plugins
# kubectl create configmap loadtest-locustfile --from-file locustfiles/example/main.py -n locust-plugins

helm upgrade -i -n locust-plugins locust-plugins locust-plugins/locust-plugins \
  --set loadtest.name=hello-loadtest \
  --set loadtest.locust_locustfile_configmap=loadtest-locustfile \
  --set loadtest.locust_lib_configmap=loadtest-lib

~~~



A chart to install Locust, a scalable load testing tool written in Python.

This chart will setup everything required to run a full distributed locust environment with any amount of workers.

This chart will also create configmaps for storing the locust files in Kubernetes, this way there is no need to build custom docker images.

By default it will install using an example locustfile and lib from [stable/locust/locustfiles/example](https://github.com/deliveryhero/helm-charts/tree/master/stable/locust/locustfiles/example). When you want to provide your own locustfile, you will need to create 2 configmaps using the structure from that example:

```console
kubectl create configmap my-loadtest-locustfile --from-file path/to/your/main.py
kubectl create configmap my-loadtest-lib --from-file path/to/your/lib/
```

And then install the chart passing the names of those configmaps as values:

```console
helm install locust deliveryhero/locust \
  --set loadtest.name=my-loadtest \
  --set loadtest.locust_locustfile_configmap=my-loadtest-locustfile \
  --set loadtest.locust_lib_configmap=my-loadtest-lib
```



## Maintainers

| Name          | Email                     | Url |
|---------------|---------------------------| --- |
| kimsoungryoul | <kimsoungryoul@gmail.com> |  |
