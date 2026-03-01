from C_SchemaPackage.request import LoanAccountDeleteSchema, LoanAccountUpdateSchema, LoanAccountCreateSchema
from F_RepositoryPackage.loan_repository_logic import LoanRepositoryLogic
from G_ServiceFunctionPackage.loan_service_function import LoanServiceFunction
from sqlalchemy.orm import Session

class LoanServiceImpl(LoanServiceFunction):

    def __init__(self):
        self.loan_repository = LoanRepositoryLogic()

    def create_loan_account(self, database: Session, register: LoanAccountCreateSchema, current_login_user: str):
        return self.loan_repository.create_loan_account(database, register, current_login_user)

    def fetch_loan_accounts(self, database: Session, current_login_user: str):
        return self.loan_repository.fetch_loan_accounts(database, current_login_user)

    def update_loan_account(self, database: Session, create_update: LoanAccountUpdateSchema, current_login_user: str):
        return self.loan_repository.update_loan_account(database, create_update, current_login_user)

    def delete_loan_account(self, database: Session, create_delete: LoanAccountDeleteSchema, current_login_user: str):
        return self.loan_repository.delete_loan_account(database, create_delete, current_login_user)