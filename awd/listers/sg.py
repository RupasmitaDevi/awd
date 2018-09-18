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
        click.secho("implementation pending", fg="yellow")

    def execute(self):
        if self.sg:
            self.__list_sg_rules()
        else:
            self.__list_security_groups()
