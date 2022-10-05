import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="whatsapp-api-client-python-sadiv",
    version="0.0.1-alpha",
    author="Ivan Sadovy",
    author_email="sadiv@bk.ru",
    description="This library helps you easily create a python '\
        'application to connect the WhatsApp API using service green-api.com",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/green-api/whatsapp-api-client-python",
    packages=['src'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)