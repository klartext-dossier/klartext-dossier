from setuptools import setup, find_packages

setup(
    name                    = "klartext",
    version                 = "0.1.0",

    packages                = find_packages(),    
    package_data            = { "klartext": ["py.typed"] },
    exclude_package_data    = { },

    author                  = "Matthias Hölzer-Klüpfel",
    author_email            = "matthias@hoelzer-kluepfel.de",
    description             = "The klartext parser",
    url                     = "https://www.klartext-dossier.org/klartext-dossier",
    keywords                = "documentation processing",

    license                 = "BSD-3-Clause",
    license_files           = [ "../LICENSE.md" ],

    classifiers             = [                             	
                                "Development Status :: 3 - Alpha",
                                "Environment :: Console",
                                "Intended Audience :: Developers",
                                "Programming Language :: Python :: 3",
                                "Topic :: Documentation",
                                "Topic :: Software Development :: Documentation",
                                "Topic :: Text Processing :: Markup",
                                "Typing :: Typed",
                              ],

    # install_requires=["docutils>=0.3"],

    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
)