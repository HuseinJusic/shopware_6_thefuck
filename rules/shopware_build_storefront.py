def match(command):
	return('./psh.phar' in command.script or
		'storefront:build in command.output')

def get_new_command(command):
	return './psh.phar storefront:build'.format(command.script);

enabled_by_default = True
