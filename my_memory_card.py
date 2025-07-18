from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QVBoxLayout, QGroupBox,
                             QRadioButton, QPushButton, QLabel,
                             QButtonGroup, QMessageBox)
from random import shuffle, randint

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
#sfdgdfgdfhf
def show_result():
    ''' Показать панель ответов '''
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    ''' Показать панель вопросов '''
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    global correct_answers, total_questions
    total_questions += 1
    if answers[0].isChecked():
        show_correct('Правильно!')
        correct_answers += 1
    else:
        show_correct('Неверно!')

def next_question():
    global cur_question
    cur_question = randint(0, len(question_list) - 1) 
    print_statistics() 
    q = question_list[cur_question]
    ask(q)

def click_ok():
    ''' определяет, надо ли показывать другой вопрос или проверить ответ на этот вопрос'''
    if 'Ответить' == btn_OK.text():
        check_answer()
        print_statistics() 
        calculate_rating()
    else:
        next_question()

def print_statistics():
    print(f"Верных ответов: {correct_answers}")
    print(f"Всего вопросов: {total_questions}")

def calculate_rating():
    if total_questions > 0:
        rating = (correct_answers / total_questions) * 100
        print(f"Рейтинг: {rating:.2f}%") 
    else:
        print("Нет данных для расчета рейтинга.")

app = QApplication([])

btn_OK = QPushButton('Ответить')
lb_Question = QLabel('')

rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

RadioGroupBox = QGroupBox("Варианты ответов")
layout_ans = QVBoxLayout()
layout_ans.addWidget(rbtn_1)
layout_ans.addWidget(rbtn_2)
layout_ans.addWidget(rbtn_3)
layout_ans.addWidget(rbtn_4)
RadioGroupBox.setLayout(layout_ans)

AnsGroupBox = QGroupBox("Результат теста")
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')
layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))

layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addWidget(btn_OK, stretch=2)
layout_line3.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

window = QWidget()
window.setWindowTitle('Memo Card')
window.resize(400, 200)
window.setLayout(layout_card)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

question_list = []
question_list.append(Question('Государственный язмик Бразилии', 'Португальский', 'Испанский', 'Бразильский', 'Итальянский'))
question_list.append(Question('Какого цвета нет на флаге России', 'Зелёный', 'Красный', 'Синий', 'Белый'))
question_list.append(Question('Столица Франции', 'Париж', 'Лондон', 'Берлин', 'Рим'))
question_list.append(Question('Что такое Python', 'Язык программирования', 'Змея', 'Фильм', 'Планета'))

correct_answers = 0
total_questions = 0
cur_question = -1 

btn_OK.clicked.connect(click_ok)

next_question()

window.show()
app.exec_()
