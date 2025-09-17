movies = {
    "avengers":{"premium":20,"normal":80},
    "inception":{"premium":25,"normal":80},
    "interstellar":{"premium":20,"normal":80}
    
}



def show_movies():
     
     print("Avaliable  movies and seats lefts ")
     for i in movies:
        print(f"{i} --> Premium : {movies[i]["premium"]} , Normal --> {movies[i]["normal"]} ")

     
print("Welcome to ABC cinemas")
print("____________________________")
p_booking ={} #to store the booking details of notmal booking
n_booking = {}#to store the booking details of premium booking


show_movies()




while True:

    
    film = input("which movie did you want to watch ? (if u want to exit type 'exit') ")

    if film.lower() == "exit":
        print(" Thank you ")
        break


    if film  not in movies:
        print(" Please enter a valid movie name.")
        continue

    
    while True:
        seat_type = input("which seat type did you want (Premium:250rs / Normal:150rs)").lower()

        if seat_type not in ["premium" , "normal"]:
            print("Please enter a valid seat type!")
            continue


        
        while True:
            try:
                seats_no = int(input("how many tickets did you want ? (max 5)"))

            except ValueError:
                print("enter proper ticket count")
                continue
                    
            if seats_no >=6:
                print("Sorry at atime only  you can book 5 tickets ")
                continue
                
            elif seats_no > movies[film][seat_type]:
                print(f"sorry only {movies[film][seat_type]} are left ")
                continue



            # Premium ticket booking
            if seat_type == "premium":
                p_booking[film] = p_booking.get(film , 0)+ seats_no  

                start = movies[film]["premium"]
                end = start - seats_no

                print(" Your Premium seats are")

                for seat_no in range(start , end ,-1):  #seat no dispaly
                    print(f" seat :{seat_no}")


                bill = seats_no* 250

                print(f"The total cost of ticket is {bill} rs")
                movies[film]["premium"] -= seats_no
                break


            # normal ticket booking
            else:
                n_booking[film] = n_booking.get(film , 0)+ seats_no

                start = movies[film]["normal"]
                end = start - seats_no

                print(" Your Normal seats are")

                for seat_no in range(start , end ,-1):
                    print(f" seat :{seat_no}")


                bill = seats_no* 150

                print(f"The total cost of ticket is {bill} rs")
                movies[film]["normal"] -= seats_no

                break


        # ASK USER TO BOOK AGAIN
        again = input("Do you want to book again? (yes/no): ").lower()

        if again == "yes":
            show_movies()
            break        
        else:                       
            print(" Thank you for booking with ABC Cinemas")
            exit()
        