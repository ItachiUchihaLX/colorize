# Author: ItachiUchihaLX
# Version v0.1


colors = [['31', 'red'], ['32', 'green'], ['33', 'yellow'], ['34', 'blue'], ['35', 'magenta'], ['36', 'cyan'], ['37', 'white'], ['90', 'b_black'],
            ['91', 'b_red'], ['92', 'b_green'], ['93', 'b_yellow'], ['94', 'b_blue'], ['95', 'b_magenta'], ['96', 'b_cyan'], ['97', 'b_white'], ['0', 'standart']]

for color in colors:
    exec(f'def {color[1]}(text, toggle=False):\n toggle = "" if toggle else "\033[m" \n return f"\033[1;{color[0]}m" + text + toggle')

