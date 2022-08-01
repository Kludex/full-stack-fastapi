docker_image(
    name="blog",
    dependencies=["src/python/blog:main"],
    restartable=True,
    registries=["localhost:33807"],
    image_tags=["{build_args.EXPECTED_TAG}"],
)
