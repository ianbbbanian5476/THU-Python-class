def find_min_integer(List_of_integer : list):  #定義 find_min_integer() 作為找到 list 中數字最小的元素的功能
    List_of_integer = list(map(int,List_of_integer)) #因為 input() 所導入的值為 string ，無法進行數字大小比較，因此需要將每一項變動資料形態
    return min(List_of_integer) #回傳 list 中的最小值

def Selection_sort(List_of_integer : list): #定義 Selection_sort() 作為選擇排序法的功能
    List_of_integer = list(map(int,List_of_integer)) #因為 input() 所導入的值為 string ，無法進行數字大小比較，因此需要將每一項變動資料形態
    #選擇排序法是從 list 中的第一項開始至倒數第二項，依序向該項的後面所有元素的最小值進行比較，若該項之值大於該項的後面所有元素的最小值，
    #則該項的值就需要跟該項後面所有元素最小值的那項進行值的交換，交換過後就進行下一項，直到運行至倒數第二項結束。
    for i in range(len(List_of_integer)):  #len()表示得知list中元素的多寡，在直接放進去range的情況下，剛好會運行至倒數第二項停下
        now = List_of_integer[i] #取得第 i 項的值做佔存
        if min(List_of_integer[i:]) < now: #與第 i 項後面所有元素進行比較  #若第 i 項的值大於第 i 項後面所有元素的最小值：
            List_of_integer[i] , List_of_integer[List_of_integer.index(min(List_of_integer[i:]))] = List_of_integer[List_of_integer.index(min(List_of_integer[i:]))] , List_of_integer[i] #則第 i 項的值就需要跟第 i 項後面所有元素最小值的那項進行值的交換

    return List_of_integer #回傳經過 Selection_sort 選擇排序法排序的 list

numlist = input().split(' ') #讓使用者進行輸入 split(' ') 可以將輸入的一串字串以空格(' ') 進行分割成為 list
print(find_min_integer(numlist)) #套用 find_min_integer() 並進行輸出
print(Selection_sort(numlist))  #套用 Selection_sort() 並進行輸出