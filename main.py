# talking total amount as input.
Amount = int(input("please Enter amount to withdraw"))

note_1 = Amount//100
note_2 = (Amount%100)//50
note_3 = ((Amount%100)%50)//10

print ("Notes of a hundred :" , note_1)
print ("notes of a 50 :" , note_2)
print ("notes of a 10 :" , note_3)