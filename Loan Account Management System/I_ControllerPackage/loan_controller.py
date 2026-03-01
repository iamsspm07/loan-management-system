from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from A_DatabasePackage.secure_database_connection import loan_jwt_database_connection
from C_SchemaPackage.request import *
from E_JWTTokenSecurityPackage.jwt_security import get_current_user
from H_ServiceImplPackage.loan_service_impl import LoanServiceImpl

router = APIRouter(prefix="/loan", tags=["loan"])
serviceLoan = LoanServiceImpl()

@router.post("/create")
def create_loan_account(register: LoanAccountCreateSchema, current_login_user: str = Depends(get_current_user),
                        database: Session = Depends(loan_jwt_database_connection)):
    return serviceLoan.create_loan_account(database, register, current_login_user)

@router.get("/get")
def fetch_loan_accounts(current_login_user: str = Depends(get_current_user),
                        database: Session = Depends(loan_jwt_database_connection)):
    return serviceLoan.fetch_loan_accounts(database, current_login_user)

@router.put("/update")
def update_loan_account(create_update: LoanAccountUpdateSchema, current_login_user: str = Depends(get_current_user),
                        database: Session = Depends(loan_jwt_database_connection)):
    return serviceLoan.update_loan_account(database, create_update, current_login_user)

@router.delete("/delete")
def delete_loan_account(create_delete: LoanAccountDeleteSchema, current_login_user: str = Depends(get_current_user),
                        database: Session = Depends(loan_jwt_database_connection)):
    return serviceLoan.delete_loan_account(database, create_delete, current_login_user)