from setuptools import setup, find_packages

setup(
    name="cronexpressions",
    version="0.1.1",
    description="A library for predefined and custom cron expressions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Youcef Hanaia",
    author_email="hanaiayoucef@gmail.com",
    url="https://github.com/poysa213/cronexpressions.git",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
