from  fastapi import FastAPI
from A_DatabasePackage.secure_database_connection import BASE, ENGINE
from I_ControllerPackage import user_controller, loan_controller

BASE.metadata.create_all(bind=ENGINE)

app = FastAPI(
    title="Loan Account Management System",
    version="1.0",
    description="This application allows you to manage your loan accounts."
)
@app.get('/')
def home():
    return {'message': 'Welcome to Loan Account Management System!'}

app.include_router(user_controller.router)
app.include_router(loan_controller.router)