import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
load_dotenv()

email_from = os.environ.get('EMAIL_FROM')
password = os.environ.get('PASSWORD')
email_to = os.environ.get('EMAIL_TO')

message_text = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!
%website% — это новая версия онлайн-курса по программированию.
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя.

Как будет проходить ваше обучение на %website%?
→ Попрактикуешься на реальных кейсах.

Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей.
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.

→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят.
Регистрируйся → %website%

На модули, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""
replacement = message_text.replace('%friend_name%', 'Максим')
replacement = replacement.replace('%my_name%', 'Руслан')
replacement = replacement.replace('%website%', 'https://dvmn.org/profession-ref-program/tatarin08.96/prjNs/')

message = MIMEMultipart()
message['From'] = email_from
message['To'] = email_to
message['Subject'] = "Важно!"

message.attach(MIMEText(replacement, 'plain', 'utf-8'))

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(email_from, password)
server.send_message(message)
server.quit()
