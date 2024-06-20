def get_starting_number():
    return 99

def sing(num_bottles):
    for bottles in range(num_bottles, 0, -1):
        print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
        print(f"Take one down and pass it around, {bottles - 1} bottles of beer on the wall.\n")
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")