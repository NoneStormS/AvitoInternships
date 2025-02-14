## Запуск автотестов

### macOS/Linux

1. Установите виртуальное окружение:
   ```sh
   python3.10 -m venv venv
   ```

2. Активируйте виртуальное окружение:
   ```sh
   source venv/bin/activate
   ```

3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```

4. Запустите тесты:
   ```sh
   pytest task_2_1/test/test.py
   ```
   ```sh
   pytest task_2_2/test.py
   ```

---

### Windows

1. Установите виртуальное окружение:
   ```sh
   python -m venv venv
   ```

2. Активируйте виртуальное окружение:
   ```sh
   venv\Scripts\activate
   ```

3. Установите зависимости:
   ```sh
   pip install -r requirements.txt
   ```

4. Запустите тесты:
   ```sh
   pytest task_2_1/test/test.py
   ```
   ```sh
   pytest task_2_2/test.py
   ```
