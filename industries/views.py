from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.shortcuts import render

dct = {
    'list': {'intro': 'Hello, there are list of game industries:',
             'description': ['Electronic_Arts', 'Nintendo', 'Activision_Blizzard']},
    'Electronic_Arts': {'intro': 'Here are our franchises:', 'description': ['Battlefield', 'Plants_vs_Zombies']},
    'Nintendo': {'intro': 'Here are our franchises:', 'description': ['The_Legend_of_Zelda', 'Donkey_Kong']},
    'Activision_Blizzard': {'intro': 'Here are our franchises:', 'description': ['Call_of_Duty', 'Warcraft']},
    'Warcraft ': {'intro': 'List:', 'description': ['Warcraft: Orcs & Humans', 'Warcraft II: Tides of Darkness',
                                                    'Warcraft II: Beyond the Dark Portal',
                                                    'Warcraft II: Battle.net Edition',
                                                    'Warcraft III: Reign of Chaos', 'Warcraft III: The Frozen Throne',
                                                    'World of Warcraft',
                                                    'World of Warcraft: The Burning Crusade',
                                                    'World of Warcraft: Wrath of the Lich King',
                                                    'World of Warcraft: Cataclysm',
                                                    'World of Warcraft: Mists of Pandaria', 'Hearthstone',
                                                    'World of Warcraft: Warlords of Draenor',
                                                    'World of Warcraft: Legion',
                                                    'World of Warcraft: Battle for Azeroth',
                                                    'World of Warcraft Classic', 'Warcraft III: Reforged',
                                                    'World of Warcraft: Shadowlands',
                                                    'World of Warcraft: The Burning Crusade Classic']},
    'Call_of_Duty': {'intro': 'List:',
                     'description': ['Call of Duty', 'Call of Duty: United Offensive', 'Call of Duty: Finest Hour',
                                     'Call of Duty 2', 'Call of Duty 2: Big Red One', 'Call of Duty 3',
                                     'Call of Duty: Roads to Victory',
                                     'Call of Duty 4: Modern Warfare',
                                     'Call of Duty: World at War',
                                     'Call of Duty: World at War – Final Fronts',
                                     'Call of Duty: World at War – Zombies',
                                     'Call of Duty: Modern Warfare 2',
                                     'Call of Duty Classic',
                                     'Call of Duty: Black Ops',
                                     'Call of Duty: Black Ops Zombies',
                                     'Call of Duty: Modern Warfare 3',
                                     'Call of Duty: Black Ops II',
                                     'Call of Duty: Black Ops Declassified',
                                     'Call of Duty Online',
                                     'Call of Duty: Strike Team',
                                     'Call of Duty: Ghosts',
                                     'Call of Duty: Heroes',
                                     'Call of Duty: Advanced Warfare',
                                     'Call of Duty: Black Ops III',
                                     'Call of Duty: Infinite Warfare',
                                     'Call of Duty: Modern Warfare Remastered',
                                     'Call of Duty: WWII',
                                     'Call of Duty: Black Ops 4',
                                     'Call of Duty: Mobile',
                                     'Call of Duty: Modern Warfare',
                                     'Call of Duty: Warzone',
                                     'Call of Duty: Modern Warfare 2 Campaign Remastered',
                                     'Call of Duty: Black Ops Cold War',
                                     'Call of Duty: Vanguard']}
}


def getinfo(request, name):
    if dct.get(name):
        data = {
            'name': name,
            'intro': dct.get(name)['intro'],
            'info': dct.get(name)['description']
        }
        return render(request, 'industry_names/my_industries.html', context=data)
    else:
        return HttpResponseRedirect('404')


def getNotFound(request):
    return HttpResponse(render_to_string('industry_names/mygames.html'))
