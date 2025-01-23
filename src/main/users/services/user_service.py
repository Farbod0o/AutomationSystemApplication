from src.main.database.da import DataAccess


class UserService:
    @staticmethod
    def save(obj, entity):
        entity_da = DataAccess(entity)
        entity_da.save(obj)
        return obj

    @staticmethod
    def find_by_id(entity, id):
        entity_da = DataAccess(entity)
        return entity_da.find_by_id(id)
