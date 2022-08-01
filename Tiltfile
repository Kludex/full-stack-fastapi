load('ext://pulumi', 'pulumi_resource')

custom_build(
    ref='blog',
    command='./pants package src/docker/blog:blog',
    deps=['./src/python/blog', './src/docker/blog'],
)

# https://github.com/tilt-dev/tilt-extensions/tree/master/pulumi
# https://blog.tilt.dev/2022/03/23/pulumi.html
pulumi_resource(
  'blog',
  stack='dev',
  dir='./infra',
  deps=['./infra/__main__.py'],
  image_deps=['blog'],
  image_configs=['image'],
  labels=['blog'],
  port_forwards=['8000:8000']
)
