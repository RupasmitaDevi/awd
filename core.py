import sys
import click
import boto3
from tabulate import tabulate

from awd.listers.cmd import lister


@click.group()
def main():
    pass


main.add_command(lister)
