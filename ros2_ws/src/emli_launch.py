from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
	return LaunchDescription([
		Node(
			package='emli_package',
			executable='emli_pub_node',
			namespace='group1',
			name='emli_pub_node1'
		),
		Node(
			package='emli_package',
			executable='emli_sub_node',
			namespace='group1',
			name='emli_sub_node1'
		),

		Node(
			package='emli_package',
			executable='emli_pub_node',
			namespace='group2',
			name='emli_pub_node2'
		),
		Node(
			package='emli_package',
			executable='emli_sub_node',
			namespace='group2',
			name='emli_sub_node2'
		)
	])
