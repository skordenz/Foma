from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('О ВУЗе 🏰', callback_data='btn1'),
            InlineKeyboardButton('О факультете 🏛', callback_data='btn2'),
        ],
        [
            InlineKeyboardButton('Стипендии и льготы 💴', callback_data='btn3'),
        ],
        [
            InlineKeyboardButton('Расписание 📅', 
                                 callback_data='btn4'),
            InlineKeyboardButton('Учёба 📚', callback_data='btn5'),
        ],
        [
            InlineKeyboardButton('Общежития 🏠', callback_data='btn6'),
            InlineKeyboardButton('Мед. помощь 💊', callback_data='btn7'),
        ],
        [
            InlineKeyboardButton('Иностранным студентам 🇺🇳', callback_data='btn8'),
        ],
        [
            InlineKeyboardButton('Внеучебная деятельность 🏆', callback_data='btn9'),
        ],
        [
            InlineKeyboardButton('Информационные ресурсы 💻', callback_data='btn10'),
        ],
        [
            InlineKeyboardButton('Военный учёт и военная кафедра 🪖', callback_data='btn11'),
        ]
    ]
)

faculty_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Расположение 🧭', callback_data='btn12'),
        ],
        [
            InlineKeyboardButton('Кафедры 🧐', callback_data='btn13'),
            InlineKeyboardButton('Деканат 🎓', callback_data='btn14')
        ],
        [
            InlineKeyboardButton('Наши преподаватели 👩‍🏫',
                                 callback_data='btn15')
        ],
        [
            InlineKeyboardButton('Управление по работе с молодежью 🐣', callback_data='btn16')
        ],
        [
            InlineKeyboardButton('Учебный отдел 📁', callback_data='btn17')
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main')
        ]
    ]
)

money_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Стипендия СПбГУ ⚓️', callback_data='btn19'),
        ],
        [
            InlineKeyboardButton('Мат. помощь 🛟', callback_data='btn51'),
        ],
        [
            InlineKeyboardButton('БСК 🚌', callback_data='btn52'),
        ],
        [
            InlineKeyboardButton('Повышенная академическая стипендия 📈',
                                 callback_data='btn18'),
        ],
        [
            InlineKeyboardButton('Социальная стипендия ✨',
                                 callback_data='btn20'),
        ],
        [
            InlineKeyboardButton(f'Повышенная соц.'
                                 'стипендия (1-2 курс) 👶',
                                 callback_data='btn21'),
        ],
        [
            InlineKeyboardButton(f'Именные стипендии 👨‍🎓', callback_data='btn22'),
        ],
        [
            InlineKeyboardButton('Иные стипендии 👽',
                                 callback_data='btn23'),
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main'),
        ]
    ]
)
educ_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Иностранные языки 🌏', callback_data='btn24'),
            InlineKeyboardButton('Практика 🛠', callback_data='btn25'),
        ],
        [
            InlineKeyboardButton('Академическая мобильность 🛫', callback_data='btn26'),
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main'),
        ]
    ]
)

med_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Медицинский осмотр 👩‍⚕️', callback_data='btn27'),
        ],
        [
            InlineKeyboardButton('Первичная мед. помощь 🆘', callback_data='btn28'),
        ],
        [
            InlineKeyboardButton('Список здравпунктов СПбГУ 🏨', callback_data='btn29'),
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main'),
        ]
    ]
)

int_stud_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Клуб иностранных обучающихся 🗺', callback_data='btn30'),
        ],
        [
            InlineKeyboardButton(f'Правила пребывания в РФ 🇷🇺', callback_data='btn31'),
        ],
        [
            InlineKeyboardButton(f'Мед. помощь для '
                                  'иностранных обучающихся 👨‍⚕️', callback_data='btn32'),
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main')
        ]
    ]
)

