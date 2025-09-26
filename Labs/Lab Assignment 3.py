square_miles = float(input("How many square miles are there?: "))
acres = float(input("How many acres are there?: "))
square_km = float(input("How many square kilometers are there?: "))

#these values are taken from the assigment
sm_to_h = square_miles * 258.9988
#sm_to_h = square miles to hectares
a_to_h = acres * 0.4047
#a_to_h = acres to hectares
sk_to_h = square_km * 100
#sk_to_h = square kilometers to hectares

#this code will calculate the total area in hectares and each variable converted to hectares
print(f"{square_miles} square miles is {square_miles*258.9988:.1f} hectares.")
print(f"{acres} acres is {acres*0.4047:.1f} hectares.")
print(f"{square_km} square kilometers is {square_km*100:.1f} hectares.")
print(f"The total area is {sm_to_h + a_to_h + sk_to_h:.1f} hectares.")

