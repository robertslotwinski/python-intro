from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 4 - Beta',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 11',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
]


setup(
    name="r_lib",
    version="0.1",
    packages=find_packages(),
    install_requires=[],
    author="Robert Słotwiński",
    author_email="szx87407@student.szczecin.merito.pl",
    description="Python library for various utilities",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="",
    url="",
    classifiers=classifiers,
    python_requires=">=3.6",
)