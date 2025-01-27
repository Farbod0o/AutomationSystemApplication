from model.da.da import DataAccess
from model.entity.employment import Employment

employment = Employment("2020-01-01", "start activity in company")

employment_da = DataAccess(Employment)
employment_da.save(employment)

print(employment)
