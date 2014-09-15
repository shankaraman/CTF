import csv

bin_flag, bin_names, bin_pt, bin_qn = [], [], [], []
crypt_flag, crypt_names, crypt_pt, crypt_qn = [], [], [],[]
rev_flag, rev_names, rev_pt, rev_qn = [], [], [], []
for_flag, for_names, for_pt, for_qn = [], [], [], []
web_flag, web_names, web_pt, web_qn = [], [], [],[] 
names, keys, points, questions = [], [], [], []


def flags(file_obj, flag_col_no, names_col_no, points_col_no, qn_col_no):
    flag,names,points,qn = [],[],[],[]
    reader = csv.reader(file_obj,delimiter=',')
    for row in reader:
        flag.append(row[flag_col_no])
        names.append(row[names_col_no])
        points.append(row[points_col_no])
        qn.append(row[qn_col_no])
    del(flag[0],names[0],points[0],qn[0])
    return flag,names,points,qn

f = open('Binary.csv',"rb")
bin_flag, bin_names, bin_pt, bin_qn = flags(f,3,1,6,5)
f = open('Forensics.csv',"rb")
for_flag, for_names, for_pt, for_qn = flags(f,5,1,4,6)
f = open('Reverse.csv',"rb")
rev_flag, rev_names, rev_pt, rev_qn = flags(f,4,1,5,6)
f = open('Crypto.csv',"rb")
crypt_flag, crypt_names, crypt_pt, crypt_qn = flags(f,4,1,5,6)
f = open('Web.csv','rb')
web_flag, web_names, web_pt, web_qn = flags(f,3,1,4,2)


for i in range(len(bin_flag)):
    names.append(bin_names[i])
    keys.append(bin_flag[i])
    points.append(bin_pt[i])
    questions.append(bin_qn[i])

for i in range(len(crypt_flag)):
    names.append(crypt_names[i])
    keys.append(crypt_flag[i])
    points.append(crypt_pt[i])
    questions.append(crypt_qn[i])

for i in range(len(rev_flag)):
    names.append(rev_names[i])
    keys.append(rev_flag[i])
    points.append(rev_pt[i])
    questions.append(rev_qn[i])

for i in range(len(for_flag)):
    names.append(for_names[i])
    keys.append(for_flag[i])
    points.append(for_pt[i])
    questions.append(for_qn[i])

for i in range(len(web_flag)):
    names.append(web_names[i])
    keys.append(web_flag[i])
    points.append(web_pt[i])
    questions.append(web_qn[i])

for i in range(len(names)):
    print names[i]
    print questions[i]
    print keys[i]
    print points[i]
