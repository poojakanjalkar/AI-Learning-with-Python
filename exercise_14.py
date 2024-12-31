class Hotel:
    def __init__(self):
        self.rooms = {
            101: {'type': 'Single', 'price': 1000, 'status': 'Available'},
            102: {'type': 'Single', 'price': 1000, 'status': 'Available'},
            201: {'type': 'Double', 'price': 2000, 'status': 'Available'},
            202: {'type': 'Double', 'price': 2000, 'status': 'Available'},
            301: {'type': 'Suite', 'price': 5000, 'status': 'Available'}
        }
        self.booked_rooms = {}

    def display_available_rooms(self):
        print("\nAvailable Rooms:")
        for room_no, details in self.rooms.items():
            if details['status'] == 'Available':
                print(f"Room {room_no} ({details['type']}) - ₹{details['price']}")

    def book_room(self, room_no, customer_name):
        if room_no in self.rooms:
            if self.rooms[room_no]['status'] == 'Available':
                self.rooms[room_no]['status'] = 'Booked'
                self.booked_rooms[room_no] = customer_name
                print(f"\nRoom {room_no} has been successfully booked for {customer_name}.")
            else:
                print(f"\nRoom {room_no} is already booked.")
        else:
            print("\nInvalid Room Number!")

    def checkout_room(self, room_no):
        if room_no in self.booked_rooms:
            customer_name = self.booked_rooms.pop(room_no)
            room_details = self.rooms[room_no]
            room_details['status'] = 'Available'
            print(f"\n{customer_name} has checked out from Room {room_no}.")
            print(f"Total Bill: ₹{room_details['price']}")
        else:
            print("\nRoom is not booked or invalid room number!")

    def display_booked_rooms(self):
        if not self.booked_rooms:
            print("\nNo rooms are currently booked.")
        else:
            print("\nBooked Rooms:")
            for room_no, customer_name in self.booked_rooms.items():
                room_type = self.rooms[room_no]['type']
                print(f"Room {room_no} ({room_type}) - Booked by {customer_name}")


def main():
    hotel = Hotel()

    while True:
        print("\n--- Hotel Management System ---")
        print("1. View Available Rooms")
        print("2. Book a Room")
        print("3. Checkout a Room")
        print("4. View Booked Rooms")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hotel.display_available_rooms()
        elif choice == '2':
            hotel.display_available_rooms()
            room_no = int(input("Enter Room Number to book: "))
            customer_name = input("Enter Customer Name: ")
            hotel.book_room(room_no, customer_name)
        elif choice == '3':
            room_no = int(input("Enter Room Number to checkout: "))
            hotel.checkout_room(room_no)
        elif choice == '4':
            hotel.display_booked_rooms()
        elif choice == '5':
            print("\nThank you for using the Hotel Management System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please try again!")


if __name__ == "__main__":
    main()
