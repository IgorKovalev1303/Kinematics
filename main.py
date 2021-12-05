from modules.pol_vel import velocity
from modules.kinematics import kinem

resp = None

while resp != '0':
    print('''[1] - Кинематика
[2] - Поле скоростей
[0] - Выход
    ''')
    resp = input("=: ").strip()
    if resp == '1':
        kinem()
    elif resp == '2':
        velocity()
    elif resp == '0':
        print('Выход')
    else:
        print('Неверные данные')
    

