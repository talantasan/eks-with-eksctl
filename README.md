# eks-with-eksctl
## create cluster from command line
## 1. 
```
eksctl create cluster --name dev-cluster --nodes 2 --node-type m5.large --region us-east-1 > cluster2.yaml
```

## 2. 
```
eksctl create cluster --name my-cluster --nodes 3 --node-type m5.large --region us-east-1 --version 1.29 --nodegroup-name talant-node-group
```

## Delete cluster from config file
```
eksctl delete cluster -f config.yaml
```
