from hikka import Hikka


h = Hikka()
for i in h.get_stuff("fullmetal-alchemist-brotherhood-fc524a"):
    print("\n", i.name_native, i.name_en)
    print(i.roles)

# print(len(h.genres.list))
