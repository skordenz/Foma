import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import InputFile, InputMediaPhoto

import keyboard.main_menu as kb
import keyboard.main_en_menu as kb_en
from template_engine import render_template

print(os.getcwd())

bot = Bot(token='TOKEN', parse_mode='HTML')
dp = Dispatcher(bot)


########  Функционал кнопок ###########
@dp.callback_query_handler(lambda x: x.data == 'back_to_main' or x.data == 'ru_lang')
async def process_callback_button10(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNFkbvr2ZPozlCEEPe4GWwABwu91-_AAAhMwAAKIJ3BLpfPrD8pXU1kvBA',
    )
    await bot.send_message(
        callback_query.from_user.id, 
        text='Главное меню 🐈',
        reply_markup=kb.main_menu,
        disable_web_page_preview=True
    )

@dp.callback_query_handler(lambda x: x.data == 'en_back_to_main' or x.data == 'en_lang')
async def process_callback_button10(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNFkbvr2ZPozlCEEPe4GWwABwu91-_AAAhMwAAKIJ3BLpfPrD8pXU1kvBA',
    )
    await bot.send_message(
        callback_query.from_user.id, 
        text='Main menu 🐈',
        reply_markup=kb_en.main_menu,
        disable_web_page_preview=True
    )

@dp.callback_query_handler(lambda x: x.data == 'btn1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = render_template(
        'about_spbu.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=f'{text}',
        reply_markup=kb.back_to_main,
        disable_web_page_preview=True
    )

@dp.callback_query_handler(lambda x: x.data == 'en_about_uni')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = render_template(
        'about_spbu_en.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=f'{text}',
        reply_markup=kb_en.back_to_main,
        disable_web_page_preview=True
    )

#____________  О факультете ________________
@dp.callback_query_handler(lambda x: x.data == 'btn2' or x.data == 'back_to_fuc')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = render_template(
        'about_fmo.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id, 
        text=f'{text}',
        reply_markup=kb.faculty_menu,
        disable_web_page_preview=True
    )

FUC = {
    'btn12': 'about_fmo_location.html',
    'btn13': 'about_fmo_departments.html',
    'btn14': 'dean.html',
    'btn15': 'lecturers.html',
    'btn16': 'youth_office.html',
    'btn17': 'student_office.html'
}

async def process_callback_button1(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = FUC.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb.back_to_fuc,
            disable_web_page_preview=True
        )

for callback in FUC:
    dp.register_callback_query_handler(
        process_callback_button1, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

@dp.callback_query_handler(lambda x: x.data == 'en_about_faculty' or x.data == 'en_back_to_fuc')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = render_template(
        'about_fmo_en.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id, 
        text=f'{text}',
        reply_markup=kb_en.faculty_menu,
        disable_web_page_preview=True
    )


EN_FUC = {
    'en_location': 'about_fmo_location_en.html',
    'en_departments': 'about_fmo_departments_en.html',
    'en_deans_office': 'dean_en.html',
    'en_lecturers': 'lecturers_en.html',
    'en_youth': 'youth_office_en.html',
    'en_study_department': 'student_office_en.html'
}

async def about_fmo_en(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EN_FUC.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb_en.back_to_fuc,
            disable_web_page_preview=True
        )

for callback in EN_FUC:
    dp.register_callback_query_handler(
        about_fmo_en, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )
#_____________________________________________________

#____________  Стипендия и льготы ________________
@dp.callback_query_handler(lambda x: x.data == 'btn3' or x.data == 'back_to_money')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id, 
        text='Стипендии и льготы 💴',
        reply_markup=kb.money_menu,
        disable_web_page_preview=True
    )

MONEY = {
    'btn19': 'scholarship_spbu.html',
    'btn51': 'money_aid.html',
    'btn52': 'bsk.html',
    'btn18': 'scholarship_enhanced.html',
    'btn20': 'scholarship_social.html',
    'btn21': 'scholarship_enhanced_social.html',
    'btn22': 'scholarship.html',
    'btn23': 'scholarship_other.html'
}

async def process_callback_button2(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = MONEY.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb.back_to_money,
            disable_web_page_preview=True
        )

