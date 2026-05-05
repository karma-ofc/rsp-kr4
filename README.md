# RSP KR4 Project
Установка зависимостей: pip install fastapi uvicorn[standard] pydantic httpx pytest pytest-asyncio faker

Запуск приложения: uvicorn main:app --reload

Команды для тестирования ключевых сценариев:

Синхронные тесты (test_main.py): pytest test_main.py -v

Асинхронные тесты (test_main_async.py): pytest test_main_async.py -v --asyncio-mode=auto

Задание 9.1 Была применена первоначальная миграция к базе данных, таблица Product вместе с полями "id", "title", "price" и "count" успешно создалась
<img width="825" height="129" alt="image" src="https://github.com/user-attachments/assets/227d2783-9181-47b8-baff-6672d7802be3" />
Добавлены две записи в таблицу
<img width="680" height="167" alt="{5905C94E-B5D1-48AF-9396-31D677139937}" src="https://github.com/user-attachments/assets/5ca3f7db-46fa-4e7a-9975-f7d58dee8d70" />
Добавлено новое поле "description" (not null) к сущности "Product", сгенерирован новый сценарий миграции через Alembic, применена новая миграция к базе данных
<img width="1094" height="214" alt="{D128EED1-A074-4633-9B9F-E8273595ACCC}" src="https://github.com/user-attachments/assets/33f93f3e-361b-4a78-847e-b1a1cd4ed88b" />
Задание 10.1 Создано приложение FastAPI, настроены пользовательские классы исключений (CustomExceptionA, CustomExceptionB), Зарегистрированы пользовательские обработчики исключений, определены модели реагирования на ошибки (Pydantic), созданы две конечные точки API
Тест (GET) /trigger-a со (status 400)
<img width="1429" height="897" alt="{C53B8986-336B-4142-8913-7B8357CF60BA}" src="https://github.com/user-attachments/assets/b6e92b50-49be-460a-800f-1ccf5383491a" />
Тест успешного (GET) /trigger-a со (status 200)
<img width="1408" height="867" alt="{5C70F7EB-E3B2-4461-A8FB-690CA7663E40}" src="https://github.com/user-attachments/assets/781492c9-5d2b-4c6f-ae72-4428de4d7f2a" />
Тест (GET) /trigger-b/{item_id} (status 404)
<img width="1400" height="882" alt="{96FC19E8-6D9B-485D-B686-563D644E1C9D}" src="https://github.com/user-attachments/assets/7b03a0c8-91dc-4298-84e3-a2aec2e4be8b" />
Тест успешного (GET) /trigger-b/{item_id} со (status 200)
<img width="1416" height="903" alt="{AFA86D90-263E-4895-A327-407F4A002EBE}" src="https://github.com/user-attachments/assets/b99b1c87-6a2b-4147-b940-5e392ff96bdd" />
Задание 10.2 Создано FastAPI-приложение с моделью Pydantic User, обеспечивающей строгую валидацию входящих данных (возраст, email, пароль).
Тест (POST) /users с корректными данными (status 200)
<img width="1429" height="630" alt="{1E08571B-5134-477D-AE81-E92D7685113A}" src="https://github.com/user-attachments/assets/354017fa-307b-472e-8bfc-250b9d748b40" />
<img width="1447" height="726" alt="{17ADFCF1-9238-41BB-8A54-67E11A296C8E}" src="https://github.com/user-attachments/assets/ca2ad6d4-0c7e-466a-9f74-118ce79edae8" />
Тест (POST) /users с вводом неверного age (<19) (status 422)
<img width="1420" height="707" alt="{7C284C98-AC45-4617-BBAC-1A0D45457B13}" src="https://github.com/user-attachments/assets/2083083c-3bcf-48a8-8e9b-74e41cbfc945" />
<img width="1430" height="818" alt="{950ED962-8B73-41BF-986B-180873BC9320}" src="https://github.com/user-attachments/assets/b0063407-788a-44e5-872c-31ca4fc92c99" />
Тест (POST) /users с вводом неверного email (status 422)
<img width="1419" height="720" alt="{F84506EA-16FB-4DBE-8AAD-6DF8E44C4178}" src="https://github.com/user-attachments/assets/e0bd9b9a-a5a9-433a-877b-39184adc9c37" />
<img width="1480" height="764" alt="{79F2AAB1-99AA-4851-9F1E-56C55BCB54AD}" src="https://github.com/user-attachments/assets/22e681d4-9ca9-43db-b58b-b26fadf01203" />
Тест (POST) /users с вводом короткого пароля (status 422)
<img width="1436" height="731" alt="image" src="https://github.com/user-attachments/assets/633b4590-ed60-4b91-a60e-61ed375e0167" />
<img width="1378" height="903" alt="{22FDF93D-985B-40A9-9C8C-0808ADE2D0EE}" src="https://github.com/user-attachments/assets/bdd75551-e461-4288-bae2-85a87ab7b00c" />
Тест (POST) /users с вводом слишком длинного пароля (status 422)
<img width="1396" height="788" alt="{C61CFF2A-D681-411A-958E-F5A9B80F7DAC}" src="https://github.com/user-attachments/assets/825d059f-4b0a-4fc9-854c-908fcc0dc48d" />
<img width="1427" height="900" alt="{0FFBF0A8-F3A3-464E-A419-37BA3F08529E}" src="https://github.com/user-attachments/assets/a1e7f6b6-ac83-46a1-965e-dc0837afda9a" />
Тест (POST) /users с отсутствием обязательного поля возраста (status 422)
<img width="1428" height="759" alt="{3FA29E40-0C05-49A0-BD55-637643543D79}" src="https://github.com/user-attachments/assets/130348ef-e9d1-467c-9897-f7d6f2a4fe66" />
<img width="1430" height="897" alt="{E0E0FA85-93EC-403F-A93F-89B6A219C019}" src="https://github.com/user-attachments/assets/7fee0b8e-ce21-4311-8c91-77c7f6cf378e" />
Задание 11.1 Настроено приложение FastAPI с тремя конечными точками API

