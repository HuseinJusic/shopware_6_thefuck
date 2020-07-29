# shopware_6_thefuck
Here are some Rules for the TheFuck-Plugin to correct common mistakes with the Shopware 6 commands

# TheFuck - Check it out 
https://github.com/nvbn/thefuck

# Usage
Place all Files of "rules" in *~/.config/thefuck/rules*
_____________

# Example:
```bash
test:development user$ ./psh.par administration:watch
-bash: ./psh.par: No such file or directory
test:development test$ fuck
./psh.phar administration:watch [enter/↑/↓/ctrl+c]

###################

SHOPWARE Developer Version

       _
      | |
   ___| |__   ___  _ ____      ____ _ _ __ ___
  / __| '_ \ / _ \| '_ \ \ /\ / / _` | '__/ _ \
  \__ \ | | | (_) | |_) \ V  V / (_| | | |  __/
  |___/_| |_|\___/| .__/ \_/\_/ \__,_|_|  \___|
                  | |
                  |_|

Using .psh.yaml.dist extended by .psh.yaml.override 

Starting Execution of 'administration:watch' ('/Users/user/Entwicklung/shopware/development/dev-ops/administration/actions/watch.sh')


(1/2) Starting
...
```
```bash
test:development user$ ./psh.phar strfront:build

###################

SHOPWARE Developer Version

       _
      | |
   ___| |__   ___  _ ____      ____ _ _ __ ___
  / __| '_ \ / _ \| '_ \ \ /\ / / _` | '__/ _ \
  \__ \ | | | (_) | |_) \ V  V / (_| | | |  __/
  |___/_| |_|\___/| .__/ \_/\_/ \__,_|_|  \___|
                  | |
                  |_|

Using .psh.yaml.dist extended by .psh.yaml.override 

Script with name strfront:build not found

Have you been looking for this?
Available commands:


storefront:
 - storefront:build               Builds the project for production

1 script(s) available

test:development user$ fuck
./psh.phar storefront:build [enter/↑/↓/ctrl+c]
...
```
