#!/usr/bin/env python
# coding: utf-8

# In[9]:


import sqlite3


# In[5]:


conn = sqlite3.connect('orders.db')


# In[6]:


cur = conn.cursor()


# In[8]:


cur.execute("YOUR-SQL-QUERY-HERE;")


# In[13]:


cur.execute("""CREATE TABLE IF NOT EXISTS users(
   userid INT PRIMARY KEY,
   fname TEXT,
   lname TEXT,
   gender TEXT);
""")
conn.commit()


# In[14]:


cur.execute("""CREATE TABLE IF NOT EXISTS orders(
   orderid INT PRIMARY KEY,
   date TEXT,
   userid TEXT,
   total TEXT);
""")
conn.commit()


# In[15]:


cur.execute("""INSERT INTO users(userid, fname, lname, gender) 
   VALUES('00001', 'Nik', 'Piepenbreier', 'male');""")
conn.commit()


# In[16]:


user = ('00002', 'Lois', 'Lane', 'Female')


# In[18]:


cur.execute("INSERT INTO users VALUES(?, ?, ?, ?);", user)
conn.commit()


# In[19]:


more_users = [('00003', 'Peter', 'Parker', 'Male'), ('00004', 'Bruce', 'Wayne', 'male')]


# In[20]:


cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", more_users)
conn.commit()


# In[21]:


cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?);", customers)
cur.executemany("INSERT INTO orders VALUES(?, ?, ?, ?);", orders)
conn.commit()


# In[22]:


cur.execute("SELECT * FROM users;")
one_result = cur.fetchone()
print(one_result)


# In[23]:


cur.execute("SELECT * FROM users;")
three_results = cur.fetchmany(3)
print(three_results)


# In[24]:


cur.execute("SELECT * FROM users;")
all_results = cur.fetchall()
print(all_results)


# In[25]:


cur.execute("DELETE FROM users WHERE lname='Parker';")
conn.commit()


# In[26]:


cur.execute("select * from users where lname='Parker'")
print(cur.fetchall())


# In[27]:


cur.execute("""SELECT *, users.fname, users.lname FROM orders
    LEFT JOIN users ON users.userid=orders.userid;""")
print(cur.fetchall())


# In[29]:


# Github Link: https://github.com/om4kud/SQLite_Lab


# In[ ]:




