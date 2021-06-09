import os
import setuptools

setuptools.setup(
    name                            = "grover",
    version                         = "2.0",
    url                             = "https://github.com/stefanodangelo/grover-orquestra",
    packages                        = setuptools.find_packages(),
    classifiers                     = (
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ),
    install_requires = [
        "z-quantum-core",
        "pyquil",
        "cirq",
        "qiskit",
        "numpy"
   ],
)