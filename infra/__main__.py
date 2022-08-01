"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.core.v1 import ContainerArgs, PodSpecArgs, PodTemplateSpecArgs
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs

config = pulumi.Config()
image = config.require("image")

app_labels = {"app": "blog"}
deployment = Deployment(
    "blog-deployment",
    spec=DeploymentSpecArgs(
        selector=LabelSelectorArgs(match_labels=app_labels),
        replicas=1,
        template=PodTemplateSpecArgs(
            metadata=ObjectMetaArgs(labels=app_labels),
            spec=PodSpecArgs(containers=[ContainerArgs(name="blog", image=image)]),
        ),
    ),
)

pulumi.export("name", deployment.metadata["name"])
