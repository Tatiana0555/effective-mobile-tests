# UI tests for effective-mobile.ru 

Набор UI-тестов, реализованный с использованием Playwright, Pytest и паттерна Page Object Model.
Поддерживается локальный запуск, запуск в Docker-контейнере и генерация Allure-отчётов.

---

## 📂 Структура проекта
```
effective-mobile-tests/
│
├── pages/                    # Page Object Model
│   └── footer_page.py
│
├── tests/                    # UI-тесты
│   └── test_main_page.py
│
├── conftest.py               # Pytest фикстуры
├── requirements.txt          # Зависимости
├── pytest.ini                # Настройки Pytest
├── Dockerfile                # Docker-образ для CI/локального запуска
└── README.md
```

## 🚀 Установка и запуск локально

### 1. Клонировать репозиторий
```git clone https://github.com/Tatiana0555/effective-mobile-tests.git```

```cd effective-mobile-tests```

### 2. Создать виртуальное окружение
```python -m venv venv```

```venv\Scripts\activate```     # Windows

```# source venv/bin/activate```   # Linux/Mac

### 3. Установить зависимости
```pip install -r requirements.txt```

### 4. Установить браузеры Playwright
```playwright install```

### 5. Запуск тестов
```pytest -v```

### 6. Запуск с открытием браузера
```pytest --headed```

## 📊 Allure-отчёты

### 1. Сгенерировать Allure результаты
```pytest --alluredir=allure-results```

### 2. Построить и открыть отчёт
```allure serve allure-results```

## 🐳 Запуск в Docker
### 1. Собрать образ

```docker build -t effective-mobile-tests .```

### 2. Запустить тесты в контейнере

```docker run --rm effective-mobile-tests```

### Allure-результаты можно вывести наружу:

```docker run --rm -v %cd%/allure-results:/app/allure-results effective-mobile-tests```

## ✔️ Основной стек
Python 3.10

Playwright (UI-автотесты)

Pytest

Allure (отчёты)

Docker (контейнеризация, CI)
