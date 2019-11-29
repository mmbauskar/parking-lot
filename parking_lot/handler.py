
from operations import create_parking_lot, leave, park
from status import (
    status, slot_number_for_registration_number, slot_numbers_for_cars_with_colour,
    registration_numbers_for_cars_with_colour
)

commands_mapper = {
    'exit': '',
    'park': park,
    'leave': leave,
    'status': status,
    'create_parking_lot': create_parking_lot,
    'slot_numbers_for_cars_with_colour': slot_numbers_for_cars_with_colour,
    'slot_number_for_registration_number': slot_number_for_registration_number,
    'registration_numbers_for_cars_with_colour': registration_numbers_for_cars_with_colour
}

def invalid_operation(*args):
    print 'Invalid Command, valid commands are \n\n{0}\n\n'.format(
        '\n'.join(list(commands_mapper.keys()))
    )

def handle_cmd(cmd_str):
    commands = cmd_str.split(' ')
    cmd = commands[0]

    if len(commands) <= 0 or cmd not in commands_mapper:
        invalid_operation()

    args = [ arg.strip() for arg in commands[1:]]
    try:
        if cmd != 'exit': commands_mapper.get(cmd, invalid_operation)(*args)
    except Exception as ex:
        print('Some error occured...')
        import traceback
        traceback.print_exc()

    return cmd
