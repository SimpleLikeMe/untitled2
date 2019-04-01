# 导入数据模型模块
from orm import model
# 导入md5加密模块
from hashlib import md5

# 导入会话模块，可以获取会话对象
from sqlalchemy.orm import sessionmaker

# 创建会话对象，用于与数据库交互
session = sessionmaker()()


def md5_encryption(bf_str):
    """
    md5加密字符串
    :param bf_str:加密前的字符串
    :return: af_str加密后字符串
    """
    # 将传递过来的字符转换为字符串,并进行编码
    bf_str = str(bf_str).encode("utf8")
    # 获取md5对象
    m = md5()
    # 加密字符串
    m.update(bf_str)
    # 获取加密结果,并返回
    return m.hexdigest()


def insert_user(account, password, name="新用户", address="待完善"):
    """插入用户"""
    # md5加密方式加密密码
    password = md5_encryption(password)
    # 创建用户对象
    user = model.User(account=account, password=password, name=name, address=address)

    try:
        # 将用户插入数据库
        session.add(user)
        # 提交对象
        session.commit()
        return user
    except Exception:
        print("插入用户失败")
        return False


def check_user(account, password):
    """
    验证用户是否在数据库中存在
    :param account:用户的账号
    :param password:用户的密码
    :return: account 返回用户的账号
    """
    # md5加密方式加密密码
    password = md5_encryption(password)
    if session.query(model.User).filter(model.User.account == account).filter(model.User.password == password).first():
        return account
    else:
        return False


def query_user(account):
    """
    验证用户是否在数据库中存在
    :param account:用户的账号
    :return: user 返回用户
    """

    user = session.query(model.User).filter(model.User.account == account).first()
    if user:
        return user
    else:
        return False


def query_many_user(start=0, end=None, many=None):
    user_list = session.query(model.User).all()
    if user_list:
        return user_list
    else:
        return False


def insert_comment(article_id,user_id, content):
    """插入记录"""
    # 创建record对象并写入数据库
    comment = model.Comment(article_id=article_id, user_id=user_id, content=content)
    try:
        # 将用户插入数据库
        session.add(comment)
        # 提交对象
        session.commit()
        return comment
    except Exception:
        print("插入记录失败")
        return False


def query_article_one(id):
    """插入记录"""
    try:
        # 将用户插入数据库
        article = session.query(model.Article).filter(model.Article.id == id).first()
        return article
    except Exception:
        print("插入记录失败")
        return False


def query_record_all():
    """插入记录"""
    try:
        # 将用户插入数据库
        record = session.query(model.Comment).all()
        return record
    except Exception:
        print("插入记录失败")
        return False


def del_article(id):
    """插入记录"""
    try:
        # 将用户插入数据库
        article = session.query(model.Article).filter(model.Article.id == id)
        if article:
            article.delete()
        session.commit()
        return article
    except Exception:
        print("插入记录失败")
        return False


def insert_article(title, content, user_id):
    """插入记录"""
    # 创建record对象并写入数据库
    article = model.Article(title=title, user_id=user_id, content=content)
    try:
        # 将用户插入数据库
        session.add(article)
        # 提交对象
        session.commit()
        return article
    except Exception:
        print("插入记录失败")
        return False


def query_article_all():
    """插入记录"""
    try:
        # 将用户插入数据库
        record = session.query(model.Article).all()
        return record
    except Exception:
        print("插入记录失败")
        return False



if __name__ == "__main__":
    # insert_user(account="1", password="1", name="simple")
    # insert_article(title="希望中国", content="这个世界如此复杂，我需要简简单单、平平凡凡的生活！", user_id=1)
    insert_comment(content="Java编程攻略", article_id=1, user_id="1")
