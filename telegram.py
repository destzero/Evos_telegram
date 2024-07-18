from aiogram import types, Dispatcher, F, filters, Bot
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext


bot = Bot(token="7444244618:AAHJxtEgNBg4dgQC5Yhvd5Vs9t51PzF1sh0")
dp = Dispatcher(bot=bot)

orders = []
kb = [
    [KeyboardButton(text="Hot_dog(3) 🌭"), KeyboardButton(text="Gamburger(3) 🍔"), KeyboardButton(text="Fries(3) 🍟"), KeyboardButton(text="Sushi(3) 🍣")],
    [KeyboardButton(text="Pizza(3) 🍕"), KeyboardButton(text="Shashlik(3)"), KeyboardButton(text="Taco(3) 🌮"), KeyboardButton(text="🔙 back_from_the_foods")]
]
mb = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

menutop = [
    [KeyboardButton(text="Foods 🍽"), KeyboardButton(text="Drinks 🫖")],
    [KeyboardButton(text="🔙 Back")]
]
mmenutop = ReplyKeyboardMarkup(keyboard=menutop, resize_keyboard=True)

menuwater = [
    [KeyboardButton(text="Pepsi(1.5l) 🍷"), KeyboardButton(text="Water(1.5l) 🫗"), KeyboardButton(text="Juice(1.5l) 🧃")],
    [KeyboardButton(text="Coca-Cola(1.5l) 🍷"), KeyboardButton(text="Fanta(1.5l) 🍺"), KeyboardButton(text="Soda(1.5l) 🫗")],
    [KeyboardButton(text="Sprite(1.5l) 🍺"), KeyboardButton(text="Coffee ☕️"), KeyboardButton(text="🔙 back_from_the_drinks")]
]
mmenuwater = ReplyKeyboardMarkup(keyboard=menuwater, resize_keyboard=True)

kb_1 = [
    [KeyboardButton(text="Menu ⚡️"), KeyboardButton(text="Shoppings 🛍")],
    [KeyboardButton(text="Info ℹ️")],
    [KeyboardButton(text="About you 🫵"), KeyboardButton(text="Help 🆘")],
    [KeyboardButton(text="Language ⚙️")]
]
mb_1 = ReplyKeyboardMarkup(keyboard=kb_1, resize_keyboard=True)

kb_2 = [
    [KeyboardButton(text="Fries_medium 🍟"), KeyboardButton(text="Fries_short 🍟"), KeyboardButton(text="Fries_long 🍟")],
    [KeyboardButton(text="🔙 Back")]
]
mb_2 = ReplyKeyboardMarkup(keyboard=kb_2, resize_keyboard=True)

kb_3 = [
    [KeyboardButton(text="Chesse_burger 🍔"), KeyboardButton(text="Simple_burger 🍔"), KeyboardButton(text="Chili_burger 🍔")],
    [KeyboardButton(text="🔙 Back")]
]
mb_3 = ReplyKeyboardMarkup(keyboard=kb_3, resize_keyboard=True)

kb_4 = [
    [KeyboardButton(text="Hot_dog_medium 🌭"), KeyboardButton(text="Hot_dog_short 🌭"), KeyboardButton(text="Hot_dog_long 🌭")],
    [KeyboardButton(text="🔙 Back")]
]
mb_4 = ReplyKeyboardMarkup(keyboard=kb_4, resize_keyboard=True)

kb_5 = [
    [KeyboardButton(text="Pizza_small 🍕"), KeyboardButton(text="Pizza_medium 🍕"), KeyboardButton(text="Pizza_large 🍕")],
    [KeyboardButton(text="🔙 Back")]
]
mb_5 = ReplyKeyboardMarkup(keyboard=kb_5, resize_keyboard=True)

kb_6 = [
    [KeyboardButton(text="Shashlik_chicken"), KeyboardButton(text="Shashlik_beef"), KeyboardButton(text="Shashlik_lamb")],
    [KeyboardButton(text="🔙 Back")]
]
mb_6 = ReplyKeyboardMarkup(keyboard=kb_6, resize_keyboard=True)

kb_7 = [
    [KeyboardButton(text="Taco_beef 🌮"), KeyboardButton(text="Taco_chicken 🌮"), KeyboardButton(text="Taco_veggie 🌮")],
    [KeyboardButton(text="🔙 Back")]
]
mb_7 = ReplyKeyboardMarkup(keyboard=kb_7, resize_keyboard=True)

