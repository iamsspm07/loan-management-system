from B_EntityPackage.loan_master import LoanMasterAccount
from C_SchemaPackage.request import LoanAccountCreateSchema, LoanAccountDeleteSchema, LoanAccountUpdateSchema
from D_CustomExceptionPackage.custom_exception import AlreadyExistsException, NotFoundException
from sqlalchemy.orm import Session

class LoanRepositoryLogic:

    def create_loan_account(self, database: Session, register: LoanAccountCreateSchema, current_login_user: str):
        if database.query(LoanMasterAccount).filter(LoanMasterAccount.loan_account_number == register.loan_account_number).first():
            raise AlreadyExistsException('Loan Account Number already exists')

        if database.query(LoanMasterAccount).filter(LoanMasterAccount.loan_user_username == current_login_user,
                                                        LoanMasterAccount.loan_account_number == register.loan_account_number).first():
            raise AlreadyExistsException('Loan Account Number already exists')

        create = register.model_dump(exclude_unset=True)
        create['loan_user_username'] = current_login_user

        create_loan = LoanMasterAccount(**create)
        database.add(create_loan)
        database.commit()
        database.refresh(create_loan)
        return {
            'Status': 'Success',
            'message': 'Loan Account Created',
            'data': create_loan
        }

    def fetch_loan_accounts(self, database: Session, current_login_user: str):
        data = database.query(LoanMasterAccount).filter(LoanMasterAccount.loan_user_username == current_login_user).all()
        return {
            'Status': 'Success',
            'message': 'Loan Account List',
            'data': data
        }

    def update_loan_account(self, database: Session, create_update: LoanAccountUpdateSchema, current_login_user: str):
        data = database.query(LoanMasterAccount).filter(LoanMasterAccount.loan_account_number == create_update.loan_account_number,
                                                        LoanMasterAccount.loan_user_username == current_login_user).first()
        if not data:
            raise NotFoundException('Loan Account Number not found')

        data_loan = create_update.model_dump(exclude_unset=True)
        data_loan.pop('loan_account_number', None)

        for key, value in data_loan.items():
            setattr(data, key, value)
        database.commit()
        database.refresh(data)
        return {
            'Status': 'Success',
            'message': 'Loan Account Updated',
            'data': data
        }

    def delete_loan_account(self, database: Session, create_delete: LoanAccountDeleteSchema, current_login_user: str):
        data_delete = database.query(LoanMasterAccount).filter(
            LoanMasterAccount.loan_user_username == current_login_user,
            LoanMasterAccount.loan_account_number == create_delete.loan_account_number
        ).first()
        if not data_delete:
            raise NotFoundException('Loan Account Number not found')

        database.delete(data_delete)
        database.commit()
        return {
            'Status': 'Success',
            'message': 'Loan Account Deleted',
            'data': data_delete
        }