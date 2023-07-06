import decimal
from dataclasses import dataclass

from ..mediator import mediator
from ...domain.model.product import Product
from ...infraestructure.product_repository_implement import ProductRepositoryImpl


@dataclass
class AddProductCommand:
    title: str
    description: str
    price: decimal


class AddProductCommandHandler:
    def execute(self, command: AddProductCommand) -> Product:
        return self._add_product(command)

    def _add_product(self, command: AddProductCommand) -> Product:
        return ProductRepositoryImpl().create(
            price=command.price,
            title=command.title,
            description=command.description
        )


mediator.register(AddProductCommand, AddProductCommandHandler())