kb_8 = [
    [KeyboardButton(text="Sushi_salmon 🍣"), KeyboardButton(text="Sushi_tuna 🍣"), KeyboardButton(text="Sushi_veggie 🍣")],
    [KeyboardButton(text="🔙 Back")]
]


kb_10 = [
    [KeyboardButton(text='Buy💸'), KeyboardButton(text='View cart🛒')],
    [KeyboardButton(text='🔙 Back')]
]
mb_10 = ReplyKeyboardMarkup(keyboard=kb_10, resize_keyboard=True)

kb_9 = [
    [KeyboardButton(text="Uzbek_tili🇺🇿"), KeyboardButton(text="English_language 🏴󠁧󠁢󠁥󠁮󠁧󠁿")]
]
mb_9 = ReplyKeyboardMarkup(keyboard=kb_9, resize_keyboard=True)

kb = [
    [KeyboardButton(text="Hot_dog(3) 🌭"), KeyboardButton(text="Gamburger(3) 🍔"), KeyboardButton(text="Fries(3) 🍟"), KeyboardButton(text="Sushi(3) 🍣")],
    [KeyboardButton(text="Pizza(3) 🍕"), KeyboardButton(text="Shashlik(3)"), KeyboardButton(text="Taco(3) 🌮"), KeyboardButton(text="🔙 back_from_the_foods")]
]
mb = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)

menutop = [
    [KeyboardButton(text="Foods 🍽"), KeyboardButton(text="Drinks 🫖")],
    [KeyboardButton(text="🔙 Back")]
]
mmenutop = ReplyKeyboardMarkup(keyboard=menutop, resize_keyboard=True)

uztop = [
    [KeyboardButton(text="Ovqatlar 🍽"), KeyboardButton(text="Ichimliklar 🫖")],
    [KeyboardButton(text="🔙 Ortga")]
]
uzbbtop = ReplyKeyboardMarkup(keyboard=uztop, resize_keyboard=True)

uzwater = [
    [KeyboardButton(text="Pepsi(1.5l) 🍷"), KeyboardButton(text="Water(1.5l) 🫗"), KeyboardButton(text="Juice(1.5l) 🧃")],
    [KeyboardButton(text="Coca-Cola(1.5l) 🍷"), KeyboardButton(text="Fanta(1.5l) 🍺"), KeyboardButton(text="Soda(1.5l) 🫗")],
    [KeyboardButton(text="Sprite(1.5l) 🍺"), KeyboardButton(text="Coffee ☕️"), KeyboardButton(text="🔙 Menuga qaytish")]
]
uzbwater = ReplyKeyboardMarkup(keyboard=menuwater, resize_keyboard=True)

uz_1 = [
    [KeyboardButton(text="Menyu ⚡️"), KeyboardButton(text="Xaridlar 🛍")],
    [KeyboardButton(text="Ma'lumot ℹ️")],
    [KeyboardButton(text="Sizning ma'lumot 🫵"), KeyboardButton(text="Yordam 🆘")],
    [KeyboardButton(text="Til ⚙️")]
]
uzb_1 = ReplyKeyboardMarkup(keyboard=uz_1, resize_keyboard=True)

kb_pay = [
    [KeyboardButton(text="Humo💳"), KeyboardButton(text="Uzcard💳")]
]
mb_pay = ReplyKeyboardMarkup(keyboard=kb_pay, resize_keyboard=True)

uztili = [
    [KeyboardButton(text="Uzbek🇺🇿"), KeyboardButton(text="English 🏴󠁧󠁢󠁥󠁮󠁧󠁿")]
]
entili = ReplyKeyboardMarkup(keyboard=uztili, resize_keyboard=True)

@dp.message(filters.Command("start"))
async def start_function(message: types.Message):
    await message.answer(f"Hello {message.from_user.full_name}, welcome to the bot🤖!!!\nSalom {message.from_user.full_name}, botga xush kelibsiz!!!🤖", reply_markup=mb_9)

class Registration(StatesGroup):
    first_name = State()
    last_name = State()
    number = State()
    ism = State()
    familiya = State()
    raqam = State()
    phone_number = State()

class Card(StatesGroup):
    card_number = State()
    card_number_2 = State()
    

contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Send contact📤", request_contact=True, resize_keyboard=True)]
])

@dp.message(F.text == "Shoppings 🛍")
async def orders_function(message: types.Message):
    await message.answer("What do you need help with?", reply_markup=mb_10)

