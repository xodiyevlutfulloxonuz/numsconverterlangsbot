from aiogram import types
from aiogram.dispatcher.storage import FSMContext
from loader import dp
from states.User import Lang
import num2words
from keyboards.inline.inlinekeyboard import keyboards
@dp.callback_query_handler(state=Lang.lang)
async def callback(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    await call.message.answer("Biror bir son kiriting:")
    await state.update_data({'lang': call.data})
    data = await state.get_data()
    language = data.get('lang')
    await Lang.result.set()




@dp.message_handler(state=Lang.result)
async def result_func(message:types.Message,  state=FSMContext):
    await state.update_data({'result':message.text})
    datas= await state.get_data()
    if datas.get('result')=="/start":
        await state.finish()
        await message.answer(f"Assalomu alaykum, {message.from_user.full_name}! Tilni tanlang.", reply_markup=keyboards)
        await Lang.lang.set()
    
    elif not datas.get('result').isdigit():
        await message.answer("Iltimos son kiriting.")

    else:
        convert_number = num2words.num2words(datas.get('result'), lang=f"{datas.get('lang')}")
        await message.answer(convert_number)
    


    
    
    








        
    

    

    
    


    

    
        

    

      
    
         

    

