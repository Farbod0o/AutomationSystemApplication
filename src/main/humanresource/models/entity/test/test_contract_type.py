from model.da.da import DataAccess
from model.entity.contract_type import ContractType

contract_type = ContractType("Recruitment", "for person","done")

contract_type_da = DataAccess(ContractType)
contract_type_da.save(contract_type)

print(contract_type)
