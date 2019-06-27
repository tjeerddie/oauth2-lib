from setuptools import setup

setup(
    name="oauth2-lib",
    version="0.1",
    packages=["oauth2_lib"],
    url="https://gitlab.surfnet.nl/automation/oauth2-lib",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.x",
    ],
    license="MIT",
    author="Automation",
    author_email="automation-nw@surfnet.nl",
    description="OAUTH2 lib specific for SURFnet",
    install_requires=["flask==1.0.3", "requests==2.22.0"],
    tests_require=[
        "pytest",
        "flake8",
        "black",
        "isort",
        "flake8-bandit",
        "flake8-bugbear",
        "flake8-comprehensions",
        "flake8-docstrings",
        "flake8-logging-format",
        "flake8-pep3101",
        "flake8-print",
        "mypy",
        "mypy_extensions",
        "requests_mock",
        "flask_testing",
    ],
)
