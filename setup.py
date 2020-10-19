
from setuptools import setup

def readme():
  with open('README.MD', 'r') as doc:
    return doc.read()

setup(
  name = 'IndonesianKataBakuChecker',
  packages = ['IndonesianKataBakuChecker'],
  version = '0.1',
  license='MIT',
  description = 'Indonesian kata baku checker',
  long_description_content_type = "text/markdown",
  long_description = readme(),
  author = 'Turfa Auliarachman',
  author_email = 't.auliarachman@gmail.com',
  url = 'https://github.com/turfaa/IndonesianKataBakuChecker',
  download_url = 'https://github.com/turfaa/IndonesianKataBakuChecker/archive/v_01.tar.gz',
  keywords = ['indonesia', 'word', 'bahasa', 'kata', 'baku', 'kata baku'],
  include_package_data = True,
  package_data = {'' : ['*.txt']},
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)