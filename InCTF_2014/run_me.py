import os,csv
import sys
import hashlib
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "inctf.settings")
from secondround.helper import *
from admin.helper import *

bin_flag, bin_names, bin_pt, bin_qn = [], [], [], []
crypt_flag, crypt_names, crypt_pt, crypt_qn = [], [], [], []
rev_flag, rev_names, rev_pt, rev_qn = [], [], [], []
for_flag, for_names, for_pt, for_qn = [], [], [], []
web_flag, web_names, web_pt, web_qn = [], [], [], []
names, keys, points, questions = [], [], [], []

attachments=['', '', '', '', '', '', '', '', '', '1.tar.7z', '2.tar.7z', '3.tar.7z', '4.tar.7z', 'one.tar.7z', 'two.tar.7z', 'three.tar.7z', 'four.tar.7z', 'five.tar.7z', 'six.tar.7z', 'seven.tar.7z', 'eight.tar.7z', 'Forensics1.tar.7z', 'Forensics2.tar.7z', 'Forensics3.tar.7z', 'Forensics4.tar.7z', 'Forensics5.tar.7z', 'Forensics6.tar.7z', 'Forensics7.tar.7z', 'Forensics8.tar.7z','','','','','','','Web7.tar.gz']
hints=['bin','bin','bin','bin','bin','bin','bin','bin','bin','crypto','crypto','crypto','crypto','rev','rev','rev','rev','rev','rev','rev','rev','for','for','for','for','for','for','for','for']
cat=['bin','bin','bin','bin','bin','bin','bin','bin','bin','cry','cry','cry','cry','rev','rev','rev','rev','rev','rev','rev','rev','for','for','for','for','for','for','for','for','web','web','web','web','web','web','web']


def flags(file_obj, flag_col_no, names_col_no, points_col_no, qn_col_no):
    flag,names,points,qn = [],[],[],[]
    reader = csv.reader(file_obj,delimiter=',')
    for row in reader:
        flag.append(str(hashlib.md5(row[flag_col_no]).hexdigest()))
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

print "Generating templates..."
print "Names:",len(names),"Keys:",len(keys),"Questions:",len(questions),"Points:",len(points),"Attach:",len(attachments),"Category:",len(cat)
for i in range(len(names)):
    try:
        add_challenge(names[i], keys[i], questions[i], attachments[i], points[i])
    except:
        print names[i]
        print len(keys[i])
        sys.exit(1)

setup_secondround()
for i in range(len(names)):
    create_challenge(names[i], keys[i], points[i], questions[i], attachments[i], cat[i])
    open_challenge(names[i])
