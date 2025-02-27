# Описание проекта
Этот проект представляет собой CLI-клиент для отправки HTTP-запросов на сервер для отправки СМС-сообщений. Клиент использует конфигурационные файлы TOML для хранения настроек сервера и пользователей. После работы программы создаётся log-файл с параметрами командной строки и ответом сервиса.

# Структура проекта
### 1. client.py:
   Содержит класс Client, который отвечает за отправку СМС-сообщений на сервер. Использует объекты HttpRequest и HttpResponse для формирования и обработки запросов/ответов.
### 2. config.py:
   Обеспечивает загрузку конфигурации из TOML-файлов. Содержит классы UserConfig и ServerConfig для хранения настроек пользователей и сервера.
### 3. http_request.py:
   Определяет класс HttpRequest, который формирует HTTP-запросы для отправки на сервер.
### 4. http_response.py:
   Содержит класс HttpResponse, который обрабатывает ответы от сервера.
### 5. logger.py:
   Настройка логгера для записи событий в файл.
### 6. utils.py:
Содержит утилитные функции, такие как авторизационная кодировка и вывод результатов запросов.
### 7. main.py:
Точка входа для запуска CLI-клиента. Обрабатывает аргументы командной строки и запускает процесс отправки СМС.
### 8. config.toml:
Пример файла конфигурации, содержащий настройки сервера и пользователей.

# Как запустить проект
- Установка зависимостей:
  Для установки зависимостей, откройте терминал и введите:
  ```
  pip install -r requirements.txt

  ```

- Настройка конфигурации:
  Создайте файл `config.toml` в корне проекта с настройками сервера и пользователей.
  ``` python
  text
  title = 'configuration file for our program'

  [servers]
  [servers.server1]
  host = 'localhost'
  port = '4010'

  [users]
  [users.user1]
  username = 'user'
  password = 'qwerty123456'
  ```
- Запуск клиента:
  Выполните команду в терминале:

  ```
  python main.py <sender> <recipient> <message>
  
  ```
  Например:
  ```
  python main.py +71234567890 +70987654321 "Hello, world!"
  
  ```
- Пример вывода программы:
  ```
  Код ответа - 200
  Тело ответа - {"status":"success","message_id":"123456"}
  ```
