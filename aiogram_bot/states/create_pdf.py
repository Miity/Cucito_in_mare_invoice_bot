from aiogram.dispatcher.filters.state import StatesGroup, State


class Create_states(StatesGroup):
    start = State()
    level_1 = State()
    level_2 = State()
    level_3 = State()
    level_4 = State()
    level_5 = State()