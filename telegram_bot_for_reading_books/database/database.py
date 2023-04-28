import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Column, ForeignKey, Integer, Text


engine = create_engine("sqlite:///users.db")

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    bookmark_id = Column(Integer, ForeignKey('bookmarks.id_bookmark'))
    bookmark = relationship('Bookmark')


class Bookmark(Base):
    __tablename__ = 'bookmarks'

    id_bookmark = Column(Integer, primary_key=True)
    page = Column(Integer, nullable=False)
    text = Column(Text, nullable=False)
    user = relationship('User')


Base.metadata.create_all(engine)

# Создаем шаблон заполнения словаря с пользователями
user_dict_template: dict = {'page': 1,
                            'bookmarks': set()}

# Инициализируем "базу данных"
users_db: dict = {}
