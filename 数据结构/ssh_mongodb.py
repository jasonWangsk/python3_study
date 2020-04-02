import pymongo
from sshtunnel import SSHTunnelForwarder

def ssh_get_mongodb_client(self):
    """ssh-跳板机连接mongodb"""
    host = self.mongo_host  # 数据库主机地址
    # 跳板机参数
    server = SSHTunnelForwarder(
        ssh_address_or_host=self.ecs_host,
        ssh_password=self.ecs_password,
        ssh_username=self.ecs_user,
        remote_bind_address=(host, 27017))
    server.start()
    client = pymongo.MongoClient('127.0.0.1', server.local_bind_port)
    db = client[self.mongo_database]
    #  数据库用户/密码
    db.authenticate(self.mongo_account, self.mongo_password)  # 授权执行命令
    return db