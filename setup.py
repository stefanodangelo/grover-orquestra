import os
import setuptools

setuptools.setup(
    name                            = "tutorial",
    version                         = "0.1.0",
    author                          = "Zapata Computing, Inc.",
    author_email                    = "info@zapatacomputing.com",
    description                     = "Training models with scikit-learn in orquestra.",
    url                             = "https://github.com/stefanodangelo/grover-orquestra",
    packages                        = setuptools.find_packages(),
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        "pyquil",
        "cirq",
        "qiskit",
        "numpy"
   ],
)