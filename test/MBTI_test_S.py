# For Elemantary Student v1.1
# ======================
# imports
# ======================
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import scrolledtext


# Create instance
win = tk.Tk()

global index

# Add a title
win.title("MBTI 검사 ver1.0 feat. by Song, Kim")

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

page1 = ttk.LabelFrame(tab1, text=' 검사 Page1 : 두 항목 중 본인 성격과 비슷한 것을 선택하세요.')
page1.grid(column=0, row=0, padx=8, pady=2)

page2 = ttk.LabelFrame(tab2, text=' 검사 Page2 : 두 항목 중 본인 성격과 비슷한 것을 선택하세요.')
page2.grid(column=0, row=0, padx=8, pady=2)

page3 = ttk.LabelFrame(tab3, text=' 검사 Page3 : 두 항목 중 본인 성격과 비슷한 것을 선택하세요.')
page3.grid(column=0, row=0, padx=8, pady=2)

page4 = ttk.LabelFrame(tab4, text=' 검사 Page4 : 두 항목 중 본인 성격과 비슷한 것을 선택하세요.')
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
    start_label.configure(text='안녕하세요. ' + name.get() +
                          '님 ' + ' 위에 있는  Page1 탭부터 진행하세요.')
    win.title("MBTI 검사 ver1.0 (feat. by Song,Kim) " + name.get() + " 진행중 ")


# Adding a Button
start_button = ttk.Button(page0, text=' 검사시작! ', command=click_me)
start_button.grid(column=2, row=1)

ttk.Label(page0, text="선택하세요 학년:").grid(column=1, row=0)
grade = tk.StringVar()
grade_chosen = ttk.Combobox(
    page0, width=12, textvariable=str, state='readonly')
grade_chosen['values'] = ('초1', '초2', '초3', '초4', '초5',
                          '초6', '중1', '중2', '중3', '고1', '고2', '고3', '일반인')
grade_chosen.grid(column=1, row=1)
grade_chosen.current(0)

start_label = ttk.Label(page0, text=' ')
start_label.grid(row=2, sticky='WE', columnspan=3)

name_entered.focus()      # Place cursor into name Entry


# Tab Control 1 refactoring  ---------------------------------------------------------

radioVar = []
Qnum = 40

for i in range(Qnum):
    radioVar.append(tk.IntVar())

# Questions LabelFrame
pageLF = []

for i in range(Qnum):
    if 0 <= i <= 9:
        pageLF.append(ttk.LabelFrame(page1))
        pageLF[i].grid(column=0, row=i, sticky='WE')
    elif 10 <= i <= 19:
        pageLF.append(ttk.LabelFrame(page2))
        pageLF[i].grid(column=0, row=i-10, sticky='WE')
    elif 20 <= i <= 29:
        pageLF.append(ttk.LabelFrame(page3))
        pageLF[i].grid(column=0, row=i-20, sticky='WE')
    elif 30 <= i <= 39:
        pageLF.append(ttk.LabelFrame(page4))
        pageLF[i].grid(column=0, row=i-30, sticky='WE')

resultLabel1 = ttk.LabelFrame(page5, text=' 성격 유형')
resultLabel1.grid(column=0, row=0, sticky='WE')

resultLabel2 = ttk.LabelFrame(page5, text=' 성격 특징 ')
resultLabel2.grid(column=0, row=1, sticky='WE')

resultLabel3 = ttk.LabelFrame(page5, text=' 추천 직업 ')
resultLabel3.grid(column=0, row=2, sticky='WE')

Qa = []
Qb = []
for i in range(Qnum):
    Qa.append('')
for i in range(Qnum):
    Qb.append('')

# 〈출처 : 심혜숙, 임승환 역, 성격유형과 삶의 양식〉
# Q1 질문내용  E(외향), I(내향) 검사  외향적(E)인 사람은 인간과 사물의 외면적인 세계를 지향하는 반면, 내향적(I)인 사람은 생각과 감정의 내면적 세계를 지향
Qa[0] = ' 질문1a 나는 말하기를 좋아해 실수 할 때가 종종 있다. '
Qb[0] = ' 질문1b 나는 말이 없어 주변 사람들이 답답해 할 때가 있다. '

