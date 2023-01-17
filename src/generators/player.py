from src.enum.user_enums import StatusEnum
from src.generators.player_localize import PlayerLocalize


class Player:
    def __init__(self):
        self.obj = {}
        self.reset()

    def set_status(self, status=StatusEnum.active.value):
        self.obj['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.obj['balance'] = balance
        return self

    def set_avatar(self, avatar='https://www.google.com/'):
        self.obj['avatar'] = avatar
        return self

    def set_localize(self):
        self.obj['localize'] = {
            'en': PlayerLocalize('en_US').build(),
            'ru': PlayerLocalize('ru_RU').build()
        }
        return self

    def reset(self):
        self.set_status()
        self.set_balance()
        self.set_avatar()
        self.set_localize()
        return self

    def generator_localize(self, generator):
        self.obj['localize'] = {
            'en': generator.build()
        }
        return self

    def build(self):
        return self.obj

# print(Player().set_balance(150).build())
