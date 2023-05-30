from abc import ABC

from .abstract_repository_implement import AbstractRepositoryImpl
from ..domain.model.product import Product
from ..domain.repository.abstract_repository import AbstractRepository


class ProductRepository(AbstractRepository, ABC):
    pass


class ProductRepositoryImpl(ProductRepository, AbstractRepositoryImpl):
    def __init__(self):
        super().__init__(Product)

