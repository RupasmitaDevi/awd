import click

from awd.listers.base import BaseLister
from awd.listers.controller import get_lister


@click.group(name="list")
def lister():
    pass


@click.command(name="sg")
@click.option('-s', help="security group id")
def list_sg(s):
    listr: BaseLister = get_lister('sg')(s)
    listr.execute()


@click.command(name="ec2")
@click.option('-ec2', help="ec2 instance id")
def list_ec2(s):
    pass



lister.add_command(list_sg)
lister.add_command(list_ec2)

