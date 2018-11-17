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

# 〈출처 : 심혜숙, 임승환 역, 성격유형과 삶의 양식〉
# Q1 질문내용  E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[0] = ' 질문1a 나는 말하기를 좋아해 실수 할 때가 종종 있다. '  
Qb[0] = ' 질문1a 나는 말이 없어 주변 사람들이 답답해 할 때가 있다. '

# Q2 질문내용  E(외향), I(내향) 검사
Qa[1] = ' 질문2a 나는 새로운 사람을 만나도 어색하지 않다. '
Qb[1] = ' 질문2b 나는 모르는 사람을 만나는 일이 피곤하다. '

# Q3 질문내용   E(외향), I(내향) 검사
Qa[2] = ' 질문3a 나는 말하면서 생각하고 대화도중 결심할 때가 있다. '
Qb[2] = ' 질문3b 나는 의견을 말하기 앞서 신중히 생각하는 편이다. '

# Q4 질문내용   E(외향), I(내향) 검사
Qa[3] = ' 질문4a 나는 팀으로 일하는 것이 편하다. '
Qb[3] = ' 질문4b 나는 혼자 혹은 소수로 일하는 것이 편하다. '

# Q5 질문내용   E(외향), I(내향) 검사
Qa[4] = ' 질문5a 나는 나의 견해를 사람들에게 표현하기를 좋아한다. '
Qb[4] = ' 질문5b 나는 대체로 나의 생각, 견해를 내 안에 간직하는 편이다. '

# Q6 질문내용  E(외향), I(내향) 검사
Qa[5] = ' 질문6a 말을 할 때 제스처가 큰 편이다. '
Qb[5] = ' 질문6b 말을 할 때 제스처를 사용하면 어색한 편이다. '

# Q7 질문내용   E(외향), I(내향) 검사
Qa[6] = ' 질문7a 오랜 시간 혼자 일하다 보면 외롭고 지루한 편이다. '
Qb[6] = ' 질문7b 자 오랜시간 일을 잘하는 편이다. '

# Q8 질문내용   E(외향), I(내향) 검사
Qa[7] = ' 질문8a 일 할 때 적막한 것보다는 어느 정도의 소리가 도움이 된다. '
Qb[7] = ' 질문8b 나는 소음이 있는 곳에서 일을 할 때 일하기가 힘들다. '

# Q9 질문내용   E(외향), I(내향) 검사
Qa[8] = ' 질문9a 말이 빠른편이다. '
Qb[8] = ' 질문9b 목소리가 작고 조용하게 천천히 말하는 편이다. '

# Q10 질문내용   E(외향), I(내향) 검사
Qa[9] = ' 질문10a 나는 활동적인 편이다. '
Qb[9] = ' 질문10b 나는 집에 있는 것이 편하다. '

# Q11 질문내용     S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[10] = ' 질문11a 나는 현실적이다. '
Qb[10] = ' 질문11b 나는 미래지향적이다. '

# Q12 질문내용    S(감각), N(직관) 검사 
Qa[11] = ' 질문12a 나는 경험으로 판단한다. '
Qb[11] = ' 질문12b 나는 떠오르는 직관으로 판단한다. '

# Q13 질문내용    S(감각), N(직관) 검사 
Qa[12] = ' 질문13a 나는 사실적 묘사를 잘 한다. '
Qb[12] = ' 질문13b 나는 추상적 표현을 잘 한다. '

# Q14 질문내용     S(감각), N(직관) 검사 
Qa[13] = ' 질문14a 나는 구체적이다. '
Qb[13] = ' 질문14b 나는 은유적이다. '

# Q15 질문내용     S(감각), N(직관) 검사 
Qa[14] = ' 질문15a 나는 상식적이다. '
Qb[14] = ' 질문15b 나는 창의적이다. '

# Q16 질문내용    S(감각), N(직관) 검사 
Qa[15] = ' 질문16a 나는 갔던 길로 가는 것이 편하다.  '
Qb[15] = ' 질문16b 나는 새로운 길이 재밌다.  '

# Q17 질문내용     S(감각), N(직관) 검사 
Qa[16] = ' 질문17a 나는 했던 일이 편하다. '
Qb[16] = ' 질문17b 나는 새로운 일이 흥미있다. '

# Q18 질문내용   S(감각), N(직관) 검사 
Qa[17] = ' 질문18a 나는 약도를 구체적으로 그린다. '
Qb[17] = ' 질문18b 나는 약도를 구체적으로 그리기 어렵다. '

# Q19 질문내용   S(감각), N(직관) 검사 
Qa[18] = ' 질문19a 나는 꼼꼼한 편이다. '
Qb[18] = ' 질문19b 나는 대충하는 편이다.  '

# Q20 질문내용     S(감각), N(직관) 검사 
Qa[19] = ' 질문20a 나는 실제 경험을 좋아한다. '
Qb[19] = ' 질문20b 나는 공상을 좋아한다. '