@dp.message(F.text == "Uzcard💳")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number)
    await message.answer("Enter the card number 💳")


@dp.message(Card.card_number)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer("Thank you, we accepted!")
    else:
        await message.answer("Try again!!!")
    await state.clear()


@dp.message(F.text == "Humo💳")
async def pey_function(message: types.Message, state: FSMContext):
    await state.set_state(Card.card_number_2)
    await message.answer("Enter the card number 💳")


@dp.message(Card.card_number_2)
async def card_number_function(message: types.Message, state: FSMContext):
    text = message.text
    if text.isdigit() and len(text) == 16:
        await state.update_data(card_number=message.text)
        await message.answer("Thank you, we accepted!")
    else:
        await message.answer("Try again!!!")
    await state.clear()

@dp.message(F.text == "Buy💸")
async def orders_function(message: types.Message):
    await message.answer("Select a card", reply_markup=mb_pay)

@dp.message(F.text == "View cart🛒")
async def orders_function(message: types.Message):
    if orders:
        await message.answer(f"Your orders: {', '.join(orders)}", reply_markup=mb_10)
    else:
        await message.answer("You have no orders yet.")

raqam_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontaktni yuborish📤", request_contact=True, resize_keyboard=True)]
])

@dp.message(F.text == "English_language 🏴󠁧󠁢󠁥󠁮󠁧󠁿")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Welcome\nEnter your name! ", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text == "Uzbek_tili🇺🇿")
async def start(message: types.Message, state: FSMContext):
    await state.set_state(Registration.ism)
    await message.answer("Xush kelibsiz\nIsmingizni kiriting! ", reply_markup=types.ReplyKeyboardRemove())

@dp.message(F.text == "English 🏴󠁧󠁢󠁥󠁮󠁧󠁿")
async def start(message: types.Message, state: FSMContext):
    await message.answer("Language has changed!", reply_markup=mb_1)
    await state.set_state(Registration.ism)

@dp.message(F.text == "Uzbek🇺🇿")
async def start(message: types.Message, state: FSMContext):
    await message.answer("Til o'zgardi!", reply_markup=uzb_1)
    await state.set_state(Registration.ism)


@dp.message(Registration.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.last_name)
    await message.answer("Good 👏, now enter your last name! ", reply_markup=types.ReplyKeyboardRemove())

@dp.message(Registration.ism)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.familiya)
    await message.answer("Yaxshi 👏, familiyangizni kiriting! ", reply_markup=types.ReplyKeyboardRemove())


@dp.message(Registration.last_name)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.number)
    await message.answer("Good 👏, now enter your number 📞👇! ", reply_markup=contact_button)

@dp.message(Registration.familiya)
async def last_name_function(message: types.Message, state: FSMContext):
    await state.update_data(last_name=message.text)
    await state.set_state(Registration.raqam)
    await message.answer("Yaxshi 👏, raqamingizni yuboring 📞👇! ", reply_markup=raqam_button)

