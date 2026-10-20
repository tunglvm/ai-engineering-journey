gia = {
    "mojito": 200000,
    "negroni": 230000,
    "daiquiri": 230000,
    "margarita": 230000,
    "gin tonic": 180000
}

gia["whisky sour"] = 250000 #add

del gia["daiquiri"]

gia["mojito"] = int(round(gia["mojito"] * 1.1 ))

print(gia)

print(list(gia.items()))

#Mỗi cặp là một tuple, giá nằm ở vị trí 1. Ta bảo sorted dùng cap[1] để so sánh:
#Nếu viết sorted(gia.items()) mà không có key, Python sẽ so sánh phần tử đầu tiên của mỗi cặp, tức là sắp theo tên chứ không phải theo giá.
theo_gia = sorted(gia.items, key=lambda cap: cap[1])

print(theo_gia)


print("===== MENU =====")
for mon, g in theo_gia:
    print(f"{mon.title():<12}{g:>10,}đ")
    
mon_can_tim = "martini"
g = gia.get(mon_can_tim)          # không có thì trả về None

if g is None:
    print(f"{mon_can_tim.title()}: Không có")
else:
    print(f"{mon_can_tim.title()}: {g:,}đ")
    