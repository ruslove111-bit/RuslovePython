Symbols = 100 * 50 * 25
Symbols_Data = Symbols * 4
Data = 1.44 * 1024 * 1024
Books = int(Data // Symbols_Data)
# TODO Найдите количество книг, которое можно разместить на дискете

print("Количество книг, помещающихся на дискету:", Books)
