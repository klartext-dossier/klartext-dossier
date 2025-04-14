from setuptools import setup, find_packages

setup(
    name                    = "dossier-mdx",
    version                 = "0.1.0",

    packages                = find_packages(),    
    package_data            = { "mdx": ["*.json"] },
    exclude_package_data    = { },

    author                  = "Matthias Hölzer-Klüpfel",
    author_email            = "matthias@hoelzer-kluepfel.de",
    description             = "Markdown externions",
    url                     = "https://klartext-dossier.github.io/klartext-dossier",
    keywords                = "documentation processing",

    classifiers             = [ 
                            	"License :: OSI Approved :: BSD License",
                                "Development Status :: 3 - Alpha",
                                "Environment :: Console",
                                "Intended Audience :: Developers",
                                "Programming Language :: Python :: 3",
                                "Topic :: Documentation",
                                "Topic :: Software Development :: Documentation",
                                "Topic :: Text Processing :: Markup :: Markdown",
                                "Typing :: Typed",
                              ],

    # install_requires=["docutils>=0.3"],

    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
)