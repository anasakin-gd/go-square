# go-square

## Prerequisites

1. Minikube is installed
2. [ArgoCD installed](https://argo-cd.readthedocs.io/en/stable/getting_started/#1-install-argo-cd)
3. [VPA is installed](https://github.com/kubernetes/autoscaler/tree/master/vertical-pod-autoscaler#installation)  
4. Labeling namespaces for Goldilocks. To do that use`kubectl label ns NAMESPACE_NAME goldilocks.fairwinds.com/enabled=true`
5. Kubeconfig file is updated to work with your Minikube

## Deployment

1. Run `kubectl apply -f ./bootstrap` to install bootstrap **app-of-apps**.
It will create "argocd" namespace and will deploy bootstrap application that will deploy go-square application and ApplicationSet for Goldilocks and Polaris.
2. Get initial ArgoCD password via `k get secret argocd-initial-admin-secret -n argocd -o jsonpath='{.data.*}' | base64 -d`
3. Use Port Forwarding to access ArgoCD and deployed applications.  

    ```shell
    kubectl port-forward services/argocd-server 8080:80 -n argocd
    kubectl port-forward services/go-square 8000:8000 -n go-square
    kubectl port-forward services/goldilocks-dashboard 8081:80 -n goldilocks
    kubectl port-forward services/polaris-dashboard 8082:80 -n polaris
    ```

4. Test availability of apps.
