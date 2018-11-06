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
page0.grid(column=0, row=0, padx=8, pady=4)

page1 = ttk.LabelFrame(tab1, text=' �˻� Page1 ')
page1.grid(column=0, row=0, padx=8, pady=4)

page2 = ttk.LabelFrame(tab2, text=' �˻� Page2 ')
page2.grid(column=0, row=0, padx=8, pady=4)

page3 = ttk.LabelFrame(tab3, text=' �˻� Page3 ')
page3.grid(column=0, row=0, padx=8, pady=4)

page4 = ttk.LabelFrame(tab4, text=' �˻� Page4 ')
page4.grid(column=0, row=0, padx=8, pady=4)

page5 = ttk.LabelFrame(tab5, text=' �˻� ��� ')
page5.grid(column=0, row=0, padx=8, pady=4)


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
Qa[14] = ' ����15a �������� ������ �����ɷ��� �ִ�. '
Qb[14] = ' ����15b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q16 ��������
Qa[15] = ' ����16a �������� ������ �����ɷ��� �ִ�. '
Qb[15] = ' ����16b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q17 ��������
Qa[16] = ' ����17a �������� ������ �����ɷ��� �ִ�. '
Qb[16] = ' ����17b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q18 ��������
Qa[17] = ' ����18a �������� ������ �����ɷ��� �ִ�. '
Qb[17] = ' ����18b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q19 ��������
Qa[18] = ' ����19a �������� ������ �����ɷ��� �ִ�. '
Qb[18] = ' ����19b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q20 ��������
Qa[19] = ' ����20a �������� ������ �����ɷ��� �ִ�. '
Qb[19] = ' ����20b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q21 ��������
Qa[20] = ' ����21a �������� ������ �����ɷ��� �ִ�. '
Qb[20] = ' ����21b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q22 ��������
Qa[21] = ' ����22a �������� ������ �����ɷ��� �ִ�. '
Qb[21] = ' ����22b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q23 ��������
Qa[22] = ' ����23a �������� ������ �����ɷ��� �ִ�. '
Qb[22] = ' ����23b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q24 ��������
Qa[23] = ' ����24a �������� ������ �����ɷ��� �ִ�. '
Qb[23] = ' ����24b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q25 ��������
Qa[24] = ' ����25a �������� ������ �����ɷ��� �ִ�. '
Qb[24] = ' ����25b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q26 ��������
Qa[25] = ' ����26a �������� ������ �����ɷ��� �ִ�. '
Qb[25] = ' ����26b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q27 ��������
Qa[26] = ' ����27a �������� ������ �����ɷ��� �ִ�. '
Qb[26] = ' ����27b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q28 ��������
Qa[27] = ' ����28a �������� ������ �����ɷ��� �ִ�. '
Qb[27] = ' ����28b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q29 ��������
Qa[28] = ' ����29a �������� ������ �����ɷ��� �ִ�. '
Qb[28] = ' ����29b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q30 ��������
Qa[29] = ' ����30a �������� ������ �����ɷ��� �ִ�. '
Qb[29] = ' ����30b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q31 ��������
Qa[30] = ' ����31a �������� ������ �����ɷ��� �ִ�. '
Qb[30] = ' ����31b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q32 ��������
Qa[31] = ' ����32a �������� ������ �����ɷ��� �ִ�. '
Qb[31] = ' ����32b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q33 ��������
Qa[32] = ' ����33a �������� ������ �����ɷ��� �ִ�. '
Qb[32] = ' ����33b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q34 ��������
Qa[33] = ' ����34a �������� ������ �����ɷ��� �ִ�. '
Qb[33] = ' ����34b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q35 ��������
Qa[34] = ' ����35a �������� ������ �����ɷ��� �ִ�. '
Qb[34] = ' ����35b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q36 ��������
Qa[35] = ' ����36a �������� ������ �����ɷ��� �ִ�. '
Qb[35] = ' ����36b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q37 ��������
Qa[36] = ' ����37a �������� ������ �����ɷ��� �ִ�. '
Qb[36] = ' ����37b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q38 ��������
Qa[37] = ' ����38a �������� ������ �����ɷ��� �ִ�. '
Qb[37] = ' ����38b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q39 ��������
Qa[38] = ' ����39a �������� ������ �����ɷ��� �ִ�. '
Qb[38] = ' ����39b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q40 ��������
Qa[39] = ' ����40a �������� ������ �����ɷ��� �ִ�. '
Qb[39] = ' ����40b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q41 ��������
Qa[40] = ' ����41a �������� ������ �����ɷ��� �ִ�. '
Qb[40] = ' ����41b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q42 ��������
Qa[41] = ' ����42a �������� ������ �����ɷ��� �ִ�. '
Qb[41] = ' ����42b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q43 ��������
Qa[42] = ' ����43a �������� ������ �����ɷ��� �ִ�. '
Qb[42] = ' ����43b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q44 ��������
Qa[43] = ' ����44a �������� ������ �����ɷ��� �ִ�. '
Qb[43] = ' ����44b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q45 ��������
Qa[44] = ' ����45a �������� ������ �����ɷ��� �ִ�. '
Qb[44] = ' ����45b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q46 ��������
Qa[45] = ' ����46a �������� ������ �����ɷ��� �ִ�. '
Qb[45] = ' ����46b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q47 ��������
Qa[46] = ' ����47a �������� ������ �����ɷ��� �ִ�. '
Qb[46] = ' ����47b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '

# Q48 ��������
Qa[47] = ' ����48a �������� ������ �����ɷ��� �ִ�. '
Qb[47] = ' ����48b �� �ڽ��� �����ϸ� ��ܼ��� �ְ� ���ϴ�. '   


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
    
for i in range(Qnum):
    radioBtnA.append( tk.Radiobutton(pageLF[i], text= Qa[i], variable=radioVar[i], value=(i+1)*10+1, command=radioCall ) )
    radioBtnA[i].grid(column=0, row=0, sticky=tk.W)
    radioBtnB.append( tk.Radiobutton(pageLF[i], text= Qb[i], variable=radioVar[i], value=(i+1)*10+2, command=radioCall ) )
    radioBtnB[i].grid(column=0, row=1, sticky=tk.W)

def _msgBox():
    msg.showinfo(' ��� �����ؾ� �˴ϴ�. �ٽ� �ϼ���. ') 
    
# Tab Control 2 refactoring  ---------------------------------------------------------

# We are creating a container frame to hold all other widgets -- Tab2
page2 = ttk.LabelFrame(tab2, text=' Page 2 ')
page2.grid(column=0, row=0, padx=8, pady=4)

# Using a scrolled Text control    
scrol_w  = 80
scrol_h  = 40
scr = scrolledtext.ScrolledText(page5, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, sticky='WE', columnspan=3)   

#======================
# Start GUI
#======================
win.mainloop()
