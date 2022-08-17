import re
import datetime
import pytz
import inflect

from sqlalchemy import Column, Integer, DateTime, ForeignKey, Text, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declared_attr



def current_time():
    return datetime.datetime.now(tz=pytz.timezone('UTC'))


inflect = inflect.engine()


class CommonBase:
    __name__: str

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(
        DateTime(timezone=True),
        default=current_time, nullable=False
    )
   
    status = Column(Integer, nullable=True)

    @classmethod
    def get_table_name(cls, make_plural: bool = True):
        name_arr = re.split('(?=[A-Z]', f"{cls.__name__}")
        name_arr[-1] = name_arr[-1].lower() if inflect.singular_noun(name_arr[-1].lower()) else inflect.plural(name_arr[-1].lower())
        return "_".join(name_arr).lower()

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.get_table_name()




class SimpleCommonBase(CommonBase):
    name = Column(String(255))
    description = Column(Text, nullable=True)
