from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='TOPSIS-Shubham-101803589',
  version='0.0.1',
  description='Technique of Order Preference Similarity to the Ideal Solution',
  long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/BaffledCoder/TOPSIS-Shubham-101803589',  
  author='Shubham Sharma',
  author_email='ssharma5_be18@thapar.edu',
  license='MIT', 
  classifiers=classifiers,
  keywords=['topsis', 'thapar'], 
  packages=find_packages(),
  install_requires=['pandas'] 
)
