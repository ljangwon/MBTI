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
page0.grid(column=0, row=0, padx=8, pady=2)

page1 = ttk.LabelFrame(tab1, text=' 검사 Page1 ')
page1.grid(column=0, row=0, padx=8, pady=2)

page2 = ttk.LabelFrame(tab2, text=' 검사 Page2 ')
page2.grid(column=0, row=0, padx=8, pady=2)

page3 = ttk.LabelFrame(tab3, text=' 검사 Page3 ')
page3.grid(column=0, row=0, padx=8, pady=2)

page4 = ttk.LabelFrame(tab4, text=' 검사 Page4 ')
page4.grid(column=0, row=0, padx=8, pady=2)

page5 = ttk.LabelFrame(tab5, text=' 검사 결과 ')
page5.grid(column=0, row=0, padx=8, pady=2)


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

# 〈출처 : 심혜숙, 임승환 역, 성격유형과 삶의 양식〉
# Q1 질문내용  E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[0] = ' 질문1a 나는 깊게 생각하는 것보다 행동하는 것이 좋다. '  
Qb[0] = ' 질문1a 나는 행동하는 것보다 깊게 생각하는 것을 즐긴다. '

# Q2 질문내용  S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[1] = ' 질문2a 그냥 전체를 보자마자 떠오르는 생각이 좋다. '
Qb[1] = ' 질문2b 따라해보거나 자세히 관찰을 해서 새로운 사실을 배운다. '

# Q3 질문내용   T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[2] = ' 질문3a 나는 진실을 찾는게 중요하다. 나는 논리적으로 더 결정을 내린다. '
Qb[2] = ' 질문3b 나는 남들과 좋은 관계를 갖는것이 중요하다. 나는 느낌으로 더 결정을 내린다. '

# Q4 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[3] = ' 질문4a 앞으로 할 것에 대해 미리 결정해 놓기보다 어떻게 될지 모르지만 이런 저런 시도를 하면서 다양한 경험을 하길 원한다. '
Qb[3] = ' 질문4b 앞으로 할 것을 미리 결정해 놓고 잘 하기 위해 그것에만 집중하는 것을 좋아한다. '

# Q5 질문내용  E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[4] = ' 질문5a 쉽게 주의가 산만해진다. '
Qb[4] = ' 질문5b 집중을 잘 한다. '

# Q6 질문내용  S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[5] = ' 질문6a 전통적인 것과 이미 친숙한 것들의 진가를 인정하며 즐긴다. '
Qb[5] = ' 질문6b 새로운 것과 남다른 경험들의 진가를 인정하며 즐긴다.. '

# Q7 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[6] = ' 질문7a 비합리적인 논리를 금방 알아낸다. '
Qb[6] = ' 질문7b 사람들이 언제 도움을 필요로 하는지 금방 알아낸다 '

# Q8 질문내용  J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[7] = ' 질문8a 나는 그 어떤 것도 놓치지 않도록 나의 삶을 가능한 한 융통성 있게 유지한다. '
Qb[7] = ' 질문8b 나는 계획된 순서대로 정착된 삶을 위하여 일한다.. '

# Q9 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[8] = ' 질문9a 혼자 있을 수 있는 사적인 영역을 즐긴다. '
Qb[8] = ' 질문9b 많은 일들이 생기는 대중적인 영역을 즐긴다. '

# Q10 질문내용   S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[9] = ' 질문10a 상상력이 풍부한 행동을 한다. '
Qb[9] = ' 질문10b 실제적으로 행동한다. '

# Q11 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[10] = ' 질문11a 논리적인 원칙에 따라 세상만사가 이루어지기를 기대한다. '
Qb[10] = ' 질문11b 세상이 개인차를 인정해 주기를 기대한다. '

# Q12 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[11] = ' 질문12a 참을성이 있으며 적응능력이 있다. '
Qb[11] = ' 질문12b 나 자신을 통제하며 결단성이 있고 엄하다. '

