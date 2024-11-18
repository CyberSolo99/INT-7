from nicegui import ui
from datetime import datetime


# Функция обработки отправки формы
def submit_form():
    # Собираем данные из полей
    data = {
        "Дата сообщения": date_input.value,
        "Источник сообщения": source_input.value,
        "Название организации": organization_input.value,
        "Тип инцидента": incident_type_input.value,
        "Атакуемые IP-адреса": ip_addresses_input.value,
        "Комментарий": comment_input.value,  # Добавляем комментарий
    }
    # Отображаем уведомление с подтверждением отправки данных
    ui.notify(
        "Данные отправлены! Проверьте консоль для просмотра введённой информации."
    )
    print("Информация об инциденте:", data)

    # Очистка полей формы после отправки
    date_input.set_value("")
    source_input.set_value("")
    organization_input.set_value("")
    incident_type_input.set_value("")
    ip_addresses_input.set_value("")
    comment_input.set_value("")
    other_incident_type_input.set_value("")  # Очистка дополнительного поля


# Добавляем стиль для заднего фона
ui.add_head_html(
    """
    <style>
        body {
            background: linear-gradient(135deg, #4facfe, #00f2fe);
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
    ui.label("Форма заполнения информации об инциденте").style(
        "font-size: 28px; font-weight: bold; color: #333; margin-bottom: 20px; text-align: center;"
    )

    # Поле для ввода даты с календарем
    date_input = ui.date("Дата сообщения").style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )

    # Устанавливаем значение даты
    date_input.set_value(datetime.now().strftime("%Y-%m-%d"))

    # Поле для ввода источника сообщения
    source_input = ui.input(
        "Источник сообщения", placeholder="Название канала, форума или чата..."
    ).style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )

    # Поле для ввода названия организации-жертвы
    organization_input = ui.input(
        "Название организации",
        placeholder="Организация, на которую направлена угроза...",
    ).style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )

    # Поле для выбора типа инцидента
    incident_type_input = ui.select(
        ["DDoS-атака", "Утечка данных", "Взлом", "Фишинг", "Другое"],
        label="Тип инцидента",
        value="DDoS-атака",
    ).style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )

    # Поле для ввода другого типа инцидента (если выбрано "Другое")
    other_incident_type_input = ui.input(
        "Укажите другой тип инцидента",
        placeholder="Введите тип инцидента...",
    ).style(
        "margin-bottom: 15px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7; display: none;"
    )

    # Показать поле для ввода другого типа инцидента, если выбран "Другое"
    def show_other_type_input():
        if incident_type_input.value == "Другое":
            other_incident_type_input.style("display: block;")
        else:
            other_incident_type_input.style("display: none;")

    incident_type_input.on("change", show_other_type_input)

    # Поле для ввода атакуемых IP-адресов
    ip_addresses_input = ui.input(
        "Атакуемые IP-адреса",
        placeholder="Введите атакуемые IP-адреса, если известны...",
    ).style(
        "margin-bottom: 25px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )

    # Добавляем поле для комментариев
    comment_input = ui.input(
        "Комментарий",
        placeholder="Введите комментарий...",
    ).style(
        "margin-bottom: 25px; padding: 10px; border-radius: 8px; border: 1px solid #ccc; font-size: 16px; width: 100%; background-color: #f7f7f7;"
    )

    # Кнопка для отправки формы с улучшенным дизайном
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
