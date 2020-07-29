def match(command):
        return('./psh.phar' in command.script or
                'storefront:hot-proxy in command.output')

def get_new_command(command):
        return './psh.phar storefront:hot-proxy'.format(command.script);

enabled_by_default = True
