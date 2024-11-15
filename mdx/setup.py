from setuptools import setup, find_packages

setup(
    name                    = "mdx",
    version                 = "0.1.0",

    packages                = find_packages(),    
    package_data            = { "mdx": ["*.json"] },
    exclude_package_data    = { },

    author                  = "Matthias Hölzer-Klüpfel",
    author_email            = "matthias@hoelzer-kluepfel.de",
    description             = "Markdown externions",
    url                     = "http://www.hoelzer-kluepfel.de",
    keywords                = "documentation processing",

    license                 = "Other/Proprietary License",

    # install_requires=["docutils>=0.3"],

    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
)