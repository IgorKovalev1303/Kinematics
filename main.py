from function.kinematics.graph_kin import show_kin
from function.pol_vel.graph_vel import show_vel

resp = None

while resp != '0':
    print('''[1] - Кинематика
[2] - Поле скоростей
[0] - Выход
    ''')
    resp = input("=: ").strip()
    if resp == '1':
        show_kin()
    elif resp == '2':
        show_vel()
    elif resp == '0':
        print('Выход')
    else:
        print('\nНеверные данные\n')