# Q2 질문내용  E(외향), I(내향) 검사
Qa[1] = ' 질문2a 나는 새로운 사람을 만나도 어색하지 않다. '
Qb[1] = ' 질문2b 나는 모르는 사람을 만나는 일이 피곤하다. '

# Q3 질문내용   E(외향), I(내향) 검사
Qa[2] = ' 질문3a 나는 말하면서 생각하고 대화도중 결심할 때가 있다. '
Qb[2] = ' 질문3b 나는 의견을 말하기 앞서 신중히 생각하는 편이다. '

# Q4 질문내용   E(외향), I(내향) 검사
Qa[3] = ' 질문4a 나는 여러사람들과 함께 일하는 것이 편하다. '
Qb[3] = ' 질문4b 나는 혼자 혹은 소수로 일하는 것이 편하다. '

# Q5 질문내용   E(외향), I(내향) 검사
Qa[4] = ' 질문5a 나는 나의 견해를 사람들에게 표현하기를 좋아한다. '
Qb[4] = ' 질문5b 나는 대체로 나의 생각, 견해를 내 안에 간직하는 편이다. '

# Q6 질문내용  E(외향), I(내향) 검사
Qa[5] = ' 질문6a 말을 할 때 몸동작이 큰 편이다. '
Qb[5] = ' 질문6b 말을 할 때 몸동작을 사용하면 어색한 편이다. '

# Q7 질문내용   E(외향), I(내향) 검사
Qa[6] = ' 질문7a 오랜 시간 혼자 일하다 보면 외롭고 지루해한다. '
Qb[6] = ' 질문7b 혼자 오랜시간 일을 잘하는 편이다. '

# Q8 질문내용   E(외향), I(내향) 검사
Qa[7] = ' 질문8a 일 할 때 적막한 것보다는 어느 정도의 소리가 도움이 된다. '
Qb[7] = ' 질문8b 나는 소음이 있는 곳에서 일을 할 때 일하기가 힘들다. '

# Q9 질문내용   E(외향), I(내향) 검사
Qa[8] = ' 질문9a 목소리가 크고 말이 빠른편이다. '
Qb[8] = ' 질문9b 목소리가 작고 조용하게 천천히 말하는 편이다. '

# Q10 질문내용   E(외향), I(내향) 검사
Qa[9] = ' 질문10a 나는 집밖에서 활동하는 것이 편이다. '
Qb[9] = ' 질문10b 나는 집에 있는 것이 편하다. '

# Q11 질문내용     S(감각), N(직관) 검사 감각적(S)인 사람은 세부사항을 면밀히 조사해 보는 반면, 직관적(N인 사람은 큰 문제에 집중하기를 좋아하는 경향
Qa[10] = ' 질문11a 나는 당장 오늘 하루의 일이 앞으로의 일보다 더 중요하다. '
Qb[10] = ' 질문11b 나는 오늘 하루의 일보다 앞으로 일어날 일을 먼저 생각한다. '

# Q12 질문내용    S(감각), N(직관) 검사
Qa[11] = ' 질문12a 나는 직접 체험하고 판단하는 것이 좋다. '
Qb[11] = ' 질문12b 나는 즉시 떠오르는 느낌으로 판단하는 것이 좋다. '

# Q13 질문내용    S(감각), N(직관) 검사
Qa[12] = ' 질문13a 나는 눈에 보이는 대로 나타내는 것을 잘 한다. '
Qb[12] = ' 질문13b 나는 머리 속으로 상상한 것을 나타내는 것을 잘 한다. '

# Q14 질문내용     S(감각), N(직관) 검사
Qa[13] = ' 질문14a 나는 있는 그대로 정확하게 얘기하는 것이 좋다. '
Qb[13] = ' 질문14b 나는 의미를 숨기고 돌려서 얘기하는 것이 좋다. '

# Q15 질문내용     S(감각), N(직관) 검사
Qa[14] = ' 질문15a 나는  보통 사람들이 하는대로 따르는 것이 편하다. '
Qb[14] = ' 질문15b 나는 다른 사람들과는 조금 다르게 생각하고 행동하는 것이 좋다. '

# Q16 질문내용    S(감각), N(직관) 검사
Qa[15] = ' 질문16a 나는 갔던 길로 가는 것이 편하다.  '
Qb[15] = ' 질문16b 나는 새로운 길이 재밌다.  '

