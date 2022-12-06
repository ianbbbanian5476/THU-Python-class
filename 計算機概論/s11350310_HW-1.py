upresult = ''  #儲存整數部分的二進制結果
downresult = ''  #儲存小數部分的二進制結果
while True: #提供使用者可以不斷使用此計算機
    try:  #檢驗使用者輸入的值是否為整數或小數
        ten = float(input('請輸入10進制的數字：'))  #輸入10進制的數字
    except:  
        print('你輸入的不是數字，請再試一次。') #顯示提示字詞
        continue #重新跑迴圈讓使用者再次輸入
    startwithint = int(ten) #取整數位
    startwithpoint = ten - float(startwithint) #取小數位
    #整數部分
    while startwithint >= 2: #當當前整數位>2時進入迴圈
        upresult = str(startwithint % 2) + upresult #整數位進行短除法除以2取餘數並儲存至upresult內
        startwithint = int(startwithint/2) #短除法後的商取代整數位
    if startwithint == 1: #迴圈(短除法)跑完後結果應該會是1，所以要補加上，但以防使用者輸入的整數位本身是0，所以用if判斷
        upresult = '1' + upresult #在整數部分的二進制運算結果最前面加上1
    #小數部分
    while startwithpoint != 0:  #當不等於0時進入迴圈，避免0*2=0
        downresult = downresult + str(int(startwithpoint * 2)) #小數部分*2後取整數位
        startwithpoint = startwithpoint * 2 - int(startwithpoint * 2) #*2取整數位後的小數部分取代原本小數部分
    #整理
    if upresult == '' : #如果整數部分因輸入值的關係不用進行運算，則整數部分的二進制結果為0
        upresult = '0' 
    if downresult == '': #如果小數部分因輸入值的關係不用進行運算，則小數部分的二進制結果為0
        downresult = '0'
    print(upresult + '.' + downresult) #引出二進制運算結果
    #print(downresult)
    upresult = '' #整數部分運算結果歸0，方便下次運算
    downresult = '' #小數部分運算結果歸0，方便下次運算