@dp.message(Registration.number)
async def phone_function(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Good 👏!\nYour name is: {data['first_name']}\nYour last name is: {data['last_name']}\nYour number📞: +{data['number']}", reply_markup=mb_1)
    await state.clear()

@dp.message(Registration.raqam)
async def phone_function(message: types.Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"Yaxshi 👏!\nIsmingiz: {data['first_name']}\nFamiliyangiz: {data['last_name']}\nRaqamingiz📞: +{data['number']}", reply_markup=uzb_1)
    await state.clear()

@dp.message(F.text == "Menu ⚡️")
async def menu_function(message: types.Message):
    await message.answer_photo(photo="https://static.vecteezy.com/system/resources/previews/016/063/037/original/fast-food-restaurant-table-menu-template-vector.jpg",
                               caption="Get acquainted with the menu", reply_markup=mmenutop)

@dp.message(F.text == "Menyu ⚡️")
async def menu_function(message: types.Message):
    await message.answer_photo(photo="https://static.vecteezy.com/system/resources/previews/016/063/037/original/fast-food-restaurant-table-menu-template-vector.jpg",
                               caption="Menyu bilan tanishing", reply_markup=uzbbtop)

@dp.message(F.text == "Foods 🍽")
async def ovqat_function(message: types.Message):
    await message.answer("select the type of food🍽", reply_markup=mb)

@dp.message(F.text == "Ovqatlar 🍽")
async def ovqat_function(message: types.Message):
    await message.answer("Ovqat turini tanlang🍽", reply_markup=mb)

@dp.message(F.text == "Drinks 🫖")
async def ichimliklar_function(message: types.Message):
    await message.answer("select the type of drink🫖", reply_markup=mmenuwater)

@dp.message(F.text == "Ichimliklar 🫖")
async def ichimliklar_function(message: types.Message):
    await message.answer("Ichimlikni tanlang🫖", reply_markup=mmenuwater)

@dp.message(F.text == "Pepsi(1.5l) 🍷")
async def pepsi_function(message: types.Message):
    orders.append("Pepsi:15ming so'm💵")
    await message.answer_photo(photo="https://orzon.uz/upload/iblock/359/3597fe28c257438dcb94643a7f71af0d.jpg",
                               caption="Price:15ming so'm")

@dp.message(F.text == "Water(1.5l) 🫗")
async def suv_function(message: types.Message):
    orders.append("Water:7ming so'm💵")
    await message.answer_photo(photo="https://www.icemountainwater.com/sites/g/files/zmtnxh171/files/2022-10/ice_mountain-spring-water-product-detail--1.5L-single-right.png",
                               caption="Price:7ming so'm")

@dp.message(F.text == "Juice(1.5l) 🧃")
async def sharbat_function(message: types.Message):
    orders.append("Juice:10ming so'm💵")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1TOQZ67PqIP-4qaUvaydlTauPXb9h3hYrJg&s",
                               caption="Price:10ming so'm")

@dp.message(F.text == "Coca-Cola(1.5l) 🍷")
async def coca_cola_function(message: types.Message):
    orders.append("Juice:12ming so'm💵")
    await message.answer_photo(photo="https://images.uzum.uz/cia493tenntd8rfc2s40/original.jpg",
                               caption="Price:12ming so'm")

@dp.message(F.text == "Fanta(1.5l) 🍺")
async def fanta_function(message: types.Message):
    orders.append("Juice:12ming so'm💵")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRi65yaIWEBgmY48WVEPT8dVnyFs2JT-5gaiw&s",
                               caption="Price:12ming so'm")

@dp.message(F.text == "Soda(1.5l) 🫗")
async def soda_function(message: types.Message):
    orders.append("Juice:8ming so'm💵")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiBK5l5iJpNhOrJNUW5XWNnK2HtWL4o5pxqg&s",
                               caption="Price:8ming so'm")

@dp.message(F.text == "Sprite(1.5l) 🍺")
async def sprite_function(message: types.Message):
    orders.append("Juice:12ming so'm💵")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTiqCbz93wZjO101ANkNrzhkO2aC56quDny7A&s",
                               caption="Price:12ming so'm")

@dp.message(F.text == "Coffee ☕️")
async def coffee_function(message: types.Message):
    orders.append("Juice:7ming so'm💵")
    await message.answer_photo(photo="https://images.immediate.co.uk/production/volatile/sites/30/2020/08/flat-white-3402c4f.jpg?quality=90&resize=500,454",
                               caption="Price:7ming so'm")

@dp.message(F.text == "🔙 back_from_the_drinks")
async def tea_function(message: types.Message):
    await message.answer("you are back to the menu", reply_markup=mmenutop)

@dp.message(F.text == "🔙 Back")
async def tea_function(message: types.Message):
    await message.answer("You are back to the menu", reply_markup=mb_1)

@dp.message(F.text == "🔙 Ortga")
async def tea_function(message: types.Message):
    await message.answer("Ortga qaytdingiz", reply_markup=mb_1)

@dp.message(F.text == "Language ⚙️")
async def tea_function(message: types.Message):
    await message.answer("Select a language", reply_markup=entili)

@dp.message(F.text == "Til ⚙️")
async def tea_function(message: types.Message):
    await message.answer("Tilni tanlang", reply_markup=entili)

@dp.message(F.text == "Help 🆘")
async def tea_function(message: types.Message):
    await message.answer("If you need help, call this number: +998 93-512-05-12", reply_markup=mb_1)

@dp.message(F.text == "Yordam 🆘")
async def tea_function(message: types.Message):
    await message.answer("Agar yordam kerak bo'lsa shu raqamga qo'giroq qiling: +998 93-512-05-12", reply_markup=mb_1)

