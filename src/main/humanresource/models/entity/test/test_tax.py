from model.da.da import DataAccess
from model.entity.tax import Tax

tax = Tax("Tax on salary", "for employees")

tax_da = DataAccess(Tax)
tax_da.save(tax)
print(tax)
