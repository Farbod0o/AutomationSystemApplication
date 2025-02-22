from model.da.da import DataAccess
from model.entity.contract import Contract

contract = Contract("Recruitment", "for Recruitment in company")
contract_da = DataAccess(Contract)
contract_da.save(contract)


print(contract)
