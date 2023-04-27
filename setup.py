from setuptools import setup, find_packages

setup(
    name="census-income",
    version=0.1,
    author="Faisal",
    author_email="fhrt811@gmail.com",
    packages=find_packages(),
    install_requires=["pandas","numpy","flask"]
)