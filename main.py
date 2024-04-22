from hikka import Hikka


h = Hikka()
for i in h.get_voices_by_character("alphonse-elric-e3622e"):
    print(i)

# print(len(h.genres.list))
