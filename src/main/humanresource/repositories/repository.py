from src.main.database.da import DataAccess


class Repository:
    @staticmethod
    def save(obj, entity):
        entity_da = DataAccess(entity)
        entity_da.save(obj)
        return obj

    @staticmethod
    def find_by_id(entity, id):
        entity_da = DataAccess(entity)
        return entity_da.find_by_id(id)

    @staticmethod
    def find_all(entity):
        entity_da = DataAccess(entity)
        return entity_da.find_all()

    @staticmethod
    def delete(entity, id):
        entity_da = DataAccess(entity)
        entity_da.remove(id)
