import os
import setuptools

setuptools.setup(
    name                            = "grover-orquestra",
    version                         = "0.0.0",
    author                          = "Test",
    author_email                    = "test@example.com",
    packages                        = setuptools.find_packages(),
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        "numpy"
   ],
)