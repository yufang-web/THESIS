import sys




def max_index(lst_int):
    index = []
    max_n = max(lst_int)
    for i in range(len(lst_int)):
        if lst_int[i] == max_n:
            index.append(i)
    return index


			
####读入文件
def fasta2dict(file1):
    # 按行读取序列
    # 输入fasta文件，返回名称，序列
    inf=open(file1,'r')
    name=""
    samples = {}
    for line in inf:
        line = line.strip()
        if line.startswith('>'):
            name = line
            samples[name] = ''
        else:
            samples[name] += line
    return samples


##读入 HBB flanking region



##打分函数
def get_score(seq1,seq2):
	score=0
	for i in range(len(seq1)):
		if seq1[i]=='A' and seq2[i]=='A':
			score=score+1
		elif seq1[i]=='T' and seq2[i]=='T':
			score=score+1
		elif seq1[i]=='C' and seq2[i]=='C':
			score=score+1
		elif seq1[i]=='G' and seq2[i]=='G':
			score=score+1
		elif seq1[i]=='A' and seq2[i]=='G':
			score=score+1
	score=score/len(seq1)
	return(score)
##拆分序
def break_up(seq,k):
	short=list()
	for start in range(0, len(seq) - k + 1):
		seq1 = seq[start:start + k]
		short.append(seq1)
	return(short)

def over(short,hbb):
	short_part = []
	j = 0
	for seq in short:
		for i in range(0, len(hbb) - len(seq) + 1):
			part_seq = hbb[i:i + len(seq)]
			score = get_score(seq, part_seq)
			if score >=0.85:
				info = [j, seq, score, i, i + len(seq), part_seq]
				short_part.append(info)
		j = j + 1
	return(short_part)




HBB = fasta2dict("HBB.fasta")
up = fasta2dict("upstream.fasta")
down = fasta2dict("downstream.fasta")
hbb_seq = list(HBB.values())[0]
up_seq = list(up.values())[0]
down_seq = list(down.values())[0]
short1 = break_up(up_seq, 20)
short2 = break_up(down_seq, 20)
hbb_list1 = []
for short in short1:
	hbb_list1.append(hbb_seq)

hbb_list2 = []
for short in short2:
	hbb_list2.append(hbb_seq)

short_part1 = over(short1,hbb_seq)
short_part2 = over(short2,hbb_seq)
result_file1 = open('result1.xlsx', 'w')
for item in short_part1:
	for info in item:
		result_file1.write(str(info) + "\t")
	result_file1.write("\n")

result_file2 = open('result2.xlsx', 'w')
for item in short_part2:
	for info in item:
		result_file2.write(str(info) + "\t")
	result_file2.write("\n")









