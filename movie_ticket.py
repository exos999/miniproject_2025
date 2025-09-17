movies = {
    "avengers":{"premium":20,"normal":80},
    "inception":{"premium":25,"normal":80},
    "interstellar":{"premium":20,"normal":80}
    
}

# Display movies and available seats
# Ask user for movie name + tickets needed
# If enough seats → reduce count
# If not enough → print "sorry, only X left"
# Continue until "done" need full coode
# maximum ticket 5 
# seat preium ,normal


print("Welcome to ABC cinemas")
print("____________________________")
p_booking ={}
n_booking = {}
print("Avaliable  movies and seats lefts ")

for i in movies:
    print(f"{i} --> Premium : {movies[i]["premium"]} , Normal --> {movies[i]["normal"]} ")



while True:

    

    film = input("which movie did you want to watch ? (if u want to exit type 'exit') ")

    if film.lower() == "exit":
        print(" Thank you ")

        break

    if film  not in movies:

        print("Please enter a avaliable movie name")
        continue

    else:
        while True:
            seat_type = input("which seat type did you want (Premium:250rs / Normal:150rs)")

            if seat_type.lower() == "premium":
                
                while True:
                    seats = int(input("how many tickets did you want ? (max 5)"))
                    
                    if seats >=6:
                        print("Sorry at atime only  you can book 5 tickets ")
                        seats = int(input("how many tickets did you want ? (max 5)"))
                        

                    elif seats > movies[film]["premium"]:

                        print(f"sorry only {movies[film]["premium"]} are left ")
                        continue
                        

                    else:
                        p_booking[film] = p_booking.get(film , 0)+ seats
                        start = movies[film]["premium"]
                        end = start - seats

                        print(" Your Premium seats are")

                        for seat_no in range(start , end ,-1):

                            print(f" seat :{seat_no}")

                    


                        bill = seats* 250

                        print(f"The total cost of ticket is {bill} rs")
                        movies[film]["premium"] -= seats

                        break
                    
            elif seat_type.lower() == "normal":


                while True:

                    seats = int(input("how many tickets did you want ? (max 5)"))
                    
                    
                    if seats >=6:
                        print("Sorry at atime only  you can book 5 tickets ")
                        seats = int(input("how many tickets did you want ? (max 5)"))
                        

                    elif seats > movies[film]["normal"]:

                        print(f"sorry only {movies[film]["normal"]} are left ")
                        continue
                        

                    else:
                        n_booking[film] = n_booking.get(film , 0)+ seats
                        start = movies[film]["normal"]
                        end = start - seats

                        print(" Your Normal seats are")

                        for seat_no in range(start , end ,-1):

                            print(f" seat :{seat_no}")

                    


                        bill = seats* 150

                        print(f"The total cost of ticket is {bill} rs")
                        movies[film]["normal"] -= seats

                        break




            else:

                print("please select the valid option")
                # seat_type = input("which seat type did you want (Premium:250rs / Normal:150rs)")

                continue
            break

    again = input("Do you want to book again? (yes/no): ").lower()
    if again == "yes":
                print("Avaliable  movies and seats lefts ")
                for i in movies:
                    print(f"{i} --> Premium : {movies[i]["premium"]} , Normal --> {movies[i]["normal"]} ")
                    
                
    else:                       
                print(" Thank you for booking with ABC Cinemas")
                break