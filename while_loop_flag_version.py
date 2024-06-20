def get_starting_number():
    return 99

def sing(num_bottles):
    bottles = num_bottles
    keep_singing = True
    while keep_singing:
        if bottles > 0:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            bottles -= 1
            print(f"Take one down and pass it around, {bottles} bottles of beer on the wall.\n")
        else:
            keep_singing = False
    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall.")