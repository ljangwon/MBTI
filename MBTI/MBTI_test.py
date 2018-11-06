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
win.title("MBTI 검사1")

tabControl = ttk.Notebook(win)    # Create Tab Control

# Tab Control 0 refactoring  ---------------------------------------------------------
tab0 = ttk.Frame(tabControl)
tabControl.add(tab0, text=' 인적사항 ')
tab1 = ttk.Frame(tabControl)            
tabControl.add(tab1, text='Page 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Page 2')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Page 3')
tab4 = ttk.Frame(tabControl)
tabControl.add(tab4, text='Page 4')
tab5 = ttk.Frame(tabControl)
tabControl.add(tab5, text='결과')
tabControl.pack(expand=1, fill="both")  # Pack to make visible

# LabelFrame using tab0 as the parent
page0 = ttk.LabelFrame(tab0, text=' 인적사항 ')
page0.grid(column=0, row=0, padx=8, pady=4)

page1 = ttk.LabelFrame(tab1, text=' 검사 Page1 ')
page1.grid(column=0, row=0, padx=8, pady=4)

page2 = ttk.LabelFrame(tab2, text=' 검사 Page2 ')
page2.grid(column=0, row=0, padx=8, pady=4)

page3 = ttk.LabelFrame(tab3, text=' 검사 Page3 ')
page3.grid(column=0, row=0, padx=8, pady=4)

page4 = ttk.LabelFrame(tab4, text=' 검사 Page4 ')
page4.grid(column=0, row=0, padx=8, pady=4)

page5 = ttk.LabelFrame(tab5, text=' 검사 결과 ')
page5.grid(column=0, row=0, padx=8, pady=4)


