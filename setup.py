from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='est',
      version='0.1',
      long_description=long_description,
      description='Collection of conditional density estimators',
      url='https://github.com/freelunchtheorem/conditional_density_estimators',
      author='Jonas Rothfuss, Fabio Ferreira',
      author_email='jonas.rothfuss@gmx.de, fabioferreira@mailbox.org',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'Keras',
        'numpy',
        'pandas',
        'tensorflow>=1.4,<=1.7.0',
        'matplotlib',
        'edward>=1.3.4,<=1.3.5',
        'seaborn',
        'scipy',
        'pytest',
        'scikit_learn',
        'statsmodels',
        'ml_logger<=99.99',
        'progressbar2'
      ],
      dependency_links=["https://github.com/jonasrothfuss/ml_logger/archive/2d373835ea159587fc323140ed0e8a8ea1bf9843.zip#egg=ml_logger-99.99"],
      zip_safe=False)