# Проект по автоматизации тестирования API сервиса "Яндекс.Самокат"

1. Основа для написания автотестов — фреймворк pytest.
2. Установить зависимости — pip install -r requirements.txt.
3. Команда для запуска всех тестов — pytest . 
4. Для формирования отчета в формате веб-страницы: allure serve allure_results

# Описание тестов: 

1. test_create_courier.py - проверка создание курьера
2. test_login_courier.py - проверка авторизации курьера 
3. test_delete_courier.py - проверка удаления курьера
4. test_create_order.py - проверка создания заказа
5. test_order_list.py - проверка полного списка заказов