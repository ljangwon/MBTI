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
Qnum = 48

for i in range(Qnum):
    radioVar.append( tk.IntVar() )

# Questions LabelFrame 
pageLF = []

for i in range(Qnum):
    if 0<= i <= 11 :
        pageLF.append( ttk.LabelFrame(page1) )
        pageLF[i].grid(column=0, row=i, sticky='WE')
    elif 12<= i <= 23 :
        pageLF.append( ttk.LabelFrame(page2) )
        pageLF[i].grid(column=0, row=i-12, sticky='WE')
    elif 24<= i <= 35 :            
        pageLF.append( ttk.LabelFrame(page3) )
        pageLF[i].grid(column=0, row=i-24, sticky='WE')
    elif 36<= i <= 47 :
        pageLF.append( ttk.LabelFrame(page4) )
        pageLF[i].grid(column=0, row=i-36, sticky='WE')    
 
Qa = []
Qb = []
for i in range(Qnum):
    Qa.append( '' )    
for i in range(Qnum):
    Qb.append( '' )    


# Q1 ��������
Qa[0] = ' ����1a ���� �ൿ�� �����ϰ� Ȱ���� �ൿ�� �����Ѵ�. '
Qb[0] = ' ����1a ���� ������ �����ϰ� ���� �������� �����Ѵ�. '

# Q2 ��������
Qa[1] = ' ����2a �Ϲ����� ������ ���� ���ο� ���� ����. '
Qb[1] = ' ����2b ���� ������ ���� ���ο� ����� ����. '

# Q3 ��������
Qa[2] = ' ����3a ���� ������ ��ǥ�� ��´�. ���� �̼����� �� ������ ������. '
Qb[2] = ' ����3b ���� ��ȭ�� ��ǥ�� ��´�. ���� �������� �� ������ ������. '

# Q4 ��������
Qa[3] = ' ����4a ���� �λ��� ������ �� �ֱ⸦ ���ϸ� � �����̵� �ϱ� ���Ѵ�. '
Qb[3] = ' ����4b ���� �λ��� �����Ǿ� �ְ� �λ��� ���� ������ �ݿ��ϴ� ���� ��ȣ�Ѵ�. '

# Q5 ��������
Qa[4] = ' ����5a ���� ���ǰ� �길������. '
Qb[4] = ' ����5b ������ �� �Ѵ�. '

# Q6 ��������
Qa[5] = ' ����6a �������� �Ͱ� �̹� ģ���� �͵��� ������ �����ϸ� ����. '
Qb[5] = ' ����6b ���ο� �Ͱ� ���ٸ� ������� ������ �����ϸ� ����.. '

# Q7 ��������
Qa[6] = ' ����7a ���ո����� ���� �ݹ� �˾Ƴ���. '
Qb[6] = ' ����7b ������� ���� ������ �ʿ�� �ϴ��� �ݹ� �˾Ƴ��� '

# Q8 ��������
Qa[7] = ' ����8a ���� �� � �͵� ��ġ�� �ʵ��� ���� ���� ������ �� ���뼺 �ְ� �����Ѵ�. '
Qb[7] = ' ����8b ���� ��ȹ�� ������� ������ ���� ���Ͽ� ���Ѵ�.. '

# Q9 ��������
Qa[8] = ' ����9a ȥ�� ���� �� �ִ� ������ ������ ����. '
Qb[8] = ' ����9b ���� �ϵ��� ����� �������� ������ ����. '

# Q10 ��������
Qa[9] = ' ����10a ������ ǳ���� �ൿ�� �Ѵ�. '
Qb[9] = ' ����10b ���������� �ൿ�Ѵ�. '

# Q11 ��������
Qa[10] = ' ����11a ������ ��Ģ�� ���� ���󸸻簡 �̷�����⸦ ����Ѵ�. '
Qb[10] = ' ����11b ������ �������� ������ �ֱ⸦ ����Ѵ�. '

