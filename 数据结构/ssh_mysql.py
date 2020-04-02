def ssh_mysql_select(sql, *args):
    """跳板机连接mysql 查询方法"""
    with SSHTunnelForwarder(
            (host, int(port)),
            ssh_username=ssh_username,
            ssh_password=ssh_password,
            remote_bind_address=(ssh_host, int(ssh_port)),
            # ssh_pkey=pk_file

    ) as tunnel:
        conn = pymysql.connect(host='127.0.0.1',
                               port=tunnel.local_bind_port,  # 5154
                               user=db_user,
                               password=db_password,
                               charset='utf8')
        cur = conn.cursor()
        conn.commit()
        cur.execute(sql, *args)
        result = cur.fetchall()
        conn.close()
        return result


def mysql_submit_revision(sql, *args):
    """
    跳板机连接mysql/提交 修改方法
    :param sql:
    :param args:
    :return:
    """
    try:
        with SSHTunnelForwarder(
                (host, int(port)),
                ssh_username=ssh_username,
                ssh_password=ssh_password,
                remote_bind_address=(ssh_host, int(ssh_port)),

        ) as tunnel:
            connection = pymysql.connect(host='127.0.0.1',
                                         port=tunnel.local_bind_port,
                                         user=db_user,
                                         password=db_password,
                                         charset='utf8')
            cursor = connection.cursor()
            cursor.execute(sql, *args)  # 执行sql语句
            connection.commit()  # 执行update操作时需要写这个，否则就会更新不成功
            connection.close()
            return "\n %s OK \n" % sql
