from model.da.da import DataAccess
from model.entity.insurance import Insurance

insurance = Insurance("alborz", "insurance for employee", "Supplementary", 1234, 2026)

insurance_da = DataAccess(Insurance)
insurance_da.save(insurance)

print(insurance)