extracurricular_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Студенческий совет ФМО 🦊', callback_data='btn33'),
        ],
        [
            InlineKeyboardButton('Стартапы 📈', callback_data='btn34'),
        ],
        [
            InlineKeyboardButton('Студенческое научное общество 🔬', callback_data='btn35'),
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main')
        ]
    ]
)

info_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Электронная библиотека 🖥', callback_data='btn36'),
        ],
        [
            InlineKeyboardButton('Библиотека 📚', callback_data='btn37'),
        ],
        [
            InlineKeyboardButton('Корпоративная почта ✉️', callback_data='btn38'),
        ],
        [
            InlineKeyboardButton('Личный кабинет обучающегося 💼', callback_data='btn39'),
        ],
        [
            InlineKeyboardButton('Blackboard СПбГУ ⬛️', callback_data='btn50'),
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main')
        ]
    ]
)

scholarship_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                f'Стипендии Правительства и '
                f'Президента РФ для '
                f'обучающихся по приоритетным '
                f'направлениям или'
                f'специальностям',
                url='https://clck.ru/34Fivh'
            )
        ],
        [
            InlineKeyboardButton(
                f'Стипендии Правительства РФ, '
                 'Президента РФ, Персональные '
                 'стипендии для студентов и '
                 'аспирантов',
                 url='https://clck.ru/34FkBp'
            )
        ],
        [
            InlineKeyboardButton(
                f'Именные стипендии '
                 'Правительства Санкт-Петербурга',
                 url='https://clck.ru/34FkDU'
            )
        ],
        [
            InlineKeyboardButton(
                f'Именная стипендия академика '
                 'С.П. Меркурьева',
                 url='https://clck.ru/enwzo'
            )
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main')
        ]
    ]
)

fmo_students_council_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Комитеты 👔', callback_data='btn40'
            )
        ],
        [
            InlineKeyboardButton(
                'Членство 🙋', callback_data='btn41'
            )
        ],
        [
            InlineKeyboardButton(
                'Компетенции 👨‍💻', callback_data='btn42'
            )
        ],
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_extracurricular'
            )
        ]
    ]
)

dorm_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Получение места 🛌', callback_data='btn43'
            )
        ],
        [
            InlineKeyboardButton(
                'Общежития СПбГУ 🏘', callback_data='btn44'
            )
        ],
        [
            InlineKeyboardButton(
                'Оплата проживания 🤲', callback_data='btn45'
            )
        ],
        [   
            InlineKeyboardButton(
                'Подключение интернета 🌐', callback_data='btn46'
            )
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main')
        ]
    ]
)

military_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Воинский учёт 🗂', callback_data='btn47'
            )
        ],
        [
            InlineKeyboardButton(
                'Право на обучение в ВУЦ 🫡', callback_data='btn48'
            )
        ],
        [
            InlineKeyboardButton(
                'Как поступить в ВУЦ 📝', callback_data='btn49'
            )
        ],
        [
            InlineKeyboardButton('Назад ⏪', callback_data='back_to_main')
        ]

    ]
)

back_to_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_main'
            )
        ],
    ]
)

back_to_fuc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_fuc'
            )
        ],
    ]
)

back_to_money = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_money'
            )
        ],
    ]
)

back_to_educ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_educ'
            )
        ],
    ]
)

back_to_dorm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_dorm'
            )
        ],
    ]
)

back_to_med = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_med'
            )
        ],
    ]
)

back_to_int_stud = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_int_stud'
            )
        ],
    ]
)

back_to_extracurricular = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_extracurricular'
            )
        ],
    ]
)

back_to_council = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_council'
            )
        ],
    ]
)

back_to_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_info'
            )
        ],
    ]
)

back_to_military = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Назад ⏪', callback_data='back_to_military'
            )
        ],
    ]
)

starting_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('RUS 🇷🇺', callback_data='ru_lang'),
            InlineKeyboardButton('ENG 🇬🇧', callback_data='en_lang')
        ]
    ]
)
