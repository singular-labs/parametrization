from setuptools import setup

REQUIREMENTS = ['pytest', 'six']

setup(
    name='pytest-parametrization',
    version='2019.1.3',
    py_modules=['parametrization'],
    provides=['parametrization'],
    description='Simpler PyTest parametrization',
    author="Singular Labs",
    author_email='contact@singular.net',
    url='https://github.com/singular-labs/parametrization',
    keywords="pytest, parametrize, parametrization, singular",
    install_requires=REQUIREMENTS,
    license="MIT License",
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    include_package_data=True,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
  ],
)
