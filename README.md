# Design a parking lot using Python OOP principles

Description:

1. We create n number of slots for cars as per the user request.

2. The program allocate each parking lot to a selected car

3. If any slot needed to be vacated the user can prompt the program of the required slot.

4.The system  provides with the ability to find out:

    a. Registration numbers of all cars of a particular colour.

    b. Slot number in which a car with a given registration number is parked.

    c. Slot numbers of all slots where a car of a particular colour is parked.

create_parking_lot 6
park KA-01-HH-1234 White
park KA-01-HH-9999 White
park KA-01-BB-0001 Black
park KA-01-HH-7777 Red
park KA-01-HH-2701 Blue
park KA-01-HH-3141 Black
leave 4
status
park KA-01-P-333 White
park DL-12-AA-9999 White
registration_numbers_for_cars_with_colour White
slot_numbers_for_cars_with_colour White
slot_number_for_registration_number KA-01-HH-3141
slot_number_for_registration_number MH-04-AY-1111
