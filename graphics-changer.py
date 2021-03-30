#!/usr/bin/python3

# IMPORTING MODULES
import os	# for system commands
import subprocess	# for communicating with system76-power
import PySimpleGUI as psg	# for GUI

# LAYOUT
# Element settings
BUTTON_INFO = {'size':(20, 1)}
psg.theme("DarkGrey14")

# Layout itself
layout = [
	[psg.Text('Current mode:')],
	[psg.Text('              ', key = 'modeInfoText')],
	[psg.Button('Integrated', **BUTTON_INFO, key = 'buttonInteg')],
	[psg.Button('Hybrid', **BUTTON_INFO, key = 'buttonHybrid')],
	[psg.Button('Nvidia', **BUTTON_INFO, key = 'buttonNvidia')]
]
			
def change_graphics(mode):	# Function that changes graphics mode with system76-power command
	try:
		os.system('system76-power graphics ' + mode)
		psg.popup('Graphics mode set to:\n' + mode + '\nYou may need to reboot now')
	except Exception as e:
		 psg.popup('Unable to change graphics mode\n' + e)
		 
def check_mode():	# Function that checks current mode
	result = subprocess.run(['system76-power', 'graphics'], stdout=subprocess.PIPE)
	out = str(result.stdout.decode('utf-8'))
	return(out)
	
def main():
	global layout
	window = psg.Window('Graphics mode changer', layout)	# Creating a window
	
	while True:	# Main window loop
		event, values = window.read(timeout=500)
		if event == psg.WIN_CLOSED:	# Exiting loop
			break
		elif event == 'buttonInteg':
			change_graphics('integrated')
		elif event == 'buttonHybrid':
			change_graphics('hybrid')
		elif event == 'buttonNvidia':
			change_graphics('nvidia')
		else:	# Checking and displaying current mode
			mode_info = check_mode()
			window['modeInfoText'].update(mode_info)
			
if __name__ == '__main__':
	main()
	exit(0)
