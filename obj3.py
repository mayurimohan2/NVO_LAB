import openstack
import time
import paramiko
import time

# create an OpenStack connection using credentials
conn = openstack.connect(auth_url="http://172.16.204.15/identity",
                         project_name="admin",
                         username="admin",
                         password="Lab123",
                         user_domain_name="Default",
                         project_domain_name="Default")

security_group_name = 'default'
protocol = 'icmp'
remote_ip = '0.0.0.0/0'
security_groups = conn.network.security_groups()

# Print the name and ID of each security group
for sg in security_groups:
    print('Security Group Name:', sg.name)
    print(type( sg.id))
    if sg.id == '74dded3a-a79f-4dc8-a690-3541cd63dd58':
         print("lk")
         security_group = conn.network.find_security_group(sg.id)

         rule = conn.network.create_security_group_rule(
              security_group_id=security_group.id,
               direction='ingress',
               remote_ip_prefix=remote_ip,
               protocol=protocol,
             )
         rule = conn.network.create_security_group_rule(
              security_group_id=security_group.id,
               direction='egress',
               remote_ip_prefix=remote_ip,
               protocol=protocol,
             )

         print(rule)
