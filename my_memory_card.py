from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QRadioButton, QGroupBox, QButtonGroup
)
from random import (shuffle, randint)
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Испанский', 'Немецкий', 'Английский'))
questions_list.append(Question('Какого цвета нет на флаге России', 'красный', 'чёрный', 'белый', 'синий'))
questions_list.append(Question('Какого числа начинается учеба', '2 сентября', '1 сентября', '3 мая', '7 ноября'))
questions_list.append(Question('Сколько часов в сутках', '12 часов', '18 часов', '24 часа', '22 часа'))
questions_list.append(Question('Сколько градусов в круге', '150', '90', '180', '360'))
questions_list.append(Question('Сколько дней в декабре', '27', '30', '31', '29'))
questions_list.append(Question('Сколько месяцев в году', '11', '4', '12', '14'))
questions_list.append(Question('Самая длинная река в мире', 'Амазонка', 'Нил', 'Хуанхэ', 'Янцзы'))
questions_list.append(Question('Правильное название', 'Memory Card', 'Mmory Card', 'Memry Card', 'Card Memory'))
questions_list.append(Question('Сколько _ у init', '4', '2', '1', '3'))
app = QApplication([])
main_win = QWidget()
btn_ok = QPushButton('Ответить')
text1 = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()

layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)
AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft| Qt.AlignTop))
layout_res.addWidget(lb_Result, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)
layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(text1, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)


layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]
shuffle(answers)

def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer) 
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Correct.setText(q.right_answer)
    show_question()
def show_correct(res):
    lb_Result.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно!')
        main_win.score += 1
        print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов: ', main_win.score)
        print('Рейтинг: ', (main_win.score/main_win.total*100), '%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')
def next_question():
    main_win.total += 1
    print('Статистика\n-Всего вопросов:', main_win.total, '\n-Правильных ответов: ', main_win.score)
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    main_win.cur_question += 1
    if main_win.cur_question >= len(questions_list):
        main_win.cur_question = 0
    q = questions_list[main_win.cur_question]
    ask(q)
def click_OK():
    if btn_ok.text == 'Ответить':
        check_answer()
    else:
        next_question()

#def start_test():
#    if 'Ответить' == btn_ok.text():
#        show_result()
#    else:
#        show_question()
main_win.cur_question = -1
btn_ok.clicked.connect(click_OK)
main_win.score = 0
main_win.total = 0
next_question()
main_win.setLayout(layout_card)
main_win.show()
app.exec_()

#создай приложение для запоминания информации