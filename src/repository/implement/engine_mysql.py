#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from decouple import config
from sqlalchemy.ext.declarative import declarative_base

from . import Base
from ..empleados import Empleados


class DB_storage(object):

    __engine = None
    __session = None

    def __init__(self):
        """Init method."""
        mysql_user = config('MYSQL_USER')
        mysql_pwd = config('MYSQL_PWD')
        mysql_host = config('MYSQL_HOST')
        mysql_db = config('MYSQL_DB')
        self.__engine = create_engine(
            f'mysql+pymysql://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_db}?charset=utf8mb4')
        self.__session = self.reload()

    def new(self, obj):
        """Create an new register in DB

        Args:
            obj (class): class schema
        """
        if (obj):
            self.__session.add(obj)
            self.__save()
            return self.__session.query(Empleados).filter(Empleados.usuario == obj.usuario)

    def find(self):
        return self.__session.query(Empleados).all()

    def find_one(self, usuario):
        if (usuario):
            return self.__session.query(Empleados).filter(Empleados.usuario == usuario)
        return None

    def __save(self):
        self.__session.commit()

    def update(self, data):
        if (data.get('id')):
            user = self.__session.query(Empleados).filter(Empleados.id == data.get('id'))
            if (user):
                user.update(data)
                self.__save()
                return user

    def delete(self, obj):
        self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database (feature of SQLAlchemy)."""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        return Session()

    def close(self):
        """Close SQLAlchemy actual session"""
        self.__session.close()


    def delete_by_id(self, id):
        users = self.__session.query(Empleados).filter(Empleados.id == id)
        if (users):
            for user in users:
                self.__session.delete(user)
                self.__save()
                return True
        return False

