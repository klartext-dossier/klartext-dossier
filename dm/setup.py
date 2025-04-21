from setuptools import setup, find_packages

setup(
    name                    = "dm",
    version                 = "0.1.0",

    packages                = find_packages(),    
    package_data            = { "dm": [ "Tools/*/*" ] },
    exclude_package_data    = { "dm": [ "Tools/css/*.less", "Tools/docx/*.dotm" ] },

    author                  = "Matthias Hölzer-Klüpfel",
    author_email            = "matthias@hoelzer-kluepfel.de",
    description             = "The dossier management system",
    url                     = "https://www.klartext-dossier.org/klartext-dossier",
    keywords                = "dossier documentation processing",

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


    entry_points            = {
                                'console_scripts': [ 'dm = dm:run_dm', ]
                              }

    # install_requires=["docutils>=0.3"],

    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
)