from dataclasses import dataclass

from ddd.product.domain.model.product import Product
from ddd.product.infraestructure.product_repository_implement import ProductRepositoryImpl


@dataclass
class GetProductCommand:
    id: int


class GetProductCommandHandler:

    def execute(self, command: GetProductCommand) -> Product:
        product: Product = ProductRepositoryImpl().get_by_id(command.id)
        return product
