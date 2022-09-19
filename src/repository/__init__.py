from flask_sqlalchemy import SQLAlchemy
from injector import Module, singleton

class RepositoryModule(Module):
    def __init__(self, db, postgresdb):
        self.db = db
        self.postgresdb = postgresdb

    def configure(self, binder):
        pass