@dp.message(F.text == "Info ℹ️")
async def tea_function(message: types.Message):
    await message.answer("We can deliver a variety of food and drinks to your home free of charge!", reply_markup=mb_1)

@dp.message(F.text == "Ma'lumot ℹ️")
async def tea_function(message: types.Message):
    await message.answer("Biz sizning uyingizga turli xil oziq-ovqat va ichimliklarni bepul yetkazib berishimiz mumkin!", reply_markup=mb_1)

@dp.message(F.text == "About you 🫵")
async def you_function(message: types.Message):
    await message.answer(f"Name:{message.from_user.full_name} \nLast_name:{message.from_user.last_name} \nId:{message.from_user.id}", reply_markup=mb_1)

@dp.message(F.text == "Fries(3) 🍟")
async def fries_function(message: types.Message):
    await message.answer("choose a frie🍟", reply_markup=mb_2)

@dp.message(F.text == "Gamburger(3) 🍔")
async def gamburger_function(message: types.Message):
    await message.answer("choose a burger🍔", reply_markup=mb_3)

@dp.message(F.text == "Hot_dog(3) 🌭")
async def hotdog_function(message: types.Message):
    await message.answer("choose a hot dog🌭", reply_markup=mb_4)

@dp.message(F.text == "Pizza(3) 🍕")
async def pizza_function(message: types.Message):
    await message.answer("choose a pizza 🍕", reply_markup=mb_5)

@dp.message(F.text == "Shashlik(3)")
async def shashlik_function(message: types.Message):
    await message.answer("choose a shashlik", reply_markup=mb_6)

@dp.message(F.text == "Taco(3) 🌮")
async def taco_function(message: types.Message):
    await message.answer("choose a taco 🌮", reply_markup=mb_7)

@dp.message(F.text == "Sushi(3) 🍣")
async def sushi_function(message: types.Message):
    await message.answer("choose a sushi 🍣", reply_markup=mb_8)

@dp.message(F.text == "🔙 back_from_the_foods")
async def sushi_function(message: types.Message):
    await message.answer("you are back to the menu", reply_markup=mmenutop)

@dp.message(F.text == "Fries_medium 🍟")
async def fries_medium_function(message: types.Message):
    orders.append("Juice:13ming so'm💵")
    await message.answer_photo(photo="https://s7d1.scene7.com/is/image/mcdonalds/DC_202002_8932_MediumFries_832x472:1-3-product-tile-desktop?wid=765&hei=472&dpr=off",
                               caption="Price:13ming so'm")

@dp.message(F.text == "Fries_long 🍟")
async def fries_long_function(message: types.Message):
    orders.append("Juice:15ming so'm💵")
    await message.answer_photo(photo="https://i.ytimg.com/vi/tguPrkEJoFY/maxresdefault.jpg",
                               caption="Price:15ming so'm")

@dp.message(F.text == "Fries_short 🍟")
async def fries_short_function(message: types.Message):
    orders.append("Juice:10ming so'm💵")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRBzqoyf7fvJORIQ_ZOuGodnhEIXjm5gE73bg&s",
                               caption="Price:10ming so'm")

@dp.message(F.text == "Chesse_burger 🍔")
async def chesse_burger_function(message: types.Message):
    orders.append("Juice:24ming so'm💵")
    await message.answer_photo(photo="https://s7d1.scene7.com/is/image/mcdonalds/mcdonalds-triple-cheeseburger-april-promo:nutrition-calculator-tile?wid=822&hei=822&dpr=off",
                               caption="Price:24ming so'm")

@dp.message(F.text == "Chili_burger 🍔")
async def chili_burger_function(message: types.Message):
    orders.append("Juice:24ming so'm💵")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlvUPYubVQ1oEVPTEyEzBQlfUPHxisrT1PBw&s",
                               caption="Price:24ming so'm")

@dp.message(F.text == "Simple_burger 🍔")
async def simple_burger_function(message: types.Message):
    orders.append("Juice:23ming so'm💵")
    await message.answer_photo(photo="https://assets.epicurious.com/photos/57c5c6d9cf9e9ad43de2d96e/master/pass/the-ultimate-hamburger.jpg",
                               caption="Price:23ming so'm")

@dp.message(F.text == "Hot_dog_medium 🌭")
async def hot_dog_medium_function(message: types.Message):
    orders.append("Juice:26ming so'm💵")
    await message.answer_photo(photo="https://www.licious.in/blog/wp-content/uploads/2016/07/Hot-Dogs.jpg",
                               caption="Price:26ming so'm")

