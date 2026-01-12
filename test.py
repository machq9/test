# 测试AI代码Review的综合用例
import sqlite3

# 1. 语法错误：函数定义缺少冒号、缩进错误
def get_user(user_id)
    # 2. 安全漏洞：SQL注入（字符串拼接）
    conn = sqlite3.connect("test.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM users WHERE id = " + str(user_id)  # 高危：无参数化查询
    cursor.execute(sql)
    result = cursor.fetchone()
    
    # 3. 规范问题：不符合PEP8（变量名大驼峰、行长度超标）
    UserInfo = result  # 应改为user_info
    LongVariableNameThatExceedsPEP8StandardForLineLength = 123  # 行长度超过80字符
    
    # 4. 逻辑错误：边界条件未覆盖（等于18岁未判定为成年）
    def is_adult(age):
        if age > 18:  # 应改为 >=18
            return True
        else:
            return False
    
    # 5. 性能问题：低效循环（可改用生成器）
    def get_large_list():
        return [i for i in range(100000)]  # 大列表占用内存，应改为 (i for i in range(100000))
    
    # 6. 资源泄漏：未关闭数据库连接
    return UserInfo
