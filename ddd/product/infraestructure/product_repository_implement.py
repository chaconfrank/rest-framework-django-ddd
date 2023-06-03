from .abstract_repository_implement import AbstractRepositoryImpl
from ..domain.model.product import Product
from ..domain.repository.product_repository import ProductRepository


class ProductRepositoryImpl(ProductRepository, AbstractRepositoryImpl):
    def __init__(self):
        super().__init__(Product)

