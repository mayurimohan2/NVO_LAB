CSCI 5380 - Network Virtualization and Orchestration



 Lab 9
Automate VM, VN, Docker, and BGP path




University of Colorado Boulder
Department of Computer Science
Network Engineering





Professor Levi Perigo, Ph.D.

 
Summary:
In this lab, you will use what you have learned in previous labs and automate the processes into a single application.
Required technologies:
•	BGP
•	Hypervisor/Orchestrator (such as OpenStack)
•	Containers
•	SDN Controller
•	Hardware server
•	Service-chain
Objectives: Virtualized Network Automation
Create an application that meets the following functionality (each objective must be a separate Python module in your code i.e. your main .py file should import the different modules you write):
1)	Automate the creation of multiple virtual networks (VNs) within the hypervisor and their connection to the public network.

I created 2 networks DHCP and my_network. I added interfaces of the virtual router to all these networks so the VMs could reach internet
 <img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231091975-d0917ef8-7359-4833-adcb-76f94746b749.png">
<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231093252-0bf4d9c3-ac01-47ad-88a6-6ca6113b8f9f.png">

2)	Automate the creation of multiple VMs within the hypervisor-
a)	Both single tenant (same VN) and multi-tenant (different VNs).
b)	All VMs should be accessible from the host server and be able to access the Internet.

I created 2 VM in network my_network and 1 VM in DHCP network. Using the virtual router these VMs are aboe to ping each other and the internet 
<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231093870-437d2850-8937-4920-9d8c-339645fe946b.png">
<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231093918-df8003fc-bf71-4d51-abc0-b77a22fa8446.png">
<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231093961-f137e7db-b3eb-4fa9-9fc9-8e930fc0b8e1.png">

 
 
3)	Automate the security groups and port security configuration to make intra-VN and inter-VN communication possible.
In this section I added ICMP for both the ingress and egress port to enable the connectivity 
<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231094251-2299fa59-f586-4871-895d-893eeb0548fd.png">

 
4)	Automate spinning up and configuring a Quagga/FRR BGP router as a Docker container.
a)	Automate its BGP configuration to peer with the SDN controller in the next objective.

For this I created a Dockerfile to create image of ExaBGP and RYU controller using pyhton code. Then i used this image to create containers for the same using script. 

<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231094748-cf7ceb22-e4c4-4b8e-98ce-adca2dcbe89d.png">
<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231094831-ae6d1bbf-2a94-4b83-8763-220fe72f1983.png">

For the BGP neighborship I created bgp.conf file for the containers and was able to establish the neighborship.
	 
5)	Automate spinning up and configuring an SDN controller as another Docker container.
a)	Automate its BGP speaker configuration to peer with Quagga/FRR.
 
 For this I created a Dockerfile to create image of ExaBGP and RYU controller using pyhton code. Then i used this image to create containers for the same using automation. 

<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231094748-cf7ceb22-e4c4-4b8e-98ce-adca2dcbe89d.png">
<img width="468" alt="image" src="https://user-images.githubusercontent.com/98084044/231094831-ae6d1bbf-2a94-4b83-8763-220fe72f1983.png">

For the BGP neighborship I created bgp.conf file for the containers and was able to establish the neighborship.


Deliverable:
Create a personal GitHub page that demonstrates the required functionality.
![image](https://user-images.githubusercontent.com/98084044/231091806-ae78a0b6-334c-4693-8a55-3b1cf43924b8.png)
