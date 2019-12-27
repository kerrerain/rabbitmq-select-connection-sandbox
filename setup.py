from setuptools import setup, find_packages

setup(
    name="rabbitmq",
    version="0.0.1",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "pika==1.1.0",
        "retry==0.9.2"
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "pylint",
            "autopep8",
        ]
    }
)
