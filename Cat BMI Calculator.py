# This program will calculate your cat's
# BMI and tell you whether your cat is healthy or overweight


leg = int(input("Measure one of your cats rear legs in centimeters."))
rib = int(input("Measure the ribcage of your cat around the ninth rib in centimeters."))

# This is the equation to get the fbmi score
fbmi = ((rib / 0.7062 - leg) / 0.9156) - leg
print(fbmi)


# This allows for telling if your cat if healthy or overweight based on their fbmi score
if 15 <= fbmi <= 29.9:
    print("Your cat is at a normal weight.")
elif 30 <= fbmi <= 42:
    print("Your cat is overweight.")
elif fbmi > 42:
    print("Your cat is obese.")
else:
    print("Your cat is underweight.")
