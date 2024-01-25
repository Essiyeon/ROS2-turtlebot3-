from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'ros_siyeon'
share_dir = "share/" + package_name

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (share_dir + "/launch", glob(os.path.join("launch", "*.launch.py"))),
        (share_dir + "/param", glob(os.path.join("param", "*.yaml"))),
    ],    
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='siyeon',
    maintainer_email='aeiou0302@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'move_turtlesim = ros_siyeon.move_turtlesim:main',
            'move_turtlebot = ros_siyeon.move_turtlebot:main',
            "simple_pub = ros_siyeon.simple_pub:main",
            "simple_sub = ros_siyeon.simple_sub:main",
            "simple_sub2 = ros_siyeon.simple_sub2:main",
            "simple_time_pub = ros_siyeon.simple_time_pub:main",
            "simple_time_sub = ros_siyeon.simple_time_sub:main",
            "move_turtlebot_s = ros_siyeon.move_turtlebot_s:main",
            "simple_image_sub = ros_siyeon.simple_image_sub:main",
            "simple_service_server = ros_siyeon.simple_service_server:main",
            "simple_service_client = ros_siyeon.simple_service_client:main",
            "simple_action_server = ros_siyeon.simple_action_server:main",
            "simple_action_client = ros_siyeon.simple_action_client:main"
        ],
    },
)