for callback in MONEY:
    dp.register_callback_query_handler(
        process_callback_button2, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

@dp.callback_query_handler(lambda x: x.data == 'en_scholarships' or x.data == 'en_back_to_money')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id, 
        text='Scholarships and privileges 💴',
        reply_markup=kb_en.money_menu,
        disable_web_page_preview=True
    )

EN_MONEY = {
    'en_spbu_scholarship': 'scholarship_spbu_en.html',
    'en_financial_support': 'money_aid_en.html',
    'en_bsk': 'bsk_en.html',
    'en_enhanced_scholarship': 'scholarship_enhanced_en.html',
    'en_social_scholarship': 'scholarship_social_en.html',
    'en_enhanced_social_scholarship': 'scholarship_enhanced_social_en.html',
    'en_endowed_scholarships': 'scholarship_en.html',
    'en_other_scholarships': 'scholarship_other_en.html'
}

async def money_en(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EN_MONEY.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb_en.back_to_money,
            disable_web_page_preview=True
        )

for callback in EN_MONEY:
    dp.register_callback_query_handler(
        money_en, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )
#_______________________________________________________

#____________________Расписание_________________________
@dp.callback_query_handler(lambda x: x.data == 'btn4')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = render_template(
        'timetable.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=f'{text}',
        reply_markup=kb.back_to_main,
        disable_web_page_preview=True
    )

@dp.callback_query_handler(lambda x: x.data == 'en_timetable')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = render_template(
        'timetable_eng.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=f'{text}',
        reply_markup=kb_en.back_to_main,
        disable_web_page_preview=True
    )
#_____________________________________________________

#___________________  Учеба __________________________
@dp.callback_query_handler(lambda x: x.data == 'btn5' or x.data == 'back_to_educ')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNNkbvr9ywnqkVU4jHqQDVWXNa4FuwACfjMAAq-NcUtvqCWa9bQG0C8E'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Учеба 📚',
        reply_markup=kb.educ_menu
    )

STUDY = {
    'btn24': 'foreign_languages.html',
    'btn25': 'internship.html',
    'btn26': 'academic_mobility.html',
}

async def process_callback_button3(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = STUDY.get(callback_data)
    if template:
        if template == 'internship.html':
            photo_path1 = os.path.join(os.getcwd(), 'bot_fmo', 'img', 'int_types.png')
            photo_path2 = os.path.join(os.getcwd(), 'bot_fmo', 'img', 'int_kinds.png')
            fs_photo1 = InputFile(photo_path1)
            fs_photo2 = InputFile(photo_path2)

            await bot.send_photo(callback_query.from_user.id, photo=fs_photo1)
            await bot.send_photo(callback_query.from_user.id, photo=fs_photo2, 
                                 reply_markup=kb.back_to_educ)
        else:
            text = render_template(template)
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(
                callback_query.from_user.id,
                text=f'{text}',
                reply_markup=kb.back_to_educ,
                disable_web_page_preview=True
            )

for callback in STUDY:
    dp.register_callback_query_handler(
        process_callback_button3, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

@dp.callback_query_handler(lambda x: x.data == 'en_education' or x.data == 'en_back_to_educ')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNNkbvr9ywnqkVU4jHqQDVWXNa4FuwACfjMAAq-NcUtvqCWa9bQG0C8E'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Education 📚',
        reply_markup=kb_en.educ_menu
    )

EN_STUDY = {
    'en_foreign_languages': 'foreign_languages_en.html',
    'en_internship': 'internship_en.html',
    'en_academic_mobility': 'academic_mobility_en.html',
    
}

async def study_en(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EN_STUDY.get(callback_data)
    if template:
        if template == 'internship_en.html':
            photo_path1 = os.path.join('bot_fmo', 'img', 'int_types_eng.png')
            photo_path2 = os.path.join('bot_fmo', 'img', 'int_kinds_eng.png')
            fs_photo1 = InputFile(photo_path1)
            fs_photo2 = InputFile(photo_path2)

            await bot.send_photo(callback_query.from_user.id, photo=fs_photo1)
            await bot.send_photo(callback_query.from_user.id, photo=fs_photo2, 
                                 reply_markup=kb_en.back_to_educ)
        else:
            text = render_template(template)
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(
                callback_query.from_user.id,
                text=f'{text}',
                reply_markup=kb_en.back_to_educ,
                disable_web_page_preview=True
            )

for callback in EN_STUDY:
    dp.register_callback_query_handler(
        study_en, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )
#_____________________________________________________

#__________________ Общежитие ________________________
@dp.callback_query_handler(lambda x: x.data == 'btn6' or x.data == 'back_to_dorm')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNVkbvsGyWbt9ITtq8tX05gLJQjN3wACJScAAxF5S3J39R39BTiPLwQ'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Об общежитиях 🏠',
        reply_markup=kb.dorm_menu
    )

DORM = {
    'btn43': 'dormitory_place.html',
    'btn44': 'dormitory_list.html',
    'btn45': 'dormitory_payment.html',
    'btn46': 'dormitory_internet.html'
}

async def process_callback_button4(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = DORM.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb.back_to_dorm,
            disable_web_page_preview=True
        )

for callback in DORM:
    dp.register_callback_query_handler(
        process_callback_button4, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

@dp.callback_query_handler(lambda x: x.data == 'en_dormitories' or x.data == 'en_back_to_dorm')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNVkbvsGyWbt9ITtq8tX05gLJQjN3wACJScAAxF5S3J39R39BTiPLwQ'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Dormitories 🏠',
        reply_markup=kb_en.dorm_menu
    )

EN_DORM = {
    'en_getting_place': 'dormitory_place_en.html',
    'en_spbsu_dorms': 'dormitory_list_en.html',
    'en_accommodation': 'dormitory_payment_en.html',
    'en_internet': 'dormitory_internet_en.html'
}

async def dorm_info_en(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EN_DORM.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb_en.back_to_dorm,
            disable_web_page_preview=True
        )

for callback in EN_DORM:
    dp.register_callback_query_handler(
        dorm_info_en, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )
#_____________________________________________________

#___________________ Мед помощь ______________________
@dp.callback_query_handler(lambda x: x.data == 'btn7' or x.data == 'back_to_med')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGN9kbvsrzQGn_459-ZGLnNfQaFtWcAAC-i4AAoGPcEuYFHSZNAXc5i8E',
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Мед. помощь 💊',
        reply_markup=kb.med_menu
    )

