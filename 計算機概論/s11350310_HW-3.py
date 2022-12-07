char = input('Enter the English sentence:') #使用者輸入帶有數字之英文句子
numbers = ['0','1','2','3','4','5','6','7','8','9'] #定義何為數字
record = '' #儲存轉換後的char

for i in range(len(char)): #一個一個字檢查是否為數字
    if char[i] not in numbers: #如果這個字不是數字
        record += char[i] #那就把這個字放進record

print(record) #輸出結果