# Q17 질문내용     S(감각), N(직관) 검사
Qa[16] = ' 질문17a 나는 했던 일이 편하다. '
Qb[16] = ' 질문17b 나는 새로운 일이 흥미있다. '

# Q18 질문내용   S(감각), N(직관) 검사
Qa[17] = ' 질문18a 나는 길찾아가는 지도를 자세하게 그린다. '
Qb[17] = ' 질문18b 나는 길찾아가는 지도를 자세하게 그릴 수 없다. '

# Q19 질문내용   S(감각), N(직관) 검사
Qa[18] = ' 질문19a 나는 일을 처리할 때 꼼꼼한 편이다. '
Qb[18] = ' 질문19b 나는 일을 처리할 때 대충하는 편이다.  '

# Q20 질문내용     S(감각), N(직관) 검사
Qa[19] = ' 질문20a 나는 실제 경험을 좋아한다. '
Qb[19] = ' 질문20b 나는 머리 속으로 상상하는 것을 좋아한다. '

# Q21 질문내용  T(사고) F(감정) 검사  사고적(T)인 사람은 어떤 일을 논리적이고 객관적으로 판단하기를 원하는 반면,감정적(F)인 사람은 보다 주관적인 바탕 위에서 어떤 결정을 내리기를 선호
Qa[20] = ' 질문21a 나는 원인관계를 따지는 것을 좋아한다. '
Qb[20] = ' 질문21b 나는 대상에 대해 느끼는 감정이 풍부하다. '

# Q22 질문내용  T(사고) F(감정) 검사
Qa[21] = ' 질문22a 나는 내가 보고 느끼는 것이 남의 생각보다 더 중요하다. '
Qb[21] = ' 질문22b 나는 남이 어떻게 생각할지를 먼저 생각하려 한다. '

# Q23 질문내용   T(사고) F(감정) 검사
Qa[22] = ' 질문23a 나는 감정에 치우치지 않고 의사결정한다.. '
Qb[22] = ' 질문23b 나는 상황을 생각하며 의사결정한다. '

# Q24 질문내용   T(사고) F(감정) 검사
Qa[23] = ' 질문24a 나는 이성과 논리로 행동한다. '
Qb[23] = ' 질문24b 나는 일반적인 사람들의 생각 기준으로 행동한다. '

# Q25 질문내용  T(사고) F(감정) 검사
Qa[24] = ' 질문25a 나는 능력있다는 소리를 듣기 좋아한다. '
Qb[24] = ' 질문25b 나는 따뜻하다는 소리를 듣기 좋아한다. '

# Q26 질문내용  T(사고) F(감정) 검사
Qa[25] = ' 질문26a 나는 다른 사람들과 경쟁하는 것을 좋아한다. '
Qb[25] = ' 질문26b 나는 다른 사람들에게 양보하는 것을 좋아한다. '

# Q27 질문내용  T(사고) F(감정) 검사
Qa[26] = ' 질문27a 나는 있는 그래도 솔직하게 말하는 것이 편하다. '
Qb[26] = ' 질문27b 나는 사실이 아니어도 남을 배려하는 말이 편하다. '

# Q28 질문내용   T(사고) F(감정) 검사
Qa[27] = ' 질문28a 나는 사건의 원인과 결과를 쉽게 파악한다.  '
Qb[27] = ' 질문28b 나는 사람의 기분을 쉽게 파악한다.  '

# Q29 질문내용   T(사고) F(감정) 검사
Qa[28] = ' 질문29a 나는 다른 사람들을 대할 때 맺고 끊는 것이 확실한 편이다. '
Qb[28] = ' 질문29b 나는 다른 사람들을 대할 때 마음이 따뜻하다고 생각한다. '

# Q30 질문내용  T(사고) F(감정) 검사
Qa[29] = ' 질문30a 나는 문제가 있다고 생각할 때 할 말은 한다. '
Qb[29] = ' 질문30b 나는 문제가 있더라도 좋게 생각하는 편이다. '

