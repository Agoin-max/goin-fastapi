FastAPI
-------
### **利用aerich数据库迁移 MySQL8以后版本正常**

```pip install aerich```

```aerich init -t 数据库指定配置```

```aerich init-db```

```修改模型后 -> aerich migrate ```

```把新生成的SQL推送到数据库 -> aerich upgrade```

```aerich downgrade 版本回退```