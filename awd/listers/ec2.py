from awd.listers.base import BaseLister
import click
import boto3
from tabulate import tabulate


class EC2Lister(BaseLister):

    def __init__(self):
        super().__init__()

    def __list_ec2_instances(self):
        click.secho("listing ec2 instances", fg="green")
        client = boto3.client('ec2')
        response = client.describe_instances()
        response = response['Reservations']
        table = []
        sl = 0
        for key in response:
            sl = sl + 1
            Tags = key['Instances'][0]['Tags']
            for k in Tags:
                if k['Key'] == 'Name':
                    name = k['Value']
                else:
                    name = '---'
            if len(name) > 20 :
                name = name[:17]
                name = name.ljust(20,'.')

            if 'PublicIpAddress' in key['Instances'][0].keys():
                public_ip = key['Instances'][0]['PublicIpAddress']
            else:
                public_ip = '---'

            if 'KeyName' in key['Instances'][0].keys():
                key_name = key['Instances'][0]['KeyName']
            else:
                key_name = '---'
            if len(key_name) > 20 :
                key_name = key_name[:17]
                key_name = key_name.ljust(20,'.')

            table.append({

                'Sl': sl,
                'Instance Id': key['Instances'][0]['InstanceId'],
                'Private Ip': key['Instances'][0]['PrivateIpAddress'],
                'Key Name': key_name,
                'Public Ip': public_ip,
                'Name': name
            })
        print(tabulate(table, headers = "keys"))

    def execute(self):
        self.__list_ec2_instances()
