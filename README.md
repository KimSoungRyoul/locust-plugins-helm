# locust-plugins-helm ![Version: 0.31.5](https://img.shields.io/badge/Version-0.31.5-informational?style=flat-square) ![AppVersion: 2.15.1](https://img.shields.io/badge/AppVersion-2.15.1-informational?style=flat-square)


* based-on deliveryhero/locust
* Alternative: [Locust-Swarm](https://github.com/SvenskaSpel/locust-swarm)

## QuickStart
~~~shell
minikube start --cpus 4 --memory 4G

kubectl create ns locust-plugins
helm repo add locust-plugins https://kimsoungryoul.github.io/locust-plugins-helm

# see sample code more detail https://github.com/KimSoungRyoul/locust-plugins-helm/tree/main/locustfiles/example
kubectl create configmap loadtest-lib --from-file locustfiles/example/lib -n locust-plugins
kubectl create configmap loadtest-locustfile --from-file locustfiles/example/main.py -n locust-plugins

helm upgrade -i -n locust-plugins locust-plugins locust-plugins/locust-plugins \
  --set loadtest.name=hello-loadtest \
  --set loadtest.locust_locustfile_configmap=loadtest-locustfile \
  --set loadtest.locust_lib_configmap=loadtest-lib \
  --set=sample_apiserver.enable=true # <---- set false if install in prod
~~~

## helm chart resource


~~~shell
# minikube 
kubectl get all -n locust-plugins
NAME                                                   READY   STATUS    RESTARTS   AGE
pod/locust-plugins-grafana-56f865cfbc-7rng2            1/1     Running   0          13m
pod/locust-plugins-master-5fd7f85fd-bjgfv              1/1     Running   0          13m
pod/locust-plugins-sample-apiserver-696c9bc8b9-82z4l   1/1     Running   0          13m
pod/locust-plugins-sample-apiserver-696c9bc8b9-8zlw8   1/1     Running   0          13m
pod/locust-plugins-sample-apiserver-696c9bc8b9-qcmmn   1/1     Running   0          13m
pod/locust-plugins-timescaledb-59dd579b44-fx75n        1/1     Running   0          13m
pod/locust-plugins-worker-6c4bd49c85-26b45             1/1     Running   0          13m

NAME                                      TYPE           CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
service/locust-plugins                    ClusterIP      10.101.64.100   <none>        5557/TCP,5558/TCP,8089/TCP   13m
service/locust-plugins-grafana            LoadBalancer   10.111.48.148   <pending>     4000:32370/TCP               13m
service/locust-plugins-sample-apiserver   LoadBalancer   10.100.110.40   <pending>     8000:32286/TCP               13m
service/locust-plugins-timescaledb        LoadBalancer   10.103.216.24   <pending>     5432:31502/TCP               13m

NAME                                              READY   UP-TO-DATE   AVAILABLE   AGE
deployment.apps/locust-plugins-grafana            1/1     1            1           13m
deployment.apps/locust-plugins-master             1/1     1            1           13m
deployment.apps/locust-plugins-sample-apiserver   3/3     3            3           13m
deployment.apps/locust-plugins-timescaledb        1/1     1            1           13m
deployment.apps/locust-plugins-worker             1/1     1            1           13m

NAME                                                         DESIRED   CURRENT   READY   AGE
replicaset.apps/locust-plugins-grafana-56f865cfbc            1         1         1       13m
replicaset.apps/locust-plugins-master-5fd7f85fd              1         1         1       13m
replicaset.apps/locust-plugins-sample-apiserver-696c9bc8b9   3         3         3       13m
replicaset.apps/locust-plugins-timescaledb-59dd579b44        1         1         1       13m
replicaset.apps/locust-plugins-worker-6c4bd49c85             1         1         1       13m

~~~

## locust-plugin dashboard

* `kubectl -n locust-plugins port-forward svc/locust-plugins-grafana 3000:3000`
* http://localhost:3000
### locust grafana dashboard
<img width="1744" alt="스크린샷 2024-04-27 오전 2 47 31" src="https://github.com/KimSoungRyoul/locust-plugins-helm/assets/24240623/4867ffe5-16c1-4922-9b0a-b0efec13bd95">
<img width="1740" alt="스크린샷 2024-04-27 오전 2 47 22" src="https://github.com/KimSoungRyoul/locust-plugins-helm/assets/24240623/a67a82fa-66f1-4e3c-a4c1-ab62c2342bdf">
<img width="1746" alt="스크린샷 2024-04-27 오전 2 47 11" src="https://github.com/KimSoungRyoul/locust-plugins-helm/assets/24240623/a972ca75-ca7f-467e-b846-36a773d6e7f8">

### locust requests scatter
<img width="1739" alt="스크린샷 2024-04-27 오전 2 46 49" src="https://github.com/KimSoungRyoul/locust-plugins-helm/assets/24240623/3e9366da-38cb-4418-8b49-48fb4b6d0116">


## locust Master UI
* `kubectl -n locust-plugins port-forward service/locust-plugins 8089:8089`
* http://localhost:8089
<img width="1394" alt="스크린샷 2024-04-27 오전 2 45 56" src="https://github.com/KimSoungRyoul/locust-plugins-helm/assets/24240623/1f19aaf0-638a-4f8e-9e1b-6467af3f63ab">



## Maintainers

| Name          | Email                     | Url |
|---------------|---------------------------| --- |
| kimsoungryoul | <kimsoungryoul@gmail.com> |  |