# Q13 질문내용  E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[12] = ' 질문13a 외부의 사건이나 질문에 대응하기 전에 생각할 시간을 갖는다. '
Qb[12] = ' 질문13b 외부의 사건이나 질문에 대하여 신속하게 대응한다. '

# Q14 질문내용  S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[13] = ' 질문14a 자료가 제시하고 있는 도전과 미래의 기회들을 알고 싶어 한다. '
Qb[13] = ' 질문14b 자료의 실제적이고 현실적인 적용을 알고 싶어 한다. '

# Q15 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[14] = ' 질문15a 사교적이고 친근감이 있고 또한 때로는 시간 보내기형의 이야기를 나눈다. '
Qb[14] = ' 질문15b 짧고 요약된 의사소통을 선호한다. '

# Q16 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[15] = ' 질문16a 변화의 가능성을 생각하면서 입장을 임시적인 것으로 간주한다. '
Qb[15] = ' 질문16b 명확하게 언급하면서 입장과 결정에 대해 단언을 내린다. '

# Q17 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[16] = ' 질문17a 말로 혹은 얼굴을 맞대고 의사소통하기보다는 글로 하는 것을 더 선호한다. '
Qb[16] = ' 질문17b 글로 의사를 전달하기보다는 얼굴을 맞대고 말로 하는 것을 더 선호한다. '

# Q18 질문내용   S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[17] = ' 질문18a 우선적으로 나의 통찰과 개념, 생각들을 제시한다. '
Qb[17] = ' 질문18b 우선적으로 내가 지닌 증거, 사실, 세부사항 그리고 사례들을 제시한다. '

# Q19 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[18] = ' 질문19a 다른 사람들의 약점을 본다. '
Qb[18] = ' 질문19b 다른 사람들의 장점을 본다. '

# Q20 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[19] = ' 질문20a 결과와 성취지향적인 의사소통을 한다. '
Qb[19] = ' 질문20b 선택성과 우연성을 지향하는 의사소통을 한다. '

# Q21 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[20] = ' 질문21a 개인적인 정보들을 쉽게 말한다. '
Qb[20] = ' 질문21b 개인적인 정보들을 이야기하기를 망설인다. '

# Q22 질문내용  S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[21] = ' 질문22a 자유롭게 은유와 유추를 사용한다. '
Qb[21] = ' 질문22b 세부적인 서술을 빈번하게 사용한다. '

# Q23 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[22] = ' 질문23a 논리적이고 객관적인 토론을 생각해야 할 자료로 인식한다. '
Qb[22] = ' 질문23b 사람들의 감정과 정서들을 생각해야 할 자료로 인식한다. '

# Q24 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[23] = ' 질문24a 모임에서 빗나가는 토론을 좋아하지 않는다. '
Qb[23] = ' 질문24b 모임에서 토론이 옆길로 새는 것에 대해 마음을 두지 않는다. '

# Q25 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[24] = ' 질문25a 새로운 인간관계를 시작할 때 조심성을 보인다. '
Qb[24] = ' 질문25b 새로운 인간관계를 쉽게 시작하며 조심성을 많이 보이지 않는다. '

# Q26 질문내용  S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[25] = ' 질문26a 나의 인간관계에 대해 절대적인 것으로써 예견 가능성을 추구한다. '
Qb[25] = ' 질문26b 나의 인간관계에 있어서 변화란 절대적인 중요성을 가지는 것으로 평가한다. '

# Q27 질문내용   T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[26] = ' 질문27a 인간관계에 대해 논리적인 이유를 규명한다. '
Qb[26] = ' 질문27b 인간관계에 대해 나의 개인적인 이유를 규명한다. '

# Q28 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[27] = ' 질문28a 두 사람간의 관계에서 문제가 일어날 때에 문제를 다룬다. '
Qb[27] = ' 질문28b 두 사람간의 관계에 대한 문제를 다루기 위해 시기를 정해 놓기를 원한다. '

