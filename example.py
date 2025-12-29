# 1.「hello world」と出力
print("hello world")

#2.greet関数を実装し、「こんにちは」と出力
greet = print("こんにちは")

#3.nameを引数に摂り「私の名前は{name}です」と出力するprint_name関数を実装
def print_name(name):
    print(f"私の名前は{name}です")

print(print_name("太郎"))

#4.「おはようございます」という文字列を戻り値として返すget_greet関数を実行し、戻り値をprint関数で出力
def get_greet():
      return f"おはようございます"
print(get_greet())

#5.a,bを引数に取り、その足し算を戻り値として返すadd関数を実装し、関数を呼び出して結果をprint関数で出力
def add(a, b):
      return a + b

print(add(2, 3))



      
