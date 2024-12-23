class Flight:
    def __init__(self,f_no,dep_city,arr_city,dur):
        self.f_no = f_no
        self.dep_city = dep_city
        self.arr_city = arr_city
        self.dur=dur

    def details(self):
        print("Flight No : ",self.f_no)
        print("Departure City : ",self.dep_city)
        print("Arrival City : ",self.arr_city)
        print("Duration (in hrs) : ",self.dur)

class DomesticFlight(Flight):
    def __init__(self, f_no, dep_city, arr_city, dur,distance,b_weight):
        super().__init__(f_no, dep_city, arr_city, dur)
        self.distance = distance
        self.b_weight=b_weight

    def fare_calc(self):
        price= self.distance*10 # assuming fare to be Rs.10/KM and Baggage to be Rs.5/KG
        return price

    def details(self):
        return super().details()
    
class InternationalFlight(Flight):
    def __init__(self, f_no, dep_city, arr_city, dur,distance,b_weight):
        super().__init__(f_no, dep_city, arr_city, dur)
        self.distance=distance
        self.b_weight=b_weight

    def fare_calc(self):
        price= self.distance*12 # assuming fare to be Rs.12/KM and Baggage to be Rs.5/KG
        return price
    
    def details(self):
        return super().details()
    
class Passenger:
    def __init__(self,p_id,p_name):
        self.p_id=p_id
        self.p_name=p_name
        self.price=None
        self.pay_status=False
        self.reservation_history=[]

        
    def book_flight(self,flight,no_of_passengers,b_weight_no):
        if flight.b_weight<=b_weight_no:
            print(f"Baggage Weight Exceeded")
            return
        else:
            self.price = flight.fare_calc()
            if flight.f_no[0]=='D':
                self.price = self.price + b_weight_no*5
            if flight.f_no[0]=='I':
                self.price = self.price + b_weight_no*3
            print(f"Flight Booked for {no_of_passengers} persons!")            
            print(f"Price of 1 Flight : {self.price}")
            print(f"Total Price : {no_of_passengers*self.price}")
            print("\nFlight Details : ")
            flight.details()
            self.reservation_history.append(( self.p_id, self.p_name, no_of_passengers, self.price*no_of_passengers, flight.f_no))

    def payment(self,amt):
        if amt==self.price:
            self.pay_status=True
            print("Payment Successfull")
        else:
            print("Please Enter Correct Amount")


    def reservation_details(self):
        print("----Booking/Reservation Details----\n")
        print( 'FlightNo|Name|NoOfPersons|TotalPrice|FlightID' )
        for rec in self.reservation_history:
            print(rec)




# FlightNumber | DepartureCity | ArrivalCity | Duration(hrs) | Distance | BaggageLimit(KG)

domestic_flight = DomesticFlight("D123","Delhi","Banglore",3,1200,25)
international_flight = InternationalFlight("I001","Jewar","LasVegas",8,12000,30)


# PassengerID/Passport | PassengerName

passenger1 = Passenger(12345, "Mr.Sharma")
passenger2 = Passenger(98765,"Mr.Chawla")

print()
print()

# FlightInfo | Persons | Baggage

passenger1.book_flight(domestic_flight,2,10)

print()
print()

passenger2.book_flight(international_flight,2,15)

print()
print()

passenger1.reservation_details()
 
print()

passenger2.reservation_details()

print()
print()

# domestic_flight.details()






