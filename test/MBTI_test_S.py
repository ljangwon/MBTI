# -*- coding: cp949 -*-
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg 
from tkinter import scrolledtext 

# Create instance
win = tk.Tk()

global index

# Add a title       
win.title("MBTI �˻�1")

tabControl = ttk.Notebook(win)    # Create Tab Control

# Tab Control 0 refactoring  ---------------------------------------------------------
tab0 = ttk.Frame(tabControl)
tabControl.add(tab0, text=' �������� ')
tab1 = ttk.Frame(tabControl)            
tabControl.add(tab1, text='Page 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Page 2')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Page 3')
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='Page 4')
tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='���')
tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using tab0 as the parent
page0 = ttk.LabelFrame(tab0, text=' �������� ')
page0.grid(column=0, row=0, padx=8, pady=2)

page1 = ttk.LabelFrame(tab1, text=' �˻� Page1 ')
page1.grid(column=0, row=0, padx=8, pady=2)

page2 = ttk.LabelFrame(tab2, text=' �˻� Page2 ')
page2.grid(column=0, row=0, padx=8, pady=2)

page3 = ttk.LabelFrame(tab3, text=' �˻� Page3 ')
page3.grid(column=0, row=0, padx=8, pady=2)

page4 = ttk.LabelFrame(tab4, text=' �˻� Page4 ')
page4.grid(column=0, row=0, padx=8, pady=2)

page5 = ttk.LabelFrame(tab5, text=' �˻� ��� ')
page5.grid(column=0, row=0, padx=8, pady=2)


