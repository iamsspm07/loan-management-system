from A_DatabasePackage.secure_database_connection import BASE
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.sql import func

class LoanMasterAccount(BASE):
    __tablename__ = 'loan_account'

    loan_id = Column(Integer, primary_key=True, index=True) # Need to Delete from Schema
    loan_user_username = Column(ForeignKey('user_account.user_username', ondelete='CASCADE'), nullable=False) # Need to Delete from Schema
    loan_provider = Column(String, nullable=False)
    loan_account_number = Column(String, nullable=False, unique=True)
    loan_amount = Column(String, nullable=False)
    loan_taken_date = Column(Date, nullable=False, server_default=func.current_date()) # Need to Delete from Schema
    loan_tenure = Column(String, nullable=False)
    loan_roi_annual = Column(String, nullable=False)
    loan_emi_amount = Column(String, nullable=False)
    loan_emi_date = Column(Date, nullable=False)
    loan_disburse_account = Column(String, nullable=False)
    loan_disburse_bank = Column(String, nullable=False)
    loan_disburse_bank_ifsc = Column(String, nullable=False)
    loan_disburse_amount = Column(String, nullable=False)
    loan_disburse_date = Column(String, nullable=False)
    loan_status = Column(String, nullable=False, default='Active') # Need to Delete from Schema