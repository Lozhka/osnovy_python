def user_data(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}', end=", ")


user_data(name='Yan', surname='Shishkin', year_birth=1995,
          city_residence='Orel', email='secret@mail.ru', telephone='+7(900)000-00-00')