# Modify adding a Label using mighty as the parent instead of win
a_label = ttk.Label(page0, text="�Է��ϼ��� �̸�:")
a_label.grid(column=0, row=0, sticky='W')

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(page0, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')               # align left/West

# Modified Button Click Function
def click_me(): 
    start_label.configure(text='Hello ' + name.get() + ' ' + 
                     grade_chosen.get() + ' Now MBTI Start ... ')
    win.title( "MBTI �˻�  "+ name.get() + " ������ ")
# Adding a Button
start_button = ttk.Button(page0, text=' �˻����! ', command=click_me)   
start_button.grid(column=2, row=1)                                

ttk.Label(page0, text="�����ϼ��� �г�:").grid(column=1, row=0)
grade = tk.StringVar()
grade_chosen = ttk.Combobox(page0, width=12, textvariable=str, state='readonly')
grade_chosen['values'] = ('E3', 'E4', 'E5', 'E6', 'M1', 'M2', 'M3')
grade_chosen.grid(column=1, row=1)
grade_chosen.current(0)

start_label = ttk.Label(page0, text= ' ')
start_label.grid(row=2, sticky='WE', columnspan=3)

name_entered.focus()      # Place cursor into name Entry

# Tab Control 1 refactoring  ---------------------------------------------------------

radioVar = []
Qnum = 40

for i in range(Qnum):
    radioVar.append( tk.IntVar() )

# Questions LabelFrame 
pageLF = []

for i in range(Qnum):
    if 0<= i <= 9 :
        pageLF.append( ttk.LabelFrame(page1) )
        pageLF[i].grid(column=0, row=i, sticky='WE')
    elif 10<= i <= 19 :
        pageLF.append( ttk.LabelFrame(page2) )
        pageLF[i].grid(column=0, row=i-10, sticky='WE')
    elif 20<= i <= 29 :            
        pageLF.append( ttk.LabelFrame(page3) )
        pageLF[i].grid(column=0, row=i-20, sticky='WE')
    elif 30<= i <= 39 :
        pageLF.append( ttk.LabelFrame(page4) )
        pageLF[i].grid(column=0, row=i-30, sticky='WE')    
 
Qa = []
Qb = []
for i in range(Qnum):
    Qa.append( '' )    
for i in range(Qnum):
    Qb.append( '' )    

# ����ó : ������, �ӽ�ȯ ��, ���������� ���� ��ġ�
# Q1 ��������  E(����), I(����) �˻�  ������(E)�� ����� �ΰ��� �繰�� �ܸ����� ���踦 �����ϴ� �ݸ�, ������(I)�� ����� ������ ������ ������ ���踦 ����
Qa[0] = ' ����1a ���� ���ϱ⸦ ������ �Ǽ� �� ���� ���� �ִ�. '  
Qb[0] = ' ����1a ���� ���� ���� �ֺ� ������� ����� �� ���� �ִ�. '

# Q2 ��������  E(����), I(����) �˻�
Qa[1] = ' ����2a ���� ���ο� ����� ������ ������� �ʴ�. '
Qb[1] = ' ����2b ���� �𸣴� ����� ������ ���� �ǰ��ϴ�. '

# Q3 ��������   E(����), I(����) �˻�
Qa[2] = ' ����3a ���� ���ϸ鼭 �����ϰ� ��ȭ���� ����� ���� �ִ�. '
Qb[2] = ' ����3b ���� �ǰ��� ���ϱ� �ռ� ������ �����ϴ� ���̴�. '

# Q4 ��������   E(����), I(����) �˻�
Qa[3] = ' ����4a ���� ������ ���ϴ� ���� ���ϴ�. '
Qb[3] = ' ����4b ���� ȥ�� Ȥ�� �Ҽ��� ���ϴ� ���� ���ϴ�. '

# Q5 ��������   E(����), I(����) �˻�
Qa[4] = ' ����5a ���� ���� ���ظ� ����鿡�� ǥ���ϱ⸦ �����Ѵ�. '
Qb[4] = ' ����5b ���� ��ü�� ���� ����, ���ظ� �� �ȿ� �����ϴ� ���̴�. '

# Q6 ��������  E(����), I(����) �˻�
Qa[5] = ' ����6a ���� �� �� ����ó�� ū ���̴�. '
Qb[5] = ' ����6b ���� �� �� ����ó�� ����ϸ� ����� ���̴�. '

# Q7 ��������   E(����), I(����) �˻�
Qa[6] = ' ����7a ���� �ð� ȥ�� ���ϴ� ���� �ܷӰ� ������ ���̴�. '
Qb[6] = ' ����7b �� �����ð� ���� ���ϴ� ���̴�. '

# Q8 ��������   E(����), I(����) �˻�
Qa[7] = ' ����8a �� �� �� ������ �ͺ��ٴ� ��� ������ �Ҹ��� ������ �ȴ�. '
Qb[7] = ' ����8b ���� ������ �ִ� ������ ���� �� �� ���ϱⰡ �����. '

# Q9 ��������   E(����), I(����) �˻�
Qa[8] = ' ����9a ���� �������̴�. '
Qb[8] = ' ����9b ��Ҹ��� �۰� �����ϰ� õõ�� ���ϴ� ���̴�. '

# Q10 ��������   E(����), I(����) �˻�
Qa[9] = ' ����10a ���� Ȱ������ ���̴�. '
Qb[9] = ' ����10b ���� ���� �ִ� ���� ���ϴ�. '

# Q11 ��������     S(����), N(����) �˻� ������(S)�� ����� ���λ����� ����� ������ ���� �ݸ�, ������(N�� ����� ū ������ �����ϱ⸦ �����ϴ� ����
Qa[10] = ' ����11a ���� �������̴�. '
Qb[10] = ' ����11b ���� �̷��������̴�. '

# Q12 ��������    S(����), N(����) �˻� 
Qa[11] = ' ����12a ���� �������� �Ǵ��Ѵ�. '
Qb[11] = ' ����12b ���� �������� �������� �Ǵ��Ѵ�. '

# Q13 ��������    S(����), N(����) �˻� 
Qa[12] = ' ����13a ���� ����� ���縦 �� �Ѵ�. '
Qb[12] = ' ����13b ���� �߻��� ǥ���� �� �Ѵ�. '

# Q14 ��������     S(����), N(����) �˻� 
Qa[13] = ' ����14a ���� ��ü���̴�. '
Qb[13] = ' ����14b ���� �������̴�. '

# Q15 ��������     S(����), N(����) �˻� 
Qa[14] = ' ����15a ���� ������̴�. '
Qb[14] = ' ����15b ���� â�����̴�. '

# Q16 ��������    S(����), N(����) �˻� 
Qa[15] = ' ����16a ���� ���� ��� ���� ���� ���ϴ�.  '
Qb[15] = ' ����16b ���� ���ο� ���� ��մ�.  '

# Q17 ��������     S(����), N(����) �˻� 
Qa[16] = ' ����17a ���� �ߴ� ���� ���ϴ�. '
Qb[16] = ' ����17b ���� ���ο� ���� ����ִ�. '

# Q18 ��������   S(����), N(����) �˻� 
Qa[17] = ' ����18a ���� �൵�� ��ü������ �׸���. '
Qb[17] = ' ����18b ���� �൵�� ��ü������ �׸��� ��ƴ�. '

# Q19 ��������   S(����), N(����) �˻� 
Qa[18] = ' ����19a ���� �Ĳ��� ���̴�. '
Qb[18] = ' ����19b ���� �����ϴ� ���̴�.  '

# Q20 ��������     S(����), N(����) �˻� 
Qa[19] = ' ����20a ���� ���� ������ �����Ѵ�. '
Qb[19] = ' ����20b ���� ������ �����Ѵ�. '

# Q21 ��������  T(���) F(����) �˻�  �����(T)�� ����� � ���� �����̰� ���������� �Ǵ��ϱ⸦ ���ϴ� �ݸ�,������(F)�� ����� ���� �ְ����� ���� ������ � ������ �����⸦ ��ȣ
Qa[20] = ' ����21a ���� �м����̴�. '
Qb[20] = ' ����21b ���� �������� ǳ���ϴ�. '

# Q22 ��������  T(���) F(����) �˻� 
Qa[21] = ' ����22a ���� �������̴�. '
Qb[21] = ' ����22b ���� �������̴�. '

# Q23 ��������   T(���) F(����) �˻� 
Qa[22] = ' ����23a ���� ������ ġ��ġ�� �ʰ� �ǻ�����Ѵ�.. '
Qb[22] = ' ����23b ���� ��Ȳ�� �����ϸ� �ǻ�����Ѵ�. '

# Q24 ��������   T(���) F(����) �˻� 
Qa[23] = ' ����24a ���� �̼��� ���� �ൿ�Ѵ�. '
Qb[23] = ' ����24b ���� ��ġ���� ��� �߽����� �ൿ�Ѵ�. '

# Q25 ��������  T(���) F(����) �˻� 
Qa[24] = ' ����25a ���� �ɷ��ִٴ� �Ҹ��� ��� �����Ѵ�. '
Qb[24] = ' ����25b ���� �����ϴٴ� �Ҹ��� ��� �����Ѵ�. '

# Q26 ��������  T(���) F(����) �˻� 
Qa[25] = ' ����26a ���� �����Ѵ�. '
Qb[25] = ' ����26b ���� �纸�Ѵ�. '

# Q27 ��������  T(���) F(����) �˻� 
Qa[26] = ' ����27a ���� �������� ���� ���ϴ�. '
Qb[26] = ' ����27b ���� ����ϴ� ���� ���ϴ�. '

# Q28 ��������   T(���) F(����) �˻� 
Qa[27] = ' ����28a ���� ����� ���ΰ� ����� ���� �ľ��Ѵ�.  '
Qb[27] = ' ����28b ���� ����� ����� ���� �ľ��Ѵ�.  '

# Q29 ��������   T(���) F(����) �˻� 
Qa[28] = ' ����29a ���� ������� ���� �����ٰ� ������ ���̴�. '
Qb[28] = ' ����29b ���� ������� ���� �����ϴٰ� �ϴ� ���̴�. '

# Q30 ��������  T(���) F(����) �˻� 
Qa[29] = ' ����30a ���� �� ���� �Ѵ�. '
Qb[29] = ' ����30b ���� ���� �����ϴ� ���̴�. '

# Q31 ��������   J(�Ǵ�), P(�ν�) �˻�  �Ǵ� ������(J)�� ����� ��ȣ�ϰ� Ȯ���� ��ǥ�� ���� ���� �����ϱ⸦ �����ϸ�,�ν� ������(P)�� ����� ���뼺�� �ְ�, ���� ���� ������ ����� �ϴ� ����
Qa[30] = ' ����31a ���� ������ ���ؼ� �� �������� �ʴ� ���̴�. '
Qb[30] = ' ����31b ���� ������ ���ؼ� ���뼺�� �ִ� ���̴�. '

# Q32 ��������   J(�Ǵ�), P(�ν�) �˻�
Qa[31] = ' ����32a ���� ��ȹ�� ���ؼ� ���� ó���ϴ� ���̴�. '
Qb[31] = ' ����32b ���� �������� �ӹ����� ���� ���� ó���ϴ� ���̴�. '

# Q33 ��������  J(�Ǵ�), P(�ν�) �˻�
Qa[32] = ' ����33a ���� ��ȹ�� ������ ���ϴ�.'
Qb[32] = ' ����33b ���� ���ڱ� ������ ������ ���ϴ�. '

# Q34 ��������   J(�Ǵ�), P(�ν�) �˻�
Qa[33] = ' ����34a ���� ���������� ���� �ϴ� ���̴�. '
Qb[33] = ' ����34b ���� �� ��Ƽ� �����ϴ� ���̴�. '

# Q35 ��������    J(�Ǵ�), P(�ν�) �˻�
Qa[34] = ' ����35a ���� �������� �����⿡ ���� �� �ȴ�. '
Qb[34] = ' ����35b ���� ��ſ� �����⿡ ���� �� �ȴ�. '

# Q36 ��������  J(�Ǵ�), P(�ν�) �˻�
Qa[35] = ' ����36a ���� ��ȹ���̰� �������̴�.  '
Qb[35] = ' ����36b ���� ���� ���߷��� �ϴ´�. '

# Q37 ��������   J(�Ǵ�), P(�ν�) �˻�
Qa[36] = ' ����37a ���� �Թ��� �����Ѵ�. '
Qb[36] = ' ����37b ���� �����ο� ���� �����Ѵ�. '

# Q38 ��������  J(�Ǵ�), P(�ν�) �˻�
Qa[37] = ' ����38a ���� �� �� �� ģ������. '
Qb[37] = ' ����38b ���� �� �� ģ������. '

# Q39 ��������  J(�Ǵ�), P(�ν�) �˻�
Qa[38] = ' ����39a �� å���� ������ �� �Ǿ� �ִ�.  '
Qb[38] = ' ����39b �� å���� ����ϰ� �Ǿ� �ִ�. '

# Q40 ��������  J(�Ǵ�), P(�ν�) �˻�
Qa[39] = ' ����40a ������ �� �� ���� ���� ���̴�. '
Qb[39] = ' ����40b ������ �� �� ���� �ʰ� �׳� ���� ���̴�.'

radioBtnA = []
radioBtnB = []

def radioCall():
    done = True
    for i in range(Qnum):
        answer = radioVar[i].get()
        if answer == 0:            
            done = False            
            break
            
    if done == False:
        win.title( name.get() + "��" + "��� �˻��ϼ���. ")
    else :
        win.title( name.get() + "��" + "�˻簡 �Ϸ�Ǿ����ϴ�. ")
        msg.showinfo( '�Ϸ�', '��� ���ϼ̽��ϴ�. ��� ���������� ����� Ȯ���ϼ���.')
        showResult()

for i in range(Qnum):
    radioBtnA.append( tk.Radiobutton(pageLF[i], text= Qa[i], variable=radioVar[i], value=(i+1)*10+1, command=radioCall ) )
    radioBtnA[i].grid(column=0, row=0, sticky=tk.W)
    radioBtnB.append( tk.Radiobutton(pageLF[i], text= Qb[i], variable=radioVar[i], value=(i+1)*10+2, command=radioCall ) )
    radioBtnB[i].grid(column=0, row=1, sticky=tk.W)

       
# Using a scrolled Text control    
scrol_w  = 80
scrol_h  = 40

scr = scrolledtext.ScrolledText(page5, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, sticky='WE', columnspan=3)   

MBTI_result = ''

def showResult():
    global R1a_score
    global R2a_score
    global R3a_score
    global R4a_score
    
    global R1b_score
    global R2b_score
    global R3b_score
    global R4b_score
    
    R1a_score = 0
    R2a_score = 0
    R3a_score = 0
    R4a_score = 0
    
    R1b_score = 0
    R2b_score = 0
    R3b_score = 0
    R4b_score = 0
    
    for i in range(Qnum):
        r = radioVar[i].get()
        
        if r==11 or  r==21 or r==31 or r==41 or r==51 or r==61 or r==71 or r==81 or r==91 :
            R1a_score += 1
        elif r==12 or  r==22 or r==32 or r==42 or r==52 or r==62 or r==72 or r==82 or r==92 :
            R1b_score += 1
           
        elif r==111 or  r==121 or r==131 or r==141 or r==151 or r==161 or r==171 or r==181 or r==191 :
            R2a_score += 1
        elif r==112 or  r==122 or r==132 or r==142 or r==152 or r==162 or r==172 or r==182 or r==192  :
            R2b_score += 1

        elif r==211 or  r==221 or r==231 or r==241 or r==251 or r==261 or r==271 or r==281 or r==291 :
            R3a_score += 1
        elif r==212 or  r==222 or r==232 or r==242 or r==252 or r==262 or r==272 or r==282 or r==292 :
            R3b_score += 1

        elif r==311 or  r==321 or r==331 or r==341 or r==351 or r==361 or r==371 or r==381 or r==391 :
            R4a_score += 1
        elif r==312 or  r==322 or r==332 or r==342 or r==352 or r==362 or r==372 or r==382 or r==392 :
            R4b_score += 1

# Q1  : E,  I    Q2 :  S, N     Q3 :  T, F      Q4 : J, P  
            
    global scr
    
    text = 'R1 E(���� extroversion ) : '+  str(R1a_score) + '   R1 I(���� introversion ) : ' + str(R1b_score) + '  '
    print (text)
    scr.insert(tk.INSERT, text )
    
    text = 'R2 S(���� sensing) : '+  str(R2a_score) + '   R2 N(����intuition) : ' + str(R2b_score) + '  '
    print (text)
    scr.insert(tk.INSERT, text )
    
    text = 'R3 T(��� thinking) : '+  str(R3a_score) + '   R3 F(���� feeling) : ' + str(R3b_score) + '  '
    print (text)
    scr.insert(tk.INSERT, text )
    
    text = 'R4 J(�Ǵ� judging) : '+  str(R4a_score) + '   R4 P(�ν� perceiving) : ' + str(R4b_score) + '  '
    print (text)
    scr.insert(tk.INSERT, text )
    
    global MBTI_result 
    
    global intention
    
    global  p
    
    intention =0 
    
    MBTI_result = ''
    
    if R1a_score > R1b_score :
        intention += R1a_score
        MBTI_result += 'E'
    elif R1a_score == R1b_score :
        MBTI_result += 'E(I)'
    else :
        intention += R1b_score
        MBTI_result += 'I'
        
    if R2a_score > R2b_score :
        intention += R2a_score
        MBTI_result += 'S'
    elif R2a_score == R2b_score :
        MBTI_result += 'S(N)'
    else :
        intention += R2b_score    
        MBTI_result += 'N'

    if R3a_score > R3b_score :
        intention += R3a_score        
        MBTI_result += 'T'
    elif R3a_score == R3b_score :
        MBTI_result += 'T(F)'        
    else :
        intention += R3b_score       
        MBTI_result += 'F'
        
    if R4a_score > R4b_score :
        intention += R4a_score       
        MBTI_result += 'J'
    elif R3a_score == R3b_score :
        MBTI_result += 'J(P)' 
    else :
        intention += R4b_score
        MBTI_result += 'P'

    
    p = int(intention / 36 *100)
     
    text = 'MBTI  result : '+  MBTI_result + ' (' + str(p) +'%)'
    scr.insert(tk.INSERT, text ) 
    print (text)
    
    
#======================
# Start GUI
#======================
win.mainloop()