# Modify adding a Label using mighty as the parent instead of win
a_label = ttk.Label(page0, text="입력하세요 이름:")
a_label.grid(column=0, row=0, sticky='W')

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(page0, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')               # align left/West

# Modified Button Click Function
def click_me(): 
    start_label.configure(text='Hello ' + name.get() + ' ' + 
                     grade_chosen.get() + ' Now MBTI Start ... ')
    win.title( "MBTI 검사  "+ name.get() + " 진행중 ")
# Adding a Button
start_button = ttk.Button(page0, text=' 검사시작! ', command=click_me)   
start_button.grid(column=2, row=1)                                

ttk.Label(page0, text="선택하세요 학년:").grid(column=1, row=0)
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

# Q1 질문내용
Qa[0] = ' 질문1a 나는 행동에 집착하고 활동과 행동을 지향한다. '
Qb[0] = ' 질문1a 나는 생각에 집착하고 사고와 생각들을 지향한다. '

# Q2 질문내용
Qa[1] = ' 질문2a 일반적인 개념을 통해 새로운 것을 배운다. '
Qb[1] = ' 질문2b 모방과 관찰을 통해 새로운 사실을 배운다. '

# Q3 질문내용
Qa[2] = ' 질문3a 나는 진실을 목표로 삼는다. 나의 이성으로 더 결정을 내린다. '
Qb[2] = ' 질문3b 나는 조화를 목표로 삼는다. 나의 감정으로 더 결정을 내린다. '

# Q4 질문내용
Qa[3] = ' 질문4a 나의 인생에 적응할 수 있기를 원하며 어떤 경험이든 하길 원한다. '
Qb[3] = ' 질문4b 나의 인생이 결정되어 있고 인생에 나의 의지를 반영하는 것을 선호한다. '

# Q5 질문내용
Qa[4] = ' 질문5a 쉽게 주의가 산만해진다. '
Qb[4] = ' 질문5b 집중을 잘 한다. '

# Q6 질문내용
Qa[5] = ' 질문6a 전통적인 것과 이미 친숙한 것들의 진가를 인정하며 즐긴다. '
Qb[5] = ' 질문6b 새로운 것과 남다른 경험들의 진가를 인정하며 즐긴다.. '

# Q7 질문내용
Qa[6] = ' 질문7a 비합리적인 논리를 금방 알아낸다. '
Qb[6] = ' 질문7b 사람들이 언제 도움을 필요로 하는지 금방 알아낸다 '

# Q8 질문내용
Qa[7] = ' 질문8a 나는 그 어떤 것도 놓치지 않도록 나의 삶을 가능한 한 융통성 있게 유지한다. '
Qb[7] = ' 질문8b 나는 계획된 순서대로 정착된 삶을 위하여 일한다.. '

# Q9 질문내용
Qa[8] = ' 질문9a 혼자 있을 수 있는 사적인 영역을 즐긴다. '
Qb[8] = ' 질문9b 많은 일들이 생기는 대중적인 영역을 즐긴다. '

# Q10 질문내용
Qa[9] = ' 질문10a 상상력이 풍부한 행동을 한다. '
Qb[9] = ' 질문10b 실제적으로 행동한다. '

# Q11 질문내용
Qa[10] = ' 질문11a 논리적인 원칙에 따라 세상만사가 이루어지기를 기대한다. '
Qb[10] = ' 질문11b 세상이 개인차를 인정해 주기를 기대한다. '

# Q12 질문내용
Qa[11] = ' 질문12a 참을성이 있으며 적응능력이 있다. '
Qb[11] = ' 질문12b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q13 질문내용
Qa[12] = ' 질문13a 외부의 사건이나 질문에 대응하기 전에 생각할 시간을 갖는다. '
Qb[12] = ' 질문13b 외부의 사건이나 질문에 대하여 신속하게 대응한다. '

# Q14 질문내용
Qa[13] = ' 질문14a 자료가 제시하고 있는 도전과 미래의 기회들을 알고 싶어 한다. '
Qb[13] = ' 질문14b 자료의 실제적이고 현실적인 적용을 알고 싶어 한다. '

# Q15 질문내용
Qa[14] = ' 질문15a 참을성이 있으며 적응능력이 있다. '
Qb[14] = ' 질문15b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q16 질문내용
Qa[15] = ' 질문16a 참을성이 있으며 적응능력이 있다. '
Qb[15] = ' 질문16b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q17 질문내용
Qa[16] = ' 질문17a 참을성이 있으며 적응능력이 있다. '
Qb[16] = ' 질문17b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q18 질문내용
Qa[17] = ' 질문18a 참을성이 있으며 적응능력이 있다. '
Qb[17] = ' 질문18b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q19 질문내용
Qa[18] = ' 질문19a 참을성이 있으며 적응능력이 있다. '
Qb[18] = ' 질문19b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q20 질문내용
Qa[19] = ' 질문20a 참을성이 있으며 적응능력이 있다. '
Qb[19] = ' 질문20b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q21 질문내용
Qa[20] = ' 질문21a 참을성이 있으며 적응능력이 있다. '
Qb[20] = ' 질문21b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q22 질문내용
Qa[21] = ' 질문22a 참을성이 있으며 적응능력이 있다. '
Qb[21] = ' 질문22b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q23 질문내용
Qa[22] = ' 질문23a 참을성이 있으며 적응능력이 있다. '
Qb[22] = ' 질문23b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q24 질문내용
Qa[23] = ' 질문24a 참을성이 있으며 적응능력이 있다. '
Qb[23] = ' 질문24b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q25 질문내용
Qa[24] = ' 질문25a 참을성이 있으며 적응능력이 있다. '
Qb[24] = ' 질문25b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q26 질문내용
Qa[25] = ' 질문26a 참을성이 있으며 적응능력이 있다. '
Qb[25] = ' 질문26b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q27 질문내용
Qa[26] = ' 질문27a 참을성이 있으며 적응능력이 있다. '
Qb[26] = ' 질문27b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q28 질문내용
Qa[27] = ' 질문28a 참을성이 있으며 적응능력이 있다. '
Qb[27] = ' 질문28b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q29 질문내용
Qa[28] = ' 질문29a 참을성이 있으며 적응능력이 있다. '
Qb[28] = ' 질문29b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q30 질문내용
Qa[29] = ' 질문30a 참을성이 있으며 적응능력이 있다. '
Qb[29] = ' 질문30b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q31 질문내용
Qa[30] = ' 질문31a 참을성이 있으며 적응능력이 있다. '
Qb[30] = ' 질문31b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q32 질문내용
Qa[31] = ' 질문32a 참을성이 있으며 적응능력이 있다. '
Qb[31] = ' 질문32b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q33 질문내용
Qa[32] = ' 질문33a 참을성이 있으며 적응능력이 있다. '
Qb[32] = ' 질문33b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q34 질문내용
Qa[33] = ' 질문34a 참을성이 있으며 적응능력이 있다. '
Qb[33] = ' 질문34b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q35 질문내용
Qa[34] = ' 질문35a 참을성이 있으며 적응능력이 있다. '
Qb[34] = ' 질문35b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q36 질문내용
Qa[35] = ' 질문36a 참을성이 있으며 적응능력이 있다. '
Qb[35] = ' 질문36b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q37 질문내용
Qa[36] = ' 질문37a 참을성이 있으며 적응능력이 있다. '
Qb[36] = ' 질문37b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q38 질문내용
Qa[37] = ' 질문38a 참을성이 있으며 적응능력이 있다. '
Qb[37] = ' 질문38b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q39 질문내용
Qa[38] = ' 질문39a 참을성이 있으며 적응능력이 있다. '
Qb[38] = ' 질문39b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q40 질문내용
Qa[39] = ' 질문40a 참을성이 있으며 적응능력이 있다. '
Qb[39] = ' 질문40b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q41 질문내용
Qa[40] = ' 질문41a 참을성이 있으며 적응능력이 있다. '
Qb[40] = ' 질문41b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q42 질문내용
Qa[41] = ' 질문42a 참을성이 있으며 적응능력이 있다. '
Qb[41] = ' 질문42b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q43 질문내용
Qa[42] = ' 질문43a 참을성이 있으며 적응능력이 있다. '
Qb[42] = ' 질문43b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q44 질문내용
Qa[43] = ' 질문44a 참을성이 있으며 적응능력이 있다. '
Qb[43] = ' 질문44b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q45 질문내용
Qa[44] = ' 질문45a 참을성이 있으며 적응능력이 있다. '
Qb[44] = ' 질문45b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q46 질문내용
Qa[45] = ' 질문46a 참을성이 있으며 적응능력이 있다. '
Qb[45] = ' 질문46b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q47 질문내용
Qa[46] = ' 질문47a 참을성이 있으며 적응능력이 있다. '
Qb[46] = ' 질문47b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q48 질문내용
Qa[47] = ' 질문48a 참을성이 있으며 적응능력이 있다. '
Qb[47] = ' 질문48b 나 자신을 통제하며 결단성이 있고 엄하다. '   


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
        print( '계속 질문에 답 하세요.')
    else :
        msg.showinfo( '완료', '모두 답하셨습니다. 다음 페이지로 넘어가세요.')          
    
for i in range(Qnum):
    radioBtnA.append( tk.Radiobutton(pageLF[i], text= Qa[i], variable=radioVar[i], value=(i+1)*10+1, command=radioCall ) )
    radioBtnA[i].grid(column=0, row=0, sticky=tk.W)
    radioBtnB.append( tk.Radiobutton(pageLF[i], text= Qb[i], variable=radioVar[i], value=(i+1)*10+2, command=radioCall ) )
    radioBtnB[i].grid(column=0, row=1, sticky=tk.W)

def _msgBox():
    msg.showinfo(' 모두 선택해야 됩니다. 다시 하세요. ') 
    
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
