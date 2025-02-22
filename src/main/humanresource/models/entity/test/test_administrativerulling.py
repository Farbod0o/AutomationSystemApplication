from model.da.da import DataAccess
from model.entity.administrativerulings import AdministrativeRulings

# unit test
administrativerulings = AdministrativeRulings("Employment", "for Employment person in company", "reward", 986.64)
administrativerulings_da = DataAccess(AdministrativeRulings)
administrativerulings_da.save(administrativerulings)

print(administrativerulings)




