from setuptools import setup

setup(
    name='pi_fan_ctrl',
    version='0.0.1',
    description='Fan control for the Raspberry Pi',
    long_description='Fan control for the Raspberry Pi',
    author='Jeremie Deray',
    author_email='jeremie.deray@canonical.com',
    url='https://github.com/artivis/pi_fan_ctrl',
    install_requires=['RPi.GPIO', 'pyyaml'],
    include_package_data=True,
    zip_safe=True,
    license='Creative Commons Attribution Share Alike 4.0',
    keywords='RaspberryPi, fan, control',
    scripts=['scripts/pi_fan_ctrl']
)
