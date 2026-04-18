# Запуск проекта

## Установка и настройка виртуального окружения

```bash
cd backend/
python -m venv venv
```
**Что делает**
- `cd backend/` - переходит в папку `backend`
-`python -m venv venv` - создает виртуальное окружение Python в папке `venv`. Это изолирует зависимости проекта от глобальных пакетов.

## Активация окружения
```bash
# Windows:
source venv/Scripts/activate
# Linux/Mac:
source venv/bin/avtivate
```
**Что делает:**
- Активирует виртуальное окружение. После активации в терминале появится `(venv)`.
 

 ## Установка зависимостей
 ```bash
 pip install -r requirements.txt
 ```

 **Что делает:**
 - Устанавливает все пакеты из файла `requirements.txt` (Django и др.).

**Как запустить сервер:**
-python manage.py runserver