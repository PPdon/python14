#การแสดงค่าในlist
fruits = ["apple","bfanana","cherry","watermelon","blueberry"]
print(fruits[1])
#เปลี่ยนค่าในlist
fruits[1]="blackcurrant"
print(fruits[1])
#เปลี่ยนค่าในlistหลายตําแหน่ง
fruits[1:3]=["kiwi","mango","pineapple"]
print(fruits)
fruits.append("orange")
print(fruits)
fruits.insert(3,"grape")
print(fruits)
tropical=["mango","pineapple","papaya"]
fruits.extend(tropical)
print(fruits)
#ลบค่าในlist
fruits.remove("watermelon")
print(fruits)
fruits.pop(1)
#del fruits
fruits.sort(reverse=True)
print(fruits)
#นายพีรดนย์ หลอดทอง