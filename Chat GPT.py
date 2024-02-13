import sys
import openai
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton

# Установите ключ API OpenAI
openai.api_key = "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"

def generate_response  ( prompt ): # Используйте модель ChatGPT для генерации ответа     model_engine = "text-davinci - 002"     Prompt = ( f" {prompt} \n" )     Completes = openai.Completion.create(engine=model_engine, Prompt= подсказка, max_tokens= 1024 , n= 1 , stop= None , температура= 0,5 )     message =completes.choices[ 0 ].text return message.strip()

    class  ChatWindow ( QWidget ):
        def  __init__ ( self ):
            super ().__init__()

        # Создаем QTextEdit для отображения разговора
            self.conversation = QTextEdit(self)
            self.conversation.setReadOnly( True )
            self.setWindowTitle( "ChatGPT" )

        # Создаём QLineEdit для ввода сообщений
            self.message_input = QLineEdit(self)
            self.message_input.returnPressed.connect(self.send_message)

        # Создаём QPushButton для отправки сообщений
            self.send_button = QPushButton( "Send" , self)
            self.send_button .clicked.connect(self.send_message)

        # Создайте QHBoxLayout для хранения кнопки ввода и отправки сообщения
            self.input_layout = QHBoxLayout()
            self.input_layout.addWidget(self.message_input)
            self.input_layout.addWidget(self.send_button)

        # Создать QVBoxLayout для хранения диалога и макета ввода
            self.layout = QVBoxLayout(self)
            self.layout.addWidget(self.conversation)
            self.layout.addLayout(self.input_layout)

        def  send_message ( self ):
        # Получить сообщение пользователя
            message = self.message_input.text()

        # Очистка поля ввода сообщения
            self.message_input.clear()

        # Добавляем сообщение пользователя в диалог
            self.conversation.append( "You: " + message)

        # Генерируем ответ
            response=generate_response(message )

        # Добавляем ответ бота к разговору
            self.conversation.append( "Bot: " + response)

    def  main ():
    # Создаём экземпляр QApplication
        app = QApplication(sys.argv)

    # Создаём экземпляр ChatWindow и показываем его
        window = ChatWindow()
        window.show()

    # Запускаем цикл событий приложения
        sys.exit(app.exec_())

    if __name__ == "__main__":
        main()

