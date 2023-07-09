from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('About Uni 🏰', callback_data='en_about_uni'),
            InlineKeyboardButton('About Faculty 🏛', callback_data='en_about_faculty'),
        ],
        [
            InlineKeyboardButton('Scholarships and privileges 💴', callback_data='en_scholarships'),
        ],
        [
            InlineKeyboardButton('Timetable 📅',
                                 callback_data='en_timetable'),
            InlineKeyboardButton('Education 📚', callback_data='en_education'),
        ],
        [
            InlineKeyboardButton('Dormitories 🏠', callback_data='en_dormitories'),
            InlineKeyboardButton('Med. care 💊', callback_data='en_med_care'),
        ],
        [
            InlineKeyboardButton('For international students 🇺🇳', 
                                 callback_data='en_international_students'),
        ],
        [
            InlineKeyboardButton('Extracurricular activities 🏆', 
                                 callback_data='en_extracurricular_activities'),
        ],
        [
            InlineKeyboardButton('Informational resources 💻', 
                                 callback_data='en_informational_resources'),
        ]
    ]
)

faculty_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Location 🧭', callback_data='en_location'),
        ],
        [
            InlineKeyboardButton('Departments 🧐', callback_data='en_departments'),
            InlineKeyboardButton('Dean\'s Office 🎓', callback_data='en_deans_office')
        ],
        [
            InlineKeyboardButton('Our lecturers 👩‍🏫',
                                 callback_data='en_lecturers')
        ],
        [
            InlineKeyboardButton('Department of Youth Services 🐣', callback_data='en_youth')
        ],
        [
            InlineKeyboardButton('Study Department 📁', callback_data='en_study_department')
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main')
        ]
    ]
)

money_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('SPBU Scholarship ⚓️', callback_data='en_spbu_scholarship'),
        ],
        [
            InlineKeyboardButton('Financial aid 🛟', callback_data='en_financial_support'),
        ],
        [
            InlineKeyboardButton('Transportation Pass 🚌', callback_data='en_bsk'),
        ],
        [
            InlineKeyboardButton('Enhanced academic scholarship 📈',
                                 callback_data='en_enhanced_scholarship'),
        ],
        [
            InlineKeyboardButton('Social scholarship ✨',
                                 callback_data='en_social_scholarship'),
        ],
        [
            InlineKeyboardButton(f'Enhanced Social scholarship '
                                 '(1-2 year) 👶',
                                 callback_data='en_enhanced_social_scholarship'),
        ],
        [
            InlineKeyboardButton('Other scholarships 👽',
                                 callback_data='en_other_scholarships'),
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main'),
        ]
    ]
)
educ_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Foreign languages 🌏', 
                                 callback_data='en_foreign_languages'),
            InlineKeyboardButton('Internship 🛠', callback_data='en_internship'),
        ],
        [
            InlineKeyboardButton('Academic mobility 🛫', callback_data='en_academic_mobility'),
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main'),
        ]
    ]
)

med_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Medical checkup 👩‍⚕️', callback_data='en_medical_checkup'),
        ],
        [
            InlineKeyboardButton('First aid 🆘', callback_data='en_first_aid'),
        ],
        [
            InlineKeyboardButton('SPBU medical centres 🏨',
                                 callback_data='en_spbsu_medical_centres'),
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main'),
        ]
    ]
)

int_stud_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('International Students Club 🗺', 
                                 callback_data='en_international_students_club'),
        ],
        [
            InlineKeyboardButton(f'Rules of stay in Russia 🇷🇺', 
                                 callback_data='en_rules_of_stay'),
        ],
        [
            InlineKeyboardButton(f'Medical care for '
                                  'international students 👨‍⚕️', 
                                  callback_data='en_int_med_care'),
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main')
        ]
    ]
)

extracurricular_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('Student Council of SIR 🦊', 
                                 callback_data='en_student_council'),
        ],
        [
            InlineKeyboardButton('Student Scientific Society 🔬', callback_data='en_sno'),
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main')
        ]
    ]
)

info_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton('E-Library 🖥', callback_data='en_e_library'),
        ],
        [
            InlineKeyboardButton('Library 📚', callback_data='en_library'),
        ],
        [
            InlineKeyboardButton('Corporate mail ✉️', callback_data='en_corporate_mail'),
        ],
        [
            InlineKeyboardButton('Student\'s personal account 💼', 
                                 callback_data='en_account'),
        ],
        [
            InlineKeyboardButton('Blackboard SPBU ⬛️', callback_data='en_blackboard'),
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main')
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
                'Committees 👔', callback_data='en_committees'
            )
        ],
        [
            InlineKeyboardButton(
                'Membership 🙋', callback_data='en_membership'
            )
        ],
        [
            InlineKeyboardButton(
                'Competencies 👨‍💻', callback_data='en_competencies'
            )
        ],
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_extracurricular'
            )
        ]
    ]
)

dorm_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Getting a place 🛌', callback_data='en_getting_place'
            )
        ],
        [
            InlineKeyboardButton(
                'SPBU\'s dormitories 🏘', callback_data='en_spbsu_dorms'
            )
        ],
        [
            InlineKeyboardButton(
                'Payment for accommodation 🤲', callback_data='en_accommodation'
            )
        ],
        [   
            InlineKeyboardButton(
                'Getting the Internet 🌐', callback_data='en_internet'
            )
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main')
        ]
    ]
)

military_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Military registration 🗂', callback_data='en_military_registration'
            )
        ],
        [
            InlineKeyboardButton(
                'Applying for training 🫡', callback_data='en_training'
            )
        ],
        [
            InlineKeyboardButton(
                'How to get in 📝', callback_data='en_get_in'
            )
        ],
        [
            InlineKeyboardButton('Back ⏪', callback_data='en_back_to_main')
        ]

    ]
)

back_to_main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_main'
            )
        ],
    ]
)

back_to_fuc = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_fuc'
            )
        ],
    ]
)

back_to_money = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_money'
            )
        ],
    ]
)

back_to_educ = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_educ'
            )
        ],
    ]
)

back_to_dorm = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_dorm'
            )
        ],
    ]
)

back_to_med = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_med'
            )
        ],
    ]
)

back_to_int_stud = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_int_stud'
            )
        ],
    ]
)

back_to_extracurricular = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_extracurricular'
            )
        ],
    ]
)

back_to_council = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_council'
            )
        ],
    ]
)

back_to_info = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_info'
            )
        ],
    ]
)

back_to_military = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                'Back ⏪', callback_data='en_back_to_military'
            )
        ],
    ]
)