from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from A_DatabasePackage.secure_database_connection import loan_jwt_database_connection
from C_SchemaPackage.request import *
from E_JWTTokenSecurityPackage.jwt_security import get_current_user
from H_ServiceImplPackage.user_service_impl import UserServiceImpl

router = APIRouter(prefix="/auth", tags=["User"])
serviceUser = UserServiceImpl()

@router.post('/register')
def register_user(create: UserRegisterSchema, database: Session = Depends(loan_jwt_database_connection)):
    return serviceUser.register_user(database, create)

@router.post('/login')
def login_user(create_token: UserLoginSchema, database: Session = Depends(loan_jwt_database_connection)):
    return serviceUser.login_user(database, create_token)

@router.put('/update')
def update_user(create_update: UserUpdateSchema, current_login_user: str = Depends(get_current_user),
                database: Session = Depends(loan_jwt_database_connection)):
    return serviceUser.update_user(database, create_update, current_login_user)

@router.delete('/delete')
def delete_user(create_delete: UserDeleteSchema, current_login_user: str = Depends(get_current_user),
                database: Session = Depends(loan_jwt_database_connection)):
    return serviceUser.delete_user(database, create_delete, current_login_user)