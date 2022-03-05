from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string

dct = {
    'list': '<h1>Hello, there are list of game industries:</h1><br>Electronic_Arts/<br>Nintendo/<br>Activision_Blizzard/',
    'Electronic_Arts': '<h1>Here are our franchises:</h1><br>Battlefield/<br>Plants_vs_Zombies/',
    'Nintendo': '<h1>Here are our franchises:</h1><br>The_Legend_of_Zelda/<br>Donkey_Kong/',
    'Activision_Blizzard': '<h1>Here are our franchises:</h1><br>Call_of_Duty/<br>Warcraft/',
    'Activision_Blizzard/Warcraft ': 'List:<br>Warcraft: Orcs & Humans,<br>Warcraft II: Tides of Darkness,<br>'
                        ' 	Warcraft II: Beyond the Dark Portal,<br> 	Warcraft II: Battle.net Edition,<br>'
                        'Warcraft III: Reign of Chaos,<br>Warcraft III: The Frozen Throne,<br> World of Warcraft,<br>'
                        '	World of Warcraft: The Burning Crusade,<br>	World of Warcraft: Wrath of the Lich King,<br> '
                        'World of Warcraft: Cataclysm,<br>World of Warcraft: Mists of Pandaria,<br> Hearthstone,<br> '
                        'World of Warcraft: Warlords of Draenor,<br> 	World of Warcraft: Legion,<br> 	'
                        'World of Warcraft: Battle for Azeroth,<br>World of Warcraft Classic,<br>Warcraft III: Reforged,<br> '
                        'World of Warcraft: Shadowlands, <br>	World of Warcraft: The Burning Crusade Classic.',
    'Activision_Blizzard/Call_of_Duty': 'List:<br>Call of Duty<br>Call of Duty: United Offensive<br>Call of Duty: Finest Hour<br>'
                                        'Call of Duty 2<br>Call of Duty 2: Big Red One<br>Call of Duty 3<br>Call of Duty: Roads to Victory<br>'
                                        'Call of Duty 4: Modern Warfare<br>'
}


def getinfo(request, name):
    if dct.get(name):
        return HttpResponse(dct[name])
    else:
        return HttpResponseRedirect('404')


def getNotFound(request):
    return HttpResponse(render_to_string('mygames.html'))