# Q21 질문내용  T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[20] = ' 질문21a 나는 분석적이다. '
Qb[20] = ' 질문21b 나는 감수성이 풍부하다. '

# Q22 질문내용  T(사고) F(감정) 검사 
Qa[21] = ' 질문22a 나는 객관적이다. '
Qb[21] = ' 질문22b 나는 공감적이다. '

# Q23 질문내용   T(사고) F(감정) 검사 
Qa[22] = ' 질문23a 나는 감정에 치우치지 않고 의사결정한다.. '
Qb[22] = ' 질문23b 나는 상황을 생각하며 의사결정한다. '

# Q24 질문내용   T(사고) F(감정) 검사 
Qa[23] = ' 질문24a 나는 이성과 논리로 행동한다. '
Qb[23] = ' 질문24b 나는 가치관과 사람 중심으로 행동한다. '

# Q25 질문내용  T(사고) F(감정) 검사 
Qa[24] = ' 질문25a 나는 능력있다는 소리를 듣기 좋아한다. '
Qb[24] = ' 질문25b 나는 따뜻하다는 소리를 듣기 좋아한다. '

# Q26 질문내용  T(사고) F(감정) 검사 
Qa[25] = ' 질문26a 나는 경쟁한다. '
Qb[25] = ' 질문26b 나는 양보한다. '

# Q27 질문내용  T(사고) F(감정) 검사 
Qa[26] = ' 질문27a 나는 직선적인 말이 편하다. '
Qb[26] = ' 질문27b 나는 배려하는 말이 편하다. '

# Q28 질문내용   T(사고) F(감정) 검사 
Qa[27] = ' 질문28a 나는 사건의 원인과 결과를 쉽게 파악한다.  '
Qb[27] = ' 질문28b 나는 사람의 기분을 쉽게 파악한다.  '

# Q29 질문내용   T(사고) F(감정) 검사 
Qa[28] = ' 질문29a 나는 사람들이 나를 차갑다고 느끼는 편이다. '
Qb[28] = ' 질문29b 나는 사람들이 나를 따뜻하다고 하는 편이다. '

# Q30 질문내용  T(사고) F(감정) 검사 
Qa[29] = ' 질문30a 나는 할 말은 한다. '
Qb[29] = ' 질문30b 나는 좋게 생각하는 편이다. '

# Q31 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[30] = ' 질문31a 나는 결정에 대해서 잘 변경하지 않는 편이다. '
Qb[30] = ' 질문31b 나는 결정에 대해서 융통성이 있는 편이다. '

# Q32 질문내용   J(판단), P(인식) 검사
Qa[31] = ' 질문32a 나는 계획에 의해서 일을 처리하는 편이다. '
Qb[31] = ' 질문32b 나는 마지막에 임박했을 때에 일을 처리하는 편이다. '

# Q33 질문내용  J(판단), P(인식) 검사
Qa[32] = ' 질문33a 나는 계획된 여행이 편하다.'
Qb[32] = ' 질문33b 나는 갑자기 떠나는 여행이 편하다. '

# Q34 질문내용   J(판단), P(인식) 검사
Qa[33] = ' 질문34a 나는 정리정돈을 자주 하는 편이다. '
Qb[33] = ' 질문34b 나는 날 잡아서 정리하는 편이다. '

# Q35 질문내용    J(판단), P(인식) 검사
Qa[34] = ' 질문35a 나는 조직적인 분위기에 일이 잘 된다. '
Qb[34] = ' 질문35b 나는 즐거운 분위기에 일이 잘 된다. '

# Q36 질문내용  J(판단), P(인식) 검사
Qa[35] = ' 질문36a 나는 계획적이고 조직적이다.  '
Qb[35] = ' 질문36b 나는 나의 순발력을 믿는다. '

# Q37 질문내용   J(판단), P(인식) 검사
Qa[36] = ' 질문37a 나는 규범을 좋아한다. '
Qb[36] = ' 질문37b 나는 자유로운 것을 좋아한다. '

# Q38 질문내용  J(판단), P(인식) 검사
Qa[37] = ' 질문38a 나는 일 할 때 친해진다. '
Qb[37] = ' 질문38b 나는 놀 때 친해진다. '

# Q39 질문내용  J(판단), P(인식) 검사
Qa[38] = ' 질문39a 내 책상은 정리가 잘 되어 있다.  '
Qb[38] = ' 질문39b 내 책상은 편안하게 되어 있다. '

# Q40 질문내용  J(판단), P(인식) 검사
Qa[39] = ' 질문40a 쇼핑을 갈 때 적어 가는 편이다. '
Qb[39] = ' 질문40b 쇼핑을 갈 때 적지 않고 그냥 가는 편이다.'

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

    
    p = int(intention / 36 *100)
     
    text = 'MBTI  result : '+  MBTI_result + ' (' + str(p) +'%)'
    scr.insert(tk.INSERT, text ) 
    print (text)
    
    
#======================
# Start GUI
#======================
win.mainloop()