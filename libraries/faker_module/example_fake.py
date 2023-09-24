from faker import Faker

# Создаем экземпляр Faker
fake = Faker()  # по умолчанию en-US
fake_ru = Faker("ru_RU")  # русский
fake_en_ua_ru = Faker(["en_US", "uk_UA", "ru_RU"])  # на нескольких языках

# Генерируем случайное имя
name = fake.name()
name_ru = fake_ru.name()
print(f"Имя: {name}")
print(f"Имя: {name_ru}")

# Генерируем случайные профайлы
print(f"{fake.profile() = }")
print(f"{fake.simple_profile() = }")

# Генерируем случайный адрес
address = fake.address()
address_ru = fake_ru.address()
print(f"Адрес: {address}")
print(f"Адрес: {address_ru}")

# Генерируем случайный адрес электронной почты
email = fake.email()
email_ru = fake_ru.email()
print(f"Email: {email}")
print(f"Email: {email_ru}")

# Генерируем случайный номер телефона
phone_number = fake.phone_number()
phone_number_ru = fake_ru.phone_number()
print(f"Номер телефона: {phone_number}")
print(f"Номер телефона: {phone_number_ru}")

# Генерируем случайный текст
text = fake.text()
text_ru = fake_ru.text()
print(f"Текст: {text}")
print(f"Текст: {text_ru}")

# Генерируем случайную профессию
job = fake.job()
job_ru = fake_ru.job()
print(f"Профессия: {job}")
print(f"Профессия: {job_ru}")

# Генерируем случайную пути
file_path = fake.file_path()
print(f"Путь: {file_path}")


# Генерируем случайную кредитную карту
credit_card = fake.credit_card_number()
card_date = fake.credit_card_expire()
card_code = fake.credit_card_security_code()
print(f"Номер кредитной карты: {credit_card} Дата: {card_date} Секретный код: {card_code}")

# Генерируем случайный цвет
color_hex = fake.hex_color()
color_rgb = fake.rgb_color()
print(f"hex color: {color_hex}")
print(f"rgb color: {color_rgb}")