# Q31 질문내용   J(판단), P(인식) 검사  판단 지향적(J)인 사람은 단호하고 확실한 목표를 정한 일을 추진하기를 좋아하며,인식 지향적(P)인 사람은 융통성이 있고, 보다 많은 정보를 얻고자 하는 경향
Qa[30] = ' 질문31a 나는 결정에 대해서 잘 변경하지 않는 편이다. '
Qb[30] = ' 질문31b 나는 결정에 대해서 변경을 잘 하는 편이다. '

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
Qa[34] = ' 질문35a 나는 체계적인 분위기에 일이 잘 된다. '
Qb[34] = ' 질문35b 나는 즐거운 분위기에 일이 잘 된다. '

# Q36 질문내용  J(판단), P(인식) 검사
Qa[35] = ' 질문36a 나는 미리 계획을 세워, 체계적으로 처리하는 것이 좋다.  '
Qb[35] = ' 질문36b 나는 계획없이 그때 그때 순발력으로 처리해도 잘 된다. '

# Q37 질문내용   J(판단), P(인식) 검사
Qa[36] = ' 질문37a 나는 정해진 규칙이 있는 것이 좋다. '
Qb[36] = ' 질문37b 나는 정해진 것 없이 자유로운 것을 좋아한다. '

# Q38 질문내용  J(판단), P(인식) 검사
Qa[37] = ' 질문38a 나는 사람들과 일 할 때 더 잘 친해진다. '
Qb[37] = ' 질문38b 나는 사람들과 놀 때 더 잘 친해진다. '

# Q39 질문내용  J(판단), P(인식) 검사
Qa[38] = ' 질문39a 내 책상은 정리가 잘 되어 있다.  '
Qb[38] = ' 질문39b 내 책상은 편안하게 되어 있다. '

# Q40 질문내용  J(판단), P(인식) 검사
Qa[39] = ' 질문40a 쇼핑을 갈 때 적어 가는 편이다. '
Qb[39] = ' 질문40b 쇼핑을 갈 때 적지 않고 그냥 가는 편이다.'

radioBtnA = []
radioBtnB = []

finished = False


def radioCall():
    global finished

    done = True
    for i in range(Qnum):
        answer = radioVar[i].get()
        if answer == 0:
            if 0 <= i <= 9:
                win.title(name.get() + "님" + " Page1 검사를 계속해 주세요.")
            elif 10 <= i <= 19:
                win.title(name.get() + "님" + " Page2 검사를 계속해 주세요.")
            elif 20 <= i <= 29:
                win.title(name.get() + "님" + " Page3 검사를 계속해 주세요.")
            else:
                win.title(name.get() + "님" + " Page4 검사를 계속해 주세요.")
            done = False
            break

    if done == False:
        pass

    else:
        win.title(name.get() + "님" + "검사가 완료되었습니다. ")
        if finished == True:
            msg.showinfo('이미완료', '이미 테스트 완료하였습니다.')

        else:
            msg.showinfo('완료', '모두 답하셨습니다. 결과 페이지에서 결과를 확인하세요.')
            finished = True
            showResult()


for i in range(Qnum):
    radioBtnA.append(tk.Radiobutton(
        pageLF[i], text=Qa[i], variable=radioVar[i], value=(i+1)*10+1, command=radioCall))
    radioBtnA[i].grid(column=0, row=0, sticky=tk.W)
    radioBtnB.append(tk.Radiobutton(
        pageLF[i], text=Qb[i], variable=radioVar[i], value=(i+1)*10+2, command=radioCall))
    radioBtnB[i].grid(column=0, row=1, sticky=tk.W)

# Using a scrolled Text control
scrol_w = 60
scrol_h = 10

scr1 = scrolledtext.ScrolledText(
    resultLabel1, width=30, height=2, wrap=tk.WORD)
scr1.grid(column=0, row=0, sticky='WE', columnspan=2)

