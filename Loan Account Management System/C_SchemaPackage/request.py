from pydantic import BaseModel, EmailStr
from datetime import date
from typing import Optional

# Create & Register Request:
class UserRegisterSchema(BaseModel):
    user_username: str
    user_password: str
    user_email: EmailStr

class LoanAccountCreateSchema(BaseModel):
    loan_provider: str
    loan_account_number: str
    loan_amount: str
    loan_tenure: str
    loan_roi_annual: str
    loan_emi_amount: str
    loan_emi_date: date
    loan_disburse_account: str
    loan_disburse_bank: str
    loan_disburse_bank_ifsc: str
    loan_disburse_amount: str
    loan_disburse_date: str

# Update User & Loan Account Request:
class UserUpdateSchema(BaseModel):
    user_username: Optional[str] # Need to delete it should not change
    user_password: Optional[str]
    user_email: Optional[EmailStr] # Need to delete it should not change

class LoanAccountUpdateSchema(BaseModel):
    loan_provider: Optional[str]
    loan_account_number: Optional[str] # Need to delete it should not change
    loan_amount: Optional[str]
    loan_tenure: Optional[str]
    loan_roi_annual: Optional[str]
    loan_emi_amount: Optional[str]
    loan_emi_date: Optional[date]
    loan_disburse_account: Optional[str]
    loan_disburse_bank: Optional[str]
    loan_disburse_bank_ifsc: Optional[str]
    loan_disburse_amount: Optional[str]
    loan_disburse_date: Optional[str]


# Delete User & Loan Account Request:
class UserDeleteSchema(BaseModel):
    user_username: str
    user_password: str

class LoanAccountDeleteSchema(BaseModel):
    loan_account_number: str

# Login User Account Request:
class UserLoginSchema(BaseModel):
    user_username: str
    user_password: str