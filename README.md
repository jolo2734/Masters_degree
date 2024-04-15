# Masters_degree
For my Master's degree. Maily to save all yaml files for Kubernetes deployments. Maybe for IaaC.

### Description:
- Part 1. Plan is to deploy secure Kubernetes cluster with automatic security features like active network policy with monitoring(probably Prometheus+Grafana)
- Part 2. Compare Kubernetes security features/capabilities with DockerSwarm security features/capabilities.

## Tasks
- [ ] deploy 4 hosts
- [ ] deploy k8s cluster on these hosts
- [ ] harden cluster
- [ ] harden hosts
- [ ] deploy applications to generate some traffic
- [ ] deploy monitoring of these applications
- [ ] prepare attacks at cluster
- [ ] prepare auto-defense mechanisms

### Deploy 4 hosts
There will be 4 VMs with [Ubuntu 20.04.04 LTS](https://ubuntu.com/download/desktop/thank-you?version=22.04.4&architecture=amd64) created on VirtualBox:
- 1 master
  - mgr-k8s-master-01
- 3 workers
  - mgr-k8s-worker-01
  - mgr-k8s-worker-02
  - mgr-k8s-worker-03

### Deploy Kubernetes 1.28.6
This version of Kubernetes is chosen due to compatibility with Kubespray.

Kubernetes will be deployed by [Kubespray v2.24.1](https://github.com/kubernetes-sigs/kubespray/tree/v2.24.1).

### Cluster hardening

### Host hardening

### Deploy some applications

### Deploy monitoring of these applications

### Attacks

### Auto-defense mechanisms


