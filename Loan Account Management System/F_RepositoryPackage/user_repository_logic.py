from B_EntityPackage.user_entity import UserMasterTable
from C_SchemaPackage.request import UserLoginSchema, UserRegisterSchema, UserUpdateSchema, UserDeleteSchema
from E_JWTTokenSecurityPackage.jwt_security import create_access_token, password_hash, verify_password
from D_CustomExceptionPackage.custom_exception import UnauthorizedException, AlreadyExistsException, NotFoundException
from sqlalchemy.orm import Session

class RepositoryUserLogic:

    def register_user(self, database: Session, create: UserRegisterSchema):
        if database.query(UserMasterTable).filter(UserMasterTable.user_username == create.user_username).first():
            raise AlreadyExistsException('User Already Registered')

        if database.query(UserMasterTable).filter(UserMasterTable.user_email == create.user_email).first():
            raise AlreadyExistsException('User Already Registered')

        create_data = create.model_dump(exclude_unset=True)
        create_data['user_password'] = password_hash(create.user_password)

        create_user = UserMasterTable(**create_data)
        database.add(create_user)
        database.commit()
        database.refresh(create_user)
        return {
            'Status': 'Success',
            'Message': f'{create_user.user_username} Registered Successfully'
        }


    def login_user(self, database: Session, create_token: UserLoginSchema):
        data = database.query(UserMasterTable).filter(UserMasterTable.user_username == create_token.user_username).first()
        if not data:
            raise UnauthorizedException('Invalid Username')

        if not verify_password(create_token.user_password, data.user_password):
            raise UnauthorizedException('Invalid Password')

        access_token = create_access_token(token_data={
            'user_username': create_token.user_username
        })

        return {
            'Status': 'Success',
            'Message': 'Token Created & Login Successful',
            'access_token': access_token,
            'token_type': 'Bearer',
            'UserName': create_token.user_username
        }


    def update_user(self, database: Session, create_update: UserUpdateSchema, current_login_user: str):
        if create_update.user_username != current_login_user:
            raise UnauthorizedException('Invalid Username')

        update_user_details = database.query(UserMasterTable).filter(UserMasterTable.user_username == current_login_user).first()
        if not update_user_details:
            raise NotFoundException('User Not Found')

        update_details = create_update.model_dump(exclude_unset=True)
        if 'user_password' in update_details:
            update_details['user_password'] = password_hash(create_update.user_password)

        update_details.pop('user_username', None)
        update_details.pop('user_email', None)

        for key, value in update_details.items():
            setattr(update_user_details, key, value)

        database.commit()
        database.refresh(update_user_details)
        return {
            'Status': 'Success',
            'Message': 'User Updated Successfully',
            'UserName': update_user_details
        }

    def delete_user(self, database: Session, create_delete: UserDeleteSchema, current_login_user: str):
        if create_delete.user_username != current_login_user:
            raise UnauthorizedException('Invalid Username')

        data = database.query(UserMasterTable).filter(UserMasterTable.user_username == current_login_user).first()
        if not data:
            raise NotFoundException('User Not Found')

        if not verify_password(create_delete.user_password, data.user_password):
            raise UnauthorizedException('Invalid Password')

        database.delete(data)
        database.commit()
        return {
            'Status': 'Success',
            'Message': 'User Deleted Successfully',
            'UserName': create_delete.user_username
        }