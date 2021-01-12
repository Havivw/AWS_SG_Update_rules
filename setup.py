from setuptools import setup, find_packages 
  
with open('requirements.txt') as f: 
    requirements = f.readlines() 
  
long_description = "IP setter for amazon - for OTORIO's PT team"
  
setup( 
        name ='ipsetter',
        version ='1.0.0', 
        description ='IP setter',
        long_description = long_description, 
        long_description_content_type ="text/markdown",
        packages = find_packages(),
        entry_points ={
            'console_scripts': [ 
                'ipsetter = ipsetter.ipsetter:main'
            ] 
        }, 
        classifiers =( 
            "Programming Language :: Python :: 3",
            "Operating System :: OS Independent",
        ), 
        install_requires = requirements, 
        zip_safe = False
)