MED = {
    'btn27': 'health_checkup.html',
    'btn28': 'first_aid.html',
    'btn29': 'health_centers.html'
}

async def process_callback_button5(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = MED.get(callback_data)
    if template:
        if template == 'health_centers.html':
            photo_path1 = os.path.join('bot_fmo', 'img', 'med_centers.png')
            fs_photo1 = InputFile(photo_path1)

            await bot.send_photo(callback_query.from_user.id, photo=fs_photo1, 
                                 reply_markup=kb.back_to_med)
        else:

            text = render_template(template)
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(
                callback_query.from_user.id,
                text=f'{text}',
                reply_markup=kb.back_to_med,
                disable_web_page_preview=True
            )

for callback in MED:
    dp.register_callback_query_handler(
        process_callback_button5, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

@dp.callback_query_handler(lambda x: x.data == 'en_med_care' or x.data == 'en_back_to_med')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGN9kbvsrzQGn_459-ZGLnNfQaFtWcAAC-i4AAoGPcEuYFHSZNAXc5i8E',
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Med. care 💊',
        reply_markup=kb_en.med_menu
    )

EN_MED = {
    'en_medical_checkup': 'health_checkup_en.html',
    'en_first_aid': 'first_aid_en.html',
    'en_spbsu_medical_centres': 'health_centers_en.html'
}

async def medcare_info_en(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EN_MED.get(callback_data)
    if template:
        if template == 'health_centers_en.html':
            photo_path1 = os.path.join('bot_fmo', 'img', 'med_centers_eng.png')
            fs_photo1 = InputFile(photo_path1)

            await bot.send_photo(callback_query.from_user.id, photo=fs_photo1, 
                                 reply_markup=kb_en.back_to_med)
        else:
            text = render_template(template)
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(
                callback_query.from_user.id,
                text=f'{text}',
                reply_markup=kb_en.back_to_med,
                disable_web_page_preview=True
            )

for callback in EN_MED:
    dp.register_callback_query_handler(
        medcare_info_en, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )
#________________________________________________________________

#___________________ Иностранным студентам ______________________
@dp.callback_query_handler(lambda x: x.data == 'btn8' or x.data == 'back_to_int_stud')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNdkbvsRTb--mf9W8tYGWPi2ImaOuwAC1C4AAhmdcUs6Dtjk-nZv8i8E'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Иностранным студентам 🇺🇳',
        reply_markup=kb.int_stud_menu
    )

INT_STUD = {
    'btn30': 'foreign_students_club.html',
    'btn31': 'rules_of_stay.html',
    'btn32': 'medical_aid_foreigners.html',

}

async def process_callback_button6(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = INT_STUD.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        if template == 'rules_of_stay.html':
            await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb.back_to_int_stud,
        )
        else:
            await bot.send_message(
                callback_query.from_user.id,
                text=f'{text}',
                reply_markup=kb.back_to_int_stud,
                disable_web_page_preview=True
            )

for callback in INT_STUD:
    dp.register_callback_query_handler(
        process_callback_button6, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

@dp.callback_query_handler(lambda x: x.data == 'en_international_students' or x.data == 'en_back_to_int_stud')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNdkbvsRTb--mf9W8tYGWPi2ImaOuwAC1C4AAhmdcUs6Dtjk-nZv8i8E'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='For international students 🇺🇳',
        reply_markup=kb_en.int_stud_menu
    )

EN_INT_STUD = {
    'en_international_students_club': 'foreign_students_club_en.html',
    'en_rules_of_stay': 'rules_of_stay_en.html',
    'en_int_med_care': 'medical_aid_foreigners_en.html',

}

async def international_students_en(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EN_INT_STUD.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        if template == 'rules_of_stay_en.html':
            await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb_en.back_to_int_stud,
        )
        else:
            await bot.send_message(
                callback_query.from_user.id,
                text=f'{text}',
                reply_markup=kb_en.back_to_int_stud,
                disable_web_page_preview=True
            )

for callback in EN_INT_STUD:
    dp.register_callback_query_handler(
        international_students_en, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )
#________________________________________________________________

#___________________ Внеучебная деятельность ____________________
@dp.callback_query_handler(lambda x: x.data == 'btn9' or x.data == 'back_to_extracurricular')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNlkbvsYnzJ7eN2NnezYEj-CQ65C4QACTzIAArsacUvINvUl1NpCCS8E'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Внеучебная деятельность 🏆',
        reply_markup=kb.extracurricular_menu
    )

