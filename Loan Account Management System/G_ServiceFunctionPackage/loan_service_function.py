from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from C_SchemaPackage.request import *


class LoanServiceFunction(ABC):

    @abstractmethod
    def create_loan_account(self, database: Session, register: LoanAccountCreateSchema, current_login_user: str): pass

    @abstractmethod
    def fetch_loan_accounts(self, database: Session, current_login_user: str): pass

    @abstractmethod
    def update_loan_account(self, database: Session, create_update: LoanAccountUpdateSchema, current_login_user: str): pass

    @abstractmethod
    def delete_loan_account(self, database: Session, create_delete: LoanAccountDeleteSchema, current_login_user: str): pass