import webbrowser, random

for _ in range(30):
    a = random.randrange(-100, 100)
    webbrowser.open(f'https://www.bing.com/search?FORM=U523DF&PC=U523&q={a}+{a+1}')