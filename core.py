import sys
import click
import boto3
from tabulate import tabulate


@click.group()
def main():
	pass 

@click.command(name="list-sg")
def listsg():
	"""
	Lists all the security groups in your configured aws account.
	"""
	click.secho("listing sg", fg="green")
	client = boto3.client('ec2',region_name='eu-west-1')
	ls = client.describe_security_groups()
	securityGroups = ls['SecurityGroups']
	sl = 0
	table = []
	for key in securityGroups:
		sl = sl + 1
		table.append({

			'Sl' : sl,
			'GroupId' : key['GroupId']

			})
	print(tabulate(table, headers="keys"))


@click.command(name="list-traffic")
@click.argument('sg')
@click.option('-t', type=click.Choice(['i', 'o']), help="traffic-type.")
def list_traffic_rules(sg, t='i'):
	"""
	Lists all the inbound and outbound rules in mentioned security-groups.
	"""
	client = boto3.client('ec2', region_name="eu-west-1")

	response = client.describe_security_groups(GroupIds=[sg])

	sgs = response['SecurityGroups']

	if len(sgs) == 0:
		click.secho("Could not find security group with name {}".format(sg), fg="red")
		sys.exit(1)

	sg_ = sgs[0]
	table = []

	if t == 'o':

		ip_permissions_egress = sg_['IpPermissionsEgress']

		#print(ip_permissions_egress)

		if len(ip_permissions_egress) == 0:
			click.secho("No Outboud rules have been defined", fg="green")
			sys.exit(0)

		sl = 0

		for ip_perm_egress in ip_permissions_egress:

			sl = sl + 1
			dest = ""
			for ip_rng in ip_perm_egress['IpRanges']:
				dest = ip_rng['CidrIp']

			port_ranges = ""
			from_port = ""
			ip_protocol = ""

			if 'FromPort' in ip_perm_egress.keys():

				if ip_perm_egress['FromPort'] == ip_perm_egress['ToPort']:
					port_ranges = ip_perm_egress['FromPort']
				else:
					port_ranges = str(ip_perm_egress['FromPort'])+'-'+str(ip_perm_egress['ToPort'])
				ip_protocol = ip_perm_egress['IpProtocol']
			else:

				port_ranges = "all"
				ip_protocol = "all"


			table.append({
				'Sl' : sl,
				'Protocol': ip_protocol,
				'Port Range': port_ranges,
				'Destination': dest
			})


	else:
		ip_permissions = sg_['IpPermissions']

		#print(ip_permissions)

		if len(ip_permissions) == 0:
			click.secho("No Inboud rules have been defined", fg="green")
			sys.exit(0)

		sl = 0

		for ip_perm in ip_permissions:

			sl = sl + 1
			filtered_sgs = [] 
			for ip_grp in ip_perm['UserIdGroupPairs']:
				filtered_sgs.append(ip_grp['GroupId'])

			ip_ranges = []
			for ip_rng in ip_perm['IpRanges']:
				ip_ranges.append(ip_rng['CidrIp'])


			port_ranges = ""
			from_port = ""
			ip_protocol = ""

			if 'FromPort' in ip_perm.keys():

				if ip_perm['FromPort'] == ip_perm['ToPort']:
					port_ranges = ip_perm['FromPort']
				else:
					port_ranges = str(ip_perm['FromPort'])+'-'+str(ip_perm['ToPort'])
				ip_protocol = ip_perm['IpProtocol']
			else:

				port_ranges = "all"
				ip_protocol = "all"


			table.append({
				'Sl' : sl,
				'Protocol': ip_protocol,
				'Port Range': port_ranges,
				'Source': ','.join(filtered_sgs)+ ','.join(ip_ranges)
			})

	print(tabulate(table, headers="keys"))


main.add_command(listsg)
main.add_command(list_traffic_rules)