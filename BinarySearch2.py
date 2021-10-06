import pyinputplus as pyip

list = [1, 2, 3, 4, 5, 6, 7, 8]
key = pyip.inputInt("What would you like to find: ", min = 0, max = len(list))
start = 0
end = len(list) - 1
mid = (end + start)//2
while key != list[mid]:
    mid = (end + start)//2
    if list[mid] < key:
        start = mid + 1
    else:
        end = mid - 1
else:
    print(f"{key} is at index {mid}.")
    
    #hello
