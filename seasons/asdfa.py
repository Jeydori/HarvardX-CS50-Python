from datetime import date

b = str("2001-06-15").strip().split("-")
c = str(date.today()).split("-")
b = date(int(b[0]), int(b[1]), int(b[2]))
c = date(int(c[0]), int(c[1]), int(c[2]))
a = c - b
print(a)

