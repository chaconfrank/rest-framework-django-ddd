from ..domain.repository.abstract_repository import AbstractRepository


class AbstractRepositoryImpl(AbstractRepository):

    def __init__(self, model_class):
        self._model_class = model_class

    def get_by_id(self, id):
        model = self._get_model()
        return model.objects.get(id=id)

    def get_all(self):
        model = self._get_model()
        return model.objects.all()

    def create(self, **data):
        model = self._get_model()
        instance = model.objects.create(**data)
        return instance

    def update(self, id, data):
        model = self._get_model()
        instance = model.objects.get(id=id)
        for attr, value in data.items():
            if attr != 'id':
                setattr(instance, attr, value)
        instance.save()
        return instance

    def delete(self, id):
        model = self._get_model()
        instance = model.objects.get(id=id)
        instance.delete()

    def filter(self, **kwargs):
        model = self._get_model()
        return model.objects.filter(**kwargs)

    def _get_model(self):
        return self._model_class