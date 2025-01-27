from model.da.da import DataAccess
from model.entity.loan import Loan

loan = Loan("2020-01-01", 200, 4, 50, "01-05-2020", "done")

loan_da = DataAccess(Loan)
loan_da.save(loan)

print(loan)




