import json
from __init__ import parking_info

def create_parking_lot(size, *args):
    ''' create the parking lot and slots '''

    if not all([size, size.isdigit(), int(size) > 0]):
        print 'Invalid Input'

    # check if the parking slot is already created
    if parking_info.get('slot_size', 0):
        print 'Parking lot is already created, Please exit first and then create a lot'

    parking_info.update({ 'slot_size': int(size) })
    print 'Created parking lot with lot {0} slots'.format(size)

def leave(slot, *args):
    ''' remove car's from the parking lot '''
    slot_size = parking_info.get('slot_size', [])
    parked_cars = parking_info.get('parked_cars', [])
    empty_parking = parking_info.get('empty_parking', [])
    cars_by_color = parking_info.get('cars_by_color', {})
    cars_by_registration_no = parking_info.get('cars_by_registration_no', {})

    if not slot.isdigit() or slot_size < int(slot):
        print 'Invalid Input, Available slots in the parking area are {0}'.format(slot_size)

    elif int(slot) not in parked_cars:
        print 'Can not found, slot in parked car, Please check again'

    slot = int(slot)
    car_details = parking_info.get(slot, {})

    color = car_details.get('color', '')
    registration_no = car_details.get('registration_no', '')

    parking_info.pop(slot)
    parked_cars.remove(slot)
    cars_by_registration_no.pop(registration_no)

    same_colored_car_slots = cars_by_color.get(color, [])
    same_colored_car_slots.remove(slot)
    cars_by_color.update({ color: same_colored_car_slots })

    empty_parking.append(slot)
    empty_parking.sort()

    parking_info.update({
        'cars_by_color': cars_by_color,
        'empty_parking': empty_parking,
        'cars_by_registration_no': cars_by_registration_no
    })

def park(registration_no, color, *args):
    ''' park the car to parking lot '''

    # validate the input

    if not all([registration_no, color]):
        print 'Invalid Registration No or Color'

    slot = 0

    # first check if there are any empty parking spots available to park
    # else park car in the next available parking space

    slot_size = parking_info.get('slot_size', [])
    parked_cars = parking_info.get('parked_cars', [])
    cars_by_color = parking_info.get('cars_by_color', {})
    empty_parking = parking_info.get('empty_parking', [])
    cars_by_registration_no = parking_info.get('cars_by_registration_no', {})

    if len(parked_cars) >= slot_size:
        print "Empty slot not available\n"
        return
    elif cars_by_registration_no.get(registration_no, None):
        print "Invalid Registration No, car is already parked at slot {0}".format(
            cars_by_registration_no.get(registration_no, None)
        )
        return

    if len(empty_parking):
        # empty_parking.sort()
        slot = empty_parking.pop(0)
    else:
        slot = max(parked_cars) + 1 if parked_cars else 1
        parked_cars.append(slot)
        parked_cars.sort()

    same_colored_car_slots = cars_by_color.get(color, [])
    same_colored_car_slots.append(slot)

    cars_by_color.update({
        color.lower(): same_colored_car_slots
    })

    cars_by_registration_no.update({ registration_no: slot })

    parking_info.update({
        'parked_cars': parked_cars,
        'empty_parking': empty_parking,
        'cars_by_registration_no': cars_by_registration_no,
        slot: {
            'color': color,
            'registration_no': registration_no
        }
    })

    print "Allocated slot number: {0}\n".format(slot)