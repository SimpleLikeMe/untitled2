# 导入引擎创建模块
from sqlalchemy import create_engine
# 导入创建基础类的模块，封装了基础的sql语句
from sqlalchemy.ext.declarative import declarative_base
# 导入数据支持
from sqlalchemy import Column, String, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
import datetime

# 创建引擎对象
engine = create_engine("mysql+mysqlconnector://root:SimpleID450326@localhost/blog", encoding='utf8', echo=True)

# 获取基础类,绑定当前引擎对象
Base = declarative_base(bind=engine)


# 创建数据表类型
class User(Base):
    __tablename__ = "user"
    account = Column(String(30), primary_key=True)
    name = Column(String(50), nullable=False)
    password = Column(String(60), nullable=False)
    address = Column(String(50), nullable=False, server_default="待完善")
    email = Column(String(50), nullable=False, server_default="待完善")
    phone = Column(String(11), nullable=False, server_default="15088888888")
    gender = Column(String(1), nullable=False, server_default="男")
    age = Column(String(3), nullable=False, server_default="0")
    integration = Column(Integer, nullable=False, server_default="100")
    status = Column(Boolean, nullable=False, server_default="1")
    remark = Column(String(255), nullable=False, server_default="待完善")


# class Goods(Base):
#     __tablename__ = "goods"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     name = Column(String(50), nullable=False)
#     price = Column(Integer, nullable=False)


# class Order(Base):
#     __tablename__ = "orders"
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     user_id = Column(Integer, ForeignKey("user.account"))
#     goods_id = Column(Integer, ForeignKey("goods.id"))
#     num = Column(Integer, nullable=False, server_default='0')
#     user = relationship("User", backref="order")


class Article(Base):
    """定义一个记录类"""
    __tablename__ = "article"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(String(255), nullable=False)
    comment_count = Column(Integer, nullable=False, server_default="0")
    read_count = Column(Integer, nullable=False, server_default="0")
    is_del = Column(Boolean, nullable=False, server_default="0")
    a_type = Column(String(20), nullable=False, server_default="编程语言")
    publish_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    user_id = Column(String(30), ForeignKey("user.account"))
    user = relationship("User", backref='article')
    comment = relationship("Comment", backref='comment')


class Comment(Base):
    """定义一个记录类"""
    __tablename__ = "comment"
    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String(255), nullable=False)
    article_id = Column(Integer, ForeignKey("article.id"))
    user_id = Column(String(30), ForeignKey("user.account"))
    comment_time = Column(DateTime, nullable=False, default=datetime.datetime.now)
    article = relationship("Article", backref='article')
    user = relationship("User", backref='user')


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
