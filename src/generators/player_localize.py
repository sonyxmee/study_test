from faker import Faker


class PlayerLocalize:
    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            'nickname': self.fake.first_name()
        }

    def set_age(self, age=18):
        self.result['age'] = age
        return self

    def build(self):
        return self.result
