from glob import iglob
import os
from Bio.Blast.Applications import NcbimakeblastdbCommandline
from Bio.Blast.Applications import NcbiblastnCommandline
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


def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print
        "---  new folder...  ---"
        print
        "---  OK  ---"

    else:
        print
        "---  There is this folder!  ---"
up_short="up_short"
down_short="down_short"
mkdir(up_short)
mkdir(down_short)
up=fasta2dict("upstream.fasta")
down=fasta2dict("downstream.fasta")
up_seq=list(up.values())[0]
down_seq=list(down.values())[0]

##拆分短序列
short = list()
for num in range(10, 25):
    for start in range(0, len(up_seq)-num+1):
        seq1=up_seq[start:start+num]
        short.append(seq1)
short2 = list()
for num in range(10, 25):
    for start in range(0, len(down_seq)-num+1):
        seq1=up_seq[start:start+num]
        short2.append(seq1)

####
i=0
for seq in short:
    i=i+1
    xx='up_short/seq'+str(i)+'.fasta'
    file=open(xx,'w')
    file.write('>' + str(i) + '\n')
    file.write(seq)
j=0
for seq in short:
    j=j+1
    xx='down_short/seq'+str(j)+'.fasta'
    file=open(xx,'w')
    file.write('>'+str(j)+'\n')
    file.write(seq)

up_re="up_re"
down_re="down_re"
mkdir(up_re)
mkdir(down_re)
makedb = NcbimakeblastdbCommandline(dbtype = 'nucl',input_file = 'C:/Users/fangyu/Desktop/all/com/python/ensemblout.fasta',out = 'C:/Users/fangyu/Desktop/all/com/python/ensembl.fasta')
stdout,stderr = makedb()
fasta_file=os.listdir('C:/Users/fangyu/Desktop/all/com/python/up_short')
k=0
for file in fasta_file:
    k=k+1
    blastn = NcbiblastnCommandline(query ='C:/Users/fangyu/Desktop/all/com/python/up_short/'+file, db = 'C:/Users/fangyu/Desktop/all/com/python/ensembl.fasta',outfmt = 6,out = 'C:/Users/fangyu/Desktop/all/com/python/up_re/'+str(k)+'out.txt')
    stdout,stderr = blastn()





