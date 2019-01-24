from setuptools import setup

REQUIREMENTS = ['pytest', 'six']

setup(
    name='pytest-parametrization',
    version='2019.1.1',
    py_modules=['parametrization'],
    provides=['parametrization'],
    description='Simpler PyTest parametrization',
    author="Singular Labs",
    author_email='contact@singular.net',
    url='https://github.com/singular/parametrization',
    keywords="pytest, parametrize, parametrization, singular",
    install_requires=REQUIREMENTS,
    license="MIT License",
    python_requires='>=2.6, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    include_package_data=True,

)
