pre_chr = [*"`1234567890-=qwertyuiop[]\ asdfghjkl;'zxcvbnm,./"]
pre_chr.remove(' ')
af_chr  = [*"./`1234567890-=qwertyuiop[]\ asdfghjkl;'zxcvbnm,"]
af_chr.remove(' ')

while True:
    txt = input().lower()
    if txt != '':
        txt = [*txt]
        tran_txt = ''
        for j in txt:
            if j == ' ':
                tran_txt += ' '
            else:
                tran_txt += af_chr[pre_chr.index(j)]
        print(tran_txt)
    else:
        break


