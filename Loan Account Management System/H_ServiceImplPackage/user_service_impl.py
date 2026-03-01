from sqlalchemy.orm import Session

from C_SchemaPackage.request import UserDeleteSchema, UserUpdateSchema, UserLoginSchema, UserRegisterSchema
from F_RepositoryPackage.user_repository_logic import RepositoryUserLogic
from G_ServiceFunctionPackage.user_service_function import UserServiceFunction

class UserServiceImpl(UserServiceFunction):

    def __init__(self):
        self.user_repository = RepositoryUserLogic()

    def register_user(self, database: Session, create: UserRegisterSchema):
        return self.user_repository.register_user(database, create)

    def login_user(self, database: Session, create_token: UserLoginSchema):
        return self.user_repository.login_user(database, create_token)

    def update_user(self, database: Session, create_update: UserUpdateSchema, current_login_user: str):
        return self.user_repository.update_user(database, create_update, current_login_user)

    def delete_user(self, database: Session, create_delete: UserDeleteSchema, current_login_user: str):
        return self.user_repository.delete_user(database, create_delete, current_login_user)