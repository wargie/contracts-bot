from aiogram.fsm.state import StatesGroup, State

class ContractFSM(StatesGroup):
    start = State()
    contract_type = State()
    customer_name = State()
    customer_inn = State()
    customer_kpp = State()
    contractor_name = State()
    contractor_inn = State()
    contractor_kpp = State()
    params_number = State()
    params_date = State()
    params_city = State()
    params_subject = State()
    params_price = State()
    params_payment = State()
    params_term = State()
    params_penalties = State()
    output_format = State()
    confirm = State()

class CheckFSM(StatesGroup):
    wait_inn = State()

class FlexFSM(StatesGroup):
    # Новый упрощённый сценарий: после выбора юрлица и формы оплаты
    # спрашиваем только ИНН контрагента и фамилию менеджера.
    wait_inn = State()
    wait_manager = State()