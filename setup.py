from setuptools import setup, find_packages

with open("README", 'r') as f:
    long_description = f.read()

setup(
    name='Corona analysis',
    version='1.0',
    description='A module providing data to analyse coronavirus in Poland',
    license="MIT",
    long_description=long_description,
    author='Patryk Gronkiewicz, Piotr Krawiec',
    packages=find_packages(include=['corona_analysis', 'corona_analysis.*']),
    install_requires=['pandas', 'beautifulsoup4', 'demjson', 'statsmodels',
                      'seaborn']
)
