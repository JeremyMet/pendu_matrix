from matrix_utils_ext import matrix_utils_ext ;
from modules.pendu_bot.pendu_bot import pendu_bot ;
from modules.mastermind.mastermind_bot import mastermind_bot ;
from modules.greeting.greeting import greeting ;
from modules.admin.admin import admin ;
from modules.quotes.quotes import quotes ;
from modules.template.template import template ;
from modules.regex.regex import regex ;
from modules.loto.loto_bot import loto_bot;
from modules.url.url_bot import url_bot;
import time ;


if __name__ == "__main__":


    # Instantiate modules
    my_pendu = pendu_bot("pendu", is_permanent = True) ;
    my_mastermind = mastermind_bot("mastermind", is_permanent = True)
    #my_greeting = greeting("greeting") ;
    #my_admin = admin("admin", is_permanent = True) ;
    my_quotes = quotes("quotes", hour=7, minute=0) ;
    my_loto = loto_bot("loto", hour=20, minute=30);
    my_url = url_bot();
    # Then Create the matrix object, add rooms, services and timers.
    matrix_obj = matrix_utils_ext() ;

    gaming_room = matrix_obj.add_room("#botgaming:mandragot.org", "Tbot, ready for action !")
    science_room = matrix_obj.add_room("#sciences:mandragot.org")
    music_room = matrix_obj.add_room("#musiciensdimanche:mandragot.org")
    main_room = matrix_obj.add_room("#deuxsurdix:mandragot.org")

    matrix_obj.add_service_to_room(gaming_room, my_quotes) ;
    matrix_obj.add_service_to_room(gaming_room, my_pendu) ;
    matrix_obj.add_service_to_room(gaming_room, my_mastermind) ;
    matrix_obj.add_service_to_room(gaming_room, my_loto) ;

    matrix_obj.add_service_to_room(gaming_room, my_url) ;
    matrix_obj.add_service_to_room(science_room, my_url) ;
    matrix_obj.add_service_to_room(music_room, my_url) ;
    matrix_obj.add_service_to_room(main_room, my_url) ;



    matrix_obj.start_timer() ; # start clock thread (for clock sensitive processes/modules)
    matrix_obj.spawn() ;
