from setuptools import setup

setup(
    name='mavericks-tag',
    version='1.0a1',
    packages=[''],
    url='http://schwa.io',
    license='BSD 2-clause',
    author='Jonathan Wight',
    author_email='jwight@mac.com',
    description='Tool for interacting with OS X 10.9 tags',
	install_requires = [
		'docopt',
        'biplist',
        'xattr',
		],
	py_modules=['tag'],
	scripts=['tag'],
    )
