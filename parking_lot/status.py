from __init__ import parking_info

def status():
    ''' display the status for the parking lot '''
    parked_cars = parking_info.get('parked_cars', [])
    if len(parked_cars):
        print "Slot No\tReg No\tColor"
        for car in parked_cars:
            car_details = parking_info.get(car, {})
            print "{0}\t{registration_no}\t{color}".format(car, **car_details)
    else:
        print "Parking slots are empty"

def slot_numbers_for_cars_with_colour(color):
    ''' show the registration number of the car with same color '''
    available_cars = parking_info.get('cars_by_color', {}).get(color, [])
    if len(available_cars):
        print 'You will find all {0} cars at following slots: {1}'.format(
            color, ', '.join(map(str, available_cars)))
    else:
        print 'There are no cars available in parking spot with color {0}'.format(
            color
        )

def slot_number_for_registration_number(reg_no):
    ''' show the slot number for the given reg no ''' 
    cars_by_registration_no = parking_info.get('cars_by_registration_no', {})
    car_slot = cars_by_registration_no.get(reg_no, 0)

    if not car_slot:
        print 'Car is not available'
    else:
        print '{0} car is available at slot: {1}'.format(reg_no, car_slot)

def registration_numbers_for_cars_with_colour(color):
    available_cars = parking_info.get('cars_by_color', {}).get(color, [])
    if len(available_cars):
        reg_nos = [parking_info.get(slot, {}).get('registration_no') for slot in available_cars ]
        print 'Registration Number for the {0} colored cars are: {1}'.format(
            color, ', '.join(reg_nos))
    else:
        print 'There are no cars available in parking spot with color {0}'.format(
            color
        )