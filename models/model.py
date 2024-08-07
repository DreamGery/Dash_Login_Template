import os
import sys

sys.path.append('..')
sys.path.append(os.getcwd())

import orjson
import pandas as pd
from sqlalchemy import JSON, Column, Integer, String, create_engine, exists, select
from sqlalchemy.orm import Session, declarative_base

from utils import str2md5

# 定义数据库模型基类
Base = declarative_base()

# 定义用户模型
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    user_role = Column(String(255), nullable=False)
    user_permission = Column(JSON, nullable=False)
    refresh_token = Column(String(255), nullable=True)
    

class Auth:
    def __init__(self):
        engine = create_engine('sqlite:///./models/users.db')

        # 创建数据库表
        Base.metadata.create_all(engine)

        self.engine = engine

    def add_user(self, username: str, password: str, user_role: str, user_permission: dict):
        with Session(self.engine) as add_user_session:
            if self.check_users_name(username=username)['status'] == 'exist':
                return {'status': 'error', 'message': '用户名已存在'}
            else:
                new_user = User(
                    username=username, 
                    password=password, 
                    user_role=user_role, 
                    user_permission=user_permission
                )
                add_user_session.add(new_user)
                add_user_session.commit()
                return {'status': 'success', 'message': '添加成功'}

    def delete_user(self, username: list):
        with Session(self.engine) as delete_session:
            try:
                delete_session.query(User).filter(User.username.in_(username)).delete()
                delete_session.commit()
                return {'status': 'success', 'message': '删除成功'}
            except Exception as e:
                delete_session.rollback()
                return {'status': 'error', 'message': f'{e}'}
    
    def change_user_information(self, username: str, changed_data: dict):
        with Session(self.engine) as change_session:
            try:
                change_session.query(User).filter_by(username=username).update(changed_data)
                change_session.commit()
                return {'status': 'success', 'message': '修改成功'}
            except Exception as e:
                change_session.rollback()
                return {'status': 'error', 'message': f'{e}'}

    # 查询用户名是否存在
    def check_users_name(self, username: str):
        with Session(self.engine) as check_users_name_session:
            exist_or_not = (
                check_users_name_session
                .query(exists().where(User.username == username))
                .scalar()
            )
            if exist_or_not:
                return {'status': 'exist'}
            else:
                return {'status': 'notExist'}

    # 验证密码是否正确
    def check_password(self, username: str, password: str):
        with Session(self.engine) as password_session:
            db_password = password_session.query(User.password).filter_by(username=username).first()[0]
            if db_password == password:
                return {'status': 'success', 'message': '密码验证成功'}
            else:
                return {'status': 'error', 'message': '密码验证失败'}
            
    def return_user_information(self, username: str):
        with Session(self.engine) as information_session:
            user_information = (
                information_session.scalars(
                    select(User)
                    .where(User.username == username)
                ).one()
            )
            return user_information
    
    def return_user_table(self):
        df = pd.read_sql(
            'SELECT * FROM users', 
            con=self.engine, 
            dtype_backend='pyarrow'
        ).drop(columns='password')
        
        data = (
            df
            .assign(
                permission=lambda p: p['user_permission'].apply(
                    lambda x: orjson.loads(x)
                )
            )
            .assign(
                permission=lambda per: per['permission'].apply(
                    lambda s: [
                        {
                            'tag': i,
                            'color': 'cyan'
                        } for i in s.get('permission')
                    ]
                )
            )
        )
        return data

auth = Auth()        

# 使用数据库
if __name__ == '__main__':

    auth.add_user(
        username='test',
        password=str2md5('test'),
        user_role='超级管理员',
        user_permission={
            'permission': []
        }
    )


    





