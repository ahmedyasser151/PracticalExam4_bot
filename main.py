from decouple import config
from random import sample
from time import sleep
from telebot.async_telebot import AsyncTeleBot
import telebot
import exam_data

BOT_TOKEN = config('BOT_TOKEN')
bot = AsyncTeleBot(BOT_TOKEN)

################### starting of specific spots func ###################
# catalase spot
async def send_catalase_spot(bacteria, message_chat_id):
    photo = open(f'{bacteria.get_catalase_test()}', 'rb')
    m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
    sleep(4)
    await bot.delete_message(message_chat_id, m.message_id)

# blood agar spot
async def send_blood_agar_spot(bacteria, message_chat_id):
    photo = open(f'{bacteria.get_blood_agar()}', 'rb')
    m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
    sleep(4)
    await bot.delete_message(message_chat_id, m.message_id)

################### ending of specific spots func ###################

#################################### exam and answers func ####################################
async def send_staph_spots(bacteria, message_chat_id):
    # show catalase test
    try:
        await send_catalase_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with catalase test in staph")
    # show blood agar
    try:
        await send_blood_agar_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with blood agar in staph")
    # show gelatinase test
    try:
        photo = open(f'{bacteria.get_gelatinase_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with gelatinase test in staph")
    
    # show coagulase test
    try:
        photo = open(f'{bacteria.get_coagulase_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with coagulase test in staph")

    # show nutrient agar
    try:
        photo = open(f'{bacteria.get_nutrient_agar()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with nutrient agar in staph")

async def send_staph_answers(bacteria, message_chat_id):
    await bot.send_message(message_chat_id,f'''
    The MO is {bacteria.get_name().replace('imeges/', '').replace('.jpg', '')}
*******************
spot 1:
Test name: catealase test  
Result: {bacteria.get_catalase_test().replace('imeges/', '').replace('.jpg', '')}
spot 2:
Test name: Blood Agar 
Result: {bacteria.get_blood_agar().replace('imeges/', '').replace('.jpg', '')}  
spot 3:
Test name: gelatinase test
Result: {bacteria.get_gelatinase_test().replace('imeges/', '').replace('.jpg', '')}
spot 4:
Test name: co-agulase 
Result: {bacteria.get_coagulase_test().replace('imeges/', '').replace('.jpg', '')}
spot 5:
Test name: Nutrient Agar
Result: {bacteria.get_nutrient_agar().replace('imeges/', '').replace('.jpg', '')}
*******************
                ''')

async def send_gamma_hemolytic_strepto_spots(bacteria, message_chat_id):
    # show macconkey agar
    try:
        photo = open(f'{bacteria.get_MacConkey_agar()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with MacConkey agar in gamma hemolytic strepto")
    # show NaCl test
    try:
        photo = open(f'{bacteria.get_NaCl_sensitive()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with NaCl test in gamma hemolytic strepto")

    # show blood agar
    try:
        await send_blood_agar_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with blood agar in gamma hemolytic strepto")
    # show catalase test
    try:
        await send_catalase_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with catalase test in gamma hemolytic strepto")

    # show penicillin test
    try:
        photo = open(f'{bacteria.get_penicillin_sensitivity_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Penicillin sensitivity test\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with penicillin test in gamma hemolytic strepto")

async def send_gamma_hemolytic_strepto_answers(bacteria, message_chat_id):
    await bot.send_message(message_chat_id,f'''
    The MO is {bacteria.get_name().replace('imeges/', '').replace('.jpg', '')}
*******************
spot 1:
Test name: MacConkey Agar
Result: {bacteria.get_MacConkey_agar().replace('imeges/', '').replace('.jpg', '')}
spot 2:
Test name: NaCl sensitivity test  
Result: {bacteria.get_NaCl_sensitive().replace('imeges/', '').replace('.jpg', '')}
spot 3:
Test name: Blood Agar 
Result: {bacteria.get_blood_agar().replace('imeges/', '').replace('.jpg', '')}  
spot 4:
Test name: catalase test
Result: {bacteria.get_catalase_test().replace('imeges/', '').replace('.jpg', '')}
spot 5:
Test name: penicillin_sensitivity_test 
Result: {bacteria.get_penicillin_sensitivity_test().replace('imeges/', '').replace('.jpg', '')}
*******************
                    ''')

async def send_beta_hemolytic_strepto_spots(bacteria, message_chat_id):
    # show blood agar
    try:
        await send_blood_agar_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with blood agar in beta hemolytic strepto")

    # show catalase test
    try:
        await send_catalase_spot(bacteria, message_chat_id)    
    except:
        raise Exception("something wrong with catalase test in beta hemolytic strepto")

    # show bacitracin_sensitivity_test
    try:
        photo = open(f'{bacteria.get_bacitracin_sensitivity_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with bacitracin test in beta hemolytic strepto")

async def send_beta_hemolytic_strepto_answers(bacteria, message_chat_id):
    await bot.send_message(message_chat_id,f'''
    The MO is {bacteria.get_name().replace('imeges/', '').replace('.jpg', '')}
*******************
spot 1:
Test name: Blood Agar 
Result: {bacteria.get_blood_agar().replace('imeges/', '').replace('.jpg', '')}  
spot 2:
Test name: catealase test  
Result: {bacteria.get_catalase_test().replace('imeges/', '').replace('.jpg', '')}
spot 3:
Test name: Bacitracin sensitivity 
Result: {bacteria.get_bacitracin_sensitivity_test().replace('imeges/', '').replace('.jpg', '')}
*******************
                    ''')

async def send_alpha_hemolytic_strepto_spots(bacteria, message_chat_id):
    # show catalase test
    try:
        await send_catalase_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with catalase test in alpha hemolytic strepto")

    # show optichin_sensitivity_test
    try:
        photo = open(f'{bacteria.get_optichin_sensitivity_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with optichin test in alpha hemolytic strepto")

    # show bile solubility test
    try:
        photo = open(f'{bacteria.get_bile_solublitiy_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with bile solubility test in alpha hemolytic strepto")

    # show blood agar
    try:
        await send_blood_agar_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with blood agar in alpha hemolytic strepto")

async def send_alpha_hemolytic_strepto_answers(bacteria, message_chat_id):
    await bot.send_message(message_chat_id,f'''
    The MO is {bacteria.get_name().replace('imeges/', '').replace('.jpg', '')}
*******************
spot 1:
Test name: catealase test  
Result: {bacteria.get_catalase_test().replace('imeges/', '').replace('.jpg', '')}
spot 2:
Test name: Opitichin sensitivity 
Result: {bacteria.get_optichin_sensitivity_test().replace('imeges/', '').replace('.jpg', '')}
spot 3:
Test name: Bile solubility
Result: {bacteria.get_bile_solublitiy_test().replace('imeges/', '').replace('.jpg', '')}
spot 4:
Test name: Blood Agar 
Result: {bacteria.get_blood_agar().replace('imeges/', '').replace('.jpg', '')}  
*******************
                    ''')

async def send_other_gram_positive_spots(bacteria, message_chat_id):
    # show catalase test
    try:
        await send_catalase_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with catalase test in other gram positive")

    # show blood agar
    try:
        await send_blood_agar_spot(bacteria, message_chat_id)
    except:
        raise Exception("something wrong with blood agar in other gram positive")

    # show urease test
    try:
        photo = open(f'{bacteria.get_urease_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with urease test in other gram positive")

    # show nitrate reduction test
    try:
        photo = open(f'{bacteria.get_nitrate_reduction_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with nitrate reduction test in other gram positive")

async def send_other_gram_positive_answers(bacteria, message_chat_id):
    await bot.send_message(message_chat_id,f'''
    The MO is {bacteria.get_name().replace('imeges/', '').replace('.jpg', '')}
*******************
spot 1:
Test name: catealase test  
Result: {bacteria.get_catalase_test().replace('imeges/', '').replace('.jpg', '')}
spot 2:
Test name: Blood Agar 
Result: {bacteria.get_blood_agar().replace('imeges/', '').replace('.jpg', '')}  
spot 3:
Test name: urease test
Result: {bacteria.get_urease_test().replace('imeges/', '').replace('.jpg', '')}
spot 4:
Test name: Nitrate reduction 
Result: {bacteria.get_nitrate_reduction_test().replace('imeges/', '').replace('.jpg', '')}
*******************
                ''')

async def send_gram_negative_spots(bacteria, message_chat_id):
    # show MacConkey Agar:
    try:
        photo = open(f'{bacteria.get_MacConkey_agar()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo, 'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with MacConkey agar in gram negative")
    
    # show TSI spot:
    try:
        photo = open(f'{bacteria.get_TSI()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo,'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with TSI test in gram negative")

    # show motility spot:
    try:
        photo = open(f'{bacteria.get_motility_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo, 'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with motility test in gram negative")   

    # show EMB spot:
    try:
        photo = open(f'{bacteria.get_EMB()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo, 'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with EMB in gram negative")

    # show IMViC test:
    try:
        photo = open(f'{bacteria.get_IMViC_test()}', 'rb')
        m = await bot.send_photo(message_chat_id,photo, 'Test name:\nResult:')
        sleep(4)
        await bot.delete_message(message_chat_id, m.message_id)
    except:
        raise Exception("something wrong with IMViC test in gram negative")

async def send_gram_negative_answers(bacteria, message_chat_id):
    await bot.send_message(message_chat_id,f'''
    The MO is {bacteria.get_name().replace('imeges/', '').replace('.jpg', '')}
*******************
spot 1:
Test name: MacConkey Agar  
Result: {bacteria.get_MacConkey_agar().replace('imeges/', '').replace('.jpg', '')}
spot 2:
Test name: TSI 
Result: {bacteria.get_TSI().replace('imeges/', '').replace('.jpg', '')}  
spot 3:
Test name: Motility
Result: {bacteria.get_motility_test().replace('imeges/', '').replace('.jpg', '')}
spot 4:
Test name: EMB 
Result: {bacteria.get_EMB().replace('imeges/', '').replace('.jpg', '')}
spot 5:
Test name: IMViC
Result: {bacteria.get_IMViC_test().replace('imeges/', '').replace('.jpg', '')}
*******************
            ''')

#################################### Bot func ####################################

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    # send welcoming message
    print(message.text)
    await bot.send_message(message.chat.id, 'مرحباً بك في بوت محاكاة امتحان عملي ميديكال ميكرو')

    #  show ok button
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = telebot.types.KeyboardButton('/ok')
    markup.row(itembtn1)
    await bot.send_message(message.chat.id, 'اضغط علي زر موافق',reply_markup=markup)
    await bot.send_message(message.chat.id, ' انطلق ولا تنس الدعاء')

@bot.message_handler(commands=['ok'])
async def send_ok_message(message):
    print(message.text)
    
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = telebot.types.KeyboardButton('/startexam',)
    itembtn2 = telebot.types.KeyboardButton('/help')
    markup.row(itembtn1)
    markup.row(itembtn2)
    await bot.send_message(message.chat.id, 'الآن أصبح البوت جاهزاً',reply_markup=markup)

@bot.message_handler(commands=['help'])
async def help_message(message):
    print(message.text)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = telebot.types.KeyboardButton('/mainmenu')
    markup.row(itembtn1)
    await bot.send_message(message.chat.id, 'لم انته بعد من كتابة الشرح المفصل للبوت وما ستواجهه من مشاكل.', reply_markup=markup)
    await bot.send_message(message.chat.id, 'إن شاء الله سأنتهي منه قريباً وسأعطيك الحلول لما واجهته.', reply_markup=markup)
    await bot.send_message(message.chat.id, 'إذا كان لديك اقتراحات أو واجهتك مشكلة رجاءً راسلني.', reply_markup=markup)
           
@bot.message_handler(commands=['startexam', 'startnewexam'])
async def start_exam_show_answers(message):
    print(message.text)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = telebot.types.KeyboardButton('/endexam')
    markup.row(itembtn1)
    await bot.send_message(message.chat.id, 'بسم الله الرحمن الرحيم', reply_markup=markup)
    await bot.send_message(message.chat.id, 'صل على النبي', reply_markup=markup)

    # choose random 4 mo
    exam_sample = sample(exam_data.BACTERIA_LIST, k=4)
    

    ############################### the starting of exam ###############################
    # counter for benches when examing
    i = 1
    for bacteria in exam_sample:
        # send Bench number
        bench = await bot.send_message(message.chat.id, f'Bench {i}')

        # show gram postive
        if bacteria.is_Gram_postive:
            # check if mo is staph
            if bacteria.is_staph:
                await send_staph_spots(bacteria, message.chat.id)
                
            # check if mo is strepto
            elif bacteria.is_strepto:

                if bacteria.get_blood_agar() == 'imeges/gamma_hemolytic.jpg':
                    await send_gamma_hemolytic_strepto_spots(bacteria, message.chat.id)

                elif bacteria.get_blood_agar() == 'imeges/beta_hemolytic.jpg':
                    await send_beta_hemolytic_strepto_spots(bacteria, message.chat.id)

                else:
                    await send_alpha_hemolytic_strepto_spots(bacteria, message.chat.id)

            # others gram postive
            else:
                await send_other_gram_positive_spots(bacteria, message.chat.id)

        # show gram negative 
        else:
            await send_gram_negative_spots(bacteria, message.chat.id)

        # delete bench number
        await bot.delete_message(bench.chat.id, bench.message_id)
        i += 1
    ############################### the ending of exam ###############################

    ############################### starting of send the answers ###############################
    await bot.send_message(message.chat.id,'اجابات الامتحان')

    # counter for benches when answering
    i = 1
    # send answers
    for bacteria in exam_sample:
        # send bench no
        await bot.send_message(message.chat.id, f'Bench {i}')
        ###### send answers ######
        # gram postive
        if bacteria.is_Gram_postive == True:
            # send staph
            if bacteria.is_staph:
                await send_staph_answers(bacteria, message.chat.id)
            # send strepto
            elif bacteria.is_strepto:
                # gamma hemolytic strepto
                if bacteria.get_blood_agar() == 'imeges/gamma_hemolytic.jpg':
                    await send_gamma_hemolytic_strepto_answers(bacteria, message.chat.id)

                # beta hemolytic strepto 
                elif bacteria.get_blood_agar() == 'imeges/beta_hemolytic.jpg':
                    await send_beta_hemolytic_strepto_answers(bacteria, message.chat.id)
                
                # alpha hemolytic strepto
                else:
                    await send_alpha_hemolytic_strepto_answers(bacteria, message.chat.id)

            # others gram postive   
            else:
                await send_other_gram_positive_answers(bacteria, message.chat.id)

        # send gram negative
        else:
            await send_gram_negative_answers(bacteria, message.chat.id)

        i += 1
    ############################### ending of send the answers ###############################

    end_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = telebot.types.KeyboardButton('/startnewexam')
    itembtn2 = telebot.types.KeyboardButton('/mainmenu')
    end_markup.row(itembtn1)
    end_markup.row(itembtn2)
    await bot.send_message(message.chat.id,'انتهي الامتحان', reply_markup=end_markup)

@bot.message_handler(commands=['mainmenu'])
async def back_to_main(message):
    print(message.text)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = telebot.types.KeyboardButton('/startexam',)
    itembtn2 = telebot.types.KeyboardButton('/help')
    markup.row(itembtn1)
    markup.row(itembtn2)
    await bot.send_message(message.chat.id, 'Main Menu',reply_markup=markup)

@bot.message_handler(commands=['endexam'])
async def end_exam(message):
    print(message.text)
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    itembtn1 = telebot.types.KeyboardButton('/mainmenu')
    markup.row(itembtn1)
    await bot.send_message(message.chat.id, 'Manin Menu', reply_markup=markup)
    print(message.text)
    await bot.send_message(message.chat.id,'لماذا تريد انهاء الامتحان؟ ')
    await bot.send_message(message.chat.id,'اصبر')
    await bot.send_message(message.chat.id,'للأسف لابد من انتظار دقيقة حتي يتم الانتهاء من عرض الصور')
    await bot.send_message(message.chat.id,'للأسف لابد من الانتظار')

import asyncio
asyncio.run(bot.polling())