@dp.callback_query_handler(lambda x: x.data == 'btn33' or x.data == 'back_to_council')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = render_template(
        'student_council.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=f'{text}',
        reply_markup=kb.fmo_students_council_menu,
        disable_web_page_preview=True
    )

EXTRA = {
    'btn40': 'student_council_committees.html',
    'btn41': 'student_council_membership.html',
    'btn42': 'student_council_competencies.html',
    'btn34': 'start_up.html',
    'btn35': 'sno.html'
}

async def process_callback_button7(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EXTRA.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb.back_to_council,
            disable_web_page_preview=True
        )

for callback in EXTRA:
    dp.register_callback_query_handler(
        process_callback_button7, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

@dp.callback_query_handler(lambda x: x.data == 'en_extracurricular_activities' 
                           or x.data == 'en_back_to_extracurricular')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNlkbvsYnzJ7eN2NnezYEj-CQ65C4QACTzIAArsacUvINvUl1NpCCS8E'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Extracurricular activities 🏆',
        reply_markup=kb_en.extracurricular_menu
    )

@dp.callback_query_handler(lambda x: x.data == 'en_student_council' or x.data == 'en_back_to_council')
async def process_callback_button1(callback_query: types.CallbackQuery):
    text = render_template(
        'student_council_en.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(
        callback_query.from_user.id,
        text=f'{text}',
        reply_markup=kb_en.fmo_students_council_menu,
        disable_web_page_preview=True
    )

EN_EXTRA = {
    'en_committees': 'student_council_committees_en.html',
    'en_membership': 'student_council_membership_en.html',
    'en_competencies': 'student_council_competencies_en.html',
    'en_sno': 'sno_en.html'
}

async def extracurricular_en(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EN_EXTRA.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb_en.back_to_council,
            disable_web_page_preview=True
        )

