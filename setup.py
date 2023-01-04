""" Setup as a package so that celery can access the packages.  Then
install with `requirements.txt` and `-e .`.  """
import setuptools

setuptools.setup(
    name="captain-black",
    version="1.0",
    author="Joe Collins",
    author_email="joejcollins@gmail.com",
    description="Demonstrator",
    license="MIT License",
    url="https://github.com/joejcollins/captain-black",
    packages=setuptools.find_packages(),
    package_dir={"": "./"},
    classifiers=["Development Status :: 3 - Alpha", "License :: Other/Proprietary License"],
    install_requires=[
        "ansible",
        "ansible-runner",
        "black",
        "celery",
        "debugpy",  # only required for debugging, not needed for production.
        "flake8",
        "flasgger",
        "Flask",
        "flower",
        "mkdocs",
        "mkdocs-mermaid2-plugin",
        "mkdocs-roamlinks-plugin",
        "mypy",
        "ncclient",
        "pip-tools",  # used to manage requirements.txt.
        "pytest",  # used for testing, not needed for production.
        "pytest-flask",  # used for testing, not needed for production.
        "python-dotenv",  # used for the .env secrets file.
        "redis",
        "requests",
        "UnleashClient",
    ],
)
