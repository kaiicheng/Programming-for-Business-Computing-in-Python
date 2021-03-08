# kelly wang

# input
# 有五行 input，一行一個數字
adult_num = int(input())  # 全票數量
student_num = int(input())  # 學生票數量
adult_price = int(input())  # 全票價格
student_price= int(input())  # 學生票價格
money = int(input())  # 擁有的鈔票面額
# 所需要付的金額
ttl_price = student_price * student_num + adult_price * adult_num
remaining = money - ttl_price  # 要找回的錢
# output
print(money, ttl_price, remaining, sep=',')
