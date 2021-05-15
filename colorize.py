# Author: ItachiUchihaLX
# Version v0.1

try:    
    colors = [['31', 'red'], ['32', 'green'], ['33', 'yellow'], ['34', 'blue'], ['35', 'magenta'], ['36', 'cyan'], ['37', 'white'], ['90', 'b_black'],
              ['91', 'b_red'], ['92', 'b_green'], ['93', 'b_yellow'], ['94', 'b_blue'], ['95', 'b_magenta'], ['96', 'b_cyan'], ['97', 'b_white'], ['0', 'normal']]

    def colorize(text, col):
        for i in range(len(colors)):
            if col == colors[i][1]:
                return str('\033[1;' + colors[i][0] + 'm' + text + '\033[m')
        return None

    def help():
        for i in range(len(colors)):
            print(colors[i][0], end='')            
            if i == (len(colors) - 1):
                print(' ', end='')                     
            print(' - ' + color(colors[i][1], colors[i][1]))
except:
    pass
