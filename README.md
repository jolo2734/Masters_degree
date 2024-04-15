# Masters_degree
For my Master's degree. Maily to save all yaml files for Kubernetes deployments. Maybe for IaaC.

### Description:
- Part 1. Plan is to deploy secure Kubernetes cluster with automatic security features like active network policy with monitoring(probably Prometheus+Grafana)
- Part 2. Compare Kubernetes security features/capabilities with DockerSwarm/other security features/capabilities.

(In my master work I won't take into account the security settings of deployed application inside the cluster, only setting of cluster(networking, access, privileges, ...) and host(access from pods to host layer))
## Tasks
- [ ] deploy 5 hosts(4 for cluster, 1 for monitoring)
- [ ] deploy k8s cluster
- [ ] harden cluster
- [ ] harden hosts
- [ ] deploy applications
- [ ] deploy monitoring for these applications
- [ ] prepare attacks at cluster
- [ ] prepare auto-defense mechanisms
- [ ] compare k8s with other container orchestrator

### Deploy cluster hosts
There will be 4 VMs with [Ubuntu 20.04.04 LTS](https://ubuntu.com/download/desktop/thank-you?version=22.04.4&architecture=amd64) created on VirtualBox:
- 1 master
  - mgr-k8s-master-01(1 vCPU, 8GB RAM)
- 3 workers
  - mgr-k8s-worker-01(1 vCPU, 8GB RAM)
  - mgr-k8s-worker-02(1 vCPU, 8GB RAM)
  - mgr-k8s-worker-03(1 vCPU, 8GB RAM)

After each task VMs will be snapshoted to preserve working configuration states, also will ba backed up on another disc.
### Deploy Kubernetes 1.28.6
This version of Kubernetes is chosen due to compatibility with Kubespray.

Kubernetes will be deployed by [Kubespray v2.24.1](https://github.com/kubernetes-sigs/kubespray/tree/v2.24.1).

### Cluster hardening
Hardening of Kubernetes cluster is done in compliance with CIS standards, which are ensured during creating cluster by Kubespray [with this additional options](https://github.com/kubernetes-sigs/kubespray/blob/v2.24.1/docs/hardening.md).

### Host hardening
Hardening of Ubuntu 20.04.4 LTS is done in compliance with CIS standards. It is done by Ubuntu Pro plugin which check and set proper configuration of host.
Additional hardening need to be done regarding access from pods to host machine.

### Deploy some applications
 - API?
 - other service?

### Deploy monitoring of these applications
For monitoring and managing purposes will be deployed separate, not hardened, host:
- manage-and-monitor(1 vCPU, 8GB RAM)

Monitoring stack:
- Prometheus
- Grafana

### Attacks
- [something will be here]

### Auto-defense mechanisms
- based on monitoring
- based on hardening


