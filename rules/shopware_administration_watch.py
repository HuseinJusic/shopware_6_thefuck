def match(command):
        return('./psh.phar' in command.script or
                'administration:watch in command.output')

def get_new_command(command):
        return './psh.phar administration:watch'.format(command.script);

enabled_by_default = True
