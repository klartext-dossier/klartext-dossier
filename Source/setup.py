from setuptools import setup, find_packages

setup(
    name                    = "dossier",
    version                 = "0.1.0",

    packages                = find_packages(),    
    package_data            = { "dm": [ "Tools/*/*" ] },
    exclude_package_data    = { "dm": [ "Tools/css/*.less", "Tools/docx/*.dotm" ] },

    author                  = "Matthias Hölzer-Klüpfel",
    author_email            = "matthias@hoelzer-kluepfel.de",
    description             = "The dossier document processing system",
    url                     = "http://www.hoelzer-kluepfel.de",
    keywords                = "dossier documentation processing",

    license                 = "Other/Proprietary License",
    
    scripts                 = ["bin/dm"],

    # install_requires=["docutils>=0.3"],

    # project_urls={
    #     "Bug Tracker": "https://bugs.example.com/HelloWorld/",
    #     "Documentation": "https://docs.example.com/HelloWorld/",
    #     "Source Code": "https://code.example.com/HelloWorld/",
    # },
)