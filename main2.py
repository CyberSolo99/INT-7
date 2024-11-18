from nicegui import ui
from datetime import datetime


# Функция проверки заполненности обязательных полей
def validate_form():
    all_fields_filled = True
    if not group_name_input.value:
        group_name_error.set_text("Название группировки обязательно").style(
            "color: red;"
        )
        all_fields_filled = False
    else:
        group_name_error.set_text("")

    if not organizations_input.value:
        organizations_error.set_text(
            "Названия атакуемых организаций обязательны"
        ).style("color: red;")
        all_fields_filled = False
    else:
        organizations_error.set_text("")

    if not attack_method_input.value:
        attack_method_error.set_text("Метод атаки обязателен").style("color: red;")
        all_fields_filled = False
    else:
        attack_method_error.set_text("")

    if not attack_date_input.value:
        attack_date_error.set_text("Дата атаки обязательна").style("color: red;")
        all_fields_filled = False
    else:
        attack_date_error.set_text("")

    if not all_fields_filled:
        ui.notify("Пожалуйста, заполните все обязательные поля!", color="red")
        return False

    return True


# Функция обработки отправки формы
def submit_form():
    if not validate_form():
        return

    # Собираем данные из полей
    data = {
        "Название группировки": group_name_input.value,
        "Названия атакуемых организаций": organizations_input.value,
        "Метод атаки": (
            attack_method_input.value if attack_method_input.value else "Не выбран"
        ),
        "Дата атаки": attack_date_input.value,
        "Комментарий": comment_input.value,
    }
    # Отображаем уведомление с подтверждением отправки данных
    ui.notify(
        "Данные отправлены! Проверьте консоль для просмотра введённой информации."
    )
    print("Информация о атаке:", data)

    # Очистка полей формы после отправки
    group_name_input.set_value("")
    organizations_input.set_value("")
    attack_method_input.set_value(None)
    attack_date_input.set_value("")
    comment_input.set_value("")


# Добавляем стиль для заднего фона
ui.add_head_html(
    """
    <style>
        body {
            background: linear-gradient(135deg, #f6d365, #fda085);
            margin: 0;
            font-family: Arial, sans-serif;
        }
    </style>
    """
)

# Создаём интерфейс формы
with ui.column().style(
    "max-width: 500px; margin: auto; padding: 20px; background-color: #ffffff; border-radius: 12px; box-shadow: 0 6px 10px rgba(0,0,0,0.15); margin-top: 100px;"
):
    # Заголовок формы
    ui.label("Форма заполнения информации об атаке").style(
        "font-size: 28px; font-weight: bold; color: #333; margin-bottom: 20px; text-align: center;"
    )

    # Поле для ввода названия группировки
    group_name_input = ui.input(
        "Название группировки", placeholder="Введите название группы..."
    ).style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )
    group_name_error = ui.label("").style("color: red; margin-bottom: 10px;")

    # Поле для ввода названий атакуемых организаций
    organizations_input = ui.input(
        "Названия атакуемых организаций",
        placeholder="Введите названия компаний через запятую...",
    ).style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )
    organizations_error = ui.label("").style("color: red; margin-bottom: 10px;")

    # Поле для выбора метода атаки
    attack_method_input = ui.select(
        ["Фишинг", "DDoS-атака", "Взлом", "Утечка данных", "Другое"],
        label="Метод атаки",
        value=None,
    ).style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )
    attack_method_error = ui.label("").style("color: red; margin-bottom: 10px;")

    # Поле для ввода другого метода атаки (если выбрано 'Другое')
    other_attack_method_input = ui.input(
        "Укажите другой метод атаки", placeholder="Введите метод атаки..."
    ).style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7; display: none;"
    )

    # Показать поле для ввода другого метода атаки, если выбран 'Другое'
    def show_other_method_input():
        if attack_method_input.value == "Другое":
            other_attack_method_input.style("display: block;")
        else:
            other_attack_method_input.style("display: none;")

    attack_method_input.on("change", show_other_method_input)

    # Поле для ввода даты атаки
    attack_date_input = ui.date("Дата атаки").style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )
    attack_date_error = ui.label("").style("color: red; margin-bottom: 10px;")

    # Устанавливаем значение даты по умолчанию на текущую
    attack_date_input.set_value(datetime.now().strftime("%Y-%m-%d"))

    # Поле для ввода комментариев
    comment_input = ui.input(
        "Комментарий", placeholder="Введите комментарий (необязательно)..."
    ).style(
        "margin-bottom: 25px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )

    # Кнопка для отправки формы
    submit_button = ui.button("Отправить", on_click=submit_form).style(
        "background-color: #007BFF; color: white; padding: 15px 20px; font-size: 18px; border: none; border-radius: 8px; cursor: pointer; width: 100%; transition: 0.3s; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.15);"
    )

    # Изменение цвета кнопки при наведении
    submit_button.on(
        "mouseenter", lambda: submit_button.style("background-color: #0056b3;")
    )
    submit_button.on(
        "mouseleave", lambda: submit_button.style("background-color: #007BFF;")
    )

ui.run()