# Q12 ��������
Qa[11] = ' ����12a �������� ������ �����ɷ��� �ִ�. '
Qb[11] = ' ����12b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q13 ��������
Qa[12] = ' ����13a �ܺ��� ����̳� ������ �����ϱ� ���� ������ �ð��� ���´�. '
Qb[12] = ' ����13b �ܺ��� ����̳� ������ ���Ͽ� �ż��ϰ� �����Ѵ�. '

# Q14 ��������
Qa[13] = ' ����14a �ڷᰡ �����ϰ� �ִ� ������ �̷��� ��ȸ���� �˰� �;� �Ѵ�. '
Qb[13] = ' ����14b �ڷ��� �������̰� �������� ������ �˰� �;� �Ѵ�. '

# Q15 ��������
Qa[14] = ' ����15a �米���̰� ģ�ٰ��� �ְ� ���� ���δ� �ð� ���������� �̾߱⸦ ������. '
Qb[14] = ' ����15b ª�� ���� �ǻ������ ��ȣ�Ѵ�. '

# Q16 ��������
Qa[15] = ' ����16a ��ȭ�� ���ɼ��� �����ϸ鼭 ������ �ӽ����� ������ �����Ѵ�. '
Qb[15] = ' ����16b ��Ȯ�ϰ� ����ϸ鼭 ����� ������ ���� �ܾ��� ������. '

# Q17 ��������
Qa[16] = ' ����17a ���� Ȥ�� ���� �´�� �ǻ�����ϱ⺸�ٴ� �۷� �ϴ� ���� �� ��ȣ�Ѵ�. '
Qb[16] = ' ����17b �۷� �ǻ縦 �����ϱ⺸�ٴ� ���� �´�� ���� �ϴ� ���� �� ��ȣ�Ѵ�. '

# Q18 ��������
Qa[17] = ' ����18a �켱������ ���� ������ ����, �������� �����Ѵ�. '
Qb[17] = ' ����18b �켱������ ���� ���� ����, ���, ���λ��� �׸��� ��ʵ��� �����Ѵ�. '

# Q19 ��������
Qa[18] = ' ����19a �ٸ� ������� ������ ����. '
Qb[18] = ' ����19b �ٸ� ������� ������ ����. '

# Q20 ��������
Qa[19] = ' ����20a ����� ������������ �ǻ������ �Ѵ�. '
Qb[19] = ' ����20b ���ü��� �쿬���� �����ϴ� �ǻ������ �Ѵ�. '

# Q21 ��������
Qa[20] = ' ����21a �������� �������� ���� ���Ѵ�. '
Qb[20] = ' ����21b �������� �������� �̾߱��ϱ⸦ �����δ�. '

# Q22 ��������
Qa[21] = ' ����22a �����Ӱ� ������ ���߸� ����Ѵ�. '
Qb[21] = ' ����22b �������� ������ ����ϰ� ����Ѵ�. '

# Q23 ��������
Qa[22] = ' ����23a �����̰� �������� ����� �����ؾ� �� �ڷ�� �ν��Ѵ�. '
Qb[22] = ' ����23b ������� ������ �������� �����ؾ� �� �ڷ�� �ν��Ѵ�. '

# Q24 ��������
Qa[23] = ' ����24a ���ӿ��� �������� ����� �������� �ʴ´�. '
Qb[23] = ' ����24b ���ӿ��� ����� ����� ���� �Ϳ� ���� ������ ���� �ʴ´�. '

# Q25 ��������
Qa[24] = ' ����25a ���ο� �ΰ����踦 ������ �� ���ɼ��� ���δ�. '
Qb[24] = ' ����25b ���ο� �ΰ����踦 ���� �����ϸ� ���ɼ��� ���� ������ �ʴ´�. '

# Q26 ��������
Qa[25] = ' ����26a ���� �ΰ����迡 ���� �������� �����ν� ���� ���ɼ��� �߱��Ѵ�. '
Qb[25] = ' ����26b ���� �ΰ����迡 �־ ��ȭ�� �������� �߿伺�� ������ ������ ���Ѵ�. '

