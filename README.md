CSCI 5380 - Network Virtualization and Orchestration



` `Lab 9

Automate VM, VN, Docker, and BGP path




University of Colorado Boulder

Department of Computer Science

Network Engineering





Professor Levi Perigo, Ph.D.


# Summary:
In this lab, you will use what you have learned in previous labs and automate the processes into a single application.

Required technologies:

- BGP
- Hypervisor/Orchestrator (such as OpenStack)
- Containers
- SDN Controller
- Hardware server
- Service-chain
# Objectives: Virtualized Network Automation
Create an application that meets the following functionality (each objective must be a separate Python module in your code i.e. your main .py file should import the different modules you write):

1) Automate the creation of multiple virtual networks (VNs) within the hypervisor and their connection to the public network.

1) Automate the creation of multiple VMs within the hypervisor-
   1) Both single tenant (same VN) and multi-tenant (different VNs).
   1) All VMs should be accessible from the host server and be able to access the Internet.



1) Automate the security groups and port security configuration to make intra-VN and inter-VN communication possible.

1) Automate spinning up and configuring a Quagga/FRR BGP router as a Docker container.
1) Automate its BGP configuration to peer with the SDN controller in the next objective.


1) Automate spinning up and configuring an SDN controller as another Docker container.
   1) Automate its BGP speaker configuration to peer with Quagga/FRR.




# Deliverable:
Create a personal GitHub page that demonstrates the required functionality.
Lab 9: Automate VM, VN, Docker, and BGP path
