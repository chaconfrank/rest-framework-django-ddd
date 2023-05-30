from ..commands.add_product_command_handler import AddProductCommand
from ..mediator import mediator


class ProductServices:

    def execute(self, data):

        add_command = AddProductCommand(title=data['title'],
                                        description=data['description'],
                                        price=data['price'])

        product = mediator.execute(add_command)

        return product
