from colorama import Fore, Back, Style
import random

wordlist = ['cigar','rebut','sissy','humph','awake','blush','focal','evade','naval','serve','heath','dwarf','model','karma','stink','grade','quiet','bench','abate','feign','major','death','fresh','crust','stool','colon','abase','marry','react','batty','pride','floss','helix','croak','staff','paper','unfed','whelp','trawl','outdo','adobe','crazy','sower','repay','digit','crate','cluck','spike','mimic','pound','maxim','linen','unmet','flesh','booby','forth','first','stand','belly','ivory','seedy','print','yearn','drain','bribe','stout','panel','crass','flume','offal','agree','error','swirl','argue','bleed','delta','flick','totem','wooer','front','shrub','parry','biome','lapel','start','greet','goner','golem','lusty','loopy','round','audit','lying','gamma','labor','islet','civic','forge','corny','moult','basic','salad','agate','spicy','spray','essay','fjord','spend','kebab','guild','aback','motor','alone','hatch','hyper','thumb','dowry','ought','belch','dutch','pilot','tweed','comet','jaunt','enema','steed','abyss','growl','fling','dozen','boozy','erode','world','gouge','click','briar','great','altar','pulpy','blurt','coast','duchy','groin','fixer','group','rogue','badly','smart','pithy','gaudy','chill','heron','vodka','finer','surer','radio','rouge','perch','retch','wrote','clock','tilde','store','prove','bring','solve','cheat','grime','exult','usher','epoch','triad','break','rhino','viral','conic','masse','sonic','vital','trace','using','peach','champ','baton','brake','pluck','craze','gripe','weary','picky','acute','ferry','aside','tapir','troll','unify','rebus','boost','truss','siege','tiger','banal','slump','crank','gorge','query','drink','favor','abbey','tangy','panic','solar','shire','proxy','point','robot','prick','wince','crimp','knoll','sugar','whack','mount','perky','could','wrung','light','those','moist','shard','pleat','aloft','skill','elder','frame','humor','pause','ulcer','ultra','robin','cynic','aroma','caulk','shake','dodge','swill','tacit','other','thorn','trove','bloke','vivid','spill','chant','choke','rupee','nasty','mourn','ahead','brine','cloth','hoard','sweet','month','lapse','watch','today','focus','smelt','tease','cater','movie',]
word = wordlist[random.randint(0, len(wordlist))]

count = 0

while True:
    guess = input('Enter your guess:    ').lower()
    print('\t\t\t\t', end = '')
    
    if guess == word:
        print('You got the word')
        break

    for i in range(5):
        if guess[i] == word[i]:
            print(Back.GREEN + guess[i], end = '')
        elif guess[i] in word:
            print(Back.YELLOW + guess[i], end = '')
        elif guess[i].isnumeric():
            print('Please enter a valid value')
            continue
        else:
            print(Back.RESET + guess[i], end = '')

    print(Back.RESET)
    
    count += 1
    
    if count == 5:
        print(word)
        break