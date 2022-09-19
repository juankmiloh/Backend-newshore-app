from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

class ServiceModule(Module):
    def configure(self, binder):
        pass