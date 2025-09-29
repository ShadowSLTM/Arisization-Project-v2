
label script3:

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 3 janvier 2098{/i}{/b}"
    play sound "Alarm.mp3" noloop

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft 

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 
    
    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop   

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

label password35:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password35

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Démarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Cool alors."
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 100

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    Na "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 
    
    Na "Bon on fait quoi aujourd'hui ?"
    play sound "Click.mp3" noloop

    P "Je sais ne pas trop car à la base je comptais aller à la bibliothèque et aller voir [I]."
    play sound "Click.mp3" noloop

    Na "Ah bon pourquoi !?"
    play sound "Click.mp3" noloop

    P "Oui je voulais discuter d'un truc avec elle."
    play sound "Click.mp3" noloop

    Na "Ah je vois maintenant."
    play sound "Click.mp3" noloop

    P "Et toi tu vas faire quoi ?"   
    play sound "Click.mp3" noloop

    Na "Je vais sûrement rester au dortoir pour lire."
    play sound "Click.mp3" noloop

    P "D'accord, bonne lecture alors."
    play sound "Click.mp3" noloop

    Na "Merci, à plus tard [prenom]."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Footsteps.mp3" noloop

    





    label end_script3:
    call script4 from _call_script4  
    return 

# Aris la plus belle ###################    