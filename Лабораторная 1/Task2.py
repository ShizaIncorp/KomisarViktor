# TODO Найдите количество книг, которое можно разместить на дискете

info_vol = 1.44 * 1024 * 1024
total_page = 100
numbers_str = 50
total_sym = 25

one_book_memory = 4 * total_sym * numbers_str * total_page
total_book = info_vol // one_book_memory

print("Количество книг, помещающихся на дискету:", int(total_book))
