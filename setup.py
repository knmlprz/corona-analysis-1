from setuptools import setup, find_packages

setup(
    name='Corona analysis',
    version='1.0',
    description='A module providing data to analyse coronavirus in Poland',
    license="MIT",
    author='Patryk Gronkiewicz, Piotr Krawiec',
    packages=find_packages(include=['corona_analysis', 'corona_analysis.*']),
    install_requires=['pandas', 'beautifulsoup4', 'demjson', 'statsmodels',
                      'seaborn']
)
