import webbrowser, sys, pyperclip
# webbrowser.open('https://automatetheboringstuff.com')

sys.argv # ['mapit.py', '870', 'Valencia', 'St.']

if len(sys.argv) > 1:
    # ['mapit.py', '870', 'Valencia', 'St.'] -> '870 Valencia St.'
    ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

# https://www.google.com/maps/place/<ADDRESS>
webbrowser.open('https://www.google.com/maps/place/' + address)