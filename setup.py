from setuptools import setup

setup(
    name='half-moon-tagging',
    version='1.0a1',
    packages=[''],
    url='http://schwa.io',
    license='BSD 2-clause',
    author='Jonathan Wight',
    author_email='jwight@mac.com',
    description='Mavericks command line tool for tagging files',
	install_requires = [
		'docopt',
        'biplist',
        'xattr',
		],
	py_modules=['tag'],
	scripts=['tag'],
    )