scr2 = scrolledtext.ScrolledText(
    resultLabel2, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr2.grid(column=0, row=0, sticky='WE', columnspan=2)

scr3 = scrolledtext.ScrolledText(
    resultLabel3, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr3.grid(column=0, row=0, sticky='WE', columnspan=2)


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

        if r == 11 or r == 21 or r == 31 or r == 41 or r == 51 or r == 61 or r == 71 or r == 81 or r == 91:
            R1a_score += 1
        elif r == 12 or r == 22 or r == 32 or r == 42 or r == 52 or r == 62 or r == 72 or r == 82 or r == 92:
            R1b_score += 1

        elif r == 111 or r == 121 or r == 131 or r == 141 or r == 151 or r == 161 or r == 171 or r == 181 or r == 191:
            R2a_score += 1
        elif r == 112 or r == 122 or r == 132 or r == 142 or r == 152 or r == 162 or r == 172 or r == 182 or r == 192:
            R2b_score += 1

        elif r == 211 or r == 221 or r == 231 or r == 241 or r == 251 or r == 261 or r == 271 or r == 281 or r == 291:
            R3a_score += 1
        elif r == 212 or r == 222 or r == 232 or r == 242 or r == 252 or r == 262 or r == 272 or r == 282 or r == 292:
            R3b_score += 1

        elif r == 311 or r == 321 or r == 331 or r == 341 or r == 351 or r == 361 or r == 371 or r == 381 or r == 391:
            R4a_score += 1
        elif r == 312 or r == 322 or r == 332 or r == 342 or r == 352 or r == 362 or r == 372 or r == 382 or r == 392:
            R4b_score += 1

# Q1  : E,  I    Q2 :  S, N     Q3 :  T, F      Q4 : J, P

    global scr1, scr2, scr3

    text = 'R1 E(외향 extroversion ) : ' + str(R1a_score) + \
        '   R1 I(내향 introversion ) : ' + str(R1b_score) + '  '
    print(text)
#    scr1.insert(tk.INSERT, text )

    text = 'R2 S(감각 sensing) : ' + str(R2a_score) + \
        '   R2 N(직관intuition) : ' + str(R2b_score) + '  '
    print(text)
#    scr1.insert(tk.INSERT, text )

    text = 'R3 T(사고 thinking) : ' + str(R3a_score) + \
        '   R3 F(감정 feeling) : ' + str(R3b_score) + '  '
    print(text)
#    scr1.insert(tk.INSERT, text )

    text = 'R4 J(판단 judging) : ' + str(R4a_score) + \
        '   R4 P(인식 perceiving) : ' + str(R4b_score) + '  '
    print(text)
#    scr1.insert(tk.INSERT, text )

    global MBTI_result

    global incline

    global points

    incline = 0

    MBTI_result = ''

    if R1a_score > R1b_score:
        incline += R1a_score
        MBTI_result += 'E'
    elif R1a_score == R1b_score:
        MBTI_result += 'E(I)'
    else:
        incline += R1b_score
        MBTI_result += 'I'

    if R2a_score > R2b_score:
        incline += R2a_score
        MBTI_result += 'S'
    elif R2a_score == R2b_score:
        MBTI_result += 'S(N)'
    else:
        incline += R2b_score
        MBTI_result += 'N'

    if R3a_score > R3b_score:
        incline += R3a_score
        MBTI_result += 'T'
    elif R3a_score == R3b_score:
        MBTI_result += 'T(F)'
    else:
        incline += R3b_score
        MBTI_result += 'F'

    if R4a_score > R4b_score:
        incline += R4a_score
        MBTI_result += 'J'
    elif R4a_score == R4b_score:
        MBTI_result += 'J(P)'
    else:
        incline += R4b_score
        MBTI_result += 'P'

    global type_name, type_description, type_job

    type_name = ''
    type_description = ''
    type_job = ''

    print(MBTI_result)
# 1
    if MBTI_result == "ISTJ":
        type_name = MBTI_result + '(소금형)'
        type_description = '신중하고 조용하며 집중력이 강하고 매사에 철저하다. 구체적, 체계적, 사실적, 논리적, 현실적인 성격을 띠고 있으며, 신뢰할 만 하다. 만사를 체계적으로 조직화시키려고 하며 책임감이 강하다. 성취해야 한다고 생각하는 일이면 주위의 시선에 아랑곳하지 않고 꾸준하고 건실하게 추진해 나간다.'
        type_job = '명확한 직무능력과 인내와 정확성과 조직력을 요하는 분야, 과업 지향적이고 현실에 기반을 둔 분야 - 사무직, 관리직, 법률, 회계, 엔지니어, 대행업자, 화학, 교육, 훈련, 사업, 은행감독원, 세무조사원 등'

# 2
    elif MBTI_result == "ISFJ":
        type_name = MBTI_result + '(권력형)'
        type_description = '조용하고 친근하고 책임감이 있으며 양심 바르다. 맡은 일에 헌신적이며 어떤 계획의 추진이나 집단에 안정감을 준다. 매사에 철저하고 성실하고 정확하다. 기계분야에는 관심이 적다. 필요하면 세세한 면까지도 잘 처리해 나간다. 충실하고 동정심이 많고 타인의 감정에 민감하다.'
        type_job = '정확성과 조직성을 요하며, 반복적으로 연결되는 일상의 일과 타인의 관심과 관찰력이 필요한 분야 - 교사, 비서, 사회사업, 물리치료사, 의학, 종교계, 경호원, 서비스업 등'

# 3
    elif MBTI_result == "ISTP":
        type_name = MBTI_result + '(백과사전형)'
        type_description = '차분한 방관자이다. 조용하고 과묵하며 절제된 호기심을 가지고 인생을 관찰하고 분석한다. 때로는 예기치 않게 유머 감각을 나타내기도 한다. 대체로 인간관계에 관심이 없고 기계가 어떻게, 왜 작동되는지 흥미가 많다. 논리적인 원칙에 따라 사실을 조직화하기를 좋아한다.'
        type_job = '실제적인 생산관리 분야, 해결해야 할 새롭고 긴박한 일을 처리하고 자신의 독립성이 보장되는 직업 분야 - 기계, 응용과학, 스포츠, 기술자, 측량기사, 상업디자이너, 교정직, 사무원, 법률, 통계, 경제, 판매 등'

# 4
    elif MBTI_result == "ISTJ":
        type_name = MBTI_result + '(성인군자형)'
        type_description = '말없이 다정하고 친절하고 민감하며 자기 능력을 뽐내지 않고 겸손하다. 의견의 충돌을 피하고 자기 견해나 가치를 타인에게 강요하지 않는다. 남 앞에 서서 주도해 나가기 보다 충실히 따르는 편이다. 일하는 데에도 여유가 있다. 왜냐하면 목표를 달성하기 위해 안달복달하지 않고 현재를 즐기기 때문이다.'
        type_job = '개방되어 있고 다른 사람들과 쉽게 어울릴 수 있는 직업분야, 실제적인 행동 기술을 활용할 수 있는 분야 - 예술인, 성직자, 교직자, 요리사, 정원사, 간호사, 지질학자, 사회사업, 서비스업, 체육인 등'

# 5
    elif MBTI_result == "INFJ":
        type_name = MBTI_result + '(예언자형)'
        type_description = '인내심이 많고 독창적이며 필요하거나 원하는 일이라면 끝까지 이루려고 한다. 자기일에 최선의 노력을 다한다. 타인에게 말없이 영향력을 미치며, 양심이 바르고 다른 사람에게 따뜻한 관심을 가지고 있다. 확고부동한 원리원칙을 중시한다. 공동선을 위해서는 확신에 찬 신념을 가지고 있다.'
        type_job = '자율성과 창의성을 인간교육에서 발휘하는 분야, 직관력과 사람 중심의 가치를 중시하는 분야 - 심리학자, 상담자, 성직자, 교직, 저술활동, 연구자문, 의사, 순수예술, 건축가, 사회사업가 등'

# 6
    elif MBTI_result == "INTJ":
        type_name = MBTI_result + '(과학자형)'
        type_description = '사고가 독창적이며 창의력과 비판적 분석력이 뛰어나며 내적 신념이 강하다. 독립적이고 단호하며 때때로 문제에 대하여 고집이 세다. 자신과 타인의 능력을 중요시하며 목적달성을 위하여 온 시간과 노력을 바쳐 일한다.'
        type_job = '직관력과 통찰력, 이론의 논리성을 탐색하는 분야 - 컴퓨터 프로그래머, 기술자, 사업분석가, 행정가, 철학, 엔지니어, 건축사, 자연과학자, 법조인 등'

# 7
    elif MBTI_result == "INFP":
        type_name = MBTI_result + '(잔다르크형)'
        type_description = '정열적이고 충실하나 상대방을 잘 알기 전까지는 이를 드러내지 않는 편이다. 학습, 아이디어, 언어, 자기 독립적인 일에 관심이 많다. 어떻게 하든 이루어내기는 하지만 일을 지나치게 많이 벌리려는 경향을 가지고 있다. 남에게 친근하기는 하지만, 많은 사람들을 동시에 만족시키려는 부담을 가지고 있다. 물질적 소유나 물리적 환경에는 별 관심이 없다.'
        type_job = '다른 사람들의 성장을 도모시키는 분야, 인간 이해와 인간 복지에 기여할 수 있는 분야 - 소설가, 연예인, 사회사업가, 성직자, 교수직, 저널리스트, 예술가, 정신과 의사, 건축가 등'

# 8
    elif MBTI_result == "INTP":
        type_name = MBTI_result + '(아이디어형)'
        type_description = '조용하고 과묵하다. 특히 이론적 과학적 추구를 즐기며, 논리와 분석으로 문제를 해결하기를 좋아한다. 주로 자기 아이디어에 관심이 많으나 사람들의 모임이나 잡담에는 관심이 없다. 관심의 종류가 뚜렷하므로 자기의 지적 호기심을 활용할 수 있는 분야에서 능력을 발휘할 수 있다.'
        type_job = '추상적 개념과 논리적인 문제해결이 개입되는 분야, 사고와 논리를 활용할 수 있는 분야 - 분석자, 논리학자, 수학자, 철학자, 과학자, 건축가, 작가, 신문방송인, 통계, 연구, 컴퓨터 분야'

# 9
    elif MBTI_result == "ESTP":
        type_name = MBTI_result + '(활동가형)'
        type_description = '실질적인 문제해결에 능하다. 근심이 없고 어떤 일이든 즐길 줄 안다. 기계 다루는 일이나 운동을 좋아하고 친구 사귀기를 좋아한다. 적응력이 강하고 관용적이며, 보수적인 가치관을 가지고 있다. 긴 설명을 싫어한다. 기계의 분해 또는 조립과 같은 실제적인 일을 다루는 데 능하다.'
        type_job = '정확한 사실 파악 능력, 논리와 분석능력, 적응력을 발휘할 수 있는 분야, 활동적이거나 연장이나 재료를 다루는 분야 - 전문 세일즈, 요식업, 건축업, 부동산, 무역업, 언론, 신용조사, 은행 경영자, 개인 서비스업 등'

# 10
    elif MBTI_result == "ESFP":
        type_name = MBTI_result + '(사교형)'
        type_description = '사교적이고 태평스럽고 수용적이고 친절하며, 만사를 즐기는 형이기 때문에 다른 사람들로 하여금 일에 재미를 느끼게 한다. 운동을 좋아하고 주위에 벌어지는 일에 관심이 많아 끼어들기 좋아한다. 추상적인 이론보다는 구체적인 사실을 잘 기억하는 편이다. 건전한 상식이나 사물 뿐 아니라 사람들을 대상으로 구체적인 능력이 요구되는 분야에서 능력을 발휘할 수 있다.'
        type_job = '사람들과 만나고 상호작용하는 분야, 순응을 요하고 실제적인 능력을 필요로 하는 분야 - 여행사, 유흥사업, 서비스, 판매, 영화, 프로듀서, 정치가, 연예인, 중재자, 비서직, 간호사, 교직, 건축업자 등'

# 11
    elif MBTI_result == "ESTJ":
        type_name = MBTI_result + '(사업가형)'
        type_description = '구체적이고 현실적이고 사실적이며, 기업 또는 기계에 재능을 타고 났다. 실용성이 없는 일에는 관심이 없으며 필요할 때 응용할 줄 안다. 활동을 조직화하고 주도해 나가기를 좋아한다. 타인의 감정이나 관점에 귀를 기울일 줄 알면 훌륭한 행정가가 될 수 있다.'
        type_job = '조직 안에서 책임을 맡고 실제적인 일을 처리하는 분야, 현실적, 체계적, 논리적인 분야 - 행정, 관리직, 자기 사업, 제조 생산업, 건설, 판매관리자, 공장 감독자, 변호사, 재무담당 감독자 등'

# 12
    elif MBTI_result == "ESFJ":
        type_name = MBTI_result + '(친선도모형)'
        type_description = '마음이 따뜻하고 이야기하기 좋아하고, 사람들에게 인기가 있고 양심 바르고 남을 돕는 데에 타고난 기질이 있으며 집단에서도 능동적인 구성원이다. 조화를 중시하고 인화를 이루는데 능하다. 항상 남에게 잘해주며, 격려나 칭찬을 들을 때 가장 신바람을 낸다. 사람들에게 직접적이고 가시적인 영향을 줄 수 있는 일에 가장 관심이 많다.'
        type_job = '인화를 도모하는 분야, 규칙과 규정을 잘 따르고 의무와 봉사를 하는 분야, 행동을 요구하는 분야 - 자원봉사, 세일즈, 교직, 인력개발관리, 사회사업, 상담, 서비스업, 보건 종사자, 성직자 등'

# 13
    elif MBTI_result == "ENFP":
        type_name = MBTI_result + '(스파크형)'
        type_description = '따뜻하고 정열적이고 활기에 넘치며 재능이 많고 상상력이 풍부하다. 관심이 있는 일이라면 어떤 일이든지 척척 해낸다. 어려운 일이라도 해결을 잘하며 항상 남을 도와줄 태세를 가지고 있다. 자기 능력을 과신한 나머지 미리 준비하기보다 즉흥적으로 덤비는 경우가 많다. 자기가 원하는 일이라면 어떠한 이유라도 갖다 붙이며 부단히 새로운 것을 찾아 나선다.'
        type_job = '사람들과 상호작용이 요구되고 상황이 변화하는 분야, 분석적인 일의 분야 - 홍보활동가, 정치인, 판매요원, 배우, 예술가, 상담사, 성직자, 저널리스트, 광고, 경영 등'

# 14
    elif MBTI_result == "ENTP":
        type_name = MBTI_result + '(발명가형)'
        type_description = '민첩하고 독창적이고 안목이 넓으며 다방면에 재능이 많다. 새로운 일을 시도하고 추진하려는 의욕이 넘치며, 새로운 문제나 복잡한 문제를 해결하는 능력이 뛰어나며 달변이다. 그러나 일상적이고 세부적인 면은 간과하기 쉽다. 한 일에 관심을 가져도 부단히 새로운 것을 찾아 나간다. 자기가 원하는 일이면 논리적인 이유를 찾아내는데 능하다.'
        type_job = '자율성과 다양성이 제공되는 분야, 도전성이 있고 단조롭지 않은 일의 분야 - 발명가, 과학자, 신문방송인, 언론인, 컴퓨터분석가, 기업가, 감사관, 산업설계분석, 엔지니어 등'

# 15
    elif MBTI_result == "ENFJ":
        type_name = MBTI_result + '(언변능숙형)'
        type_description = '주위에 민감하며 책임감이 강하다. 다른 사람들의 생각이나 의견을 중히 여기고, 다른 사람들의 감정에 맞추어 일을 처리하려고 한다. 편안하고 능란하게 계획을 내놓거나 집단을 이끌어 가는 능력이 있다. 사교성이 풍부하고 인기있고 동정심이 많다. 남의 칭찬이나 비판에 지나치게 민감하게 반응한다.'
        type_job = '나에 대한 기대치가 있고, 나의 공로를 인정해주며, 업무 능력의 성장과 발전을 격려받을 수 있는 분야 - 지도자, 통솔자, 정책가, 활동가, 지휘관, 커뮤니케이션 분야, 보건 의료 분야, 컨설팅 분야 등'

# 16
    else:  # ENTJ
        type_name = MBTI_result + '(지도자형)'
        type_description = '열성이 많고 솔직하고 단호하고 통솔력이 있다. 대중 연설과 같이 추리와 지적 담화가 요구되는 일이라면 어떤 것이든 능하다. 보통 정보에 밝고 지식에 대한 관심과 욕구가 많다. 때로는 실제의 자신보다 더 긍정적이거나 자신 있는 듯한 사람으로 비칠 때도 있다.'
        type_job = '독립적인 프로젝트를 추진할 수 있는 분야, 추진력과 통찰력, 분석력을 활용할 수 있는 분야 - 설계, 볍률, 경영관리, 군대장교, 지휘관, 자영업, 건축, 토목, 세일즈관리자, 컴퓨터 전문가 등'

    points = int(incline / 36 * 100)

    text = type_name + ' (정확도 :' + str(points) + '%)'

    scr1.insert(tk.INSERT, text)
    scr2.insert(tk.INSERT, type_description)
    scr3.insert(tk.INSERT, type_job)


# ======================
# Start GUI
# ======================
win.mainloop()
