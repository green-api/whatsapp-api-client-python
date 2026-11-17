from pathlib import Path

from setuptools import find_packages, setup
from setuptools.command.build_py import build_py


DOCUMENTATION_FILES = ("AGENTS.md", "ARCHITECTURE.md", "CONTRIBUTING.md", "LICENSE")


class BuildPyWithDocumentation(build_py):
    """Copy root documentation into the built package; propagate copy failures."""

    def run(self):
        """Build modules and copy documentation without changing source files."""
        super().run()
        source_root = Path(__file__).resolve().parent
        destination = Path(self.build_lib) / "whatsapp_api_client_python"
        self.mkpath(str(destination))
        for name in DOCUMENTATION_FILES:
            self.copy_file(str(source_root / name), str(destination / name))

    def get_outputs(self, include_bytecode=True):
        """Report generated documents alongside the standard module outputs."""
        outputs = super().get_outputs(include_bytecode)
        destination = Path(self.build_lib) / "whatsapp_api_client_python"
        return outputs + [str(destination / name) for name in DOCUMENTATION_FILES]


with open("README.md", encoding="UTF-8") as file:
    long_description = file.read()

setup(
    name="whatsapp-api-client-python",
    version="0.0.56",
    description=(
        "This library helps you easily create"
        " a Python application with WhatsApp API."
    ),
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="GREEN API",
    author_email="support@green-api.com",
    url="https://github.com/green-api/whatsapp-api-client-python",
    packages=find_packages(exclude=["tests"]),
    cmdclass={"build_py": BuildPyWithDocumentation},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Natural Language :: Russian",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Communications",
        "Topic :: Communications :: Chat",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Application Frameworks"
    ],
    license="MIT License",
    install_requires=["requests==2.34.2", "aiofiles>=24.1.0", "aiogram>=3.28.2", "aiohttp>=3.13.5"],
    extras_require={"voip": ["aiortc>=1.15,<2", "websockets>=16,<17"]},
    python_requires=">=3.10"
)