for callback in EN_EXTRA:
    dp.register_callback_query_handler(
        extracurricular_en, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )
#________________________________________________________________

#___________________ Информационные ресурсы _____________________
@dp.callback_query_handler(lambda x: x.data == 'btn10' or x.data == 'back_to_info')
async def process_callback_button10(callback_query: types.CallbackQuery):
    text = render_template(
        'inf_res.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id,
        sticker=r'CAACAgIAAxkBAAEJGN1kbvslT3K8yFLWSyKhMntzir6lfAAC6ygAAjmAeEuCI59NxmOwXy8E'
    )
    await bot.send_message(
        callback_query.from_user.id, 
        text=f'{text}',
        reply_markup=kb.info_menu,
        disable_web_page_preview=True
    )

INFO = {
    'btn36': 'e_library.html',
    'btn37': 'library.html',
    'btn38': 'student_email.html',
    'btn39': 'account.html',
    'btn50': 'blackboard.html'
}

async def process_callback_button8(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = INFO.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb.back_to_info,
            disable_web_page_preview=True
        )

for callback in INFO:
    dp.register_callback_query_handler(
        process_callback_button8, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

@dp.callback_query_handler(lambda x: x.data == 'en_informational_resources' or x.data == 'en_back_to_info')
async def process_callback_button10(callback_query: types.CallbackQuery):
    text = render_template(
        'inf_res_en.html'
    )
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id,
        sticker=r'CAACAgIAAxkBAAEJGN1kbvslT3K8yFLWSyKhMntzir6lfAAC6ygAAjmAeEuCI59NxmOwXy8E'
    )
    await bot.send_message(
        callback_query.from_user.id, 
        text=f'{text}',
        reply_markup=kb_en.info_menu,
        disable_web_page_preview=True
    )

EN_INFO = {
    'en_e_library': 'e_library_en.html',
    'en_library': 'library_en.html',
    'en_corporate_mail': 'student_email_en.html',
    'en_account': 'account_en.html',
    'en_blackboard': 'blackboard_en.html'
}

async def infores_en(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = EN_INFO.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb_en.back_to_info,
            disable_web_page_preview=True
        )

for callback in EN_INFO:
    dp.register_callback_query_handler(
        infores_en, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )
#________________________________________________________________

#___________________ Военный учёт и военная кафедра _____________
@dp.callback_query_handler(lambda x: x.data == 'btn11' or x.data == 'back_to_military')
async def process_callback_button10(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_sticker(
        callback_query.from_user.id, 
        sticker=r'CAACAgIAAxkBAAEJGNtkbvsfRmdp8viMfFsffZbHoUzTxwACnCwAAmWAcEtcDfcidIeNLC8E'
    )
    await bot.send_message(
        callback_query.from_user.id,
        text='Военный учёт и военная кафедра 🪖',
        reply_markup=kb.military_menu
    )

MILITARY = {
    'btn47': 'military_enroll.html',
    'btn48': 'military_right.html',
    'btn49': 'military_get_in.html'
}

async def process_callback_button9(callback_query: types.CallbackQuery):
    callback_data = callback_query.data
    template = MILITARY.get(callback_data)
    if template:
        text = render_template(template)
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(
            callback_query.from_user.id,
            text=f'{text}',
            reply_markup=kb.back_to_military,
            disable_web_page_preview=True
        )

for callback in MILITARY:
    dp.register_callback_query_handler(
        process_callback_button9, lambda callback_query, 
        callback=callback: callback_query.data == callback
    )

#________________________________________________________________

@dp.message_handler(commands=['help'])
#команда '/help' выводит список команд
async def process_help_command(message: types.Message):
    await message.reply('/start\n/help')

@dp.message_handler(commands=['1'])
async def process_command_2(message: types.Message):
    await message.reply('Главное меню', reply_markup=kb.main_menu)

@dp.message_handler(commands=['2'])
async def process_command_2(message: types.Message):
    await message.reply('Main menu', reply_markup=kb_en.main_menu)

@dp.message_handler(commands=['start'])
async def process_command_2(message: types.Message):
    text = render_template(
        'starting_mess.html'
    )
    await message.reply(text=f'{text}', reply_markup=kb.starting_menu)


if __name__ == '__main__':
    executor.start_polling(dp)