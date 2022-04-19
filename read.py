data = []
count = 0
with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 10000 == 0:
            print(len(data))
print('檔案讀取完了，總共有',len(data), '筆資料')

new = []
sum_len = 0
for d in data:
    if len(d) < 100:
        new.append(d)
    sum_len += len(d)

print('一共有',len(new),'筆留延長度小於100')
print('平均是', sum_len / len(data))


# 文字計數
wc = {} # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增新的key進wc字典
# for word in wc:                         #字典當中的每個key
#     if wc[word] > 100:
#         print(word, wc[word])

print(len(wc))          # wc字典內 key的數量

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

while True:
    word = input('請問你想查甚麼字:')
    if word == 'q':
        break
    print(word, '出現過的次數為:', wc[word])
print('感謝使用本查詢功能')