# Q29 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[28] = ' 질문29a 나는 많은 친구들과 우정을 나누는 것을 좋아한다. '
Qb[28] = ' 질문29b 적은 수의 친구들과 깊은 관계를 맺기를 좋아한다. '

# Q30 질문내용  S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[29] = ' 질문30a 이상적인 관계에 대해 백일몽을 꾸며 현실을 간과한다. '
Qb[29] = ' 질문30b 백일몽을 꾸기는 하나, 관계에서 나타나는 현실은 알고 있다. '

# Q31 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[30] = ' 질문31a 나의 관심을 나의 개인적인 말과 행동을 통해 표현한다. '
Qb[30] = ' 질문31b 나의 관심을 보다 감정을 배제한 상태로 표현한다. '

# Q32 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[31] = ' 질문32a 사교적인 모임의 일정에 따르는 활동들을 해야 할 당위성을 느낀다. '
Qb[31] = ' 질문32b 사교적인 모임의 일정에 따르는 활동들에 관심을 덜 느낀다. '

# Q33 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[32] = ' 질문33a 나의 개인적인 공간과 시간을 쉽게 다른 사람들과 나눈다. '
Qb[32] = ' 질문33b 나의 개인적인 공간과 많은 사적인 시간을 필요로 한다 '

# Q34 질문내용   S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[33] = ' 질문34a 관계에 있어서 명확한 역할과 기대를 지니고 있다. '
Qb[33] = ' 질문34b 역할이나 기대 등은 언제나 타협이 가능한 것으로 믿는다. '

# Q35 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[34] = ' 질문35a 나의 인간관계를 손상시킬 수도 있는 부정적인 면들로부터 회피한다. '
Qb[34] = ' 질문35b 나의 인간관계에 도움이 될 만한 섬세한 감정들을 무시한다. '

# Q36 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[35] = ' 질문36a 함께 일함으로써 나의 인간관계를 구축한다고 간주한다. '
Qb[35] = ' 질문36b 업무는 나의 인간관계를 침범하는 것으로 간주한다. '

# Q37 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[36] = ' 질문37a 집중할 수 있는 조용함을 추구한다. '
Qb[36] = ' 질문37b 행동 지향적인 다양한 업무를 추구한다. '

# Q38 질문내용  S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[37] = ' 질문38a 이전에 내가 얻은 작업경험이 나타내는 것보다는 좀 다르게 일을 한다. '
Qb[37] = ' 질문38b 이전에 내가 습득한 작업 경험을 활용한다. '

# Q39 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[38] = ' 질문39a 나의 업무의 기본으로 논리와 분석을 사용한다. '
Qb[38] = ' 질문39b 업무의 기본으로 개인의 가치기준들과 더불어 다른 사람의 견해도 포함시킨다. '

# Q40 질문내용   J(판단), P(인식) 검사
Qa[39] = ' 질문40a 불시에 생기는 업무를 처리할 수 있을 때에 최선을 다한다. '
Qb[39] = ' 질문40b 나의 일을 계획할 수 있고 계획하는 일을 할 수 있을 때에 최선을 다한다. '

# Q41 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[40] = ' 질문41a 심사숙고를 통해 나의 생각을 발전시킨다. '
Qb[40] = ' 질문41b 토의를 통해 나의 생각을 발전시킨다. '

# Q42 질문내용   S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[41] = ' 질문42a 새로운 기술을 배우려고 하기보다는 이미 알고 있는 기존의 기술을 적용한다. '
Qb[41] = ' 질문42b 도전이나 혁신과 관련되는 새로운 기술을 배우는 것을 즐긴다. '

# Q43 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[42] = ' 질문43a 다른 사람들을 엄격하게 다루며 관리한다. '
Qb[42] = ' 질문43b 다른 사람들과 동감하면서 그들과 관리하고 관여한다. '

# Q44 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[43] = ' 질문44a 더 많은 정보를 수집하기 위해 결정에 얽매이는 것을 거부한다. '
Qb[43] = ' 질문44b 가능성을 희박하게 보며, 일단 결정을 내리면 만족한다. '