# Q27 ��������
Qa[26] = ' ����27a �ΰ����迡 ���� ������ ������ �Ը��Ѵ�. '
Qb[26] = ' ����27b �ΰ����迡 ���� ���� �������� ������ �Ը��Ѵ�. '

# Q28 ��������
Qa[27] = ' ����28a �� ������� ���迡�� ������ �Ͼ ���� ������ �ٷ��. '
Qb[27] = ' ����28b �� ������� ���迡 ���� ������ �ٷ�� ���� �ñ⸦ ���� ���⸦ ���Ѵ�. '

# Q29 ��������
Qa[28] = ' ����29a ���� ���� ģ����� ������ ������ ���� �����Ѵ�. '
Qb[28] = ' ����29b ���� ���� ģ����� ���� ���踦 �α⸦ �����Ѵ�. '

# Q30 ��������
Qa[29] = ' ����30a �̻����� ���迡 ���� ���ϸ��� �ٸ� ������ �����Ѵ�. '
Qb[29] = ' ����30b ���ϸ��� �ٱ�� �ϳ�, ���迡�� ��Ÿ���� ������ �˰� �ִ�. '

# Q31 ��������
Qa[30] = ' ����31a ���� ������ ���� �������� ���� �ൿ�� ���� ǥ���Ѵ�. '
Qb[30] = ' ����31b ���� ������ ���� ������ ������ ���·� ǥ���Ѵ�. '

# Q32 ��������
Qa[31] = ' ����32a �米���� ������ ������ ������ Ȱ������ �ؾ� �� �������� ������. '
Qb[31] = ' ����32b �米���� ������ ������ ������ Ȱ���鿡 ������ �� ������. '

# Q33 ��������
Qa[32] = ' ����33a ���� �������� ������ �ð��� ���� �ٸ� ������ ������. '
Qb[32] = ' ����33b ���� �������� ������ ���� ������ �ð��� �ʿ�� �Ѵ� '

# Q34 ��������
Qa[33] = ' ����34a ���迡 �־ ��Ȯ�� ���Ұ� ��븦 ���ϰ� �ִ�. '
Qb[33] = ' ����34b �����̳� ��� ���� ������ Ÿ���� ������ ������ �ϴ´�. '

# Q35 ��������
Qa[34] = ' ����35a ���� �ΰ����踦 �ջ��ų ���� �ִ� �������� ���κ��� ȸ���Ѵ�. '
Qb[34] = ' ����35b ���� �ΰ����迡 ������ �� ���� ������ �������� �����Ѵ�. '

# Q36 ��������
Qa[35] = ' ����36a �Բ� �������ν� ���� �ΰ����踦 �����Ѵٰ� �����Ѵ�. '
Qb[35] = ' ����36b ������ ���� �ΰ����踦 ħ���ϴ� ������ �����Ѵ�. '

# Q37 ��������
Qa[36] = ' ����37a ������ �� �ִ� �������� �߱��Ѵ�. '
Qb[36] = ' ����37b �ൿ �������� �پ��� ������ �߱��Ѵ�. '

# Q38 ��������
Qa[37] = ' ����38a ������ ���� ���� �۾������� ��Ÿ���� �ͺ��ٴ� �� �ٸ��� ���� �Ѵ�. '
Qb[37] = ' ����38b ������ ���� ������ �۾� ������ Ȱ���Ѵ�. '

# Q39 ��������
Qa[38] = ' ����39a ���� ������ �⺻���� ���� �м��� ����Ѵ�. '
Qb[38] = ' ����39b ������ �⺻���� ������ ��ġ���ص�� ���Ҿ� �ٸ� ����� ���ص� ���Խ�Ų��. '

# Q40 ��������
Qa[39] = ' ����40a �ҽÿ� ����� ������ ó���� �� ���� ���� �ּ��� ���Ѵ�. '
Qb[39] = ' ����40b ���� ���� ��ȹ�� �� �ְ� ��ȹ�ϴ� ���� �� �� ���� ���� �ּ��� ���Ѵ�. '

