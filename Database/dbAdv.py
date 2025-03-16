from typing import Optional, Dict
from Database import *
from Database.AdvInfoDao import Advertisement

class TestDb:
    def __init__(self):
        db.connect()
        db.create_tables([Advertisement], safe=True)

    def get_advertisement(self, advnumber: str) -> Optional[Dict]:
        adv = Advertisement.select().where (Advertisement.advnumber == advnumber)
        return adv[0]


    def save_advertisement(self, adv_number: str, title: str, desc: str, fraud_adv: int = 0) -> int:
        adv = Advertisement(
            advnumber=adv_number,
            title=title,
            description=desc,
            fraudadv=fraud_adv)
        
        adv.save()
        return adv.id
