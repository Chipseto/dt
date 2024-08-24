# красный, розовый, фиолетовый, черный,белый и серый, жёлтый, оранжевый, персиковый, коричневый.
question1=input('Ваш цвет из семейства красных?')
if question1=='да':
    question2=input('Ваш цвет красный или фиолетовый?')
    if question2 == 'да':
        question3=input('Ваш цвет красный?')
        if question3 == 'да':
                print('Ваш цвет красный')
        else:
            print('Ваш цвет фиолетовый')
    else:
        print('Ваш цвет розовый')
quit()
question1=input('Ваш цвет из семейства монохромных?')
if question1=='да':
    question2=input('Ваш цвет черный или белый?')
    if question2 == 'да':
        question3=input('Ваш цвет черный?')
        if question3 == 'да':

                print('Ваш цвет черный')
        else:
            print('Ваш цвет белый')
    else:
        print('Ваш цвет серый')
quit()
question7=input('Ваш цвет из семейства желтых?')
if question7=='да':
    question8=input('Ваш цвет желтый или оранжевый?')
    if question8=='да':
        question9=input('Ваш цвет желтый?')
        if question9 == 'да':
            print('Ваш цвет желтый')
        else:
            print('Ваш цвет оранжевый')
    else:
        question9=input('Ваш цвет персиковый?')
        if question9=='да':
            print('Ваш цвет персиковый')
        else:
            print('Ваш цвет коричневый')

































































