# Q41 ��������
Qa[40] = ' ����41a �ɻ���� ���� ���� ������ ������Ų��. '
Qb[40] = ' ����41b ���Ǹ� ���� ���� ������ ������Ų��. '

# Q42 ��������
Qa[41] = ' ����42a ���ο� ����� ������ �ϱ⺸�ٴ� �̹� �˰� �ִ� ������ ����� �����Ѵ�. '
Qb[41] = ' ����42b �����̳� ���Ű� ���õǴ� ���ο� ����� ���� ���� ����. '

# Q43 ��������
Qa[42] = ' ����43a �ٸ� ������� �����ϰ� �ٷ�� �����Ѵ�. '
Qb[42] = ' ����43b �ٸ� ������ �����ϸ鼭 �׵�� �����ϰ� �����Ѵ�. '

# Q44 ��������
Qa[43] = ' ����44a �� ���� ������ �����ϱ� ���� ������ �����̴� ���� �ź��Ѵ�. '
Qb[43] = ' ����44b ���ɼ��� ����ϰ� ����, �ϴ� ������ ������ �����Ѵ�. '

# Q45 ��������
Qa[44] = ' ����45a ���� ���࿡ ���� ��ȭ�� �ʿ��ϸ� �ܺ� ��ǵ��� ã�ƴٴѴ�. '
Qb[44] = ' ����45b ���� �Ͽ� �����ϰ� �ܺ� ��ǵ��� ���߿� ����. '

# Q46 ��������
Qa[45] = ' ����46a �繰���� ��ü������ ����ϴ� ���� �����Ѵ�. '
Qb[45] = ' ����46b �繰�� �Ϲ������� ����ϴ� ���� �����Ѵ�. '

# Q47 ��������
Qa[46] = ' ����47a ������ �ִ��� ȿ�������� �س��� ���� ��ȭ�� �ʿ�� �Ѵ�. '
Qb[46] = ' ����47b ��ȭ���� �ʾƵ� �� ���� �� ������ ������ ������ ȿ�������� �� �� ����. '

# Q48 ��������
Qa[47] = ' ����48a �ż��ϰ� �����ϰ� �����Ϸ� �Ѵ�. '
Qb[47] = ' ����48b ������ �̷�� ���ɼ��� ã�´�. '   


radioBtnA = []
radioBtnB = []

def radioCall():
    done = True
    for i in range(Qnum):
        answer = radioVar[i].get()
        print( i+1)
        print( ':' ) 
        print( answer )
        if answer == 0:            
            done = False            
            break
            
    if done == False:
        print( '��� ������ �� �ϼ���.')
    else :
        msg.showinfo( '�Ϸ�', '��� ���ϼ̽��ϴ�. ���� �������� �Ѿ����.')
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

R1a_score = 0
R2a_score = 0
R3a_score = 0
R4a_score = 0

R1b_score = 0
R2b_score = 0
R3b_score = 0
R4b_score = 0

def showResult():
    global R1a_score
    global R2a_score
    global R3a_score
    global R4a_score
    
    global R1b_score
    global R2b_score
    global R3b_score
    global R4b_score
        
    for i in range(Qnum):
        r = radioVar[i].get()
        if r == 11 or r == 21 or r == 32 or r == 41:
            R1a_score += 1
        elif r == 12 or r == 22 or r == 31 or r == 42:
            R1b_score += 1
            
    global scr
    scr.insert(tk.INSERT, 'R1 A : '+  str(R1a_score) + '   R1 B : ' + str(R1b_score) + '  ')
    scr.insert(tk.INSERT, 'R2 A : '+  str(R2a_score) + '   R2 B : ' + str(R2b_score) + '  ')
    scr.insert(tk.INSERT, 'R3 A : '+  str(R3a_score) + '   R3 B : ' + str(R3b_score) + '  ')
    scr.insert(tk.INSERT, 'R4 A : '+  str(R4a_score) + '   R4 B : ' + str(R4b_score) + '                      ')
    
#======================
# Start GUI
#======================
win.mainloop()