Модульные тесты для post /USERS

test_create_user_success (успешное создание с валидными данными).
test_create_user_age_too_low (ошибка валидации: age <= 18).
test_create_user_invalid_email (ошибка валидации: некорректный email).
test_create_user_password_too_short (ошибка валидации: пароль < 8 символов).
test_create_user_password_too_long (ошибка валидации: пароль > 16 символов). Get /users/{user_id}
test_get_user_success (успешное получение существующего пользователя).
test_get_user_not_found (ошибка 404: пользователь не найден). DELETE /users/{user_id}
test_delete_user_success (успешное удаление и проверка, что он исчез).
test_delete_user_not_found (ошибка 404: пользователь не найден).
<img width="1026" height="502" alt="{A3CAE681-3C58-4243-89DC-7B4C1FB9FDD4}" src="https://github.com/user-attachments/assets/d89d4f78-394f-4192-8aae-d015eeff15fd" />

Задание 11.2 Подготовлено окружение, установлены все необходимы зависимости, написаны асинхронные тесты для всех 3х эндпоинтов, сгенерированы данные через Faker, обеспечено чистое состояние между тестами.

Асинхронные тесты post /USERS
test_create_user (Тест успешного создания пользователя)
test_create_user_age_too_low (Тест валидации возраста)
test_create_user_invalid_email (Тест валидации email)
test_create_user_password_too_short (Тест ошибки валидации: пароль < 8 символов).
test_create_user_password_too_long (Тест валидации: пароль > 16 символов). Get /users/{user_id}
test_get_user_success (Тест успешного получения существующего пользователя)
test_get_user_not_found (Тест получения несуществующего пользователя) DELETE /users/{user_id}
test_delete_user_success (Тест успешного удаления пользователя)
test_delete_user_not_found (Тест удаления несуществующего пользователя)
<img width="1037" height="488" alt="{CBB2D811-72C6-4B6B-8BA7-209F766E4E2F}" src="https://github.com/user-attachments/assets/71dec3c6-0981-4cc4-833d-13c353e410c1" />
