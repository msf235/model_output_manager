import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="model-output-manager",
    version="0.0.1",
    author="Matthew Farrell",
    author_email="msf9@uw.edu",
    description="Manager for model output",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # packages=["model_output_manager"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)