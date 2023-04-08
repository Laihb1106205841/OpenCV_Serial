import sqlite3
import cv2
import numpy

# 创建连接到数据库的连接对象
conn = sqlite3.connect('image.db')

# 创建游标对象
cursor = conn.cursor()

# 创建图像表格
cursor.execute('''
    CREATE TABLE IF NOT EXISTS images (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        data BLOB
    )
''')

# 将图像数据插入到表格中
img = cv2.imread('example.jpg')
img_data = cv2.imencode('.jpg', img)[1].tobytes()
cursor.execute("INSERT INTO images (name, data) VALUES (?, ?)", ('example.jpg', img_data))

# 提交事务
conn.commit()

# 从表格中读取图像数据
cursor.execute("SELECT data FROM images WHERE name=?", ('example.jpg',))
data = cursor.fetchone()[0]
img = cv2.imdecode(numpy.fromstring(data, numpy.uint8), cv2.IMREAD_UNCHANGED)

# 关闭游标和连接对象
cursor.close()
conn.close()
