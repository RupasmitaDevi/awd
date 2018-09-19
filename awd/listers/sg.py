import boto3
import click
from tabulate import tabulate

from awd.listers.base import BaseLister


class SGLister(BaseLister):
    def __init__(self, sg=None):
        super().__init__()
        self.sg = sg

    def __list_security_groups(self):
        click.secho("listing sg", fg="green")
        client = boto3.client('ec2')
        ls = client.describe_security_groups()
        securityGroups = ls['SecurityGroups']
        sl = 0
        table = []
        for key in securityGroups:
            sl = sl + 1
            table.append({

                'Sl': sl,
                'GroupId': key['GroupId']

            })
        print(tabulate(table, headers="keys"))

    def __list_sg_rules(self):
        client = boto3.client('ec2')
        response = client.describe_security_groups(GroupIds=[self.sg])
        sgs = response['SecurityGroups']
        if len(sgs) == 0:
            click.secho("Could not find security group with name {}".format(sg), fg="red")
            sys.exit(1)
        sg_ = sgs[0]
        out_table = []
        in_table = []
        click.secho("Listing the inbound rules", fg="yellow")
        ip_permissions_egress = sg_['IpPermissionsEgress']
        if len(ip_permissions_egress) == 0:
            click.secho("No Outboud rules have been defined", fg="green")
            sys.exit(0)
        sl = 0
        for ip_perm_egress in ip_permissions_egress:

            sl = sl + 1
            for ip_rng in ip_perm_egress['IpRanges']:
                dest = ip_rng['CidrIp']

            if 'FromPort' in ip_perm_egress.keys():

                if ip_perm_egress['FromPort'] == ip_perm_egress['ToPort']:
                    port_ranges = ip_perm_egress['FromPort']
                else:
                    port_ranges = str(ip_perm_egress['FromPort']) + '-' + str(ip_perm_egress['ToPort'])
                ip_protocol = ip_perm_egress['IpProtocol']
            else:

                port_ranges = "all"
                ip_protocol = "all"

            in_table.append({
                'Sl': sl,
                'Protocol': ip_protocol,
                'Port Range': port_ranges,
                'Destination': dest
            })

        print(tabulate(in_table, headers="keys"))
        click.secho("Listing the outbound rules", fg="yellow")
        ip_permissions = sg_['IpPermissions']

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
            if 'FromPort' in ip_perm.keys():

                if ip_perm['FromPort'] == ip_perm['ToPort']:
                    port_ranges = ip_perm['FromPort']
                else:
                    port_ranges = str(ip_perm['FromPort']) + '-' + str(ip_perm['ToPort'])
                ip_protocol = ip_perm['IpProtocol']
            else:

                port_ranges = "all"
                ip_protocol = "all"

            out_table.append({
                'Sl': sl,
                'Protocol': ip_protocol,
                'Port Range': port_ranges,
                'Source': ','.join(filtered_sgs) + ','.join(ip_ranges)
            })

        print(tabulate(out_table, headers="keys"))

    def execute(self):
        if self.sg:
            self.__list_sg_rules()
        else:
            self.__list_security_groups()
