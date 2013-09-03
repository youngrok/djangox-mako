from setuptools import setup
setup(name='djangox-mako',
      description='Mako template adapter for django.',
      author='Youngrok Pak',
      author_email='pak.youngrok@gmail.com',
      keywords= 'mako django djangox',
      url='https://github.com/youngrok/djangox-mako',
      version='1.0.4',
      namespace_packages = ['djangox'],
      packages=['djangox',
                'djangox.mako', 
                ],
      classifiers = [
                     'Development Status :: 3 - Alpha',
                     'Topic :: Software Development :: Libraries',
                     'License :: OSI Approved :: BSD License']
      )