# Q45 질문내용   E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[44] = ' 질문45a 일의 진행에 종종 변화가 필요하며 외부 사건들을 찾아다닌다. '
Qb[44] = ' 질문45b 나의 일에 집중하고 외부 사건들은 안중에 없다. '

# Q46 질문내용   S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[45] = ' 질문46a 사물들을 구체적으로 언급하는 것을 좋아한다. '
Qb[45] = ' 질문46b 사물을 일반적으로 언급하는 것을 좋아한다. '

# Q47 질문내용    T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[46] = ' 질문47a 업무를 최대한 효과적으로 해내기 위해 조화를 필요로 한다. '
Qb[46] = ' 질문47b 조화롭지 않아도 잘 지낼 수 있으며 여전히 업무를 효율적으로 잘 해 낸다. '

# Q48 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[47] = ' 질문48a 신속하게 결정하고 마감하려 한다. '
Qb[47] = ' 질문48b 결정을 미루며 가능성을 찾는다. '   



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
        win.title( name.get() + "님" + "계속 검사하세요. ")
    else :
        win.title( name.get() + "님" + "검사가 완료되었습니다. ")
        msg.showinfo( '완료', '모두 답하셨습니다. 결과 페이지에서 결과를 확인하세요.')
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
        
        if r==11 or  r==52 or r==92 or r==132 or r==172 or r==211 or r==252 or r==291 or r==331 or r==372 or r==412 :
#or r==451 
            R1a_score += 1
        elif r==12 or  r==51 or r==91 or r==131 or r==171 or r==212 or r==251 or r==292 or r==332 or r==371 or r==411 :
#or r==452
            R1b_score += 1
            
        elif r==22 or  r==61 or r==102 or r==142 or r==182 or r==222 or r==261 or r==302 or r==341 or r==382 or r==421 :
#or r==461
            R2a_score += 1
        elif r==21 or  r==62 or r==101 or r==141 or r==181 or r==221 or r==262 or r==301 or r==342 or r==381 or r==422 :
#or r==462
            R2b_score += 1

        elif r==31 or  r==71 or r==111 or r==152 or r==192 or r==232 or r==271 or r==312 or r==352 or r==391 or r==431 :
#or r==472
            R3a_score += 1
        elif r==32 or r==72 or r==112 or r==151 or r==191 or r==231 or r==272 or r==311 or r==351 or r==392 or r==432 :
#or r==471
            R3b_score += 1

        elif r==42 or  r==82 or r==122 or r==162 or r==201 or r==241 or r==282 or r==321 or r==361 or r==402 or r==442 :
#or r==481
            R4a_score += 1
        elif r==41 or  r==81 or r==121 or r==161 or r==202 or r==242 or r==281 or r==322 or r==362 or r==401 or r==441 :
#or r==482
            R4b_score += 1


# Q1  : E,  I    Q2 :  S, N     Q3 :  T, F      Q4 : J, P  
            
    global scr
    
    text = 'R1 E(외향 extroversion ) : '+  str(R1a_score) + '   R1 I(내향 introversion ) : ' + str(R1b_score) + '  '
    print (text)
    scr.insert(tk.INSERT, text )
    
    text = 'R2 S(감각 sensing) : '+  str(R2a_score) + '   R2 N(직관intuition) : ' + str(R2b_score) + '  '
    print (text)
    scr.insert(tk.INSERT, text )
    
    text = 'R3 T(사고 thinking) : '+  str(R3a_score) + '   R3 F(감정 feeling) : ' + str(R3b_score) + '  '
    print (text)
    scr.insert(tk.INSERT, text )
    
    text = 'R4 J(판단 judging) : '+  str(R4a_score) + '   R4 P(인식 perceiving) : ' + str(R4b_score) + '  '
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

    
    p = int(intention / 44 *100)
     
    text = 'MBTI  result : '+  MBTI_result + ' (' + str(p) +'%)'
    scr.insert(tk.INSERT, text ) 
    print (text)
    
    
#======================
# Start GUI
#======================
win.mainloop()