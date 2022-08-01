# Full Stack FastAPI

This project presents how to work with FastAPI on a monorepo setup.

## Installation

Access the following installation pages:
- https://docs.tilt.dev/install.html
- https://k3d.io/v5.4.4/#installation
- https://www.pulumi.com/docs/get-started/install/

## Usage

First of all, we need to create our K8s cluster locally. We'll use k3d for that.

```bash
k3d cluster create cluster --registry-create cluster-registry
```

Now, you just need to run Tilt:

```bash
tilt up
```

## Stack

- [Pantsbuild](https://www.pantsbuild.org/) :: The ergonomic build system.
- [Tilt](https://docs.tilt.dev/index.html) :: Tilt is a microservice development environment for teams that deploy to Kubernetes.
- [Pulumi](https://www.pulumi.com/docs/get-started/) :: Pulumi is a modern infrastructure as code platform that allows you to use familiar programming languages and tools to build, deploy, and manage cloud infrastructure.
- [k3d](https://k3d.io/) :: k3d is a lightweight wrapper to run [k3s](https://github.com/k3s-io/k3s) (Rancher Lab’s minimal Kubernetes distribution) in docker.

## Notes

This is still work in progress. I'll update this README during the development.

Watch the repository if interested to see the development. I'll be careful with the commit history.
