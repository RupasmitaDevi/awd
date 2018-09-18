from awd.listers.base import BaseLister


class EC2Lister(BaseLister):

    def __init__(self, sg=None):
        super().__init__()
        self.sg = sg


    def __list_ec2_instance(self):
        pass


    def execute(self):
        pass
