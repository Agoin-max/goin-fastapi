from database.session import MysqlConnection
from collections import OrderedDict


def select_dict(sql, params=None, flat=False):
    connect_obj = MysqlConnection()
    db, cur = connect_obj.connect()
    if not sql:
        if flat:
            return {}
        else:
            return []
    res = {}
    try:
        cur.execute(sql, params)
        columns = [col[0] for col in cur.description]
        if flat:
            fetchone = cur.fetchone()
            if fetchone:
                res = dict(zip(columns, fetchone))
        else:
            res = [dict(zip(columns, row)) for row in cur.fetchall()]
        connect_obj.close()
        return res
    except (Exception,):
        connect_obj.close()
        if flat:
            return {}
        else:
            return []


def select_list(sql, params=None, flat=False):
    connect_obj = MysqlConnection()
    db, cur = connect_obj.connect()
    if not sql:
        return []
    res = []
    try:
        cur.execute(sql, params)
        if flat:
            fetchone = cur.fetchone()
            if fetchone:
                res = list(fetchone)
        else:
            res = [list(row) for row in cur.fetchall()]
        connect_obj.close()
        return res
    except (Exception,):
        connect_obj.close()
        return res


def sql_execute(sql, params=None):
    connect_obj = MysqlConnection()
    db, cur = connect_obj.connect()
    if not sql:
        return False
    try:
        cur.execute(sql, params)
        db.commit()
        db.close()
        return True
    except (Exception,):
        cur.rollback()
        db.close()
        return False


def get_pagination(sql, total_sql, order_by='', page=1, pagesize=20, params=None):
    # total_sql参数eg:  "select count(id) as count from user"
    if not isinstance(page, int) or not isinstance(pagesize, int):
        page = int(page)
        pagesize = int(pagesize)
    if order_by:
        sql += " order by {order_by} ".format(order_by=order_by)
    sql += " limit {start}, {pagesize} ".format(start=(page - 1) * pagesize, pagesize=pagesize)
    results = select_dict(sql, params=params)
    count = select_dict(total_sql, params=params, flat=True)

    return OrderedDict([
        ('count', count['count']),
        ('pagenum', page),
        ('pagesize', pagesize),
        ('records', results),
    ])
