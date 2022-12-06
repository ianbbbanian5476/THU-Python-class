upper_ = [*'DEFGHIJKLMNOPQRSTUVWXYZABC'] #轉換後密文字母
upper_replace = [*'ABCDEFGHIJKLMNOPQRSTUVWXYZ'] #原來的明文字母

dict1 = {} #建立一個字典儲存移位後的對照表
for key in range(26): 
    dict1[upper_[key]] = upper_replace[key] #將鍵值輸入

while True: #可不斷輸入
    txt = [*input()] #將txt的每個字元存成list
    for i in range(len(txt)): #每個元素都檢查
        txt[i] = dict1[txt[i]] #將對應的移位字母替換上
    print("".join(txt)) #將轉換後的txt輸出