@dp.message(F.text == "Hot_dog_short 🌭")
async def hot_dog_short_function(message: types.Message):
    orders.append("Hot:20ming so'm💵")
    await message.answer_photo(photo="https://cdn.jwplayer.com/v2/media/25Ez4pc2/poster.jpg?width=720",
                               caption="Price:20ming so'm")

@dp.message(F.text == "Hot_dog_long 🌭")
async def hot_dog_long_function(message: types.Message):
    orders.append("Hot_dog_long:29ming so'm💵")
    orders.append("Juice:29ming so'm💵")
    await message.answer_photo(photo="https://sausageman.co.uk/wp-content/uploads/2015/11/foot-long-sausage.jpg",
                               caption="Price:29ming so'm")

@dp.message(F.text == "Pizza_small 🍕")
async def pizza_small_function(message: types.Message):
    orders.append("Pizza_small:50ming so'm💵")
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR04AV9hm-IycrcBC5rDAjHm6v3KUkYkgcKyw&s",
                               caption="Price:50ming so'm")

@dp.message(F.text == "Pizza_medium 🍕")
async def pizza_medium_function(message: types.Message):
    await message.answer_photo(photo="https://www.allrecipes.com/thmb/nzVo4U1V3ygCcC-seYQm46jpFHY=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/M7007481_Ratatouille_Pizza_131-e4b6a91f521c42eda294945c98ba4637.png",
                               caption="Price:65ming so'm")

@dp.message(F.text == "Pizza_large 🍕")
async def pizza_large_function(message: types.Message):
    await message.answer_photo(photo="https://popmenucloud.com/cdn-cgi/image/width%3D1200%2Cheight%3D1200%2Cfit%3Dscale-down%2Cformat%3Dauto%2Cquality%3D60/oyxtwnas/b096e3cb-13d0-407c-98be-147957bf2400.jpeg",
                               caption="Price:70ming so'm")

@dp.message(F.text == "Shashlik_chicken")
async def shashlik_chicken_function(message: types.Message):
    await message.answer_photo(photo="https://theyummydelights.com/wp-content/uploads/2021/10/chicken-shashlik-6.jpg",
                               caption="Price:18ming so'm")

@dp.message(F.text == "Shashlik_beef")
async def shashlik_beef_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRCoEJMwMPy86Y1PEbuFR7pCx6BI3q9WQ9SbA&s",
                               caption="Price:20ming so'm")

@dp.message(F.text == "Shashlik_lamb")
async def shashlik_lamb_function(message: types.Message):
    await message.answer_photo(photo="https://www.thespruceeats.com/thmb/mYRWRdFvr5he3whZb4wOgKqQCJQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/lamb-shashlik-recipe-2355654-Hero_01-eae5bbb2db2849bf861966647c5a09b8.jpg",
                               caption="Price:25ming so'm")

@dp.message(F.text == "Taco_beef 🌮")
async def taco_beef_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTEhqk5cA7Wt2k7w4RFIdi97vrRAXDVNbhgsQ&s",
                               caption="Price:21ming so'm")

@dp.message(F.text == "Taco_chicken 🌮")
async def taco_chicken_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQARApmWyNOEd9JppyZqYifsaquLrIzx_qVpA&s",
                               caption="Price:22ming so'm")

@dp.message(F.text == "Taco_veggie 🌮")
async def taco_veggie_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ1n60rbGwoEn9KXoe8F2DEkTXBf42qe7jCig&s",
                               caption="Price:20ming so'm")

@dp.message(F.text == "Sushi_salmon 🍣")
async def sushi_salmon_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToiYRmShJapV_O0JJgU3ygOnOQVgnu7rL10A&s",
                               caption="Price:30ming so'm")

@dp.message(F.text == "Sushi_tuna 🍣")
async def sushi_tuna_function(message: types.Message):
    await message.answer_photo(photo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQQ4trtPlFn6tKyjZ5JBR1q4UU1j4r4SFQ4TQ&s",
                               caption="Price:28ming so'm")

@dp.message(F.text == "Sushi_veggie 🍣")
async def sushi_veggie_function(message: types.Message):
    await message.answer_photo(photo="https://www.justonecookbook.com/wp-content/uploads/2023/05/Vegetarian-Sushi-Rolls-9707-I-1.jpg",
                               caption="Price:25ming so'm")

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())