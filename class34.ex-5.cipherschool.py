name,char=str(input("user name and char: ")).split(",")
print(f"length of the name {len(name.strip())}")
print(f"char count {name.strip().lower().count(char.strip().lower())}")







