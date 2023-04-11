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

# create a new network
network = conn.network.create_network(name='my_network',shared='True',)

# create a subnet for the network
subnet = conn.network.create_subnet(name='my_subnet',
                                    network_id=network.id,
                                    ip_version=4,
                                    gateway_ip='192.168.50.1',
                                    cidr='192.168.50.0/24')

print(subnet)

router = conn.network.create_router(name='my_router')

# add the subnet to the router
#conn.network.add_interface_to_router(router.id, subnet_id=subnet.id)

ext_net_id = conn.network.find_network('public').id
m = conn.network.update_router(router.id, external_gateway_info={'network_id': ext_net_id})

router = conn.network.find_router('my_router')
subnet = conn.network.find_subnet('my_subnet')
subnet1 = conn.network.find_subnet('shared-subnet')

# add the subnet interface to the router
j= conn.network.add_interface_to_router(router.id, subnet_id=subnet.id)
k= conn.network.add_interface_to_router(router.id, subnet_id=subnet1.id)

print(k)

#create instance in openstack for network my_network """


for i in range(1,4):
   server_name = f'VM{i}'
   print(server_name)
   if server_name == 'VM1':
      image_name = 'mininet_img'
      flavor_name = 'm1.large'
      network_name = 'DHCP'
      keypair_name = f'VM_{i}'
      network2_name = 'public'
   

      image = conn.compute.find_image(image_name)
      flavor = conn.compute.find_flavor(flavor_name)
      network = conn.network.find_network(network_name)
      keypair = conn.compute.find_keypair(keypair_name)
   
   
    
      server = conn.compute.create_server(name=server_name,
                                    image_id=image.id,
                                    flavor_id=flavor.id,
                                    networks=[{'uuid': network.id}],
                                    key_name=keypair.name)

       # wait for the server to be active
      conn.compute.wait_for_server(server)

      time.sleep(15)
      print('Instance created successfully.')
      server = conn.compute.find_server(server_name)
      network = conn.network.find_network(network2_name)
      #print(network)

      # create a new floating IP address
      floating_ip = conn.network.create_ip(floating_network_id=network.id)
      print(floating_ip.floating_ip_address)
      print(server.id)

      # associate the floating IP address with the instance
      m= conn.compute.add_floating_ip_to_server(server.id, floating_ip.floating_ip_address)
      print(m)
   if server_name == 'VM2':
      image_name = 'mininet_img'
      flavor_name = 'm1.large'
      network_name = 'my_network'
      keypair_name = f'VM_{i}'
      network2_name = 'public'
   

      image = conn.compute.find_image(image_name)
      flavor = conn.compute.find_flavor(flavor_name)
      network = conn.network.find_network(network_name)
      keypair = conn.compute.find_keypair(keypair_name)
   
   
    
      server = conn.compute.create_server(name=server_name,
                                    image_id=image.id,
                                    flavor_id=flavor.id,
                                    networks=[{'uuid': network.id}],
                                    key_name=keypair.name)

       # wait for the server to be active
      conn.compute.wait_for_server(server)

      time.sleep(15)
      print('Instance created successfully.')
      server = conn.compute.find_server(server_name)
      network = conn.network.find_network(network2_name)
      #print(network)

      # create a new floating IP address
      floating_ip = conn.network.create_ip(floating_network_id=network.id)
      print(floating_ip.floating_ip_address)
      print(server.id)

      # associate the floating IP address with the instance
      m= conn.compute.add_floating_ip_to_server(server.id, floating_ip.floating_ip_address)
      print(m)
      
   if server_name == 'VM3':  
      image_name = 'cirros-0.5.2-x86_64-disk'
      flavor_name = 'm1.nano'
      network_name = 'my_network'
      keypair_name = f'VM_{i}'
      network2_name = 'public'
   

      image = conn.compute.find_image(image_name)
      flavor = conn.compute.find_flavor(flavor_name)
      network = conn.network.find_network(network_name)
      keypair = conn.compute.find_keypair(keypair_name)
   
   
    
      server = conn.compute.create_server(name=server_name,
                                    image_id=image.id,
                                    flavor_id=flavor.id,
                                    networks=[{'uuid': network.id}],
                                    key_name=keypair.name)

       # wait for the server to be active
      conn.compute.wait_for_server(server)

      time.sleep(10)
      print('Instance created successfully.') 
      
      server = conn.compute.find_server(server_name)
      network = conn.network.find_network(network_name)

# create a new floating IP address
      floating_ip = conn.network.create_ip(floating_network_id=network.id)

# associate the floating IP address with the instance
      conn.compute.add_floating_ip_to_server(server, floating_ip.floating_ip_address) 
      
 
 
#OBJ2 :CHeck internet connection and inetr VM ping 
server_ip = '172.24.4.194'
username = 'mininet'
password = 'mininet'

# create an SSH client object
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# wait for the server to boot
time.sleep(30)
print("jk")

# connect to the server
j=ssh.connect(server_ip, username=username, password=password)
print(j)


# execute a command on the server
#stdin, stdout, stderr = ssh.exec_command('ls')
ping_command = 'ping -c 5 8.8.8.8'  # ping Google DNS 5 times
stdin, stdout, stderr = ssh.exec_command(ping_command)
output = stdout.read()
print(output)
ping_command = 'ping -c 5 192.168.100.121' 
stdin, stdout, stderr = ssh.exec_command(ping_command)
output = stdout.read()
print(output)


# close the SSH connection
ssh.close()

