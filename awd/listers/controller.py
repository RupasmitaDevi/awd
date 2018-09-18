from awd.listers.ec2 import EC2Lister
from awd.listers.sg import SGLister

listers = {
    "sg": SGLister,
    "ec2": EC2Lister
}


def get_lister(typ):
    return listers[typ]