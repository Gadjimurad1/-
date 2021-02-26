class weapon:
    def __init__(self,name,type,Distance,Bullet_speed,Damage,Clip,Cartridges):
         self.name = name
         self.type = type
         self.Distance = Distance
         self.Bullet_speed = Bullet_speed
         self.Damage = Damage
         self.Clip = Clip
         self.Cartridges = Cartridges
    def start(self):
        print("Выстрел")
    def stop (self):
        print('Перезарядка')
my_weapon=weapon('M416','Винтовка','25-450 м','880 м/с','43','30','5.56 мм')
print('Название-'+my_weapon.name,'Тип-'+my_weapon.type,'Дистанция-'+my_weapon.Distance,'Скорость пули-'+my_weapon.Bullet_speed,'Урон-'+my_weapon.Damage,sep='\n')