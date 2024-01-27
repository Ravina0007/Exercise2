#The program converts the input to full kilograms and grams

def convert_to_kg_and_grams(mass_talents, mass_pounds, mass_lots):

    pounds_per_talent = 20
    lots_per_pound = 32
    grams_per_lot = 13.3


    total_grams = (mass_talents * pounds_per_talent * lots_per_pound * grams_per_lot) + \
                  (mass_pounds * lots_per_pound * grams_per_lot) + \
                  (mass_lots * grams_per_lot)


    kilograms = total_grams // 1000
    grams = total_grams % 1000

    return kilograms, grams

def main():

    talent_input = float(input("Enter mass in talents : "))
    pound_input = float(input("Enter mass in pounds : "))
    lot_input = float(input("Enter mass in lots ): "))

    kilograms, grams = convert_to_kg_and_grams(talent_input, pound_input, lot_input)


    print(f"The weight in modern units: {kilograms} kilograms and {grams} grams.")

if __name__ == "__main__":
    main()
