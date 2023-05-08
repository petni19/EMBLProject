from setuptools import setup

package_name = 'emli_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='pi',
    maintainer_email='pi@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
	'console_scripts': [
            'emli_node = emli_package.emli_node:main',
            'plant_water_alarm_pub_node = emli_package.plant_water_alarm_pub_node:main',
            'pump_water_alarm_pub_node = emli_package.pump_water_alarm_pub_node:main',
            'soil_moisture_pub_node = emli_package.soil_moisture_pub_node:main',
            'ambient_light_pub_node = emli_package.ambient_light_pub_node:main',
		    'emli_pub_node = emli_package.emli_pub_node:main',
			'emli_sub_node = emli_package.emli_sub_node:main',
        ],
    },
)
