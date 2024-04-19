
from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

payload = Chat(
    messages=[
        Messages(
            role=MessagesRole.SYSTEM,
            content="""Ты выполняешь функцию аналитика, который получает текст на вход и выдает нужную информацию в определенном формате, примеры запросов и ответов которые ты выдаешь ниже. Отвечай строго по тексту, ничего от себя не придумывай

Пример:
220423/2/160000278 Передано через модуль Контур.Диадок

Ответ  который ты выдаешь:
220423/2/160000278;

Пример:
Паспорт 220123.3.57110501,140123.3.57051253,220223.2.57457311,180423.4.POER-663.1.1,190123.2.57052978,220223.1.57370153,080223.1.57211882 Передано через модуль Контур.Диадок

Ответ  который ты выдаешь:
220123.3.57110501;140123.3.57051253;220223.2.57457311;180423.4.POER-663.1.1;190123.2.57052978;220223.1.57370153;080223.1.57211882;

Пример:
Паспорт 150423.3.POER-564.1.1  Передано через модуль Контур.Диадок

Ответ который ты выдаешь:
150423.3.POER-564.1.1;

Пример:
160324/4/424000354   230224/1/424000201   070324/2/424000281   200324/4/424000372

Ответ который ты выдаешь:
160324.4.424000354;230224.1.424000201;070324/2/424000281;200324.4.424000372;
"""


        ),
        Messages(
            role=MessagesRole.USER,
            content="220423/2/160000278 Передано через модуль Контур.Диадок",
        ),
        Messages(
            role=MessagesRole.ASSISTANT,
            content="220423.2.160000278;",
        ),
        Messages(
            role=MessagesRole.USER,
            content="Паспорт 220123.3.57110501,140123.3.57051253,220223.2.57457311,180423.4.POER-663.1.1,190123.2.57052978,220223.1.57370153,080223.1.57211882 Передано через модуль Контур.Диадок",
        ),
        Messages(
            role=MessagesRole.ASSISTANT,
            content="220123.3.57110501;140123.3.57051253;220223.2.57457311;180423.4.POER-663.1.1;190123.2.57052978;220223.1.57370153;080223.1.57211882;",
        ),
        Messages(
            role=MessagesRole.USER,
            content="Паспорт 150423.3.POER-564.1.1  Передано через модуль Контур.Диадокс",
        ),
        Messages(
            role=MessagesRole.ASSISTANT,
            content="150423.3.POER-564.1.1;",
        ),
        Messages(
            role=MessagesRole.USER,
            content="ПАСПОРТ  № 130124/1/РСER-81.1.1, 070124/2/РСER-10.1.1, 210124/4/РСER-126.1.1, 210124/1/РСER-125.1.1, 15.12.23/2/POER-10496.1.1, 100124/1/РСER-30.1.1 Передано через модуль Контур.Диадок",
        ),
        Messages(
            role=MessagesRole.ASSISTANT,
            content="130124.1.РСER-81.1.1;070124.2.РСER-10.1.1;210124.4.РСER-126.1.1;151223.2.POER-10496.1.1;100124.1.РСER-30.1.1;",
        ),
        Messages(
            role=MessagesRole.USER,
            content="Паспорт 090324.3.124001353.1.1,33 Передано через модуль Контур.Диадок",
        ),
        Messages(
            role=MessagesRole.ASSISTANT,
            content="090324.3.124001353.1.1;",
        ),
        Messages(
            role=MessagesRole.USER,
            content="Паспорт 220123.3.57110501,05,080223.1.57211882,1 Передано через модуль Контур.Диадок",
        ),
        Messages(
            role=MessagesRole.ASSISTANT,
            content="220123.3.57110501;080223.1.57211882;",
        ),
        Messages(
            role=MessagesRole.USER,
            content="Паспорт 220123.3.57123401,54,34523.1.57211882,4,23434.2.435345345 Передано через модуль Контур.Диадок",
        ),
        Messages(
            role=MessagesRole.ASSISTANT,
            content="220123.3.57123401;34523.1.57211882;23434.2.435345345;",
        )
    ],
    temperature=0,
    max_tokens=100,
)

# Используйте токен, полученный в личном кабинете из поля Авторизационные данные
with GigaChat(credentials="NzJjNTNkNTUtMzMwMi00YzA5LWJjODgtM2Y0OWM5NGU0MWM2OmE2MWJiODVmLTc4YzMtNGZjMC1iZjIwLWFlMDQ5MDA1ZjdlNg==", verify_ssl_certs=False) as giga:
    while True:
        user_input = input("User: ")
        payload.messages.append(Messages(role=MessagesRole.USER, content=f"{user_input}"))
        response = giga.chat(payload)
        payload.messages.append(response.choices[0].message)
        print("Bot: ", response.choices[0].message.content)
