from django.http import HttpResponse


def index(request):
    return HttpResponse('List: 	Warcraft: Orcs & Humans, 	Warcraft II: Tides of Darkness,'
                        ' 	Warcraft II: Beyond the Dark Portal, 	Warcraft II: Battle.net Edition,'
                        ' 	Warcraft III: Reign of Chaos, 	Warcraft III: The Frozen Throne, World of Warcraft,'
                        '	World of Warcraft: The Burning Crusade,	World of Warcraft: Wrath of the Lich King, '
                        '	World of Warcraft: Cataclysm, 	World of Warcraft: Mists of Pandaria, Hearthstone, '
                        'World of Warcraft: Warlords of Draenor, 	World of Warcraft: Legion, 	'
                        'World of Warcraft: Battle for Azeroth, 	World of Warcraft Classic, 	Warcraft III: Reforged, '
                        'World of Warcraft: Shadowlands, 	World of Warcraft: The Burning Crusade Classic.')