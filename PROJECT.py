rooms = {}
caps = {1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8}

def allot(stu):
    yr = stu["year"]
    sh = stu["share"]
    lim = caps[sh]

    if yr not in rooms:
        rooms[yr] = []

    for rm in rooms[yr]:
        if (rm["share"] == sh and 
            rm["ac"] == stu["ac"] and 
            len(rm["list"]) < lim):
            rm["list"].append(stu)
            return rm["no"]

    no = f"{yr}-R{len(rooms[yr]) + 1}"
    new = {
        "no": no,
        "share": sh,
        "ac": stu["ac"],
        "list": [stu]
    }

    rooms[yr].append(new)
    return no

while True:
    print("\nHostel Allotment")

    nm = input("Name: ")
    reg = input("Reg No: ")
    age = int(input("Age: "))
    yr = int(input("Year (1-4): "))
    st = input("State: ")

    print("\nAC Type")
    print("1. AC\n2. Non-AC")
    ac_in = int(input("Choose: "))
    ac = "AC" if ac_in == 1 else "Non-AC"

    print("\nSharing (1–8)")
    sh = int(input("Type: "))

    stu = {
        "name": nm,
        "reg": reg,
        "age": age,
        "year": yr,
        "state": st,
        "ac": ac,
        "share": sh
    }

    out = allot(stu)

    print("\nRoom Allotted")
    print(f"Name: {nm}")
    print(f"Room No: {out}")
    print(f"Sharing: {sh}")
    print(f"AC: {ac}")

    more = input("\nAdd more? (yes/no): ").lower()
    if more != "yes":
        break

print("\nFinal List")
for yr, rlist in rooms.items():
    print(f"\nYear {yr}")
    for rm in rlist:
        print(f" {rm['no']} | {rm['share']}-Share | {rm['ac']}")
        for s in rm["list"]:
            print(f"   - {s['name']} ({s['reg']})")
