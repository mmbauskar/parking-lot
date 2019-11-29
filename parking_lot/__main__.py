
from handler import handle_cmd, commands_mapper

def init():
    print "Available Commands\n\n{0}\n\nEnter the command\n\n".format(
        '\n'.join(commands_mapper.keys())
    )
    cmd = "init"

    while cmd != "exit":
        cmd_str = raw_input()
        cmd = handle_cmd(cmd_str)

if __name__ == '__main__':
    init()