import sys, webbrowser

# sys.argv = ['youtube.py', 'csgo', 'funny', 'momments']

if len(sys.argv) > 1:
    search = '+'.join(sys.argv[1:])
    webbrowser.open('https://www.youtube.com/results?search_query=' + search)
else:
    webbrowser.open('https:///www.youtube.com')