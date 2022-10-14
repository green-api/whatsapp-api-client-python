import setuptools

with open("README.md") as file:
    read_me_description = file.read()

setuptools.setup(
    name="whatsapp-api-client-python",
    version="0.0.21",
    install_requires=['requests'],
    author="Ivan Sadovy",
    author_email="sadiv@bk.ru",
    description="This library helps you easily create a python '\
        'application to connect the WhatsApp API using service green-api.com",
    long_description=read_me_description,
    long_description_content_type="text/markdown",
    url="https://github.com/green-api/whatsapp-api-client-python",
    packages=['whatsapp_api_client_python', 'whatsapp_api_client_python.tools'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)