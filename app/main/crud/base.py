from typing import Any, Generic, List, Optional, Type, TypeVar

import sqlalchemy
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette.exceptions import HTTPException

from app.main.database.db import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
            Base Service for CRUD Operation´s like READ, UPDATE, DELETE AND CREATE


        :param model: model which is used.
        """
        self.model = model

    def get(self, db_session: Session, id: Any) -> Optional[ModelType]:
        """
       Get´s a specific object from the database


       :param db_session: Current Session.
       :param id: Identifier for the object, which is going to be searched.
       :return: Found Object
        """
        return db_session.query(self.model).filter(self.model.id == id).first()

    def list(self, db_session: Session) -> List[ModelType]:
        """
        Query´s everything for the specific Object Type

           :param db_session: Current Session.
           :return: List of Objects
        """
        objs: List[ModelType] = db_session.query(self.model).all()
        return objs

    def create(self, obj: CreateSchemaType, db_session: Session) -> ModelType:
        """
        Create´s an object in the database.

        :param db_session: Current Session.
        :param obj: Object which is going to be created in the database.
        :return: Created Object
        """
        db_obj: ModelType = self.model(**obj.dict())
        db_session.add(db_obj)
        try:
            db_session.commit()
        except sqlalchemy.exc.IntegrityError as e:
            db_session.rollback()
            if "duplicate key" in str(e):
                raise HTTPException(status_code=409, detail="Conflict Error")
            else:
                raise e
        return db_obj

    def update(self, object_id: Any, obj: UpdateSchemaType, db_session: Session, ) -> Optional[ModelType]:
        """
        Update´s a specific Object in the database.

        :param object_id: Identifier of the object which is going to be updated
        :param obj: Data of the updated Object
        :return: Updated Object.
        """
        db_obj = self.get(object_id)
        for column, value in obj.dict(exclude_unset=True).items():
            setattr(db_obj, column, value)
        db_session.commit()
        return db_obj

    def delete(self, object_id: Any, db_session: Session) -> None:
        """
        Delete´s a specific Object by its Identifier

        :param object_id: Identifier of the Object which is going to be deleted
        :return:
        """

        db_obj = db_session.query(self.model).get(object_id)
        db_session.delete(db_obj)
        db_session.commit()
