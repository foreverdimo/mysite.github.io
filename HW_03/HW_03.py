import jieba
import jieba.posseg as pseg

txt_file_name = './data/水浒传.txt'
node_file_name = './output/水浒传-人物节点.csv'
link_file_name = './output/水浒传-人物连接.csv'

with open(txt_file_name,"r+",encoding="utf-8") as f:
    line_list = f.readlines()


line_name_list = []  # 每个段落出现的人物列表
name_cnt_dict = {}  # 统计人物出现次数
print('正在分段统计……')
print('已处理词数：')

ignore_list = []

progress = 0  # 用于计算进度条
for line in line_list: # 逐个段落循环处理
    word_gen = pseg.cut(line) # peseg.cut返回分词结果，“生成器”类型
    line_name_list.append([])
    
    for one in word_gen:
        word = one.word
        flag = one.flag
        
        if len(word) == 1:  # 跳过单字词
            continue
        
        if word in ignore_list:  # 跳过标记忽略的人名 
            continue
        
        # # 对指代同一人物的名词进行合并
        # if word == '孔明':
        #     word = '诸葛亮'
        # elif word == '玄德' or word == '刘玄德':
        #     word = '刘备'
        # elif word == '云长' or word == '关公':
        #     word = '关羽'
        # elif word == '后主':
        #     word = '刘禅'  
            
        if flag == 'nr': 
            line_name_list[-1].append(word)
            if word in name_cnt_dict.keys():
                name_cnt_dict[word] = name_cnt_dict[word] + 1
            else:
                name_cnt_dict[word] = 1
        
        # 因为词性分析耗时很长，所以需要打印进度条，以免用户误以为死机了
        progress = progress + 1
        progress_quo = int(progress/1000)
        progress_mod = progress % 1000 # 取模，即做除法得到的余数
        if progress_mod == 0: # 每逢整千的数，打印一次进度
            #print('---已处理词数（千）：' + str(progress_quo))
            print('\r' + '-'*progress_quo + '> '\
                  + str(progress_quo) + '千', end='')
# 循环结束点        
print()
print('基础数据处理完成')