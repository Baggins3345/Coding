# So I added a while loop to keep the user looking up a year to look at. This way you don't have to get out of the prgram to look at another year. 
# Pretty simple but this was a pretty big assignment, so I wanted to keep it simpler, tho I did have trouble making the loop work just right. 



# Load the dataset in your Python program
another = ''
while another != "no":
    with open("life-expectancy.csv") as life_file:
        next(life_file)
        min_life = 999999999
        min_country = ''
        min_year = 0

        max_life = 0
        max_country = ''
        max_year = 0
        year_list = []

        max_life_user_country = ''
        max_life_user_year = 0
        min_life_user_country = ''
        min_life_user_year = 999999999

        user_year = int(input("Enter the year of interest: "))
        # Iterate through the data line by line
        for line in life_file:
            # Split each line into parts
            life_seperate = line.strip().split(",")

            country = life_seperate[0]
            # code = life_seperate[1]
            year = int(life_seperate[2])
            life_expec = float(life_seperate[3])

            # Find the lowest value for life expectancy and the highest 
            # value for life expectancy in the dataset, and display 
            # both values. (Note that at this point, you just need 
            # the value for this, not the year and the country for that value.)
            if life_expec < min_life:
                min_life = life_expec
                min_country = country
                min_year = year

            if life_expec > max_life:
                max_life = life_expec
                max_country = country 
                max_year = year
            
            if user_year == year:
                year_list.append(life_expec)
                # amount_years = len(year_list)
                # sum_years = sum(year_list)
                # avg_year = sum_years/amount_years
                if life_expec > max_life_user_year:
                    max_life_user_year = life_expec
                    max_life_user_country = country

                if life_expec < min_life_user_year:
                    min_life_user_year = life_expec
                    min_life_user_country = country



        print(f"\nThe overall max life expectancy is: {max_life} from {max_country} in {max_year}")
        print(f"The overall min life expectancy is: {min_life} from {min_country} in {min_year}")

        if year_list:
            avg_year = sum(year_list) / len(year_list)
            print(f"\nFor the year {user_year}:")
            print(f"The average life expectancy across all countries was {avg_year:.2f}")
            print(f"The max life expectancy was in {max_life_user_country} with {max_life_user_year}")
            print(f"The min life expectancy was in {min_life_user_country} with {min_life_user_year}")
            
        else:
            print(f"\nNo data available for the year {user_year}.")
        while True:
            another = input("\nWould you like to do another year? (yes/no): ").strip().lower()
            if another in ["yes", "no"]:
                break
            else:
                print("That input isn't accepted, try again.")