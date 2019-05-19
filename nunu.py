count=0
with open(r'C:\usr\python\log_files\201811113034M.log',encoding='utf8') as f:
    for line in f:
        str1=line.split('：')[2]
        str2=str1[:12]
        if str2=='201811113034M':
            count+=1
print(count)