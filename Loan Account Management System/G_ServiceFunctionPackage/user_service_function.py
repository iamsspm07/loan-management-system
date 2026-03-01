from abc import ABC, abstractmethod
from sqlalchemy.orm import Session

from C_SchemaPackage.request import *


class UserServiceFunction(ABC):

    @abstractmethod
    def register_user(self, database: Session, create: UserRegisterSchema): pass

    @abstractmethod
    def login_user(self, database: Session, create_token: UserLoginSchema): pass

    @abstractmethod
    def update_user(self, database: Session, create_update: UserUpdateSchema, current_login_user: str): pass

    @abstractmethod
    def delete_user(self, database: Session, create_delete: UserDeleteSchema, current_login_user: str): pass