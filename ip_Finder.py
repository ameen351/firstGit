import csv
import ipaddress

def is_ip_in_subnet(ip, subnet):
    return ipaddress.ip_address(ip) in ipaddress.ip_network(subnet)

def find_matching_subnet(ip_list, subnet_list):
    matching_subnets = []
    for ip in ip_list:
        for subnet in subnet_list:
            if is_ip_in_subnet(ip, subnet):
                matching_subnets.append((ip, subnet))
                break
    return matching_subnets

def read_csv(file_path):
    data = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row[0])  # Assuming IP addresses/subnets are in the first column
    return data

# Example usage:
subnet_file_path = 'subnet_info.csv'
ip_file_path = 'ip_info.csv'

subnet_list = read_csv(subnet_file_path)
ip_list = read_csv(ip_file_path)

matching_subnets = find_matching_subnet(ip_list, subnet_list)
for ip, subnet in matching_subnets:
    print(f"The IP address {ip} is part of the subnet {subnet}.")