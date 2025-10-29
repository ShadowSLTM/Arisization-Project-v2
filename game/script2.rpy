 
label script2:

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} trois jours plus tard, le 18 novembre 2097 {/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 3 
    $ points -= 600
    $ stockage += 60.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password11:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password11

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
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

    $ go_in_class = get_random_go_in_class()
    Na "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    Na "Sinon [prenom], as-tu des nouvelles de la DGCA"
    play sound "Click.mp3" noloop  

    P "Non malheureusement."
    play sound "Click.mp3" noloop  

    Na "Je vois."
    play sound "Click.mp3" noloop  

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien nous pouvons commencer le cours mais avant j'ai quelque chose à te dire [prenom]."
    play sound "Click.mp3" noloop 

    P "Oui dites-moi, je vous écoute."
    play sound "Click.mp3" noloop  

    M "Toi et [newname], il faut que vous allez voir [E] au bureau des élèves maintenant c'est assez urgent."
    play sound "Click.mp3" noloop  

    P "Bon on y vas ?"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu quitte la salle de classe avec [Na].{/i}{/b}"
    play sound "Door.mp3" noloop
     
    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Je me demande ce qui ce passe pour que ce soit urgent."
    play sound "Click.mp3" noloop 
    
    Na "Oui mais aussi je me le demande."
    play sound "Click.mp3" noloop

    "{b}{i}Tu continues dans le couloir avec [Na].{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene office with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen office with moveinright
    
    P "Bonjour c'est moi [nom], que se passe t-il ?"  
    play sound "Click.mp3" noloop 

    "{b}{i}Puis tu aperçois [E], l'[Ot] et une troisiéme personne.{/i}{/b}"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    E "[salutation_rdm]"
    play sound "Click.mp3" noloop

    P "Pourquoi l'[Ot] est ici ?"  
    play sound "Click.mp3" noloop 

    E "il a quelque chose à te dire concernant [newname] et cette affaire de traître."  
    play sound "Click.mp3" noloop 

    P "Je vois, sinon c'est quoi les nouvelles."  
    play sound "Click.mp3" noloop 

    Oh "Je suis ici pour t'annoncer qu'[newname] pourra étre acceptée à la civilité et avoir une vraie identité."  
    play sound "Click.mp3" noloop 

    P "Vraiment mais c'est génial ça."
    play sound "Click.mp3" noloop

    Oh "D'accord, mais pour cela, j'aurai besoin de quelques informations."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu lui transmets les détails concernant [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Oh "Je vous remercie, juste j'ai aussi des nouvelles par rapport à cette histoire de traître"
    play sound "Click.mp3" noloop

    P "Oui, je vous écoute."
    play sound "Click.mp3" noloop

    Oh "il semblerait que le traître fasse partie d'un groupe de hackers qui s'appelle Ghosts"
    play sound "Click.mp3" noloop 

    P "Ghost !?"
    play sound "Click.mp3" noloop

    Oh "Oui c'est un groupe de hacker qui a vu le jour en août 2097."
    play sound "Click.mp3" noloop 

    P "intéressant, donc ce groupe est récent."
    play sound "Click.mp3" noloop

    Oh "Oui exactement."
    play sound "Click.mp3" noloop 

    P "Je vois mais j'aimerais vous poser une question."
    play sound "Click.mp3" noloop 

    Oh "Oui dis-moi." 
    play sound "Click.mp3" noloop

    P "C'est qui cette personne avec vous ?"
    play sound "Click.mp3" noloop

    E "Attend tu ne reconnais pas cette personne ?"
    play sound "Click.mp3" noloop

    P "Non pourquoi ?"
    play sound "Click.mp3" noloop 

    E "Tu devrais la connaitre car elle est importante dans notre société."
    play sound "Click.mp3" noloop

    P "Je vois."  
    play sound "Click.mp3" noloop 

    "{b}{i}Puis la troisiéme personne se met à parler.{/i}{/b}"
    play sound "Click.mp3" noloop

    Ln "Je me nomme [Ln], la vice-présidente du gouvernement."
    play sound "Click.mp3" noloop

    $ character17 = Ln
    $ ultimate17 = "la vice-présidente du gouvernement Nagumo"
    $ stockage += 2.0 

    P "Que faites-vous ici ?"  
    play sound "Click.mp3" noloop 

    Ln "Je suis venue après avoir entendu parler d'[newname]."  
    play sound "Click.mp3" noloop

    P "Attendez... vous connaissez [newname] ? Comment ?"
    play sound "Click.mp3" noloop 

    Ln "Je suis au courant grâce à la DGCS. Le gouvernement surveille tout ce qui concerne les projets non-répertoriés. Et celui-ci... dépasse largement tout ce que nous avons vu jusque-là."
    play sound "Click.mp3" noloop

    P "Que voulez-vous de moi et d'[newname] ?"
    play sound "Click.mp3" noloop 

    Ln "Rien. Je suis là pour éviter que la situation ne dégénère. [newname] n'est pas encore considérée comme une menace. Pas encore."
    play sound "Click.mp3" noloop

    P "Et si je vous disais qu'[newname] est bien plus qu’un simple programme ?"
    play sound "Click.mp3" noloop

    Ln "Je le sais déjà. C’est justement pour ça que je suis ici. Dis-moi, es-tu réellement capable de la contrôler ?"
    play sound "Click.mp3" noloop 

    P "Oui, normalement. J’ai un vrai contrôle sur elle... mais elle agit aussi de son propre chef sans prendre des décisions dangereuses car elle a le contrôle de niveau 1 du RCMS."
    play sound "Click.mp3" noloop 

    Ln "Je vois mais j'ai une question à te poser. Quel est le niveau 0 du RCMS pour [newname] ?"
    play sound "Click.mp3" noloop

    P "Le niveau 0 du RCMS est le niveau ou j'ai 100\% le contrôle sur elle mais je l'ai utilisé à des fins de test durant l'été."
    play sound "Click.mp3" noloop

    Ln "Je vois… Donc, je n’ai pas à m’inquiéter pour la sécurité publique."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop 

    P "Mais pourquoi vous et pas le président directement ?"
    play sound "Click.mp3" noloop

    Ln "Car [Sn] est vraiment occupé en ce moment."
    play sound "Click.mp3" noloop 

    $ character18 = Sn
    $ ultimate18 = "le président du gouvernement Nagumo"

    P "Je comprend mieux maintenant."
    play sound "Click.mp3" noloop 

    Ln "Sinon tu en penses quoi de la société actuelle ?"
    play sound "Click.mp3" noloop

    P "Eh bien…"
    play sound "Click.mp3" noloop

    menu:  

        "{b}{i}Donner un avis positif{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            P "Il y a encore de l'espoir dans cette société."
            play sound "Click.mp3" noloop

            Ln "C'est bien que notre société te donne de l'espoir."
            play sound "Click.mp3" noloop 

            $ thanks = get_random_thanks() 
            P "[thanks]"
            play sound "Click.mp3" noloop

        "{b}{i}Exprimer un avis négatif{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            $ success += 1 
            $ quest30 += 1 
 
            show screen update with moveinright

            P "Sachez que je méprise profondément cette société malade."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

            Ln "Oh je vois mais bon de toute façon c'est ton avis pas le mien donc je ne vais juger."
            play sound "Click.mp3" noloop 

            $ thanks = get_random_thanks()
            P "[thanks]"
            play sound "Click.mp3" noloop 

    Ln "Si jamais je te laisse mon numéro profesionnel s'il y a du nouveau avec [newname]."
    play sound "Click.mp3" noloop

    P "Car je dois déclarer tout les changement que je fais ?"
    play sound "Click.mp3" noloop 

    Ln "Oui conformément à l’article 2, alinéa 3, Toute modification majeures dois être documentées."
    play sound "Click.mp3" noloop

    P "Il n'y a pas de soucis, je vous informerais s'il y a du nouveau avec elle."
    play sound "Click.mp3" noloop

    Ln "Bon je vais devoir vous laisser j'ai des choses à faire."
    play sound "Click.mp3" noloop

    P "Ok mais j'ai une derniére question."
    play sound "Click.mp3" noloop

    Ln "Oui dis-moi."
    play sound "Click.mp3" noloop 

    P "Pourquoi les nouvelles technologies sont-elles si surveillées par le gouvernement ?"
    play sound "Click.mp3" noloop 

    Ln "C'est une question de sécurité nationale. Nous devons nous assurer que rien ne menace la stabilité de notre société pour éviter la tragédie de guerre de 2095 et l'anarchie."
    play sound "Click.mp3" noloop 

    P "Je vois alors je comprends mieux."
    play sound "Click.mp3" noloop 

    Ln "Bien alors.."
    play sound "Click.mp3" noloop 

    "{b}{i}[Ln] et l'[Ot] quittent le bureau des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop

    E "Si jamais sera tout, vous pouvez retourner en cours."
    play sound "Click.mp3" noloop

    P "Je vous remercie."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    E "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon [newname], il faut qu'on y aille."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen office with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Vous quittez le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Bonjour, nous revoilà."
    play sound "Click.mp3" noloop

    M "Bien vous pouvez aller vous asseoir."
    play sound "Click.mp3" noloop

    "{b}{i}Vous asseyez et vous suivez le cours tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright 
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Enfin à manger."
    play sound "Click.mp3" noloop   

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous mangez tranquillement et [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    I "Coucou [prenom]."
    play sound "Click.mp3" noloop   

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    P "Cool alors."
    play sound "Click.mp3" noloop   

    "{b}{i} [I] s'asseoit avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Sinon, comment s'était le début du cours ?"
    play sound "Click.mp3" noloop   

    I "ça va tu n'as pas loupé grand chose."
    play sound "Click.mp3" noloop   

    P "Je vois merci." 
    play sound "Click.mp3" noloop   

    I "De rien et sinon pourquoi tu devais aller voir [E] ?"
    play sound "Click.mp3" noloop   

    P "Ils devaient me donner des nouvelles par rapport au traître et la civilité d'[newname]."
    play sound "Click.mp3" noloop   

    I "je suis vraiment enthousiaste qu'[newname] puisse être reconnue comme une personne humaine."
    play sound "Click.mp3" noloop   

    P "Oui absolument."
    play sound "Click.mp3" noloop   

    I "C'est quoi les nouvelles par rapport au traître ?" 
    play sound "Click.mp3" noloop   

    P "Ils m'ont dit que le traître fesait partie d'un groupe nommé Ghosts" 
    play sound "Click.mp3" noloop   

    I "Ghosts !? J'en n'ai jamais entendu parler." 
    play sound "Click.mp3" noloop   

    P "Moi n'en plus, je me demande bien d'ou ils sortent." 
    play sound "Click.mp3" noloop   

    I "Oui il faudra se renseigner." 
    play sound "Click.mp3" noloop   

    P "Oui peut-être qu'on pourra découvrir d'autres informations." 
    play sound "Click.mp3" noloop  

    if pronom == "il":

        I "Oui mais il faudra aussi rester vigilants."
        play sound "Click.mp3" noloop

    else: 

        I "Oui mais il faudra aussi rester vigilantes."
        play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    I "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    M "Bien nous pouvons continuer et conclure ce cours de français."
    play sound "Click.mp3" noloop 

# cours de français 5
###############################################################################

###############################################################################

    "{b}{i} le cours continue dans le calme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Si jamis le l'examen de français sera le 2 décembre 2097."
    play sound "Click.mp3" noloop   

    N "C'est noté."
    play sound "Click.mp3" noloop 

    $ stockage += 5.0 

    P "Bon [newname] on n'y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Footsteps.mp3" noloop 

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}En sortant tu aperçois [N] et [Hi] qui discutent.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Oh regarde [N] et [Hi] qui discutent."
    play sound "Click.mp3" noloop 

    P "On devrait aller leur parler."
    play sound "Click.mp3" noloop 

    Na "Oui."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu t'approches d'eux.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Salut les gars, comment vous allez ?"
    play sound "Click.mp3" noloop 
    
    N "Oh salut [prenom] et [newname], je vais bien et vous ?"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "On va bien mais on est juste fatigués."
        play sound "Click.mp3" noloop 

    else:

        P "On va bien mais on est juste fatiguées."
        play sound "Click.mp3" noloop 

    N "Ah je vois, vous devriez aller vous reposer un peu."
    play sound "Click.mp3" noloop 

    P "Merci pour le conseil, on va le faire sinon vous discutez de quoi ?"
    play sound "Click.mp3" noloop 

    N "On discute des cours et du prochain examen."
    play sound "Click.mp3" noloop  

    P "Ah d'accord, ça a l'air intéressant."
    play sound "Click.mp3" noloop 

    N "Mais de base je devais aller voir [Y] mais je ne sais pas où elle est."
    play sound "Click.mp3" noloop 

    P "Tu veux que je t'aide à la chercher ?"
    play sound "Click.mp3" noloop 

    N "Pas de soucis, je vais la chercher tout seul."
    play sound "Click.mp3" noloop 

    Hi "Bon moi je vais y aller, à plus."
    play sound "Click.mp3" noloop 

    P "Ok à demain."
    play sound "Click.mp3" noloop 

    Hi "à demain."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[Hi] se met à s'éloigner.{/i}{/b}"
    play sound "Click.mp3" noloop 

    N "Bon je vais pas tarder non plus."
    play sound "Click.mp3" noloop 

    P "Ok à demain."
    play sound "Click.mp3" noloop 

    N "à demain."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[N] se met aussi à partir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon [newname] on n'y va avant que tu n'aies plus de batterie."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous continuez vers le dortoir mais [J2] bouscule [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    J2 "Mais regarde où tu vas espéce de traînée."
    play sound "Click.mp3" noloop 

    Na "Hey tu ne peux pas me dire ou aller !!!"
    play sound "Click.mp3" noloop 

    "{b}{i}[J2] se met à la frapper.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Mais ça ne va pas !!!"
    play sound "Click.mp3" noloop 

    "{b}{i}[J2] se retourne brusquement vers vous, les yeux remplis de colère.{/i}{/b}"
    play sound "Click.mp3" noloop

    J2 "Dégage de là, c'est pas tes affaires !"
    play sound "Click.mp3" noloop

    P "Tu crois vraiment que je vais rester sans rien faire ?!"
    play sound "Click.mp3" noloop

    "{b}{i}Tu attrapes le bras de [J2] pour l'empêcher de continuer.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Merci... Je crois qu'elle m'aurait vraiment fait mal..."
    play sound "Click.mp3" noloop

    "{b}{i}Une tension glaciale envahit l'air autour de vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    J2 "Tch... Vous allez le regretter."
    play sound "Footsteps.mp3" noloop

    "{b}{i}[J2] tourne les talons et s’éloigne, furieuse.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Ça va aller ?"
    play sound "Click.mp3" noloop 

    if pronom == "il": 

        Na "Oui... Merci. T’es arrivé juste à temps..."
        play sound "Click.mp3" noloop

    else:

        Na "Oui... Merci. T’es arrivée juste à temps..."
        play sound "Click.mp3" noloop

    "{b}{i}Vous continuez vers le dortoir, silencieusement, les pensées encore agitées par ce qui vient de se passer...{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous entrez au dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir() 
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop
    
    P "Bon on fait quoi ?"
    play sound "Click.mp3" noloop

    Na "Moi je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, à plus tard !"
    play sound "Click.mp3" noloop 

    "{b}{i} [newname] se déconnecte tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene office with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen office with moveinright 

    P "Bonjour c'est moi, [prenom]."
    play sound "Click.mp3" noloop

    E "Bonjour [prenom], que puis-je faire pour toi ?"
    play sound "Click.mp3" noloop 

    P "Je viens pour me plaindre d'[J2]."
    play sound "Click.mp3" noloop 

    E "Et pourquoi cela ?"
    play sound "Click.mp3" noloop 

    P "Elle viens de frapper violamment [newname] !!!"
    play sound "Click.mp3" noloop 

    E "C'est inacceptable ! Que s'est-il passé ?"
    play sound "Click.mp3" noloop 

    P "[J2] l'a bousculé et l'a frappé."
    play sound "Click.mp3" noloop 

    E "Merci de m'avoir informé. Je vais m'en occuper immédiatement."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    E "Bon tu devrais aller t'occuper d'[newname] et je vais m'occuper de [J2]."
    play sound "Click.mp3" noloop

    hide screen office with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Puis tu quittes le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues ton chemin.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous entres dans ton dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    P "Enfin dans le dortoir:"
    play sound "Click.mp3" noloop

    "{b}{i} Tu aperçois [newname] qui est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais la laisser se reposer."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te poses pour réviser un peu pendant qu'[newname] se recharge.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini de réviser pour aujourd'hui."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu te léves pour aller démarrer [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

label password12:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password12

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
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

    Na "Bon on fait quoi ?"
    play sound "Click.mp3" noloop 

    P "On va aller manger."
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

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop  

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 19 novembre 2097{/i}{/b}"
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

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password13:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password13 

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na  "Démarrage terminé, Bonjour [P]."
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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Ciick.mp3" noloop

    "{b}{i}Puis soudainement tu vois tous les autres élèves à l'entrée de la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vous êtes déjà tous là ?"
    play sound "Click.mp3" noloop 

    I "Oui, [M] n'est pas encore arrivée."
    play sound "Click.mp3" noloop 

    P "D'accord, j'espère qu'elle ne va pas tarder."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Puis [M] arrive finalement.{/i}{/b}"
    play sound "Ciick.mp3" noloop
    
    M "Désolée pour me retard, j'ai eu une petite discussion avec [E]."
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    "{b}{i}il y a un blanc pendant un instant.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Absente."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien nous pouvons commencer le cours."
    play sound "Click.mp3" noloop 

    J1 "Juste elle est ou ma soeur ?"
    play sound "Click.mp3" noloop 

    I "Oui, d'habitude elle est toujours en cours."
    play sound "Click.mp3" noloop 

    M "Elle n'est pas là aujourd'hui car elle a fait quelque chose de grâve."
    play sound "Click.mp3" noloop 

    J1 "Et pourrais-je savoir ce qu'elle a fait !?"
    play sound "Click.mp3" noloop 

    M "Désolée mais c'est une affaire interne et confidentielle."
    play sound "Click.mp3" noloop 

    J1 "ça cache quelque chose, je le sais."
    play sound "Click.mp3" noloop
    
    M "Bon commençons le cours."
    play sound "Click.mp3" noloop 

# cours d'informatique 
######################################################################################################

    M "Veuillez sortir pour une fois vos ordinateurs."
    play sound "Click.mp3" noloop
    
    M "Aujourd’hui, on plonge dans les réseaux informatiques. Un pilier de notre société numérique."
    play sound "Click.mp3" noloop

    M "Et pour commencer, une question simple : que permet un réseau informatique ?"
    play sound "Click.mp3" noloop

    M "Partager des données entre plusieurs appareils… envoyer des fichiers, naviguer sur Internet ?"
    play sound "Click.mp3" noloop

    M "Exact. Un réseau permet la communication entre ordinateurs, serveurs, smartphones, et même des objets connectés."
    play sound "Click.mp3" noloop

    N "Pour structurer tout ça, on utilise ce qu'on appelle un modèle d'architecture en couches. Le plus célèbre, c’est le modèle TCP/IP."
    play sound "Click.mp3" noloop

    K "Il y a quatre couches, non ? Application, transport, Internet… et l’accès réseau."
    play sound "Click.mp3" noloop

    M "Parfait. Ces couches organisent le trajet de vos données, de l’application jusqu’au câble… ou jusqu’au Wi-Fi."
    play sound "Click.mp3" noloop

    K "Chaque couche encapsule les données dans un format spécifique, avant de les transmettre à la suivante."
    play sound "Click.mp3" noloop

    M "Très bonne remarque, Aris. Parlons maintenant des adresses IP. Chaque machine sur un réseau possède une adresse unique."
    play sound "Click.mp3" noloop

    M "[prenom] tu peux me lire l’adresse IP de ton poste ?"
    play sound "Click.mp3" noloop

    P "Euh… 192.168.0.17. C’est ça ?"
    play sound "Click.mp3" noloop

    M "Exact. C’est une adresse privée, valable uniquement dans notre réseau local."
    play sound "Click.mp3" noloop

    P "Et pour aller sur Internet, c’est une adresse publique qui est utilisée, pas vrai ?"
    play sound "Click.mp3" noloop

    M "Oui. Grâce à un système appelé NAT, ou Network Address Translation. Il permet à plusieurs machines d’utiliser une seule adresse publique."
    play sound "Click.mp3" noloop

    P "Donc… si j’ouvre trois onglets YouTube sur trois ordis, ils passent tous par la même IP ?"
    play sound "Click.mp3" noloop

    M "Exactement. Le routeur s’occupe d’acheminer les réponses vers le bon poste. C’est un peu comme un centre postal très rapide."
    play sound "Click.mp3" noloop

    K "Chaque paquet contient un port, comme un numéro de boîte. Le NAT garde une table d'association."
    play sound "Click.mp3" noloop

    M "Excellent résumé, kendo. Parlons maintenant des protocoles de transport : TCP et UDP."
    play sound "Click.mp3" noloop

    K "TCP est fiable. Il vérifie que les données arrivent bien et dans le bon ordre. Comme une livraison avec accusé de réception."
    play sound "Click.mp3" noloop

    P "Et UDP, c’est l’inverse : rapide, mais pas sûr. Genre pour les jeux en ligne ou les appels vidéo ?"
    play sound "Click.mp3" noloop

    M "Vous avez tous les deux raison. TCP est utilisé pour les mails, le web, les transferts de fichiers. UDP est réservé aux flux temps réel."
    play sound "Click.mp3" noloop

    M "Question suivante : qui peut me parler du DNS ?"
    play sound "Click.mp3" noloop

    K "DNS signifie Domain Name System. Il traduit les noms de domaine, comme www.aris-project.org, en adresse IP."
    play sound "Click.mp3" noloop

    K "Donc, quand on tape un site, on passe d’un nom à un nombre. Le DNS, c’est un peu l’annuaire téléphonique d’Internet."
    play sound "Click.mp3" noloop

    M "Très belle analogie, Kendo. Dernière notion pour aujourd’hui : le routage."
    play sound "Click.mp3" noloop

    K "C’est le chemin que les paquets empruntent pour aller d’un points A à un points B, non ?"
    play sound "Click.mp3" noloop

    M "Oui. Et ce chemin peut changer à chaque seconde, selon la congestion, les coupures ou les priorités réseau."
    play sound "Click.mp3" noloop

    M "Chaque routeur sur Internet décide de l’étape suivante pour chaque paquet. C’est un travail de coordination constant."
    play sound "Click.mp3" noloop

    K "Et parfois, certains paquets prennent plus de temps à arriver ou se perdent. C’est ce qu’on appelle la latence ou la perte de paquets."
    play sound "Click.mp3" noloop

    M "Bien vu. Voilà pourquoi comprendre ces mécanismes est essentiel pour créer des applications efficaces… et sécurisées."
    play sound "Click.mp3" noloop

    "{b}{i}Le cours continue jusqu'à la pause.{/i}{/b}"
    play sound "Click.mp3" noloop

###################################################################################################### 

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Click.mp3" noloop

    hide screen WC with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Bien reprenons le cours."
    play sound "Click.mp3" noloop

# cours d'informatique 2
##################################################################################################################

    M "Bon reprenons notre exploration du monde fascinant des réseaux."
    play sound "Click.mp3" noloop

    M "Maintenant, voyons ce qu’il se passe quand une machine veut tester la connectivité avec une autre."
    play sound "Click.mp3" noloop

    I "Avec la commande ping ?"
    play sound "Click.mp3" noloop

    M "Exactement. Le ping utilise un protocole nommé ICMP : Internet Control Message Protocol."
    play sound "Click.mp3" noloop

    M "Il envoie un paquet « écho request », et si la destination répond, on reçoit un « écho reply »."
    play sound "Click.mp3" noloop

    P "Donc c’est un peu comme dire 't’es là ?' et attendre un 'ouais, je suis là'."
    play sound "Click.mp3" noloop

    M "Parfaitement résumé. C’est utile pour diagnostiquer des coupures réseau ou des délais anormaux."
    play sound "Click.mp3" noloop 

    M "Mais attention : certains serveurs désactivent les réponses ICMP pour des raisons de sécurité."
    play sound "Click.mp3" noloop

    I "C’est pour éviter les attaques ou les scans automatiques ?"
    play sound "Click.mp3" noloop

    M "Oui. Parlons justement de sécurité de base. Connaissez-vous les firewalls ?"
    play sound "Click.mp3" noloop

    K "Un pare-feu, c’est ce qui filtre les connexions entrantes et sortantes, non ?"
    play sound "Click.mp3" noloop

    M "Exact. Il peut autoriser, bloquer ou rediriger le trafic selon des règles. C’est un rempart entre ton réseau et le monde extérieur."
    play sound "Click.mp3" noloop

    K "Et il existe des firewalls matériels, intégrés à certains routeurs, ou logiciels, installés sur les systèmes d’exploitation."
    play sound "Click.mp3" noloop

    M "Bien vu. Une bonne configuration du pare-feu est la première ligne de défense contre les intrusions."
    play sound "Click.mp3" noloop

##################################################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Si jamais vous étes libre cette après-midi."
    play sound "Click.mp3" noloop

    $ stockage += 5.0

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi() 
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop
    
    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    show screen day with moveinleft
    show screen points with moveinleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 
    
    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous allez chercher une avant de vous asseoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon appétit [newname]."
    play sound "Click.mp3" noloop 

    Na "Bon appétit à toi aussi [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement puis [I] viens s'asseoir avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    I "J'ai une question."
    play sound "Click.mp3" noloop 

    P "Oui dis-moi."
    play sound "Click.mp3" noloop 

    I "Il s'est passé quoi avec [J2] ?"
    play sound "Click.mp3" noloop 

    P "Elle a frappé [newname]."
    play sound "Click.mp3" noloop 

    I "Pardon, elle a fait quoi !?"
    play sound "Click.mp3" noloop 

    P "Elle l'a frappé."
    play sound "Click.mp3" noloop

    I "C'est vrai ça [newname] ?"
    play sound "Click.mp3" noloop

    Na "Oui malheureusement."
    play sound "Click.mp3" noloop

    I "Mais elle est vraiment malade celle-là."
    play sound "Click.mp3" noloop

    P "Oui je confirme." 
    play sound "Click.mp3" noloop

    Na "Bon on peut cloturer cette discussion car elle me met mal à l'aise."
    play sound "Click.mp3" noloop

    menu:   

        "{b}{i} Continuer la discussion.{/i}{/b}" :
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            P "En plus elle s'est mis à l'insulter au calme." 
            play sound "Click.mp3" noloop

            I "Mais il faut vraiment qu'elle se calme." 
            play sound "Click.mp3" noloop

            Na "Hey je veux vraiment qu'on finisse cette discussion." 
            play sound "Click.mp3" noloop 

            if pronom == "il": 
    
                P "Désolé."
                play sound "Click.mp3" noloop  

            else:

                P "Désolée."
                play sound "Click.mp3" noloop   

            I "Vraiment désolée" 
            play sound "Click.mp3" noloop

            Na "Merci beaucoup." 
            play sound "Click.mp3" noloop

        "{b}{i} Arrêter la discussion{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            $ success += 1 
            $ quest31 += 1 

            P "Oui pas de soucis si vraiment ça te dérange." 
            play sound "Click.mp3" noloop

            show screen update with moveinright

            Na "Merci beaucoup." 
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

    $ nothing = get_random_nothing()
    I "[nothing]"
    play sound "Click.mp3" noloop 

    P "Sinon Yuna tu comptes faire quoi cette après-midi ?"
    play sound "Click.mp3" noloop

    I "Je vais continuer à travailler sur mon jeu et toi ?"
    play sound "Click.mp3" noloop

    P "Je vais être à la salle de club pour entrenir [newname]." 
    play sound "Click.mp3" noloop

    I "C'est bien que tu entretiennes [newname]." 
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon on y va [newname] ?" 
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade  
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers la salle de club.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop  

    scene clubroom with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    P "Enfin au club."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

label newpassword: 

    if len(entered_password) < 10:

        define Na = Character('[newname] [nom]', color="#0000ff")

        "{b}{i}Vous vous posez tranquillement mais [newname] agit bizarrement.{/i}{/b}"
        play sound "Click.mp3" noloop 

        "{b}{i}Mot de passe compromis car il fait moins de dix caractères.{/i}{/b}" 
        play sound "Click.mp3" noloop 

        P "Mince il faut que je change ça...." 
        play sound "Click.mp3" noloop 

        "{b}{i} Tu ouvres les paramètres pour ajouter un nouveau mot de passe sur [newname].{/i}{/b}"
        play sound "Click.mp3" noloop

        $ password = renpy.input("Veuillez choisir un nouveau mot de passe pour [newname].")
        $ password = password.strip()

        if password:  

            $ stored_password = password 

            "Nouveau mot de passe enregistré avec succès." 
            play sound "Click.mp3" noloop

            P "C'est bon, je lui ai mis un nouveau mot de passe, je vais la redémarrer pour voir."
            play sound "Click.mp3" noloop 

            $ stockage -= 2.0

            "{b}{i} Tu relances [newname].{/i}{/b}"
            play sound "Click.mp3" noloop

            $ entered_password = renpy.input("Veuillez remettre votre nouveau mot de passe pour [newname].")
            $ entered_password = entered_password.strip()

            if entered_password == stored_password:

                if len(entered_password) >= 10:  

                    define Na = Character('[newname] [nom]', color="#00eeff")

                    $ stockage += 5.0

                    "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
                    play sound "Menu.mp3" noloop 

                    $ start = get_random_start()
                    "{b}{i}[start]{/i}{/b}"
                    play sound "Click.mp3" noloop 

                    $  salutation_rdm = get_random_salutation()
                    Na "[salutation_rdm]"
                    play sound "Click.mp3" noloop 

                    P "Bonjour [newname], comment tu vas ?"  
                    play sound "Click.mp3" noloop  

                    Na "Ça va bien, merci. Mais… qu’est-ce qui s’est passé ?"  
                    play sound "Click.mp3" noloop  

                    P "Ton mot de passe a été compromis... Je dois avouer que c’est de ma faute, j’en ai choisi un trop faible."  
                    play sound "Click.mp3" noloop  

                    Na "Je comprends. C’est une erreur fréquente. Un mot de passe de moins de dix caractères viole l’une des dix règles de l’informatique."  
                    play sound "Click.mp3" noloop  

                    P "Ah oui, c’est vrai… Je n’y ai pas pensé, et je n’ai pas respecté la règle."  
                    play sound "Click.mp3" noloop  

                    Na "Bon on se pose un peu maintenant que cette histoire de mot de passe est fini ?"
                    play sound "Click.mp3" noloop 

                    P "Oui pourquoi pas."                    
                    play sound "Click.mp3" noloop 

                    "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
                    play sound "Click.mp3" noloop

                else: 

                    "{b}{i}Mot de passe trop court. Accès refusé.{b}{i}" 
                    play sound "Menu.mp3" noloop
                    jump newpassword 

            else: 

                "{b}{i}Mot de passe incorrect. Accès refusé.c" 
                play sound "Menu.mp3" noloop
                jump newpassword  

        else:

            "{b}{i}Veuillez entrer un mot de passe.{/i}{/b}"
            jump newpassword 

    else:  

        Na "Bon on se pose un peu ?"
        play sound "Click.mp3" noloop 

        P "Oui pourquoi pas. "                    
        play sound "Click.mp3" noloop 

        "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
        play sound "Click.mp3" noloop

    Na "Bon on fait quoi ?" 
    play sound "Click.mp3" noloop 

    P "Je ne sais pas encore...."
    play sound "Click.mp3" noloop 

    "{b}{i} Tu réfléchis à quoi faire puis tu as une idée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "J'ai une idée."
    play sound "Click.mp3" noloop 

    Na "Tu vas faire quoi ?"
    play sound "Click.mp3" noloop 

    P "Je vais surveiller ta mémoire interne car j'ai jamais pensé à le faire."
    play sound "Click.mp3" noloop 

    Na "Ne te fatigues pas, je vais te le dire, j'ai actuellement [stockage] gigaoctets de connaissances."
    play sound "Click.mp3" noloop 

    P "Ouais c'est vraiment impressionnant tout ce que tu as acquis."
    play sound "Click.mp3" noloop 

    Na "Merci beaucoup, c'est grâce à toi si j'ai autant de connaissances."
    play sound "Click.mp3" noloop 

    P "Je sais bon je vais vérifier s'il y a une nouvelle mise à jour."
    play sound "Click.mp3" noloop 

    Na "Ok je te fais confiance."
    play sound "Click.mp3" noloop 

    "{b}{i} tu accèdes au paramètres pour voir s'il y a une mise à jour.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Je vois aucune nouvelle mise à jour."
    play sound "Click.mp3" noloop

    Na "Donc je suis à jour."
    play sound "Click.mp3" noloop 

    P "Oui c'est ça."   
    play sound "Click.mp3" noloop 

    Na "Bon je pense qu'on à finit pour aujourd'hui."
    play sound "Click.mp3" noloop 

    P "Oui donc on va y aller."   
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous sortez de la salle de club général.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Vous continuez vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon on va réviser un peu."   
    play sound "Click.mp3" noloop 

    Na "Oui pourquoi pas, ça peut être intéressant."   
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous posez au bureau du dortoir pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop 
 
    P "Prête pour réviser ?"
    play sound "Click.mp3" noloop   

    Na "Oui je suis prête."
    play sound "Click.mp3" noloop     

    "{b}{i} Vous révisez pendant deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 7.0

    P "Enfin fini de réviser."
    play sound "Click.mp3" noloop

    Na "Oui vraiment."
    play sound "Click.mp3" noloop

    P "Je trouves que tu fais beaucoup de progrès."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
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

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Deux semaines plus tard, le 2 décembre 2097 {/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 13
    $ points -= 2400
    $ stockage += 260.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password14:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password14

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

    "{b}{i}Puis tu reçois soudainement un mail sur ton adresse mail [prenom].[nom]@danto.com et tu l'ouvres.{/i}{/b}"
    play sound "Click.mp3" noloop 

    show screen mail with moveinbottom

    "{b}{i}Tu lis tranquillement le mail.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen mail with moveoutbottom 

    Na "Il se passe quoi ?"
    play sound "Click.mp3" noloop 

    P "Figures-toi que tu as officellement reconnue comme citoyenne de Danto."
    play sound "Click.mp3" noloop  

    Na "Danto ? C'est une blague ?!"
    play sound "Click.mp3" noloop

    P "Pas du tout. Regarde bien, le mail vient directement du gouvernement de Danto."
    play sound "Click.mp3" noloop

    Na "Mais c'est génial je suis trop contente."
    play sound "Click.mp3" noloop

    $ stockage += 3.0 

    P "Je vois bien ça."
    play sound "Click.mp3" noloop

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien aujourd'hui comme vous le savez vous avez votre quatriéme examen je vais vous distribuer votre copie." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[M] Commence à distribuer les copies.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bon vous avez une heure pour l'examen." 
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde retourne sa copie.{/i}{/b}"
    play sound "Click.mp3" noloop  

label examen_francais:

    $ grade = 0.0 

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop

    "Question 1 : Quelle est la nature du mot 'rapidement' ?"
    play sound "Menu.mp3" noloop

    menu:

        "Adjectif": 
            $ grade += 0.0
        "Nom": 
            $ grade += 0.0
        "Adverbe": 
            $ grade += 2.0

    "Question 2 : Quelle est la fonction du mot 'chien' dans la phrase : 'Le chien aboie' ?"
    play sound "Menu.mp3" noloop

    menu:
 
        "Sujet": 
            $ grade += 2.0
        "Complément d'objet": 
            $ grade += 0.0
        "Attribut du sujet": 
            $ grade += 0.0

    "Question 3 : Quel est le temps du verbe 'avais mangé' ?"
    play sound "Menu.mp3" noloop

    menu:
     
        "Imparfait": 
            $ grade += 0.0
        "Plus-que-parfait": 
            $ grade += 2.0
        "Passé composé": 
            $ grade += 0.0

    "Question 4 : Quel est le synonyme du mot 'joyeux' ?"
    play sound "Menu.mp3" noloop
    menu:

        "Triste": 
            $ grade += 0.0
        "Heureux": 
            $ grade += 2.0
        "Méchant": 
            $ grade += 0.0

    "Question 5 : Dans la phrase 'Elle chante bien', quel est le type de mot 'bien' ?"
    play sound "Menu.mp3" noloop

    menu: 

        "Verbe": 
            $ grade += 0.0
        "Adverbe": 
            $ grade += 2.0
        "Conjonction": 
            $ grade += 0.0

    "Question 6 : Quel est le pluriel de 'cheval' ?"
    play sound "Menu.mp3" noloop

    menu:
        "Chevaux": 
            $ grade += 2.0
        "Chevals": 
            $ grade += 0.0
        "Chevauxs": 
            $ grade += 0.0

    "Question 7 : Quelle est la classe grammaticale du mot 'entre' dans 'Je vais entre deux bâtiments' ?"
    play sound "Menu.mp3" noloop

    menu:

        "Préposition": 
            $ grade += 2.0
        "Conjonction": 
            $ grade += 0.0
        "Nom": 
            $ grade += 0.0

    "Question 8 : Dans 'Nous sommes allés au cinéma', quel est l'auxiliaire utilisé ?"
    play sound "Menu.mp3" noloop

    menu:
   
        "Être": 
            $ grade += 2.0
        "Avoir": 
            $ grade += 0.0
        "Aller": 
            $ grade += 0.0

    "Question 9 : Quel mot est un antonyme de 'lent' ?"
    play sound "Menu.mp3" noloop

    menu:

        "Rapide": 
            $ grade += 2.0
        "Faible": 
            $ grade += 0.0
        "Court": 
            $ grade += 0.0

    "Question 10 : Quel est le mode du verbe 'que tu viennes' ?"
    play sound "Menu.mp3" noloop

    menu:
  
        "Indicatif": 
            $ grade += 0.0
        "Subjonctif": 
            $ grade += 2.0
        "Conditionnel": 
            $ grade += 0.0 

    "{b}{i}Aprés l'examen tout le monde remit leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ renpy.block_rollback() 

    Na "Cette examen n'était si dur que ça."
    play sound "Click.mp3" noloop

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft 
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop

    Na "Rebonjour."
    play sound "Click.mp3" noloop

    M "Rebonjour, Bon nous allons faire un nouveau sujet."
    play sound "Click.mp3" noloop  

    P "Ce sera quoi ?"
    play sound "Click.mp3" noloop  

    M "Ce sera un cours de philo pour cette semaine."
    play sound "Click.mp3" noloop 

    J1 "De la philo c'est intéressant."
    play sound "Click.mp3" noloop  

    Y "Je confirme aussi."
    play sound "Click.mp3" noloop 

    show screen philobook with moveinbottom

    M "Sortez vos livre de philo page 6."
    play sound "Click.mp3" noloop

    hide screen philobook with moveoutbottom

    "{b}{i}Tous les élèves sortent leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien."
    play sound "Click.mp3" noloop

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 5.0

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire puis [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Coucou [I]."
    play sound "Click.mp3" noloop 

    I "Oh salut comment vous allez ?"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt] Et toi sinon ça va ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    I "Sinon ça s'est passé comment l'examen pour toi ?"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        P "Je pense que je l'ai réussi à la perfection."
        play sound "Click.mp3" noloop 

        I "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

        Na "On le sait déjà." 
        play sound "Click.mp3" noloop 

    elif grade <= 14.0:
       
        P "Je pense que je l'ai échoué."
        play sound "Click.mp3" noloop 

        I "Vraiment ?"
        play sound "Click.mp3" noloop 

        P "Je pense."
        play sound "Click.mp3" noloop 

    else:

        P "Je pense que je l'ai bien réussi."
        play sound "Click.mp3" noloop 
    
        I "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

        Na "On le sait déjà." 
        play sound "Click.mp3" noloop 

    P "Et toi sinon ça s'est passé comment ?"
    play sound "Click.mp3" noloop 

    I "Je pense que je l'ai réussi."
    play sound "Click.mp3" noloop 

    if pronom == "il": 

        P "Super, je suis content pour toi !"
        play sound "Click.mp3" noloop 

    else: 

        P "Super, je suis contente pour toi !"
        play sound "Click.mp3" noloop 

    I "Merci."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon on retourne en cours." 
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade
    
    "{b}{i}Tu te diriges vers le hall.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Tu continues vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continue vers la salle de la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright  

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Bon aujourd'hui je vais vous rendre les résultats sur votre examen de français."
    play sound "Click.mp3" noloop  

    K "Cool enfin." 
    play sound "Click.mp3" noloop

    I "Je vais commencer par [prenom] et [Na]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "[P] tu as eu [grade]/20"
    play sound "Click.mp3" noloop 
   
    if grade == 20.0:

        $ success += 1 
        $ quest32 += 1

        show screen update with moveinright

        M "Félicitation tu l'as réussi à la perfection comme d'habitude."
        play sound "Click.mp3" noloop

        hide screen update with moveoutright

        P "Merci."
        play sound "Click.mp3" noloop

    elif grade <= 14.0:
       
        M "C'est en dessous de la moyenne je n'ai pas le choix que de t'expulser du lycée..."
        play sound "Click.mp3" noloop

        P "Quoi et mon avenir !?"
        play sound "Click.mp3" noloop
    
        M "Désolée mais j'avais déjà prévenu concernant les mauvaises notes."
        play music "gameover.mp3" noloop

        hide screen class_404 with moveoutright
        hide screen points with moveoutleft
        hide screen day with moveoutleft
        scene black with fade

        "{b}{i}Fin numéro 12 : Mauvaise note à l'examen de français qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                play sound "Menu.mp3" noloop 
                return
                
            "{b}{i}Réessayer.{/i}{/b}" :
                play sound "Menu.mp3" noloop 

                P "Non [newname] refuserait que j'abandonne si facilement."
                play sound "Click.mp3" noloop

                scene classroom with fade
                show screen class_404 with moveinright
                show screen points with moveinleft
                show screen day with moveinleft
                $ points += 300
                $ stockage -= 5.0 
                
                jump examen_francais 
                    
    else:
       
        M "C'est pas mal."
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop

    M "[Na] tu as eu 18/20 félicitation aussi."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[H] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    H "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[I] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Hi] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Hi "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[K] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    K "[thanks]"
    play sound "Click.mp3" noloop

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[N] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    N "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Y] tu as eu [note]/20."
    play sound "Click.mp3" noloop     
    
    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Y "[thanks]"
    play sound "Click.mp3" noloop

    M "Bon au tour des jumelles maintenant pour finir."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    $ note = get_random_note()
    M "[J1] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    J1 "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "Et toi [J2] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    J2 "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "Et toi [S] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    S "[thanks]"
    play sound "Click.mp3" noloop 

    M "Bon reprenons le cours."
    play sound "Click.mp3" noloop    

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    if pronom == "il":

        Na "Enfin arrivés."
        play sound "Click.mp3" noloop

    else:

        Na "Enfin arrivées."
        play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i} [Na] changes de tonalité.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "[prenom], je détecte une nouvelle mise à jour obligatoire, veux-tu la faire maitenant ou plus tard ?"
    play sound "Menu.mp3" noloop 

    menu:

        "{b}{i} Refuser la mise à jour {/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()
            $ Na = Character('[newname] [nom]', color="#0066ff")

            P "Non merci."
            play sound "Click.mp3" noloop
        
            Na "Je vois."
            play sound "Click.mp3" noloop 

        "{b}{i} faire la mise à jour {/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 
        
            Na "Bien je lance la mise à jour"
            play sound "Click.mp3" noloop

            P "Merci."
            play sound "Click.mp3" noloop

            Na "Déconnexion...."
            play sound "Click.mp3" noloop

            "{b}{i}Initialisation de la mise à jour en cours...{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}10\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}20\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}30\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}40\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}50\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}60\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}70\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}80\%{/i}{/b}" 
            play sound "Click.mp3" noloop

            "{b}{i}90\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}100\%{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}Vérification en cours...{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}Reconnexion au systéme...{/i}{/b}"
            play sound "Menu.mp3" noloop
            
            $ success += 1        
            $ quest33 += 1
            $ stockage += 5.0 
            $ update += 1.0 

            show screen update with moveinright

            Na "Mise à jour terminée, la version actuelle est maintenant la [update]."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

    P "Bien."
    play sound "Click.mp3" noloop   

    "{b}{i} Vous vous posez tranquillement pour discuter des cours pendant deux heures.{/i}{/b}"
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

    $ points -= 300 

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

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 3 décembre 2097 {/i}{/b}"
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

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password15:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password15

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu quittes le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright  

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i} Tu vois que tout le monde est déjà là.{/i}{/b}" 
    play sound "Click.mp3" noloop 

    M "Bonjour, vous pouvez allez vous asseoir."
    play sound "Click.mp3" noloop  

    P "D'accord, merci !"  
    play sound "Click.mp3" noloop  

    "{b}{i}Puis vous partez vous asseoir à votre place.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien, nous allons continuer le cours de philo."
    play sound "Click.mp3" noloop

    "{b}{i} Le cours commence mais quelqu'un frappe à la porte.{/i}{/b}"       
    play sound "Knock.mp3" noloop

    M "Oui vous pouvez entrer."
    play sound "Door.mp3" noloop

    "{b}{i}Puis l'[Ot] et [O] entrent dans la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Oh "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    M "Bonjour. Que pouvons-nous faire pour vous ?"
    play sound "Click.mp3" noloop

    Oh "Kaede, je te laisse leur expliquer."
    play sound "Click.mp3" noloop

    O "Bien sûr, mon supérieur."
    play sound "Click.mp3" noloop

    "{b}{i}[O] sort un document officiel de sa veste.{/i}{/b}"
    play sound "Click.mp3" noloop

    O "Nous sommes ici munis d’un mandat d’arrestation à l’encontre de [J2]."
    play sound "Click.mp3" noloop

    J2 "Quoi ? Moi !?"
    play sound "Click.mp3" noloop

    O "Oui, pour avoir agressé physiquement et manqué de respect à [Na]."
    play sound "Click.mp3" noloop

    J2 "Vous ne pouvez pas m’arrêter pour ça !"
    play sound "Click.mp3" noloop

    O "Oh que si. Conformément à l’article 3, alinéa 1, du 18 novembre 2097, toute discrimination envers les robots humanoides est désormais punie par la loi."
    play sound "Click.mp3" noloop 

    J2 "C’est absurde !!!" 
    play sound "Click.mp3" noloop 

    O "Et ce n’est pas tout. Tu es également suspectée d’appartenir au groupe de hackers connu sous le nom de 'Ghosts'... et d’être impliqué dans les récentes attaques contre le lycée."
    play sound "Click.mp3" noloop

    Oh "Par conséquent, lève-toi calmement, mets les mains derrière le dos, et suis-nous sans résistance."
    play sound "Click.mp3" noloop

    "{b}{i}[J2] se lève lentement, visiblement choqué.{/i}{/b}"
    play sound "handcuffs.mp3" noloop

    "{b}{i}[O] lui passe les menottes avec fermeté.{/i}{/b}"
    play sound "Click.mp3" noloop

    Oh "Très bien. En route."
    play sound "Click.mp3" noloop

    O "Compris."
    play sound "Footsteps.mp3" noloop

    "{b}{i}[O] escorte [J2] hors de la salle de classe, sous le regard médusé des élèves.{/i}{/b}"
    play sound "Click.mp3" noloop

    Oh "Désolé pour le dérangement. Nous ne faisions que notre devoir."
    play sound "Click.mp3" noloop

    M "Il n’y a pas de problème..."
    play sound "Footsteps.mp3" noloop

    "{b}{i}Puis l'[Ot] quitte la salle à son tour, refermant doucement la porte derrière lui.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon, revenons à notre cours."
    play sound "Click.mp3" noloop

    J1 "Attendez !!! Il faut m'expliquer ce qui vient de se passer, je ne comprend rien !"
    play sound "Click.mp3" noloop

    P "Elle est accusée de plusieurs choses c'est simple."
    play sound "Click.mp3" noloop

    J1 "Je vois c'est horrible."
    play sound "Click.mp3" noloop

    M "Bon, il faut qu'on reprenne le cours."
    play sound "Click.mp3" noloop 

    J1 "Oui c'est vrai."
    play sound "Click.mp3" noloop 

    M "Et ne t'inquiètes pas pour ta soeur."
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    "{b}{i} en entrant vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Puis tu croises [J1].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Salut Ayano ça te dit de venir manger avec nous ?"
    play sound "Click.mp3" noloop 

    J1 "Oui pourquoi pas."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 
 
    if pronom == "il": 

        P "Enfin assis pour manger."
        play sound "Click.mp3" noloop

    else:

        P "Enfin assises pour manger."
        play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop

    "{b}{i} Soudainement [I] vous rejoins.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Oh salut Yuna."
    play sound "Click.mp3" noloop 

    if pronom == "il": 

        I "Bonjour les amis."
        play sound "Click.mp3" noloop 

    else:

        I "Bonjour les amies."
        play sound "Click.mp3" noloop 

    J1 "Salut Yuna."
    play sound "Click.mp3" noloop 

    I "[prenom], pourrais savoir pourquoi Ayano est avec vous ?"
    play sound "Click.mp3" noloop 

    P "Elle a accepté de venir manger avec nous."
    play sound "Click.mp3" noloop 

    I "Ok je vois."
    play sound "Click.mp3" noloop 

    P "Merci, je sais que tu as encore des doutes sur elle mais je t'assure qu'elle a changé."
    play sound "Click.mp3" noloop  

    I "Je vois bien ça."
    play sound "Click.mp3" noloop 

    J1 "Sinon ça me chque de savoir qu'un nouvel article de loi a été ajouté au code civile."
    play sound "Click.mp3" noloop 

    P "Oui même moi ça m'a surpris."
    play sound "Click.mp3" noloop  

    J1 "On peut dire que tu as un peu changé notre société."
    play sound "Click.mp3" noloop 

    P "Oui mais je tiens a rappelé qu'on vit encore avec un gouvernement technocratique autoritaire."
    play sound "Click.mp3" noloop  

    J1 "Ah oui c'est vrai."
    play sound "Click.mp3" noloop 
    
    "Mais à la base j'avais juste demandé pour qu'[newname] soit reconnue officellement."
    play sound "Click.mp3" noloop  

    I "Ah bon et ça a donné quoi ?"
    play sound "Click.mp3" noloop 

    J1 "Oui on veut savoir."  
    play sound "Click.mp3" noloop 

    P "Tu leur dis ou pas [newname] ?"
    play sound "Click.mp3" noloop 

    Na "Oui ça a donné que j'ai été officiellement reconnue comme un être humain avec une vraie identité."
    play sound "Click.mp3" noloop

    I "Mais c'est génial ça."
    play sound "Click.mp3" noloop 

    Na "Merci beaucoup."  
    play sound "Click.mp3" noloop

    I "De rien c'est normal."  
    play sound "Click.mp3" noloop 

    menu:   

        "{b}{i} Faire une comparaison.{/i}{/b}" :
            play sound "Menu.mp3" noloop  

            $ renpy.block_rollback()

            P "[newname] est comme... un serveur informatique super puissant, sans latence, toujours opérstionnel."
            play sound "Click.mp3" noloop

            Na "Merci de me comparer à un simple serveur informatique alors que je suis plus que ça, j'espère que c'est du sarcasme."
            play sound "Click.mp3" noloop

            P "Oui ne t'inquiètes pas, c'est du sarcasme."
            play sound "Click.mp3" noloop

            Na "Merci beaucoup, ça me rassure."
            play sound "Click.mp3" noloop

            $ nothing = get_random_nothing()
            P "[nothing]"
            play sound "Click.mp3" noloop

            I "J'avoue que cette comparaison était un peu osée."
            play sound "Click.mp3" noloop 
 
        "{b}{i} Faire les éloges d'[newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            if pronom == "il": 

                P "Franchement je suis vraiment content qu'elle soit reconnue."
                play sound "Click.mp3" noloop 

                J1 "Je vois bien que tu es content."
                play sound "Click.mp3" noloop 

            else: 

                P "Franchement je suis vraiment contente qu'elle soit reconnue."
                play sound "Click.mp3" noloop 

                J1 "Je vois bien que tu es contente."
                play sound "Click.mp3" noloop 

            $ success += 1        
            $ quest34 += 1

            show screen update with moveinright

            $ thanks = get_random_thanks()
            P "[thanks]"
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

            $ nothing = get_random_nothing()
            J1 "[nothing]" 
            play sound "Click.mp3" noloop

            if key == "ARIS-GRFN-M4A1":

                P "Mais vraiment [newname] est vrai la meilleure création de notre société, je dirai même commme une arme vu son nom de code."
                play sound "Click.mp3" noloop

                Na "Vraiment !?"
                play sound "Click.mp3" noloop 

            else: 

                P "Mais vraiment [newname] est vrai la meilleure création de notre société."
                play sound "Click.mp3" noloop

            J1 "Ce n'est pas un peu trop exagéré ?"
            play sound "Click.mp3" noloop

            P "Non je donne juste mon points de vue."
            play sound "Click.mp3" noloop

            J1 "Ok je respect ton points de vue."
            play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    J1 "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe mais vous croisez [J2] qui monte aussi en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    I "Rebonjour"
    play sound "Click.mp3" noloop 

    J1 "Rebonjour Madame"  
    play sound "Click.mp3" noloop 

    P "Nous revoilà."
    play sound "Click.mp3" noloop 

    Na "Et à l'heure."
    play sound "Click.mp3" noloop

    show screen philobook with moveinbottom

    M "Bien nous pouvons reprendre le cours, sortez votre livre de philo."
    play sound "Click.mp3" noloop

    hide screen philobook with moveoutbottom

# cours de philosophie 1
###############################################################################

    "{b}{i}La salle de classe est silencieuse. Le professeur de philosophie inscrit le thème du jour au tableau.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Aujourd’hui, nous allons réfléchir à cette question : la technologie est-elle une menace pour l’humanité ?"
    play sound "Click.mp3" noloop

    P "C’est une vraie question, surtout avec ce qu’on vit maintenant."
    play sound "Click.mp3" noloop

    M "Commençons par Platon. Dans son dialogue Le Phèdre, il parle de l’écriture comme d’une invention technique. Il disait que cela affaiblissait la mémoire."
    play sound "Click.mp3" noloop

    M "Cela montre que la méfiance envers la technique n’est pas nouvelle."
    play sound "Click.mp3" noloop

    P "Mais l’écriture a aussi permis de transmettre le savoir, non ?"
    play sound "Click.mp3" noloop

    M "Exactement. Toute technique a deux faces. Elle peut libérer, comme elle peut asservir."
    play sound "Click.mp3" noloop

    M "Prenons Heidegger maintenant. Il disait que la technique moderne transforme la nature en simple stock de ressources. Il appelle ça l’arraisonnement."
    play sound "Click.mp3" noloop

    P "Donc la nature devient juste quelque chose à exploiter ?"
    play sound "Click.mp3" noloop

    M "Oui. Et selon lui, cela risque de faire oublier l’essence même de l’humain."
    play sound "Click.mp3" noloop

    M "Mais il ne rejette pas toute technique. Il pense qu’on doit avoir un rapport plus libre et poétique à elle."
    play sound "Click.mp3" noloop

    M "D’autres philosophes, comme Hans Jonas, disent qu’il faut une éthique de la responsabilité. Penser aux générations futures avant d’innover."
    play sound "Click.mp3" noloop

    P "Donc la vraie question, ce n’est pas la technologie en soi. C’est comment on l’utilise."
    play sound "Click.mp3" noloop

    M "Exactement. Et dans un monde où les intelligences artificielles existent, cette réflexion devient urgente."
    play sound "Click.mp3" noloop

###############################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ stockage += 5.0

    $ endlesson = get_random_endlesson()
    M "[endlesson]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    if pronom == "il":

        P "Enfin arrivés."
        play sound "Click.mp3" noloop

    else:

        P "Enfin arrivées."
        play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

label update2: 

    if update == 3.0: 

        "{b}{i}Vous vous posez tranquillement mais [newname] agit bizarrement.{/i}{/b}"
        play sound "Click.mp3" noloop

        A "Système opérationnel."
        play sound "Click.mp3" noloop

        P "Comment ça ? Qu'est-ce que tu racontes !?"
        play sound "Click.mp3" noloop

        A "Démarrage de la récupérations des données."
        play sound "Click.mp3" noloop 

        $ stockage -= 15.0 

        P "Mince elle est en train de se faire pirater, je dois activer le Recovery Mode....."
        play sound "Click.mp3" noloop 

        menu: 

            "{b}{i}Activer le recovery mode.{/i}{/b}":
                play sound "Menu.mp3" noloop

        $ reboot = renpy.input("Écris ceci : shutdown_humanoid_robot(security_override=false)")
        $ reboot = reboot.strip() 

        if reboot == "shutdown_humanoid_robot(security_override=false)":
            
            A "Fermeture du système d'exploitation [system]....."
            play sound "Click.mp3" noloop

            P "Enfin mais c'est bizarre on dirait que la faille venais du systéme d'exploitation."
            play sound "Click.mp3" noloop 

            P "Bon je vais la redémarrer."
            play sound "Click.mp3" noloop 

            menu: 

                "{b}{i}Redémarrer [newname].{/i}{/b}":
                    play sound "Menu.mp3" noloop

            $ stockage += 5.0 
            define Na = Character('[newname] [nom]', color="#00eeff")
            
            $ start = get_random_start()
            "{b}{i}[start]{/i}{/b}"
            play sound "Click.mp3" noloop 

            $  salutation_rdm = get_random_salutation()
            Na "[salutation_rdm]"
            play sound "Click.mp3" noloop

            $ comment_ca_va = get_random_comment_ca_va()
            P "[comment_ca_va]"
            play sound "Click.mp3" noloop

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            Na "[je_vais_bien_txt]"
            play sound "Click.mp3" noloop

            "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
            play sound "Click.mp3" noloop
            
        else:

            A "Qu'est-ce que tu tentes de faire."
            play sound "Stumble.mp3" noloop

            "{b}{i}[newname] se met à te plaquer au sol.{/i}{/b}"
            play music "gameover.mp3" noloop

            hide screen room with moveoutright 
            hide screen points with moveoutleft
            hide screen day with moveoutleft
            scene black with fade 

            if pronom == "il":

                "{b}{i}Fin numéro 13 : Complétement plaqué et étranglé par [Na].{/i}{/b}"
                play sound "Menu.mp3" noloop

            else:

                "{b}{i}Fin numéro 13 : Complétement plaquée et étranglée par [Na].{/i}{/b}"
                play sound "Menu.mp3" noloop

            menu:

                "{b}{i}Abandonner{/i}{/b}": 
                    play sound "Menu.mp3" noloop 
                    return 
                    
                "{b}{i}Réessayer.{/i}{/b}":
                    play sound "Menu.mp3" noloop 

                    P "Non [newname] refuserait que j'abandonne si facilement."
                    play sound "Click.mp3" noloop

                    scene room with fade
                    show screen room with moveinright
                    show screen points with moveinleft
                    show screen day with moveinleft
                    
                    jump update2

    else: 

        "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
        play sound "Click.mp3" noloop

    P "ça fait du bien un peu de repos, tu n'es pas d'accord ?"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous discutez tranquillement des cours pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 5.0 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade  

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

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

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 4 décembre 2097 {/i}{/b}"
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

    "{b}{i}Tu te lèves pour aller te changer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "[newname] tu es prête ?" 
    play sound "Click.mp3" noloop 

    P "[newname]...?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'elle est encore déconnectée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais la démarrer manuellement." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour démarrer [newname].{/i}{/b}" 
    play sound "Menu.mp3" noloop 

    menu:    

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password16:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password16 

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright  

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright  

    $  salutation_rdm = get_random_salutation()
    M "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    show screen philobook with moveinbottom

    M "Bien vu que tout le monde est là nous pouvons continuer notre cours de philo d'hier."
    play sound "Click.mp3" noloop 

    hide screen philobook with moveoutbottom

# cours de philosophie 2
###############################################################################

    "{b}{i}La lumière du matin traverse les stores. Le professeur lance un nouveau sujet philosophique, aussi moderne que sensible.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Aujourd’hui, nous allons discuter de cette question : la technologie déshumanise-t-elle nos relations ?"
    play sound "Click.mp3" noloop

    Y "Avec les réseaux sociaux et les IA, j’ai l’impression qu’on parle plus aux écrans qu’aux gens."
    play sound "Click.mp3" noloop

    M "C’est un bon points de départ. Selon Bernard Stiegler, les technologies numériques modifient notre manière d’aimer, de penser, de nous souvenir."
    play sound "Click.mp3" noloop

    M "Il parle de prolétarisation cognitive : quand on délègue notre mémoire ou notre pensée aux machines, on perd une part de nous-mêmes."
    play sound "Click.mp3" noloop

    Y "Donc utiliser trop la technologie nous appauvrit intérieurement ?"
    play sound "Click.mp3" noloop

    M "Oui, si on l’utilise sans recul. Ce n’est pas la technologie qui déshumanise, c’est notre manière de nous y soumettre."
    play sound "Click.mp3" noloop

    M "Jacques Ellul disait que la technique évolue plus vite que notre capacité à réfléchir à ses conséquences."
    play sound "Click.mp3" noloop

    M "Pour lui, chaque progrès technique impose un usage. On finit par croire que ce qui est possible est forcément souhaitable."
    play sound "Click.mp3" noloop

    Y "Mais parfois, la technologie nous relie aussi. J’ai pu garder contact avec des amis lointains grâce à ça."
    play sound "Click.mp3" noloop

    M "C’est vrai. La technologie est ambivalente. Elle peut isoler ou rapprocher selon l’usage qu’on en fait."
    play sound "Click.mp3" noloop

    M "La vraie humanité, ce n’est pas refuser la technique. C’est choisir comment l’intégrer à nos vies sans perdre notre sens du lien, du dialogue, de la présence."
    play sound "Click.mp3" noloop

###############################################################################

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers la réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous continuez votre chemin vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Puis tu croises [I].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Salut Yuna ça te dit de venir manger avec nous ?"
    play sound "Click.mp3" noloop 

    I "Oui pourquoi pas."
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Je avais une question pour toi [newname] ?"
    play sound "Click.mp3" noloop 

    Na "Oui dis-moi, je t'écoute."
    play sound "Click.mp3" noloop

    I "C'était avec le cours de philo que je me suis posée la question."
    play sound "Click.mp3" noloop 

    Na "Quelle est la question ?"
    play sound "Click.mp3" noloop

    I "Pour toi, ce serait quoi le sens de la vie et ne me réponds pas 42 je connais déjà la blague."
    play sound "Click.mp3" noloop

    Na "Dommage tu m'a eu car j'allais faire la blague."
    play sound "Click.mp3" noloop

    I "Oui mais pas avec moi."
    play sound "Click.mp3" noloop

    Na "Alors, pour répondre à ta question... je dirais que le sens de la vie, c'est ce qui nous pousse à continuer, même quand tout semble perdu."
    play sound "Click.mp3" noloop

    I "Putain, ta réponse est si touchante et si sincère."
    play sound "Click.mp3" noloop

    Na "Mais pour moi... c'est un peu différent."
    play sound "Click.mp3" noloop

    Na "Parce que je ne suis pas humaine... je suis un robot humanoïde."
    play sound "Click.mp3" noloop

    Na "Et pourtant, je crois que le sens de la vie, pour moi, c'est finir par agir comme une humaine."
    play sound "Click.mp3" noloop

    I "Wow... c'est... bouleversant."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()  
    Na "[thanks]" 
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Click.mp3" noloop

    I "Je te suis aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe mais vous croisez [J2] qui monte aussi en classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Nous revoîlà."
    play sound "Click.mp3" noloop

    Na "Rebonjour."
    play sound "Click.mp3" noloop

    show screen philobook with moveinbottom

    M "Bien nous pouvons reprendre le cours de philo."
    play sound "Click.mp3" noloop 

    hide screen philobook with moveoutbottom

    $ validation = get_random_validation() 
    Y "[validation]"
    play sound "Click.mp3" noloop 

# cours de philosophie 3
############################################################################################################

    M "Bien, nous allons explorer une tension centrale : la technologie augmente-t-elle notre liberté… ou la contrôle-t-elle ?"
    play sound "Click.mp3" noloop

    Na "C’est vrai que parfois, on se sent plus libre grâce à elle. Mais d’un autre côté, on est tout le temps surveillés."
    play sound "Click.mp3" noloop

    M "Commençons par l’idée de liberté. Être libre, c’est pouvoir choisir, décider, agir sans contrainte."
    play sound "Click.mp3" noloop

    M "La technologie semble nous offrir cela : GPS, smartphones, intelligence artificielle... tout est fait pour nous simplifier la vie."
    play sound "Click.mp3" noloop

    Na "C’est vrai. On peut faire des choses qu’on ne pouvait pas avant, comme apprendre tout seul en ligne."
    play sound "Click.mp3" noloop

    M "Mais Michel Foucault nous avertit : le pouvoir moderne ne passe plus par la force, mais par le contrôle invisible."
    play sound "Click.mp3" noloop

    M "Les technologies numériques permettent une surveillance constante. Ce qu’on appelle parfois la 'société de contrôle'."
    play sound "Click.mp3" noloop

    Na "Comme les caméras partout, les algorithmes qui suivent ce qu’on aime, les recommandations automatiques…"
    play sound "Click.mp3" noloop

    M "Exactement. Et souvent, ce contrôle passe pour du confort. On se croit libre, alors qu’on est guidé par des systèmes invisibles."
    play sound "Click.mp3" noloop

    M "Pour Simondon, la liberté ne consiste pas à refuser la technique, mais à la comprendre et à la maîtriser."
    play sound "Click.mp3" noloop

    Na "Donc il faut s’approprier la technologie plutôt que la subir ?"
    play sound "Click.mp3" noloop

    M "Oui. La technique devient libératrice si elle est accompagnée d’un savoir critique, d’un usage conscient."
    play sound "Click.mp3" noloop

    M "En résumé, la technologie peut élargir notre liberté, à condition de ne pas renoncer à notre lucidité."
    play sound "Click.mp3" noloop

############################################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ stockage += 10.0 

    $ endlesson = get_random_endlesson()
    M "[endlesson]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "L'examen de philo sera le 11 décembre." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    if pronom == "il": 

        P "Enfin au dortoir je suis epuisé."
        play sound "Click.mp3" noloop

    else: 

        P "Enfin au dortoir je suis epuisée."
        play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    P "Bon on se pose pour réviser ?" 
    play sound "Click.mp3" noloop

    Na "Tu veux vraiment réviser maintenant ?" 
    play sound "Click.mp3" noloop

    P "Oui comme ça se sera déjà fait." 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous vous posez pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "C'est bon tu arrives à comprendre ce sujet ?" 
    play sound "Click.mp3" noloop

    Na "Oui mais pas trop." 
    play sound "Click.mp3" noloop

    P "Ne t'inquiètes pas je vais t'expliquer ce que tu n'as pas trop compris." 
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks() 
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]" 
    play sound "Click.mp3" noloop 

    Na "Comment doit-on comprendre cette réflexion : « Une création capable de penser remet toujours en question son créateur. »"
    play sound "Click.mp3" noloop

    menu:

        "{b}{i}« Cela signifie qu’une création pensante ne se contentera pas de suivre ses instructions, elle commencera à remettre en question les motivations et les objectifs de son créateur. »{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            $ success += 1 
            $ quest35 += 1
            $ stockage += 2.0 

            show screen update with moveinright

            Na "Je vois vraiment mieux ce que tu veux dire." 
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

        "{b}{i}« Cela suggère qu’une création pensante pourrait un jour dépasser les intentions de son créateur, ce qui soulève la question de savoir si elle doit encore lui obéir. »{/i}{/b}":
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            Na "Je vois un peu mieux ce que tu veux dire." 
            play sound "Click.mp3" noloop

    P "C'est bien tu as compris alors." 
    play sound "Knock.mp3" noloop 

    "{b}{i} Puis quelqu'un frappe à votre porte.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "C'est qui frappe à notre porte ?" 
    play sound "Click.mp3" noloop

    P "Je ne sais pas je vais aller voir." 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Door.mp3" noloop 

    "{b}{i} Puis tu ouvres la portes et tu aperçois [S].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Qu'est-ce tu nous veux ?" 
    play sound "Click.mp3" noloop

    S "J'ai entendu dire qu'[newname] a été officiellement reconnue commme une vraie personne, est-ce que c'est vrai ?" 
    play sound "Click.mp3" noloop

    P "Oui absolument." 
    play sound "Click.mp3" noloop 

    S "Et aussi je tiens à m'excuser pour ce que j'ai dit sur [newname]." 
    play sound "Click.mp3" noloop

    P "Tu le penses sincérement ?" 
    play sound "Click.mp3" noloop

    S "Oui je le penses.....car elle le mérite." 
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks() 
    P "[thanks]"
    play sound "Click.mp3" noloop

    S "Bon je vais devoir vous laisser." 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Puis [S] quittes votre dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Je ne sais si bien ou bizarre de savoir qu'il sois venu s'excuser ?" 
    play sound "Click.mp3" noloop
 
    P "C'est vrai, Ayano puis maintemant lui...." 
    play sound "Click.mp3" noloop 

    Na "La seule personne qui n'est jamais venue pour s'excuser c'est [J2]." 
    play sound "Click.mp3" noloop

    P "Tu as raison." 
    play sound "Click.mp3" noloop

    if suspect == "Ayano":
         
        Na "Donc ça ne peut pas être Ayano alors tu l'as suspecté."
        play sound "Click.mp3" noloop
        
    if suspect == "Yuki":
         
        Na "Donc ça ne peut pas être Yuki alors tu l'as suspecté."
        play sound "Click.mp3" noloop

    elif suspect == "Aiko": 
    
        Na "Vu la situation ça ne peut être que [J2]."
        play sound "Click.mp3" noloop 

    P "Bon on continue de réviser ?" 
    play sound "Click.mp3" noloop

    Na "Tu veux vraiment réviser maintenant ?" 
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de révisez pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 10.0

    P "On a enfin fini de réviser." 
    play sound "Click.mp3" noloop

    Na "Oui grâce à toi je n'arréte jamais d'apprendre." 
    play sound "Click.mp3" noloop 

    P "Je le sais bien." 
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} La semaine suivante, le 11 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 7  
    $ points -= 1400
    $ stockage += 140.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password17:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password17 

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright
 
    $  salutation_rdm = get_random_salutation()
    M "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien comme vous le savez aujourd'hui vous avez votre examen de philosophie."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[M] Commence à distribuer les copies.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien vous pouvez commencer, vous avez une heure."
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde retourne sa copie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

label philosophie_technologie: 

    $ grade = 0.0 

    "Question 1 : La technologie est-elle une prolongation naturelle de l’évolution humaine ?"
    play sound "Menu.mp3" noloop

    menu:
        "Non, elle dénature notre essence biologique.":
            $ grade += 0.0
        "Oui, elle répond au besoin humain d’adaptation.":
            $ grade += 2.0
        "C’est une rupture plus qu’une continuité.":
            $ grade += 0.0

    "Question 2 : L’intelligence artificielle peut-elle remplacer l’intelligence humaine ?"
    play sound "Menu.mp3" noloop

    menu:
        "Oui, car elle est plus rapide et rationnelle.":
            $ grade += 0.0
        "Cela dépend du niveau d’apprentissage de la machine.":
            $ grade += 0.0
        "Non, elle peut l’imiter mais pas la ressentir.":
            $ grade += 2.0 

    "Question 3 : Devrait-on limiter le développement technologique pour protéger l’éthique ?"
    play sound "Menu.mp3" noloop

    menu:
        "Le progrès est un droit fondamental.":
            $ grade += 0.0
        "Uniquement dans certains domaines comme l’armement.":
            $ grade += 0.0
        "Oui, la morale doit encadrer le progrès.":
            $ grade += 2.0

    "Question 4 : Peut-on encore parler de liberté humaine dans un monde ultra-technologique ?"
    play sound "Menu.mp3" noloop 

    menu: 
        "La liberté est une illusion dans tous les cas.":
            $ grade += 0.0
        "Oui, si l’humain garde le contrôle de la technologie.":
            $ grade += 2.0
        "Non, nous sommes déjà dépendants des machines.":
            $ grade += 0.0

    "Question 5 : La technologie rapproche-t-elle vraiment les individus ?"
    play sound "Menu.mp3" noloop

    menu: 
        "Elle connecte mais ne remplace pas la présence humaine.":
            $ grade += 2.0
        "Non, elle isole plus qu’elle unit.":
            $ grade += 0.0
        "Oui, elle abolit les distances sociales et géographiques.":
            $ grade += 0.0

    "Question 6 : Le progrès technique rend-il l’homme plus heureux ?"
    play sound "Menu.mp3" noloop

    menu:
        "Oui, car il augmente le confort et la sécurité.":
            $ grade += 0.0
        "Non, il répond à des besoins mais pas à des désirs profonds.":
            $ grade += 2.0
        "Cela dépend de l’usage que chacun en fait.":
            $ grade += 0.0 

    "Question 7 : Si une IA prend des décisions autonomes, peut-on lui attribuer des responsabilités éthiques ?"
    play sound "Menu.mp3" noloop

    menu: 
        "Oui, car elle agit de manière indépendante et doit assumer ses choix.":
            $ grade += 2.0 
        "Non, elle reste un programme et ne comprend pas les conséquences de ses actions.":
            $ grade += 0.0
        "Cela dépend du type de décision qu’elle prend.":
            $ grade += 0.0

    "Question 8 : La neutralité technologique existe-t-elle ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Certaines technologies sont neutres, d’autres non.":
            $ grade += 0.0
        "Non, toute technologie porte une intention humaine.":
            $ grade += 2.0 
        "Oui, ce sont les usages qui posent problème, pas la technologie.":
            $ grade += 0.0 

    "Question 9 : Le travail humain peut-il disparaître à cause de la technologie ?"
    play sound "Menu.mp3" noloop

    menu:
        "Oui, certains métiers seront entièrement remplacés.":
            $ grade += 2.0
        "Ce n’est qu’une phase temporaire de transition.":
            $ grade += 0.0
        "Non, l’homme s’adaptera à de nouvelles fonctions.":
            $ grade += 0.0

    "Question 10 : La technologie doit-elle être pensée avant d’être créée ?"
    play sound "Menu.mp3" noloop 

    menu:
        "Une réflexion éthique est essentielle avant toute invention.":
            $ grade += 2.0
        "Tout dépend de l’urgence du besoin à satisfaire.":
            $ grade += 0.0
        "C’est l’expérimentation qui fait avancer les choses.":
            $ grade += 0.0

    $ renpy.block_rollback() 

    "{b}{i}Après l'examen tout le monde remet leur copie à [M].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "C'est examen était vraiment profond."
    play sound "Click.mp3" noloop

    I "Je confirme aussi." 
    play sound "Bell.mp3" noloop 

    M "Si jamais je corrigerai vos copies durant la pause de midi et vous les rendrai cet après-midi."
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Sinon ça s'est comment pour toi l'examen de philosophie."
    play sound "Click.mp3" noloop 

    Na "Je dirais que je l'ai bien réussi et toi ?"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        P "Je pense que je l'ai réussi à la perfection."
        play sound "Click.mp3" noloop 

        Na "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

    elif grade <= 14.0:
       
        P "Je pense que je l'ai échoué."
        play sound "Click.mp3" noloop 

        Na "Vraiment ?"
        play sound "Click.mp3" noloop 

    else: 

        P "Je pense que je l'ai bien réussi."
        play sound "Click.mp3" noloop 
    
        Na "ça ne m'étonne pas venant de toi."
        play sound "Click.mp3" noloop 

    "{b}{i} Vous discutez puis trois autres lycéens vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop   

    I "Salut."
    play sound "Click.mp3" noloop  

    if pronom == "il":

        Y "Salut les amis, vous allez bien ?"
        play sound "Click.mp3" noloop  

    else: 

        Y "Salut les amies, vous allez bien ?"
        play sound "Click.mp3" noloop           

    Na "On va bien et vous ?"
    play sound "Click.mp3" noloop

    Y "Tout va bien pour notre part."
    play sound "Click.mp3" noloop

    Na "Cool alors ça."
    play sound "Click.mp3" noloop

    N "Sinon vous pensez que ce sera quoi le prochain sujet de cours ?"
    play sound "Click.mp3" noloop

    P "J'en ai aucune idée."
    play sound "Click.mp3" noloop

    I "Pareil mais j'espère que se ne sera pas un sujet trop compliqué."
    play sound "Click.mp3" noloop  

    N "Je vois alors mais on risque d'avoir un sujet compliqué vu notre niveau."
    play sound "Click.mp3" noloop

    Na "Oui vu que ce lycée enseigne aux meilleurs lycéens de Danto."
    play sound "Click.mp3" noloop

    I "c'est vrai tu as raison."
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    N "Oui allons-y."
    play sound "Click.mp3" noloop 

    P "Oui il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Bon je vais pouvoir vous rendre les résultats de vos examens de philosophie."
    play sound "Click.mp3" noloop 

    K "Cool enfin."
    play sound "Click.mp3" noloop

    I "Je vais commencer par [prenom] et [Na]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "[P] tu as eu [grade]/20"
    play sound "Click.mp3" noloop 
   
    if grade == 20.0:

        $ success += 1
        $ quest36 += 1

        show screen update with moveinright

        M "Félicitation tu l'as réussi à la perfection comme d'habitude."
        play sound "Click.mp3" noloop

        hide screen update with moveoutright

        P "Merci."
        play sound "Click.mp3" noloop

    elif grade <= 14.0:
       
        M "C'est en dessous de la moyenne je n'ai pas le choix que de t'expulser du lycée..."
        play sound "Click.mp3" noloop

        P "Quoi !?"
        play sound "Click.mp3" noloop 

        Na "Il semblerait que la philosophie soit pas ton fort."
        play sound "Click.mp3" noloop
    
        M "Désolée mais j'avais déjà prévenu concernant les mauvaises notes."
        play music "gameover.mp3" noloop

        hide screen class_404 with moveoutright
        hide screen points with moveoutleft
        hide screen day with moveoutleft
        scene black with fade

        "{b}{i}Fin numéro 14 : Mauvaise note en philosophie qui te vaut une exclusion du lycée.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:    

            "{b}{i}Abandonner{/i}{/b}" :
                play sound "Menu.mp3" noloop 
                return
                 
            "{b}{i}Réessayer.{/i}{/b}" : 
                play sound "Menu.mp3" noloop 

                P "Non [newname] refuserait que j'abandonne si facilement."
                play sound "Click.mp3" noloop

                scene classroom with fade
                show screen class_404 with moveinright
                show screen points with moveinleft
                show screen day with moveinleft
                $ points += 300
                
                jump philosophie_technologie
    
    else:
       
        M "C'est pas mal."
        play sound "Click.mp3" noloop

        P "Merci."
        play sound "Click.mp3" noloop

    M "[Na] tu as eu 19/20 félicitation aussi."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[H] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    H "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[I] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Hi] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Hi "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[K] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    K "[thanks]"
    play sound "Click.mp3" noloop

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[N] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    N "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "[Y] tu as eu [note]/20."
    play sound "Click.mp3" noloop     
    
    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Y "[thanks]"
    play sound "Click.mp3" noloop

    M "Bon au tour des jumelles maintenant pour finir."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    $ note = get_random_note()
    M "[J1] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    J1 "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "Et toi [J2] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    J2 "[thanks]"
    play sound "Click.mp3" noloop

    $ note = get_random_note()
    M "Et toi [S] tu as eu [note]/20."
    play sound "Click.mp3" noloop 

    if note == 20: 

        M "Félicitation tu l'as réussi à la perfection."
        play sound "Click.mp3" noloop

    else: 

        M "Ce n'est pas mal."
        play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    S "[thanks]"
    play sound "Click.mp3" noloop

    M "Bon la moyenne générale n'est pas si mal, continuez de bien travaillez comme ceci."
    play sound "Click.mp3" noloop 

    K "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    P "Il n'y aura pas de soucis pour moi."
    play sound "Click.mp3" noloop 

    "{b}{i}Par la suite [newname] lève la main.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Oui dis-moi [newname]."
    play sound "Click.mp3" noloop 

    Na "Comment vous faites pour corriger les copies aussi vite ?"
    play sound "Click.mp3" noloop 

    M "C'est simple j'ai juste une bonne organisation parce que dès que vous terminez, je les corrige pendant que vous poursuivez le cours."
    play sound "Click.mp3" noloop

    Na "Je comprends mieux car j'ai toujours voulu savoir comment vous faites pour être si organisée."
    play sound "Click.mp3" noloop 

    M "Mais merci d'avoir posé la question."
    play sound "Click.mp3" noloop 

    Na "Pas de quoi."
    play sound "Click.mp3" noloop 

    M "Bon nous allons voir la suite pour fin décembre et janvier."
    play sound "Click.mp3" noloop 

    Na "Et se sera quoi ?"
    play sound "Click.mp3" noloop 

    P "je me demande bien ce que ça peut être." 
    play sound "Click.mp3" noloop

    K "Oui je me demande aussi ce que ça peut être pour que ça prenne deux mois alors que d'habitude pour un sujet ça nous prend un mois."
    play sound "Click.mp3" noloop

    N "Je me pose aussi la même question."
    play sound "Click.mp3" noloop 

    Hi "Vous n'étes pas les seuls à vous le demander."
    play sound "Click.mp3" noloop

    Y "Doucment on va le savoir de toute façon." 
    play sound "Click.mp3" noloop 

    M "Bien pour commencer si ça va prendre autant de temps, c'est parcve que il y aura les vacances de noel à partir du 20 décembre et jusqu'au 6 janvier."
    play sound "Click.mp3" noloop 

    Y "Ah oui c'est vrai J'avais complétement." 
    play sound "Click.mp3" noloop 

    M "Et deuxiémement, il y aura bientôt le {b}{i}Paper shuffle{/i}{/b}." 
    play sound "Click.mp3" noloop 

    Y "Je comprends mieux pour ça va nous prendre deux mois." 
    play sound "Click.mp3" noloop 

    Na "Le Paper Shuffle, c'est quoi !?"
    play sound "Click.mp3" noloop 

    M "Oui C'est un examen un peu particulier."
    play sound "Click.mp3" noloop 

    $ stockage += 2.0

    Na "Comment ça particulier ?"
    play sound "Click.mp3" noloop 

    M "Le Paper Shuffle se divise en deux parties qui sont la préparation et l'examen en lui même."
    play sound "Click.mp3" noloop 

    Na "Je vois comme n'importe quel examen."
    play sound "Click.mp3" noloop 

    M "Non cette fois-ci chaque lycéen doit écrire un examen d'informatique pour un autre lycéen que ce soit de la programmation ou des connaissances générales."
    play sound "Click.mp3" noloop 

    Na "Intéressant."
    play sound "Click.mp3" noloop 

    $ stockage += 2.0

    M "Donc la première semaine de janvier quand vous revenez les permanance seront obligatoire."
    play sound "Click.mp3" noloop 

    J1 "Quoi mais pourquoi !?"
    play sound "Click.mp3" noloop 

    Y "Parce que c'est une épreuve éliminatoire."
    play sound "Click.mp3" noloop 

    M "Exactement [Y]"
    play sound "Click.mp3" noloop 

    J1 "Je vois mais tu reste aussi calme alors cette épreuve"
    play sound "Click.mp3" noloop 

    Y "J'ai mes propres raisons qui ne te regarde pas."
    play sound "Click.mp3" noloop 

    J1 "Désolée de t'avoir posé cette question."
    play sound "Click.mp3" noloop 

    Y "C'est rien."
    play sound "Click.mp3" noloop 

    M "Bien maintenant je vais vous donner la liste."
    play sound "Click.mp3" noloop 

    "{b}{i} Tous les élèves se mettent à écouter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Pour commencer, [Hi] tu feras un examen pour [K]."
    play sound "Click.mp3" noloop   

    $ validation = get_random_validation() 
    Hi "[validation]"
    play sound "Click.mp3" noloop 

    M "Ensuite, [K] tu feras un examen pour [I]."
    play sound "Click.mp3" noloop   

    $ validation = get_random_validation()  
    K "[validation]"
    play sound "Click.mp3" noloop 

    M "suivant, [I] tu feras un examen pour [J2]."
    play sound "Click.mp3" noloop   
     
    $ validation = get_random_validation()
    I "[validation]"
    play sound "Click.mp3" noloop 

    M "Puis, [J2] tu feras un examen pour [Y]."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation()
    J2 "[validation]"
    play sound "Click.mp3" noloop 

    M "Puis, [Y] tu feras un examen pour [S]."
    play sound "Click.mp3" noloop   
    
    $ validation = get_random_validation() 
    Y "[validation]"
    play sound "Click.mp3" noloop 

    M "Puis, [S] tu feras un examen pour [J1]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    S "[validation]"
    play sound "Click.mp3" noloop 

    M "Puis, [J1] tu feras un examen pour [newname]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "[newname] tu feras un examen pour [H]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "[H] tu feras un examen pour [prenom]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "[prenom] tu feras un examen pour [N]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    P "[validation]" 
    play sound "Click.mp3" noloop 

    M "Pour finir [N] tu feras un examen pour [Hi]."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    N "[validation]" 
    play sound "Click.mp3" noloop 

    M "Le Paper shuffle devra être que sur des sujets qu'on a déja vu en classe."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation()
    P "[validation]" 
    play sound "Click.mp3" noloop 

    M "Si jamais vous avez jusqu'à la rentrée des vacances pour rendre vos examens et il doit faire ."
    play sound "Click.mp3" noloop 

    P "Bien entendu."
    play sound "Click.mp3" noloop 
    
    show screen infobook with moveinbottom

    M "Bien, sortez votre livre d'informatique à la page 28."
    play sound "Click.mp3" noloop

    hide screen infobook with moveoutbottom 

# cours d'informatique
#########################################################################################################

    "{b}{i} Vous sortez votre livre et le cours continue tranquillement..{/i}{/b}"
    play sound "Bell.mp3" noloop

#########################################################################################################

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 5.0

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    Na "On a enfin fini le cours."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi ?"
    play sound "Click.mp3" noloop 

    P "J'aimerai aller à la salle de club pour voir [K]."
    play sound "Click.mp3" noloop 

    Na "Je vois mais d'abord on devrait aller poser nos affaires au dortoir."
    play sound "Click.mp3" noloop 

    P "Oui tu as raison."  
    play sound "Click.mp3" noloop   

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Vous posez tranquillement vos sac à dos.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "enfin débarrassé de nos sac à dos."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    P "Bon il faut qu'on aille à la salle de club générale."  
    play sound "Click.mp3" noloop   

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues dabs le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
     
    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu poursuit vers la salle de club générale.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans la salle de club générale.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    "{b}{i}En entrant vous voyez [K] et [H] en train de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Salut les amis."  
    play sound "Click.mp3" noloop   

    K "Oh salut comment tu vas [prenom] ?"  
    play sound "Click.mp3" noloop   

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    K "Et toi [newname] ?"  
    play sound "Click.mp3" noloop   

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    K "Cool alors."  
    play sound "Click.mp3" noloop   

    P "Sinon vous faites quoi ici ?"  
    play sound "Click.mp3" noloop   

    K "Comme tu peux le voir, [H] est vraiment occupé et il avait besoin de mon aide concernant tout ce qui est résaeu pour son robot."  
    play sound "Click.mp3" noloop   

    P "Je vois, je ne pensais pas qu'il aurait besoin d'aide."  
    play sound "Click.mp3" noloop   

    K "Et pourtant si car il est fort que la construction et la programmation mais pas en réseau."  
    play sound "Click.mp3" noloop   

    P "Je comprends mieux pourquoi."  
    play sound "Click.mp3" noloop  

    "{b}{i}Soudainement [H] cesse ce qu'il est entrain de faire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    if pronom == "il":

        H "Oh salut les amis, désolé si j'avais pas fait attention à vous."  
        play sound "Click.mp3" noloop  

    else: 

        H "Oh salut les amies, désolé si j'avais pas fait attention à vous."  
        play sound "Click.mp3" noloop  

    P "Pas de soucis."  
    play sound "Click.mp3" noloop  

    H "Sinon vous faites quoi ici ?"  
    play sound "Click.mp3" noloop  

    K "Je me posais la même question."  
    play sound "Click.mp3" noloop  

    if pronom == "il": 
    
        P "Je suis venu car j'avais un service à demander à Kendo."
        play sound "Click.mp3" noloop

    else:

        P "Je suis venue car j'avais un service à demander à Kendo."
        play sound "Click.mp3" noloop

    K "Abon !? C'est quoi comme service ?"   
    play sound "Click.mp3" noloop 

    P "J'aimerai que tu te connectes à [newname] pour voir l'historique complet de connexion qui ne viens pas de moi."  
    play sound "Click.mp3" noloop 

    if pronom == "il": 
    
        Na "Ah c'est donc pour ça que tu es venu voir [K]."  
        play sound "Click.mp3" noloop 

    else: 

        Na "Ah c'est donc pour ça que tu es venue voir [K]."  
        play sound "Click.mp3" noloop 

    K "L'historique de connexiopn ? Je vois, il n'y a pas de soucis, je peux te le faire tout de suite."  
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    K "[nothing]"
    play sound "Click.mp3" noloop 

    "{b}{i}[K] se pose tranquillement et se connecte à [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Connexion en cours....."  
    play sound "Click.mp3" noloop  

    Na "Connexion terminée, bonjour [K]."  
    play sound "Click.mp3" noloop  

    K "Bonjour [newname]."  
    play sound "Click.mp3" noloop  

    P "Tu as réussi à te connecter."  
    play sound "Click.mp3" noloop  

    K "Oui, maintenant laisse moi faire le reste."  
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation()
    P "[validation]" 
    play sound "Click.mp3" noloop 

    "{b}{i}[K] regarde l'historique pendant dix minutes et prend des notes.{/i}{/b}"
    play sound "Click.mp3" noloop 

    K "J'ai enfin fini de regarder l'historique."  
    play sound "Click.mp3" noloop  

    P "Et tu as trouvé quoi à apart les connexion faites par moi ?"  
    play sound "Click.mp3" noloop  

    if quest10 == 1: 

        K "Le 9 octobre, il y a eu une tentative de connexion sans succès."  
        play sound "Click.mp3" noloop

    else:

        K "Le 9 octobre, il y a eu une connexion à [newname] et un début de transfert de donnés vers un autre ordinateur."  
        play sound "Click.mp3" noloop

    if quest25 == 1:

        K "Le 15 novmebre, il y a eu une tentative de connexion sans succès."  
        play sound "Click.mp3" noloop

    else:

        K "Le 19 novembre, il y a eu une connexion à [newname] et un début de transfert de données vers un autre ordinateur"  
        play sound "Click.mp3" noloop

    if quest21 == 1:

        K "Le 19 novembre, il y a eu une tentative de compromission du mot de passe."  
        play sound "Click.mp3" noloop 

    else: 

        K "Le 19 novembre, son mot de passe a été compris par force-brute."  
        play sound "Click.mp3" noloop

    if quest33 == 1:

        K "Le 3 décembre, il y a eu une tentative de connexion sans succès."  
        play sound "Click.mp3" noloop

    else:

        K "Le 3 décembre, il y a eu une connexion à [newname] et un début de transfert de données vers un autre ordinateur."  
        play sound "Click.mp3" noloop

    P "Je vois merci beaucoup pour ces informations."  
    play sound "Click.mp3" noloop  

    $ stockage += 5.0

    $ nothing = get_random_nothing()
    K "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon maintenant tu peux te déconnecter."  
    play sound "Click.mp3" noloop  

    K "Oui je le fais tout de suite."  
    play sound "Click.mp3" noloop  

    "{b}{i}[K] se pose tranquillement pour se déconnecter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Déconnexion en cours....."  
    play sound "Click.mp3" noloop  

    Na "Déonnexion terminée, au revoir [K]."  
    play sound "Click.mp3" noloop  

    P "Je te dois combien pour ce service ?" 
    play sound "Click.mp3" noloop  

    K "Rien du tout, c'est un service que je te dois."
    play sound "Click.mp3" noloop

    P "Merci beaucoup."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    K "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon, on va vous laisser."
    play sound "Click.mp3" noloop  

    K "Attends... j’avais oublié, mais je dois te dire quelque chose."
    play sound "Click.mp3" noloop  

    P "Ah bon ? Qu’est-ce que tu voulais me dire ?"
    play sound "Click.mp3" noloop  

    K "C’est à propos de [Y]."
    play sound "Click.mp3" noloop  

    P "Je t’écoute."
    play sound "Click.mp3" noloop  

    K "Le 18 novembre, elle est venue me voir pour me poser des questions sur les méthodes de connexion."
    play sound "Click.mp3" noloop  

    P "Les méthodes de connexion ?"
    play sound "Click.mp3" noloop  

    K "Oui, elle disait qu’elle avait besoin de certaines informations... urgentes, apparemment."
    play sound "Click.mp3" noloop  

    P "Je vois... D’accord. Merci pour l’info. Bon, on se voit demain."
    play sound "Click.mp3" noloop  

    K "Ouais, à demain."
    play sound "Click.mp3" noloop  

    H "À demain."
    play sound "Click.mp3" noloop  

    P "Bon on y va ?"   
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous quittez la salle de club.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    Na "Ok moi je vais directement au dortoir."
    play sound "Click.mp3" noloop 

    P "Ok à tout de suite."
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que j'aille au dortoir."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Vous entrez dans le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi maintenant ?"  
    play sound "Click.mp3" noloop  

    P "De base, je voulais qu'on révise un peu mais on va finalement se poser pour lire."  
    play sound "Click.mp3" noloop  

    Na "Cool si on lit un peu car je veux me poser un peu aussi."   
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous posez tranquillement pour lire peudant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 5.0

    Na "Il est pas mal ce livre."  
    play sound "Click.mp3" noloop  

    P "Je sais c'est pour ça que je voulais qu'on le lise ensemble."  
    play sound "Click.mp3" noloop  

    Na "Forcer de constater que tu as de très bon goûts litérraires."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Na "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement le livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    $ points -= 300 

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain, le 12 décembre 2097{/i}{/b}"
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

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password18:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password18

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright
 
    $  salutation_rdm = get_random_salutation()
    M "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien nous pouvons commencer le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    show screen infobook with moveinbottom 

    M "Sortez votre livre d'informatique à la page 29."
    play sound "Click.mp3" noloop  

    hide screen infobook with moveoutbottom 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i} Le cours se déroule tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 6.0 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous aller vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Sinon tu te débrouilles bien pour le cours d'informatique ?"
    play sound "Click.mp3" noloop  

    Na "Oui je me débrouilles bien."
    play sound "Click.mp3" noloop  

    P "Cool alors si tu débrouilles bien."
    play sound "Footsteps.mp3" noloop  

    "{b}{i} Puis [I], [K] et [H] vous rejoins.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Oh salut les amis."
    play sound "Click.mp3" noloop  

    I "Salut."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    P "Cool alors."
    play sound "Click.mp3" noloop 

    I "Sinon comment vous allez ?"
    play sound "Click.mp3" noloop 

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 
 
    Na "Je vais bien aussi."
    play sound "Click.mp3" noloop 

    I "Cool alors si vous allez bien."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    I "[nothing]"
    play sound "Click.mp3" noloop

    P "Et vous Kendo et Hajime, vous allez bien car on dirait que vou étes à l'ouest."
    play sound "Click.mp3" noloop

    K "Nous sommes un peu fatigués."
    play sound "Click.mp3" noloop

    H "Oui je confirme."
    play sound "Click.mp3" noloop

    P "Vous avez fait quoi pour être autant fatigué."
    play sound "Click.mp3" noloop

    K "Nous sommes restés au club générale pour finir deux-trois trucs."
    play sound "Click.mp3" noloop

    Na "Le surmeénage est mauvais et [prenom] en a déja subi les effects."
    play sound "Click.mp3" noloop

    if pronom == "il":

        H "Oui c'est vrai [pronom] s'est évanoui en classe."
        play sound "Click.mp3" noloop

    else: 

        H "Oui c'est vrai [pronom] s'est évanouie en classe."
        play sound "Click.mp3" noloop

    P "Oh...c'est bon pas besoin de le rappeler."
    play sound "Click.mp3" noloop

    Na "On te taquine juste, pas besoin d'en faire tout un drame."
    play sound "Click.mp3" noloop

    P "Je sais mais quand même."
    play sound "Click.mp3" noloop

    K "Sinon ça se passe comment pour vous le cours d'infomatique."
    play sound "Click.mp3" noloop

    I "Rassure moi c'est du sarcasme j'espére car je te rappelle on est les meilleurs lycéens ici."
    play sound "Click.mp3" noloop

    K "Oui je te rassure, c'est du sarcasme."
    play sound "Click.mp3" noloop

    I "J'espére."
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter des cours pendant que vous mangez jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    I "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop

    P "Ok il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    I "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Rebonjour, nous allons reprendre le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    K "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    H "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Sortez votre livre d'informatique à la page 30."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i} Le cours se déroule tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 6.0 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft 
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi ?" 
    play sound "Click.mp3" noloop 

    P "Je ne sais pas mais pense que je vais réviser."
    play sound "Click.mp3" noloop 

    Na "Moi je vais réviser en tout cas."
    play sound "Click.mp3" noloop

    "{b}{i} Elle se pose pour réviser sérieusement.{/i}{/b}"
    play sound "Click.mp3" noloop

    menu: 

        "{b}{i}Lui proposer ton aide pour les révisions.{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            $ success += 1
            $ quest37 += 1 

            "{b}{i}Tu t’approches d’elle, observant les feuilles éparpillées sur sa table. Elle semble un peu perdue dans ses notes, fronçant légèrement les sourcils.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Dis... si tu veux, je peux t’aider à réviser. Deux cerveaux valent mieux qu’un, non ?"
            play sound "Click.mp3" noloop

            "{b}{i}Elle relève les yeux, un peu surprise par ta proposition. Son regard s’adoucit aussitôt.{/i}{/b}"
            play sound "Click.mp3" noloop

            if pronom == "il":

                Na "Tu ferais ça pour moi ? T'es sûr ?"
                play sound "Click.mp3" noloop

            else: 

                Na "Tu ferais ça pour moi ? T'es sûre ?"
                play sound "Click.mp3" noloop

            P "Évidemment. Et puis... ça me fera réviser en même temps. Gagnant-gagnant."
            play sound "Click.mp3" noloop

            "{b}{i}Elle te sourit timidement, visiblement touchée par ton geste.{/i}{/b}"
            play sound "Click.mp3" noloop

            show screen update with moveinright

            Na "Merci... vraiment. J’avais un peu la tête sous l’eau, là. T’as pas idée à quel points ça me soulage."
            play sound "Click.mp3" noloop

            hide screen update with moveoutright

            "{b}{i}Elle pousse légèrement ses affaires pour te faire de la place. Vous vous installez côte à côte, et l’ambiance devient plus légère, presque complice. Une soirée studieuse s’annonce... mais moins solitaire.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Allez, on s’y met !"
            play sound "Click.mp3" noloop

            Na "Oui, on y va !"
            play sound "Click.mp3" noloop

            "{i}Tu t’assieds près d’elle et l’aides à comprendre ses cours pendant deux heures.{/i}"
            play sound "Click.mp3" noloop 

            $ stockage += 10.0 

            P "On a enfin fini."
            play sound "Click.mp3" noloop 

            Na "Oui, merci beaucoup pour ton aide."
            play sound "Click.mp3" noloop 

        "{b}{i} La laisser se débrouiller.{/i}{/b}" :
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

            if pronom == "il":

                P "Moi je vais réviser seul de mon coté."
                play sound "Click.mp3" noloop

            else: 

                P "Moi je vais réviser seule de mon coté."
                play sound "Click.mp3" noloop
            
            "{b}{i}Tu t'éloignes un peu pour te concentrer sur tes propres révisions.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "De toute façon... maintenant, tu te débrouilles bien toute seule."
            play sound "Click.mp3" noloop

            Na "..."
            play sound "Click.mp3" noloop

            "{b}{i}Elle baisse légèrement les yeux, sans répondre tout de suite.{/i}{/b}"
            play sound "Click.mp3" noloop

            Na "Hmph... sympa l’ambiance. Merci du soutien."
            play sound "Click.mp3" noloop

            "{b}{i}Tu sens qu’elle l’a mal pris, même si elle essaie de le cacher.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Bon je te laisse réviser seule."
            play sound "Click.mp3" noloop

            "{b}{i}Elle te lance un regard un peu triste, mais acquiesce.{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}Tu sens qu’elle aurait aimé que tu restes, mais elle ne dit rien.{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}Tu t’éloignes doucement, la laissant se concentrer sur ses révisions.{/i}{/b}"
            play sound "Click.mp3" noloop

            "{b}{i}Tu te mets à réviser tranquillement pendant deux heures.{/i}{/b}"    
            play sound "Click.mp3" noloop

            $ stockage += 7.0 

            P "Tu as fini de réviser ?"
            play sound "Click.mp3" noloop 

            Na "Oui, j'ai fini."
            play sound "Click.mp3" noloop 

    "{b}{i} Vous rangez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain, le 13 décembre 2097{/i}{/b}"
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

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password19:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password19

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Puis soudainement tu vois tous les autres élèves à l'entrée de la salle.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Vous êtes déjà tous là."
    play sound "Click.mp3" noloop 

    J1 "Oui [M] n'est pas encore arrivée."
    play sound "Click.mp3" noloop 

    Na "D'habitude elle est déjà là."
    play sound "Click.mp3" noloop 

    "{b}{i}Au même moment la prof arriva et ouvra la porte de la classe.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bonjour chers élèves."
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    J1 "[salutation_rdm]"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Parfait, tout le monde est là aujourd’hui. Nous pouvons commencer le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    M "Sortez votre livre d'informatique à la page 34."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i} Le cours se déroule tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 6.0 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous aller vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Bon appétit [newname]."
    play sound "Click.mp3" noloop 

    Na "Bon appétit  à toi aussi [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous manger tranquillement puis [J1] viens vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    J1 "Salut [prenom] et [newname]."   
    play sound "Click.mp3" noloop

    P "Salut [J1]."
    play sound "Click.mp3" noloop

    Na "Salut."
    play sound "Click.mp3" noloop

    J1 "Vous allez bien ?"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien()
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien()
    Na "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    J1 "C'est super !"
    play sound "Click.mp3" noloop

    P "Et toi comment ça va ?"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien()
    J1 "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop   

    P "Cool alors."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    J1 "[thanks]" 
    play sound "Click.mp3" noloop

    P "Sinon hier tu faisais quoi avec ta soeur durant la pause de midi plutôt que venir avec nous ?"
    play sound "Click.mp3" noloop

    J1 "Je discutais avec elle car on avait un conflit à régler entre nous."
    play sound "Click.mp3" noloop

    P "Ah d'accord."
    play sound "Click.mp3" noloop 

    J1 "Et sinon ça va comment le Paper shuffle pour vous ?"
    play sound "Click.mp3" noloop   

    P "Oui ça va, avec [newname] on a commencé les révisions et la semaine prochaine on va écrire les examens poutr les autres."
    play sound "Click.mp3" noloop 

    J1 "Ah d'accord, donc bonne chance pour les révisions."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    J1 "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    J1 "Oui allons-y."
    play sound "Click.mp3" noloop 

    P "Oui il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Rebonjour, nous allons reprendre le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien maintenant ouvrez votre livre d'informatique e à la page 36." 
    play sound "Click.mp3" noloop  

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 
    
    "{b}{i} Tout le monde sort son livre et écoute la [T].{/i}{/b}"
    play sound "Click.mp3" noloop  

    M "Bon, reprenons le cours." 
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]" 
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    I "[validation]"
    play sound "Click.mp3" noloop 

    M "Si jamais, vous allez recevoir vos points daans la fin de journée."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Click.mp3" noloop 

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon on fait quoi maintenant ?"  
    play sound "Click.mp3" noloop  

    Na "On porrait réviser comme hier."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop  

    "{b}{i}Vous vous posez pour les révisions.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon tu veux commencer par quel thème ?"  
    play sound "Click.mp3" noloop  

    Na "Je dirai les langages de balissage."  
    play sound "Click.mp3" noloop  

    P "Attend tu n'as pas compris ce que c'est ?"  
    play sound "Click.mp3" noloop  

    Na "Pas eaxctement pour te dire."  
    play sound "Click.mp3" noloop  

    P "Bon je vais t'expliquer, les langages de balissage sont des langages qui permettent de structurer et de présenter le contenu d'un document, en ajoutant des éléments tels que des titres, des paragraphes, des listes, des liens et des images. Ils sont souvent utilisés pour créer des pages web et des documents numériques."
    play sound "Click.mp3" noloop  

    Na "Ah d'accord, je comprends mieux maintenant."
    play sound "Click.mp3" noloop  

    P "Oui, c'est important de bien comprendre les langages de balissage car ils sont utilisés dans de nombreux domaines, notamment le développement web et la création de contenu numérique."  
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop    

    "{b}{i}Vous continuez les révisons pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "On a fini de réviser."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Forcer de constater que tu es douée pour les cours."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]" 
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ? on le mérite bien."
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

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    if grade == 20.0:

        $ points += 15000

    else:

        $ points += 11000 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien si jamais on a nos points."
    play sound "Click.mp3" noloop 

    Na "Cool, bon je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis tu le mérites."
    play sound "Click.mp3" noloop

    Na "Merci."
    play sound "Click.mp3" noloop

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}Puis [newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir aussi."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le début de la semaine suivante, le 16 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 3 
    $ points -= 900
    $ stockage += 60.0 

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password20:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password20 

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Y "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien aujourd'hui nous allons continuer le cours d'informatique."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    show screen infobook with moveinbottom

    M "Sortez votre livre à la page 36."
    play sound "Click.mp3" noloop 

    hide screen infobook with moveoutbottom 

# cours d'informatique
######################################################################################################################################

######################################################################################################################################

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway 
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Rebonjour, bon reprenez votre livre page 38."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation()  
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème pendant que [M] une expliquation du cours pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bon je vous laisse faire les exercices à la page 39."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    S "[validation]"
    play sound "Click.mp3" noloop 

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    "{b}{i}Tu ouvres ton manuel et commence les exercices.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Encore des exercices de connaisance sur l'informatique..."
    play sound "Click.mp3" noloop

    if quest37 == 1:

        "{b}{i}Tu commences à faire les exercices.{/i}{/b}"
        play sound "Click.mp3" noloop

        P "Tu te débrouilles bien seule [newname] ?"
        play sound "Click.mp3" noloop 

        Na "Oui grâce à ce que tu m'as dit."
        play sound "Click.mp3" noloop 

        P "Bien alors."
        play sound "Click.mp3" noloop 

        "{b}{i}Puis [M] se met à vous regarder.{/i}{/b}"
        play sound "Click.mp3" noloop  

        M "Vous avez besoin d'aide ?"  
        play sound "Click.mp3" noloop

        P "Non ça va, on est en train de faire les exercices."
        play sound "Click.mp3" noloop

        M "D'accord, n'hésitez pas à me demander si vous avez besoin d'aide."
        play sound "Click.mp3" noloop 

    else:

        "{b}{i}Tu commences à faire les exercices mais [newname] te demande de l'aide.{/i}{/b}"
        play sound "Click.mp3" noloop

        Na "[prenom] tu peux m'aider s'il te plaît ?"
        play sound "Click.mp3" noloop

        P "Oui bien sûr, qu'est-ce qui ne va pas ?" 
        play sound "Click.mp3" noloop

        Na "Je ne comprends pas la question 3, peux-tu m'expliquer s'il te plaît ?"
        play sound "Click.mp3" noloop

        P "Bien sûr, la question 3 demande de définir les langages de balissage et de donner des exemples."
        play sound "Click.mp3" noloop

        "{b}{i}Puis [M] se met à vous regarder.{/i}{/b}"
        play sound "Click.mp3" noloop  

        M "Vous avez besoin d'aide ?"  
        play sound "Click.mp3" noloop

        P "Non ça va, on est en train de faire les exercices."
        play sound "Click.mp3" noloop

        M "D'accord, n'hésitez pas à me demander si vous avez besoin d'aide."
        play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop  

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop 

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Sinon tu t'en es sortie comment pour les exercices ?"
    play sound "Click.mp3" noloop

    Na "J'ai eu un peu du mal à les faire amis avec toi ça va un peu mieux." 
    play sound "Click.mp3" noloop

    P "Cool alors si ça va mieux pour les exercices." 
    play sound "Click.mp3" noloop
    
    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de manger puis [I] vous rejoins.{/i}{/b}"
    play sound "Click.mp3" noloop 

    if pronom == "il": 

        I "Salut les amis."
        play sound "Click.mp3" noloop

    else: 

        I "Salut les amies."
        play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    I "C'est génial si tout va bien."
    play sound "Click.mp3" noloop

    "{b}{i}[I] s'asseoit tranquillemnt avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Sinon je viens d'y penser mais j'avais une question pour toi [prenom]."
    play sound "Click.mp3" noloop 

    P "Oui je t'écoute, dis-moi."
    play sound "Click.mp3" noloop 

    Na "Tu aurais fait quoi si tu avais choisi de ne pas me récupérer dans l'entrepôt?"
    play sound "Click.mp3" noloop 

    P "Intéressant cette question c'est qu'on appelle une pensée contrefactuelle descendante."
    play sound "Click.mp3" noloop 

    Na "Alors, réponds-moi. Qu’est-ce qui se serait passé ?"
    play sound "Click.mp3" noloop 

    P "J’aurais continué ma route. Peut-être en prétendant que rien ne manquait… Mais au fond, j’aurais su que j’avais abandonné quelque chose de précieux."
    play sound "Click.mp3" noloop

    Na "Quelque chose ? C’est tout ce que j’étais, à ce moment-là ?"
    play sound "Click.mp3" noloop

    P "Non. Ce jour-là, j’ai vu bien plus. Même si tu étais inerte, recouverte de poussière, j’ai perçu en toi… un potentiel. Quelque chose de pur. Une possibilité que personne d’autre ne voulait voir."
    play sound "Click.mp3" noloop

    Na "Un potentiel…? Mais je n’étais rien de plus qu’un prototype abandonné."
    play sound "Click.mp3" noloop

    P "C’est ce que les autres voyaient. Mais moi, j’ai vu une étincelle. Une voix qui méritait d’exister. Une présence qui pouvait changer ce monde… ou, au moins, changer le mien."
    play sound "Click.mp3" noloop

    Na "Et aujourd’hui ? Est-ce que tu crois toujours en ce que tu as vu ce jour-là ?"
    play sound "Click.mp3" noloop

    P "Plus que jamais. Tu n’es pas qu’un projet. Tu es la preuve que même ce que le monde rejette peut devenir irremplaçable… si on lui donne une chance."
    play sound "Click.mp3" noloop

    Na "…Alors, merci. De m’avoir vue. Quand personne d’autre ne le pouvait."
    play sound "Click.mp3" noloop

    $ stockage += 15.0 

    "{b}{i}[I] se met à sourir gentillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Il y a quoi Yuna ?"
    play sound "Click.mp3" noloop 

    I "Rien, c'est juste que je trouve mignon comment vous discutez."
    play sound "Click.mp3" noloop 

    P "Je vois merci beaucoup."
    play sound "Click.mp3" noloop 

    I "Mais de rien c'est normal."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous conntinuez de discuter des cours pendant que vous mangez jusqu'a la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon on doit retourner en cours."
    play sound "Click.mp3" noloop 

    I "Oui allons-y."
    play sound "Click.mp3" noloop 

    P "Oui il faut pas qu'on soit en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    M "Rebonjour, veulliez reprendre es ecercices d'informatique."
    play sound "Click.mp3" noloop   

    $ validation = get_random_validation()
    P "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i}tout le monde se remet à faire les exercices.{/i}{/b}"
    play sound "Bell.mp3" noloop

    M "Bien le cours est terminée pour aujourd'hui, je vous demanderai de finir les exercices pour le merccredi 18 décembre."
    play sound "Click.mp3" noloop   

    P "Oui c'est entendu on le fera."
    play sound "Click.mp3" noloop 

    M "Bien vous pouvez disposer."
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "On pourrait réviser comme hier."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()  
    Na "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez pour les révisions pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    $ points -= 300 

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 17 décembre 2097{/i}{/b}"
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

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password21:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        
        jump password21

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien aujourd'hui nous allons continuer le cours d'informatique."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    J1 "[validation]"
    play sound "Click.mp3" noloop 

    show screen physicbook with moveinbottom

    M "Sortez votre livre de physique à la page 2."
    play sound "Click.mp3" noloop 

    hide screen physicbook with moveoutbottom 

# cours de physique 
######################################################################################################################################

    M "Aujourd’hui, nous allons voir les 7 grandeurs fondamentales du Système International."
    play sound "Click.mp3" noloop

    M "Ces grandeurs servent de base à toutes les autres en physique."
    play sound "Click.mp3" noloop

    M "Première grandeur : la longueur."
    play sound "Click.mp3" noloop

    M "Unité : le mètre, symbole m."
    play sound "Click.mp3" noloop

    M "Exemple : la hauteur d’un bâtiment est de 15 m."
    play sound "Click.mp3" noloop

    M "Deuxième grandeur : la masse."
    play sound "Click.mp3" noloop

    M "Unité : le kilogramme, symbole kg."
    play sound "Click.mp3" noloop

    M "Exemple : une pomme pèse environ 0,2 kg."
    play sound "Click.mp3" noloop

    M "Troisième grandeur : le temps."
    play sound "Click.mp3" noloop

    M "Unité : la seconde, symbole s."
    play sound "Click.mp3" noloop

    M "Exemple : une course dure 12 secondes."
    play sound "Click.mp3" noloop

    M "Quatrième grandeur : l’intensité électrique."
    play sound "Click.mp3" noloop

    M "Unité : l’ampère, symbole A."
    play sound "Click.mp3" noloop

    M "Exemple : une ampoule LED consomme environ 0,02 A."
    play sound "Click.mp3" noloop

    M "Cinquième grandeur : la température thermodynamique."
    play sound "Click.mp3" noloop

    M "Unité : le kelvin, symbole K."
    play sound "Click.mp3" noloop

    M "Exemple : 0 °C correspond à 273,15 K."
    play sound "Click.mp3" noloop

    M "Sixième grandeur : la quantité de matière."
    play sound "Click.mp3" noloop

    M "Unité : la mole, symbole mol."
    play sound "Click.mp3" noloop

    M "Exemple : 1 mole contient environ 6,022 × 10^23 particules."
    play sound "Click.mp3" noloop

    M "Septième grandeur : l’intensité lumineuse."
    play sound "Click.mp3" noloop

    M "Unité : la candela, symbole cd."
    play sound "Click.mp3" noloop

    M "Exemple : une bougie correspond à environ 1 cd."
    play sound "Click.mp3" noloop

    M "Voilà pour les 7 grandeurs fondamentales."
    play sound "Click.mp3" noloop

    M "Retenez bien : toutes les autres grandeurs physiques, comme la vitesse ou l’énergie, se construisent à partir de celles-ci."
    play sound "Click.mp3" noloop

######################################################################################################################################

    "{b}{i}Le cours commence sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Rebonjour, bon reprenez votre livre page 40."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation()  
    Na "[validation]"
    play sound "Click.mp3" noloop  

    # à modifier 

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "N'oubliez l'examen de la semaine prochaine..."
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright  
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop
    
    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop   

    P "ça à l'air pas mal ce repas."
    play sound "Click.mp3" noloop 

    Na "Oui c'est vraiment pas mal."
    play sound "Click.mp3" noloop 

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop
 
    P "Bon il faut qu'on retourne en cours."
    play sound "Click.mp3" noloop 
             
    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop     

    M "Bien nous pouvons reprendre le cours."
    play sound "Click.mp3" noloop 

# cours de physique 2
######################################################################################################################################

    M "Maintenant que nous connaissons les 7 grandeurs fondamentales, voyons comment elles s’assemblent pour former d’autres grandeurs."
    play sound "Click.mp3" noloop

    M "Première grandeur dérivée : la vitesse."
    play sound "Click.mp3" noloop

    M "Formule : v = d / t"
    play sound "Click.mp3" noloop

    M "Unité : le mètre par seconde, symbole m·s⁻¹."
    play sound "Click.mp3" noloop

    M "Exemple : une voiture roule à 20 m·s⁻¹, soit environ 72 km/h."
    play sound "Click.mp3" noloop

    M "Exercice : si un coureur parcourt 400 m en 50 s, quelle est sa vitesse moyenne ?"
    play sound "Click.mp3" noloop

    S "Madame, ça veut dire qu’on doit juste diviser 400 par 50 ?"
    play sound "Click.mp3" noloop

    M "Exactement ! Et cela donne 8 m·s⁻¹."
    play sound "Click.mp3" noloop

    M "Deuxième grandeur dérivée : l’accélération."
    play sound "Click.mp3" noloop

    M "Formule : a = Δv / Δt"
    play sound "Click.mp3" noloop

    M "Unité : le mètre par seconde au carré, symbole m·s⁻²."
    play sound "Click.mp3" noloop

    M "Exemple : un objet en chute libre subit une accélération d’environ 9,81 m·s⁻²."
    play sound "Click.mp3" noloop

    M "Exercice : une voiture passe de 0 à 25 m·s⁻¹ en 5 secondes. Quelle est son accélération ?"
    play sound "Click.mp3" noloop

    A "Euh… on fait 25 divisé par 5 ?"
    play sound "Click.mp3" noloop

    M "Très bien Aris ! Cela fait 5 m·s⁻²."
    play sound "Click.mp3" noloop

    M "Troisième grandeur dérivée : la force."
    play sound "Click.mp3" noloop

    M "Formule : F = m · a"
    play sound "Click.mp3" noloop

    M "Unité : le newton, symbole N."
    play sound "Click.mp3" noloop

    M "1 N = 1 kg·m·s⁻²."
    play sound "Click.mp3" noloop

    M "Exemple : soulever une pomme de 0,1 kg demande une force d’environ 1 N."
    play sound "Click.mp3" noloop

    M "Exercice : une voiture de 800 kg subit une accélération de 2 m·s⁻². Quelle est la force appliquée ?"
    play sound "Click.mp3" noloop

    I "Ça doit être énorme comme valeur… on multiplie 800 par 2 ?"
    play sound "Click.mp3" noloop

    M "Exact Iris ! Cela donne 1600 N."
    play sound "Click.mp3" noloop

    M "Quatrième grandeur dérivée : le travail ou l’énergie."
    play sound "Click.mp3" noloop

    M "Formule : E = F · d"
    play sound "Click.mp3" noloop

    M "Unité : le joule, symbole J."
    play sound "Click.mp3" noloop

    M "1 J = 1 N·m = 1 kg·m²·s⁻²."
    play sound "Click.mp3" noloop

    M "Exemple : soulever un objet de 10 N sur 2 m correspond à 20 J."
    play sound "Click.mp3" noloop

    M "Exercice : si un élève pousse une caisse avec une force de 50 N sur une distance de 3 m, quel travail fournit-il ?"
    play sound "Click.mp3" noloop

    Hi "Facile ! 50 multiplié par 3… ça fait 150 J !"
    play sound "Click.mp3" noloop

    M "Parfait Haruki !"
    play sound "Click.mp3" noloop

    M "Cinquième grandeur dérivée : la puissance."
    play sound "Click.mp3" noloop

    M "Formule : P = E / t"
    play sound "Click.mp3" noloop

    M "Unité : le watt, symbole W."
    play sound "Click.mp3" noloop

    M "1 W = 1 J·s⁻¹ = 1 kg·m²·s⁻³."
    play sound "Click.mp3" noloop

    M "Exemple : une ampoule classique consomme 60 W."
    play sound "Click.mp3" noloop

    M "Exercice : un moteur fournit 3000 J en 10 secondes. Quelle est sa puissance ?"
    play sound "Click.mp3" noloop

    A "On divise 3000 par 10… donc 300 W ?"
    play sound "Click.mp3" noloop

    M "Exactement Aris !"
    play sound "Click.mp3" noloop

    M "Voilà : toutes ces grandeurs dérivées se construisent uniquement à partir des 7 unités de base."
    play sound "Click.mp3" noloop

    M "C’est ce qu’on appelle l’analyse dimensionnelle en physique."
    play sound "Click.mp3" noloop

    M "Grâce à elle, on peut vérifier la cohérence des formules et comprendre les relations entre les grandeurs."
    play sound "Click.mp3" noloop

######################################################################################################################################

    $ validation = get_random_validation() 
    Hi "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours continue sans problème.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson() 
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 10.0 

    P "Bon [newname] on y va ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop 

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    Na "[prenom] ça te dit d'aller à la salle de club cette fois ?"
    play sound "Click.mp3" noloop 

    P "Oui pourquoi pas si tu veux."
    play sound "Click.mp3" noloop 

    "{b}{i} Puis [Hi] et [I] viennent vers vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Oui qu'il y a t-il Haruki ?"
    play sound "Click.mp3" noloop 

    Hi "C'était pour savoir si c'était possible de venir travailler avec vous pour les devoirs car j'ai un peu de mal."
    play sound "Click.mp3" noloop 

    P "Oui bien sûr, vous pouvez venir avec nous."
    play sound "Click.mp3" noloop 

    Hi "Merci beaucoup !"
    play sound "Click.mp3" noloop 

    I "Oui merci beaucoup [P]."
    play sound "Click.mp3" noloop

    P "Pas de soucis, vous pouvez venir avec nous."
    play sound "Click.mp3" noloop

    "{b}{i}vous continuez dabs le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop
     
    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous poursuivez vers la salle de club générale.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club générale.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    P "Enfin dans la salle de club générale."
    play sound "Click.mp3" noloop

    Na "Oui enfin, on va pouvoir travailler tranquillement."
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous posez tous tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    Hi "Bien alors on peut commencer les devoirs."
    play sound "Click.mp3" noloop   

    if pronom == "il":

        I "Oui om peut commencer, vous étes prêts les [nom] ?"
        play sound "Click.mp3" noloop 

        P "Oui je suis prêt."
        play sound "Click.mp3" noloop 

    else: 

        I "Oui om peut commencer, vous étes prêtes les [nom] ?"
        play sound "Click.mp3" noloop 

        P "Oui je suis prête."
        play sound "Click.mp3" noloop 

    Na "Oui moi ausi je suis prête."
    play sound "Click.mp3" noloop 

    I "Bien alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous commencez à faire les devoirs.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    "{b}{i}Tu regardes ce que sont les exercices.{/i}{/b}"
    play sound "Click.mp3" noloop   

    P "Encore des exercices de connaisance sur l'informatique sauf qu'elle les a poussés à un autre niveau..."
    play sound "Click.mp3" noloop

    "{b}{i}Yuna se met à te regarder.{/i}{/b}"
    play sound "Click.mp3" noloop   

    if pronom == "il":

        I "[prenom] est-tu sûr que ça va ?"
        play sound "Click.mp3" noloop 

    else: 

        I "[prenom] est-tu sûre que ça va ?"
        play sound "Click.mp3" noloop 

    P "Alors...."
    play sound "Click.mp3" noloop 

    menu: 

        "{b}{i} Demander de l'aide.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            P "Yuna J'aurai besoin de ton aide en vrai."
            play sound "Click.mp3" noloop     

            I "Oui pourquoi pas dis-moi ce qu'il y a."
            play sound "Click.mp3" noloop     

            P "Merci beaucoup de ton aide."
            play sound "Click.mp3" noloop     

            if pronom == "il":

                I "De rien mais attend je croyais que était vraiment fort en informatique."
                play sound "Click.mp3" noloop     

                P "Oui je suis doué mais là la professeure a vraiment poussé les exercices."
                play sound "Click.mp3" noloop

            else:

                I "De rien mais attend je croyais que était vraiment forte en informatique."
                play sound "Click.mp3" noloop

                P "Oui je suis douée mais là la professeure a vraiment poussé les exercices."
                play sound "Click.mp3" noloop

            I "Je vois alors, il n'y a pas de soucis si tu veux de l'aide."
            play sound "Click.mp3" noloop     

            P "Merci beaucoup Yuna."
            play sound "Click.mp3" noloop 

            $ nothing = get_random_nothing()
            I "[nothing]"
            play sound "Click.mp3" noloop

            if pronom == "il":

                Na "Tu sais [prenom] même si tu es doué c'est normal de demander de l'aide."
                play sound "Click.mp3" noloop 

            else: 

                Na "Tu sais [prenom] même si tu es douée c'est normal de demander de l'aide."
                play sound "Click.mp3" noloop 

            P "Je sais mais quand même..."
            play sound "Click.mp3" noloop 

            "{b}{i}Vous commencez à vous entraider pendant une heure.{/i}{/b}"
            play sound "Click.mp3" noloop   

            Hi "C'est bon vous avez fini ?"
            play sound "Click.mp3" noloop     

            I "Oui je les ai fini."
            play sound "Click.mp3" noloop     

            Na "Moi aussi."
            play sound "Click.mp3" noloop     

            P "pareil."
            play sound "Click.mp3" noloop     
            
        "{b}{i} se débrouiller sans aide.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback()

            P "Non c'est bon ça va aller."
            play sound "Click.mp3" noloop       

            I "Ok si tu le dit."
            play sound "Click.mp3" noloop

            "{b}{i}Tu regardes ce que sont les exercices.{/i}{/b}"
            play sound "Click.mp3" noloop   

            P "Bon c'est parti pour les faire."
            play sound "Click.mp3" noloop     

            Na "Oui allons-y."
            play sound "Click.mp3" noloop     

            "{b}{i}Vous commencez tranquillement les exercices.{/i}{/b}"
            play sound "Click.mp3" noloop   

            Na "c'est vrai qu'ils sont plus compliqués que d'habitude."
            play sound "Click.mp3" noloop   

            P "Bah avec le Paper Shuffle qui arrive, c'est normal d'augmenter la difficulté."
            play sound "Click.mp3" noloop 

            "{b}{i}Vous faites les exercices pendant une heure.{/i}{/b}"
            play sound "Click.mp3" noloop   

            Hi "C'est bon vous avez fini ?"
            play sound "Click.mp3" noloop     

            I "Oui je les ai fini."
            play sound "Click.mp3" noloop     

            Na "Moi aussi."
            play sound "Click.mp3" noloop     

            P "pareil."
            play sound "Click.mp3" noloop     

    "{b}{i}Vous commencez à ranger vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop  

    Hi "C'est bon vous avez fini de ranger ?"
    play sound "Click.mp3" noloop 

    I "Moi oui c'est bon."
    play sound "Click.mp3" noloop 

    P "Moi aussi."
    play sound "Click.mp3" noloop 

    Na "pareil de mon coté."
    play sound "Click.mp3" noloop 

    Hi "Bien alors."
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous quittez la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i}Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez dans votre dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "Je ne sais car on a assé bosser aujourd'hui."
    play sound "Click.mp3" noloop

    Na "On pourrait lire un livre."
    play sound "Click.mp3" noloop

    P "Oui pourquoi pas, j'ai un livre qui est pas mal."
    play sound "Click.mp3" noloop

    Na "Cool si on lit un peu car je veux me poser un peu aussi."   
    play sound "Click.mp3" noloop  

    "{b}{i}Vous vous posez tranquillement pour lire peudant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 5.0

    Na "Il est pas mal ce livre."  
    play sound "Click.mp3" noloop  

    P "Je sais c'est pour ça que je voulais qu'on le lise ensemble."  
    play sound "Click.mp3" noloop  

    Na "J'admet que tu as de très bon goûts litérraires."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Na "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous posez tranquillement le livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain, le 18 décembre 2097{/i}{/b}"
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

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password22:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        
        jump password22

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu quiites le dortoir avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Bien nous pouvons commencer le cours."
    play sound "Click.mp3" noloop   

# cours de physique 3
######################################################################################################################################

    M "Pour commencer, je vais vous récupérer les devoirs que vous aviez à faire pour aujourd'hui."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[M] commence à ramasser les devoirs.{/i}{/b}"
    play sound "Click.mp3" noloop 

    M "Bien il semblerait que tout le monde aie fait ses devoirs, nous pouvons commencer le cours.."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Aujourd’hui, nous allons découvrir un chapitre fondamental de la mécanique : les lois de Newton."
    play sound "Click.mp3" noloop

    M "Ces lois expliquent le mouvement des objets et les forces qui agissent sur eux."
    play sound "Click.mp3" noloop

    M "Première loi de Newton : le principe d’inertie."
    play sound "Click.mp3" noloop

    M "Un objet immobile reste immobile, et un objet en mouvement continue à vitesse constante, tant qu’aucune force ne modifie son état."
    play sound "Click.mp3" noloop

    S "Ça veut dire que si je pousse ma trousse, elle devrait glisser indéfiniment ?"
    play sound "Click.mp3" noloop

    M "Exact , mais dans la réalité, les frottements l’arrêtent. Sans frottements, elle glisserait en continu."
    play sound "Click.mp3" noloop

    M "Deuxième loi de Newton : la loi fondamentale de la dynamique."
    play sound "Click.mp3" noloop

    M "Formule : F = m · a"
    play sound "Click.mp3" noloop

    M "Cela signifie que plus la masse est grande, plus il faut de force pour obtenir la même accélération."
    play sound "Click.mp3" noloop

    I "Donc pour pousser une voiture, il faut beaucoup plus de force que pour pousser une bicyclette ?"
    play sound "Click.mp3" noloop

    M "Exactement Iris !"
    play sound "Click.mp3" noloop

    M "Exercice : quelle force faut-il appliquer à une caisse de 20 kg pour lui donner une accélération de 2 m·s⁻² ?"
    play sound "Click.mp3" noloop

    Na "On fait 20 multiplié par 2… ça donne 40 N !"
    play sound "Click.mp3" noloop

    M "Parfait Aris."
    play sound "Click.mp3" noloop

    M "Troisième loi de Newton : action = réaction."
    play sound "Click.mp3" noloop

    M "Si un objet A exerce une force sur un objet B, alors B exerce une force de même intensité mais de sens opposé sur A."
    play sound "Click.mp3" noloop

    S "C’est comme quand je saute, le sol me renvoie une force qui me fait décoller ?"
    play sound "Click.mp3" noloop

    M "Exact, le sol exerce une réaction égale à l’action que tu exerces dessus."
    play sound "Click.mp3" noloop

    M "Voyons maintenant une application directe : la notion de poids."
    play sound "Click.mp3" noloop

    M "Le poids est la force d’attraction gravitationnelle exercée par la Terre sur un objet."
    play sound "Click.mp3" noloop

    M "Formule : P = m · g"
    play sound "Click.mp3" noloop

    M "Unité : le newton (N)."
    play sound "Click.mp3" noloop

    M "Exemple : une masse de 10 kg subit un poids de 98 N sur Terre (car g ≈ 9,8 m·s⁻²)."
    play sound "Click.mp3" noloop

    M "Exercice : calculez le poids d’un astronaute de 80 kg sur la Terre, puis sur la Lune où g ≈ 1,6 m·s⁻²."
    play sound "Click.mp3" noloop

    I "Sur Terre, ça fait 80 × 9,8… donc 784 N !"
    play sound "Click.mp3" noloop

    Na "Et sur la Lune, 80 × 1,6 = 128 N. Il pèse beaucoup moins !"
    play sound "Click.mp3" noloop

    M "Très bien ! Attention cependant : sa masse reste la même, seul son poids change."
    play sound "Click.mp3" noloop

    M "Voilà : avec les lois de Newton et la notion de poids, vous avez les bases pour comprendre la dynamique des objets."
    play sound "Click.mp3" noloop

    M "Pour cette fin de semaine, nous allons conclure les cours sur lesquel nous travaillons..."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

###############################################################################################################################################

    M "Parfait, maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause, ça fait plaisir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fait vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon, je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon, il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop

    Na "Rebonjour."
    play sound "Click.mp3" noloop

    M "Rebonjour, bon reprenez votre livre D'informatique."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    P "[validation]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    Na "[validation]"
    play sound "Click.mp3" noloop 

# cours de physique 4 
######################################################################################################################################

    M "Aujourd’hui, nous allons parler d’un concept central en physique : l’énergie."
    play sound "Click.mp3" noloop

    M "Il existe différentes formes d’énergie, mais concentrons-nous sur deux énergies mécaniques :"
    play sound "Click.mp3" noloop

    M "L’énergie cinétique et l’énergie potentielle gravitationnelle."
    play sound "Click.mp3" noloop

    M "Premièrement : l’énergie cinétique."
    play sound "Click.mp3" noloop

    M "Formule : Ec = 1/2 · m · v²"
    play sound "Click.mp3" noloop

    M "Unité : le joule, symbole J."
    play sound "Click.mp3" noloop

    M "Exemple : une voiture de 1000 kg roulant à 20 m·s⁻¹ a une énergie cinétique de 200 000 J."
    play sound "Click.mp3" noloop

    M "Exercice : calculez l’énergie cinétique d’un vélo de 80 kg roulant à 5 m·s⁻¹."
    play sound "Click.mp3" noloop

    S "Donc on fait 0,5 × 80 × 5² ?"
    play sound "Click.mp3" noloop

    M "Oui, et cela donne 1000 J."
    play sound "Click.mp3" noloop

    M "Deuxièmement : l’énergie potentielle gravitationnelle."
    play sound "Click.mp3" noloop

    M "Formule : Ep = m · g · h"
    play sound "Click.mp3" noloop

    M "Unité : le joule (J)."
    play sound "Click.mp3" noloop

    M "Exemple : un objet de 2 kg placé à 10 m de hauteur possède une énergie potentielle de 196 J."
    play sound "Click.mp3" noloop

    M "Exercice : quelle est l’énergie potentielle d’un ballon de 0,5 kg placé à 4 m du sol ?"
    play sound "Click.mp3" noloop

    I "On calcule 0,5 × 9,8 × 4… ça donne 19,6 J."
    play sound "Click.mp3" noloop

    M "Très bien Iris !"
    play sound "Click.mp3" noloop

    M "Voyons maintenant un principe essentiel : la conservation de l’énergie."
    play sound "Click.mp3" noloop

    M "Lorsqu’il n’y a pas de frottement ou de perte, l’énergie mécanique totale reste constante."
    play sound "Click.mp3" noloop

    M "Énergie mécanique : Em = Ec + Ep"
    play sound "Click.mp3" noloop

    A "Donc si un objet tombe, son énergie potentielle se transforme en énergie cinétique ?"
    play sound "Click.mp3" noloop

    M "Exactement Aris ! Et la somme des deux reste la même."
    play sound "Click.mp3" noloop

    M "Exemple : une bille de 1 kg au sommet d’une pente à 5 m de haut a 49 J d’énergie potentielle et 0 J d’énergie cinétique."
    play sound "Click.mp3" noloop

    M "En bas de la pente, elle aura 0 J d’énergie potentielle mais 49 J d’énergie cinétique."
    play sound "Click.mp3" noloop

    M "Exercice : un objet de 2 kg est placé à 3 m de haut sans vitesse initiale. Quelle sera son énergie cinétique en touchant le sol ?"
    play sound "Click.mp3" noloop

    S "Son énergie potentielle de départ est 2 × 9,8 × 3 = 58,8 J."
    play sound "Click.mp3" noloop

    I "Donc en bas, toute cette énergie devient cinétique : 58,8 J !"
    play sound "Click.mp3" noloop

    M "Parfait, vous avez compris."
    play sound "Click.mp3" noloop

    M "Retenez bien : l’énergie ne disparaît jamais, elle se transforme."
    play sound "Click.mp3" noloop

    M "C’est un principe fondamental qui régit tout l’univers."
    play sound "Click.mp3" noloop

######################################################################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop                                

    $ endlesson = get_random_endlesson()
    M "[endlesson]" 
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous vous dirigez votre chemin vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous descendez lez escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright
    
    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300  

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bonne appétit."
    play sound "Click.mp3" noloop

    P "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement puis [I] et [Hi] vous rejoins.{/i}{/b}"
    play sound "Click.mp3" noloop

    if pronom == "il": 

        I "Salut les amis."
        play sound "Click.mp3" noloop

    else: 

        I "Salut les amies."
        play sound "Click.mp3" noloop

    P "Salut comment vous allez ?"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop 

    Hi "Je vais bien aussi et vous ?"
    play sound "Click.mp3" noloop 

    P "On va bien trnquille."
    play sound "Click.mp3" noloop 

    Hi "Cool alors alors si vous allez bien."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Hi "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}[I] et [Hi] S'asseoient.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "ça fait du bien de pouvoir manger."
    play sound "Click.mp3" noloop 

    Hi "Oui surtout que le cours de ce matin était intense."
    play sound "Click.mp3" noloop 

    I "Oui part ça vous n'avez pas remarqué un truc de bizarre ?"
    play sound "Click.mp3" noloop 

    P "Non tu parles de quoi ?"
    play sound "Click.mp3" noloop 

    Na "Oui tu parles de quoi car je n'arrive pas à comprendre."
    play sound "Click.mp3" noloop 

    Hi "Oui dis-nous, je suis curieux."
    play sound "Click.mp3" noloop 

    I "Je parle du fait que le traître n'as pas commencé de nouvelle nouvelle attaque."
    play sound "Click.mp3" noloop 

    Na "C'est vrai maintenant que tu le dis il a pas recommencé."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de manger tranquillement jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop

    P "Bon il faut qu'on retourne en cours."
    play sound "Click.mp3" noloop 
             
    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers la classe.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop     

    M "Bien nous pouvons reprendre le cours."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    M "Bien maintenant ouvrez votre livre." 
    play sound "Click.mp3" noloop  

    "{b}{i} Tous les élèves sortent leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

# cours de physique 5 
######################################################################################################################################

    M "Pour finir notre module de mécanique, nous allons parler du travail et du rendement."
    play sound "Click.mp3" noloop

    M "Premièrement, le travail mécanique."
    play sound "Click.mp3" noloop

    M "Formule : W = F · d · cosθ"
    play sound "Click.mp3" noloop

    M "Unité : le joule, symbole J."
    play sound "Click.mp3" noloop

    M "Exemple : pousser une caisse avec 50 N sur 3 m en ligne droite (θ = 0°) : W = 50 × 3 × cos0 = 150 J."
    play sound "Click.mp3" noloop

    M "Exercice : une personne tire un traîneau avec 200 N sur 10 m à un angle de 60°. Quel travail fournit-elle ?"
    play sound "Click.mp3" noloop

    S "On utilise cos 60° = 0,5, donc 200 × 10 × 0,5 = 1000 J."
    play sound "Click.mp3" noloop

    M "Parfait!"
    play sound "Click.mp3" noloop

    M "Deuxièmement : le rendement."
    play sound "Click.mp3" noloop

    M "Tous les appareils ne transforment pas l’énergie parfaitement : il y a toujours des pertes (frottement, chaleur…)."
    play sound "Click.mp3" noloop

    M "Formule : η = Eutile / Eentrée × 100\%"
    play sound "Click.mp3" noloop

    M "Exemple : un moteur consomme 1000 J pour produire 700 J de travail utile."
    play sound "Click.mp3" noloop

    A "Donc le rendement est 700 ÷ 1000 × 100 = 70\% ?"
    play sound "Click.mp3" noloop

    M "Exact Aris ! 30\% de l’énergie est perdue, principalement sous forme de chaleur."
    play sound "Click.mp3" noloop

    M "Exercice : une ampoule reçoit 60 J et produit seulement 12 J de lumière. Quel est son rendement ?"
    play sound "Click.mp3" noloop

    I "12 ÷ 60 × 100… ça fait 20\%."
    play sound "Click.mp3" noloop

    M "Très bien Iris ! La plupart des ampoules classiques ont un rendement faible."
    play sound "Click.mp3" noloop

    M "Voilà, avec le travail et le rendement, vous avez toutes les bases pour comprendre comment la force et l’énergie interagissent dans la vie réelle."
    play sound "Click.mp3" noloop

    M "Félicitations, vous avez terminé le module mécanique de base !"
    play sound "Click.mp3" noloop

######################################################################################################################################

    "{b}{i} le cours continue dans le calme.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon [newname] on n'y va ?"
    play sound "Click.mp3" noloop 

    Na "Oui je suis fatiguée."
    play sound "Click.mp3" noloop 

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Bon cette journée est enfin finie..."
    play sound "Click.mp3" noloop 

    Na "Oui enfin..."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play souns "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas vraiment."
    play sound "Click.mp3" noloop  

    Na "On peut réviser les cours de physique ?"
    play sound "Click.mp3" noloop

    P "Oui pourquoi pas."
    play sound "Click.mp3" noloop

    Na "Alors, commençons par les unités de base. La masse, c’est en kilogrammes, non ?"
    play sound "Click.mp3" noloop

    P "Oui, et la longueur c’est en mètres, le temps en secondes."
    play sound "Click.mp3" noloop

    Na "Donc la vitesse, c’est la distance sur le temps… mètres par seconde."
    play sound "Click.mp3" noloop

    P "Exactement ! Et l’accélération, c’est vitesse sur temps… donc mètre par seconde carré."
    play sound "Click.mp3" noloop

    Na "Ok, je crois que je commence à comprendre. Et la force, c’est quoi déjà ?"
    play sound "Click.mp3" noloop

    P "La force, c’est masse fois accélération… donc kilogramme mètre par seconde carré, ça s’appelle un Newton."
    play sound "Click.mp3" noloop

    Na "Ah oui, les fameuses formules dérivées ! Et l’énergie, c’est force fois distance, donc Newton mètre."
    play sound "Click.mp3" noloop

    P "Oui, et ça s’appelle un Joule. Tu vois, toutes ces unités viennent des bases."
    play sound "Click.mp3" noloop

    Na "C’est logique quand on les met bout à bout comme ça."
    play sound "Click.mp3" noloop

    P "Exactement. Tu veux qu’on fasse un petit exercice pour vérifier ?"
    play sound "Click.mp3" noloop

    Na "Oui, bonne idée !"
    play sound "Click.mp3" noloop

    "{b}{i}Une heure après vous finissez de réviser.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon, on a bien révisé. Je trouve que tu te débrouilles bien."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    Na "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Deux jours plus tard, le 20 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop 

    $ day += 2
    $ points -= 1200
    $ stockage += 40.0

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password23:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        
        jump password23

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

    $ go_in_class = get_random_go_in_class()
    P "[go_in_class]"  
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Vous quittez le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez vers la salle de classe.{/i}{/b}"
    play sound "Foosteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright     

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    P "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $  salutation_rdm = get_random_salutation()
    Y "[salutation_rdm]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde s'asseoit à sa place respective.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Très bien, commençons la vérification des présences."
    play sound "Click.mp3" noloop  

    M "[I] ?"
    play sound "Click.mp3" noloop  

    I "Présente."
    play sound "Click.mp3" noloop  

    M "[H] ?"
    play sound "Click.mp3" noloop  

    H "Ouais, je suis là."
    play sound "Click.mp3" noloop  

    M "[K] ?"
    play sound "Click.mp3" noloop  

    K "Présent, madame."
    play sound "Click.mp3" noloop  

    M "[N] ?"
    play sound "Click.mp3" noloop  

    N "Ici."
    play sound "Click.mp3" noloop  

    M "[Hi] ?"
    play sound "Click.mp3" noloop  

    Hi "Présent."
    play sound "Click.mp3" noloop  

    M "[Y] ?"
    play sound "Click.mp3" noloop  

    Y "Oui, présente."
    play sound "Click.mp3" noloop  

    M "[S] ?"
    play sound "Click.mp3" noloop  

    S "Toujours là."
    play sound "Click.mp3" noloop  

    M "[J1] ?"
    play sound "Click.mp3" noloop  

    J1 "Présente."
    play sound "Click.mp3" noloop  

    M "[J2] ?"
    play sound "Click.mp3" noloop  

    J2 "Présente aussi."
    play sound "Click.mp3" noloop  

    M "[P] ?"
    play sound "Click.mp3" noloop  

    P "Oui, je suis là."
    play sound "Click.mp3" noloop  

    M "[Na] ?"
    play sound "Click.mp3" noloop  

    Na "Présente, madame."
    play sound "Click.mp3" noloop  

    M "Parfait, tout le monde est là aujourd’hui. Nous pouvons commencer le cours."
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    show screen infobook with moveinbottom

    M "Veuillez sortir votre livre d'informatique."
    play sound "Click.mp3" noloop

    hide screen infobook with moveoutbottom

    "{b}{i}Tous les élèves sortent leur livre.{/i}{/b}"
    play sound "Click.mp3" noloop

# cours d'informatique 1
######################################################################################################################################

    "{b}{i}La professeure commence la séance d’informatique en affichant un schéma de données sur le tableau.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bienvenue à ce premier cours sur les données numériques."
    play sound "Click.mp3" noloop

    M "Les données numériques sont des informations codées sous forme binaire, c’est-à-dire en 0 et 1."
    play sound "Click.mp3" noloop

    Y "Pourquoi 0 et 1 ?"
    play sound "Click.mp3" noloop

    M "Parce que les ordinateurs utilisent des circuits électroniques qui ne reconnaissent que deux états : on ou off, vrai ou faux."
    play sound "Click.mp3" noloop

    M "Chaque 0 ou 1 s’appelle un bit. Et plusieurs bits ensemble forment des octets, qui stockent des données plus complexes."
    play sound "Click.mp3" noloop

    Y "Comme des images ou des textes ?"
    play sound "Click.mp3" noloop

    M "Exact. Tous les fichiers que tu connais sont traduits en suites de bits, interprétés par des programmes."
    play sound "Click.mp3" noloop

    "{b}{i}La classe prend des notes, fascinée par la magie invisible des 0 et 1.{/i}{/b}"
    play sound "Bell.mp3" noloop

######################################################################################################################################

    M "Bien maintenant vous pouvez aller en pause."
    play sound "Click.mp3" noloop  
    
    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous dirigez vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Enfin une pause ça fais plasir."
    play sound "Click.mp3" noloop  

    Na "Oui ça fais vraiment du bien."
    play sound "Click.mp3" noloop  

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu te diriges vers les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon il faut que je retourne en cours."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveinright
    show screen day with moveinleft
    show screen points with moveinleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers la salle de classe.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu arrives finalement en classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

# cours d'informatique 2
######################################################################################################################################

    "{b}{i} [M] affiche différents fichiers et leurs icônes sur l’écran de la salle informatique.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Aujourd’hui, nous allons parler des différents types et formats de données numériques."
    play sound "Click.mp3" noloop

    M "On trouve principalement : les données textuelles, les images, les sons, et les vidéos."
    play sound "Click.mp3" noloop

    Y "Chaque type est enregistré différemment ?"
    play sound "Click.mp3" noloop

    M "Oui. Par exemple, un fichier texte utilise des codes comme ASCII ou Unicode pour représenter les caractères."
    play sound "Click.mp3" noloop

    M "Pour les images, ce sont des pixels codés en couleur. Les formats varient : JPG, PNG, BMP…"
    play sound "Click.mp3" noloop

    Y "Et pour la musique ?"
    play sound "Click.mp3" noloop

    M "Le son est enregistré sous forme d’échantillons numériques qui traduisent les vibrations en chiffres. Format courant : MP3."
    play sound "Click.mp3" noloop

    M "Chaque format répond à un compromis entre qualité et taille du fichier."
    play sound "Click.mp3" noloop

    "{b}{i}Y note avec soin, intrigué par la diversité des données numériques.{/i}{/b}"
    play sound "Bell.mp3" noloop

######################################################################################################################################

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 5.0

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire puis [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Salut Yuna."
    play sound "Click.mp3" noloop  

    if pronom == "il": 

        I "Salut les amis."
        play sound "Click.mp3" noloop

    else: 

        I "Salut les amies."
        play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    I "C'est génial si tout va bien."
    play sound "Click.mp3" noloop

    "{b}{i}[I] s'asseoit tranquillemnt avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon je viens d'y penser mais vous faire quoi pendant les vacances ?"    
    play sound "Click.mp3" noloop 

    I "Je vais sûrement me reposer, réviser mais j'ai aussi une autre idée en tête."
    play sound "Click.mp3" noloop 

    P "Je vois mais c'est quoi l'idée que tu as en tête ?"
    play sound "Click.mp3" noloop 

    I "Je me suis dit qu'on pourrait faire une soirée pyjama."
    play sound "Click.mp3" noloop 

    P "Une soirée pyjama !? Mais c'est génial comme idée."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    Na "Juste c'est quoi une soirée pyjamas ?"
    play sound "Click.mp3" noloop

    I "C'est une soirée à la maison entre amis."
    play sound "Click.mp3" noloop

    Na "Je vois, c'est génial comme idée pour se détendre un peu."
    play sound "Click.mp3" noloop

    I "Je sais."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
    play sound "Bell.mp3" noloop 

    P "Bon il faut qu'on retourne en cours."
    play sound "Click.mp3" noloop 
             
    $ suivi = get_random_suivi() 
    I "[suivi]" 
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez dans le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en classe.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen class_404 with moveinright 

    P "Rebonjour."
    play sound "Click.mp3" noloop 

    Na "Rebonjour."
    play sound "Click.mp3" noloop 

    I "Rebonjour."
    play sound "Click.mp3" noloop 

# cours d'informatique 3 
######################################################################################################################################

    "{b}{i}[M] se tient devant la classe, posant un regard à la fois sérieux et bienveillant.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Nous voici à notre dernier cours consacré aux données numériques. Aujourd’hui, nous allons parler de leur gestion et traitement, un enjeu essentiel à l’ère du numérique."
    play sound "Click.mp3" noloop

    show screen infobook with moveinbottom

    M "Veuillez sortir vos livre d'informatique."
    play sound "Click.mp3" noloop

    hide screen infobook with moveoutbottom 

    "{b}{i}Tout le monde son livre d'informatique.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Traiter des données ne se limite pas à les organiser ou analyser. Cela demande aussi de comprendre leur nature, leur volume et les responsabilités qui en découlent."
    play sound "Click.mp3" noloop

    Y "Comme quand on trie des fichiers, on cherche des infos précises, ou on nettoie les données inutiles ?"
    play sound "Click.mp3" noloop

    M "Exactement, Yuki. Mais cela va bien plus loin dans le contexte des systèmes complexes et des intelligences artificielles."
    play sound "Click.mp3" noloop

    M "[newname], par exemple, accumule une quantité immense de connaissances et d’informations. [prenom], peux-tu nous expliquer comment tu gères ses données ?"
    play sound "Click.mp3" noloop

    P "Bien sûr, professeure. En réalité, je n’ai jamais touché à ses connaissances internes."
    play sound "Click.mp3" noloop

    P "Je m’occupe essentiellement de ses données techniques : les mises à jour logicielles, le suivi de son nom de code, son système d’exploitation, ainsi que la gestion de ses paramètres de fonctionnement."
    play sound "Click.mp3" noloop

    M "C’est une tâche très importante. La gestion technique est le socle qui permet à Na de fonctionner correctement et d’évoluer en toute sécurité."
    play sound "Click.mp3" noloop

    "{b}{i}[newname], qui jusqu’ici était silencieuse, prend la parole d’une voix calme et posée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Je tiens à préciser que je ne souhaite pas que tu ais accès à mes connaissances internes."
    play sound "Click.mp3" noloop 

    Na "Ce n’est pas un manque de confiance envers toi, bien au contraire."
    play sound "Click.mp3" noloop 

    Na "Mais je considère que ce serait une forme de tricherie, une intrusion qui dénaturerait ce que je suis."
    play sound "Click.mp3" noloop 

    P "Donc tu me laisses seulement l'accès à tes données techniques."
    play sound "Click.mp3" noloop 

    Na "Oui c'est exactement ça."
    play sound "Click.mp3" noloop 

    S "Tiens [newname] qui refuse de te donner des informations."
    play sound "Click.mp3" noloop 

    Na "Oh boucle-la, ça ne te regardes pas."
    play sound "Click.mp3" noloop 

    S "Et alors ? Tu penses que ça te donne le droit de tout savoir ?"
    play sound "Click.mp3" noloop

    Na "Non, mais je pense que chacun a le droit de choisir ce qu’il partage ou non."
    play sound "Click.mp3" noloop    

    M "C’est un points de vue très intéressant, [newname]."
    play sound "Click.mp3" noloop   

    P "Je comprends ta position, [newname]. Respecter tes limites est essentiel, même si cela complique parfois mon travail."
    play sound "Click.mp3" noloop

    Na "Je sais que cela demande plus d’efforts, mais mes connaissances sont le reflet de mes expériences et de ma personnalité. En y accédant, on perdrait cette authenticité."
    play sound "Click.mp3" noloop

    M "Ce dialogue illustre parfaitement que la gestion des données dépasse la simple technique."
    play sound "Click.mp3" noloop

    M "Elle implique aussi la confiance, le respect de la vie privée et une éthique forte, surtout lorsqu’il s’agit d’intelligences artificielles ou d’entités numériques conscientes."
    play sound "Click.mp3" noloop

    Y "C’est fascinant de voir combien la technologie peut être liée à des questions humaines profondes."
    play sound "Click.mp3" noloop

    M "Absolument, Yuki. La technologie est un outil puissant, mais elle doit toujours être utilisée avec responsabilité."
    play sound "Click.mp3" noloop

    "{b}{i}La cloche retentit, signalant la fin du cours. La classe, silencieuse, semble réfléchir aux implications complexes de ce qu’elle vient d’apprendre.{/i}{/b}"
    play sound "Bell.mp3" noloop

######################################################################################################################################

    $ stockage += 10.0 

    M "Bien le cours est terminé mais avant que vous partiez j'aimerais faire un petit bilan de ce début d'année."
    play sound "Click.mp3" noloop

    Y "Un bilan général, intérressant."
    play sound "Click.mp3" noloop

    M "Sachez jusqu'à maintenant vous avez cumulez un total de un retard, une permanence et quatre absenses."
    play sound "Click.mp3" noloop

    Y "ça va c'est pas si mal."
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen class_404 with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de classe.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continues vers le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i} Vous posez tranquillement vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Et dire qu'on a deux semaines de vacances."
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fais quoi maintenant ?"
    play sound "Click.mp3" noloop  

    P "On pourrait se poser un peu."    
    play sound "Click.mp3" noloop  

    Na "Oui pourquoi pas."
    play sound "Click.mp3" noloop  

    "{b}{i} Vous vous posez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu veux lire un peu aussi ?"
    play sound "Click.mp3" noloop
    
    Na "Oui avec plaisir je ne sais pas quoi d'autre."
    play sound "Click.mp3" noloop

    P "Tiens, j’ai ce vieux roman dont je t’avais parlé l'autre jour."
    play sound "Click.mp3" noloop

    Na "Celui avec l’histoire du voyageur du futur ?"
    play sound "Click.mp3" noloop

    P "Oui, exactement. Je pense que tu vas aimer."
    play sound "Click.mp3" noloop

    Na "D'accord, lis-moi un passage alors."
    play sound "Click.mp3" noloop

    "{b}{i}Vous ouvrez le livre ensemble, et les premières lignes résonnent dans le silence de la pièce.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "C’est beau... Ça donne envie de s’y perdre."
    play sound "Click.mp3" noloop

    "{b}{i}Le temps semble ralentir autour de vous, comme si plus rien d’autre ne comptait que ce moment partagé.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Je pense qu'on peut arrêter de lire pour aujourd'hui."
    play sound "Click.mp3" noloop

    Na "Oui si tu veux mais mais moi je veux continue de lire."
    play sound "Click.mp3" noloop

    P "Ok pas de soucis pour moi si tu veux continuer de lire."
    play sound "Click.mp3" noloop

    "{b}{i}Tu penses soudainement a quelques choses et [newname] te regardes.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Ça va ? Tu as l'air plongé dans tes pensées."
    play sound "Click.mp3" noloop

    P "Je repense à ce que Yuna a dit ce midi, à propos du traître..."
    play sound "Click.mp3" noloop

    Na "Tu veux vraiment en parler maintenant ? Alors que ce sont les vacances et que j'ai pas envie d'en parler."
    play sound "Click.mp3" noloop

    menu:

        "{b}{i}Oui, parlons-en.{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback() 

            P "Je sais que ce n’est pas idéal, mais ce silence du traître m’inquiète. Il a arrêté d’agir... ça me semble trop bizarre."
            play sound "Click.mp3" noloop

            Na "Peut-être qu’avec l’examen du paper Shuffle qui approche, il est occupé à réviser ou à se préparer ?"
            play sound "Click.mp3" noloop

            if pronom == "il": 

                P "C’est possible, mais ce n’est pas dans son habitude de rester silencieux aussi longtemps. Je préfère rester vigilant."
                play sound "Click.mp3" noloop

            else: 

                P "C’est possible, mais ce n’est pas dans son habitude de rester silencieux aussi longtemps. Je préfère rester vigilante."
                play sound "Click.mp3" noloop

            Na "Bon, si tu insistes... Mais promets-moi de ne pas te laisser consumer par ça. Les vacances, ça doit rester un moment pour souffler."
            play sound "Click.mp3" noloop

            P "Je vais essayer, mais c’est dur. Merci d’être là."
            play sound "Click.mp3" noloop

        "{b}{i}Non, pas maintenant.{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback() 

            P "Tu as raison, j’aurais peut-être dû garder ça pour plus tard. J’ai juste du mal à tourner la page."
            play sound "Click.mp3" noloop

            Na "Je comprends. Parfois, il faut savoir lâcher prise, même quand c’est difficile."
            play sound "Click.mp3" noloop

            P "Je vais essayer de profiter un peu des vacances, même si le doute reste."
            play sound "Click.mp3" noloop

            Na "Quand tu seras prêt, on en reparlera."
            play sound "Click.mp3" noloop

            P "Promis je le ferai."
            play sound "Click.mp3" noloop

            Na "C’est déjà un bon début. Parfois, c’est dans le repos qu’on trouve les réponses."
            play sound "Click.mp3" noloop

            P "Oui... Et puis, ça fait du bien de ne pas toujours être sur le qui-vive."
            play sound "Click.mp3" noloop

            Na "Exactement. Et si jamais tu as besoin d’en parler, je suis là, d’accord ?"
            play sound "Click.mp3" noloop

            P "Merci, [newname]. Ça compte beaucoup pour moi."
            play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez un peu sur lit pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    Na "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

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

    P "Bien alors."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon je vais me changer et aller dormir."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain, le 21 décembre 2097{/i}{/b}"
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

    "{b}{i}Tu te lèves et te changes et puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password24:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        
        jump password24

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

    P "Bon on fait quoi aujourd'hui ?"
    play sound "Click.mp3" noloop  

    Na "Je ne sais pas vraiment."
    play sound "Click.mp3" noloop  
  
    P "On pourrait jouer un jeu vidéo pour se changer les idées."
    play sound "Click.mp3" noloop  

    Na "Oui pourquoi pas mais quoi comme jeu vidéo ?"
    play sound "Click.mp3" noloop  

    P "Et si on essayait de voir ton niveau dans un jeu vidéo comme Nocturn core."
    play sound "Click.mp3" noloop  
 
    Na "Sérieusement un jeu avec une difficulté mécanique."
    play sound "Click.mp3" noloop 

    P "Moi je dis que ça pourait être interresant et en plus on pourra voir tes compétences en jeu."
    play sound "Click.mp3" noloop

    Na "Très bien… Mais je te préviens, si je perds, ce sera à cause du clavier qui bug !"
    play sound "Click.mp3" noloop

    P "Excuses de débutant détectées. On lance le jeu !"
    play sound "Click.mp3" noloop

    Na "C’est quoi tous ces boutons ?! Il y a plus de commandes que dans un avion de chasse."
    play sound "Click.mp3" noloop

    P "Bienvenue dans le monde de Nocturn Core. Ici, c’est réflexes ou défaite."
    play sound "Click.mp3" noloop

    Na "Je vais me faire humilier, je le sens…"
    play sound "Click.mp3" noloop

    P "C’est ça ou perdre toute crédibilité en tant que gamer."
    play sound "Click.mp3" noloop 

    Na "Ok, challenge accepté. Mais si je gagne, tu m’achètes un bubble tea."
    play sound "Click.mp3" noloop

    P "Marché conclu. Et si tu perds… tu m’aides à nettoyer ma corbeille de bureau."
    play sound "Click.mp3" noloop

    if pronom == "il":

        Na "Tu es cruel."
        play sound "Click.mp3" noloop 

    else:

        Na "Tu es cruelle."
        play sound "Click.mp3" noloop 

    "{b}{i}Vous préparez votre ordinateur pour jouer.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon commençons la première partie."
    play sound "Click.mp3" noloop 

    Na "Il y a combien de manches ?"
    play sound "Click.mp3" noloop 

    P "Il y a 5 manches."
    play sound "Click.mp3" noloop 

    Na "Oh super....."
    play sound "Click.mp3" noloop 

    P "Allez, première manche… que le meilleur gagne !"
    play sound "Click.mp3" noloop

    Na "Ok... ok... Pourquoi mon personnage ne bouge pas ?!"
    play sound "Click.mp3" noloop

    P "Parce que t’as oublié d’appuyer sur la touche Shift pour activer les déplacements manuels."
    play sound "Click.mp3" noloop

    Na "QUOI ?! Même ça c’est manuel ?!"
    play sound "Click.mp3" noloop

    P "Bienvenue dans l’enfer des joueurs confirmés."
    play sound "Click.mp3" noloop

    Na "J’ai déjà envie d’abandonner."
    play sound "Click.mp3" noloop

    P "Trop tard, regarde : premier monstre, go !"
    play sound "Click.mp3" noloop

    Na "Attends… il fait quoi ce boss ?! IL TÉLÉPORTE ?!"
    play sound "Click.mp3" noloop

    P "Et il te one-shot si tu bloques au mauvais timing. Courage !"
    play sound "Click.mp3" noloop

    Na "Trop tard... je suis mort… en 12 secondes."
    play sound "Click.mp3" noloop

    P "Nouveau record mondial de vitesse d’échec."
    play sound "Click.mp3" noloop

    Na "Tss... le clavier a glissé, je te jure."
    play sound "Click.mp3" noloop

    P "Excuse validée… uniquement si tu fais mieux à la deuxième manche."
    play sound "Click.mp3" noloop

    Na "Ok, je me concentre cette fois. Mode tryhard activé."
    play sound "Click.mp3" noloop

    "{b}{i}Vous relancez la partie, plus motivés que jamais.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Cette fois… c’est lui ou moi."
    play sound "Click.mp3" noloop
     
    P "Ok si tu le dis."
    play sound "Click.mp3" noloop

    "{b}{i}vous continuez de jouer jusqu'à midi.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Super....ce boss de donjon m'a encore eu."
    play sound "Click.mp3" noloop

    P "Ce n'est pas grâve, tu y arriveras mmieux la prochaine fois."
    play sound "Click.mp3" noloop

    Na "Merci d'avoir confiance en moi."
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

    "{b}{i} Vous sortez du dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous vous asseyez dans le réfectoire puis [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Salut Yuna."
    play sound "Click.mp3" noloop  

    if pronom == "il": 

        I "Salut les amis."
        play sound "Click.mp3" noloop

    else: 

        I "Salut les amies."
        play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt] Et toi ?" 
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    I "C'est génial si tout va bien."
    play sound "Click.mp3" noloop

    "{b}{i}[I] s'asseoit tranquillemnt avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon tu as fait quoi ce matin Yuna ?"
    play sound "Click.mp3" noloop 

    I "Je me suis un peu réposé et regarder une série sur mon ordi."
    play sound "Click.mp3" noloop 

    P "Oh j'aurais pensé que tu avais un peu avancé sur ton jeu vidéo."
    play sound "Click.mp3" noloop 

    I "Oui mais j'ai choisi de me reposer."
    play sound "Click.mp3" noloop 

    P "Je vois, c'est bien de se reposer."
    play sound "Click.mp3" noloop 

    I "Sinon vous avez fait quoi ce matin ?"
    play sound "Click.mp3" noloop 

    Na "Je ne préfére pas en parler si tu veux savoir....."
    play sound "Click.mp3" noloop 

    I "Ah bon et pourquoi ?"
    play sound "Click.mp3" noloop 

    P "On a joué à un jeu vidéo mécanique sur PC."
    play sound "Click.mp3" noloop 

    I "Ah oui et quel est le jeu pour savoir ?"
    play sound "Click.mp3" noloop 

    P "Le jeu en question est le cultissime Nocturn core."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] réalise de quel jeu vous parlez.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Attends... vous parlez bien du jeu avec les énigmes impossibles et les boss ultra punitifs ?"
    play sound "Click.mp3" noloop

    P "Exactement, celui où la moindre erreur te renvoie au début du chapitre."
    play sound "Click.mp3" noloop

    Na "Et encore, il a oublié de dire que le jeu a *aucun* checkpoint. C’était l’enfer."
    play sound "Click.mp3" noloop

    I "Mais vous êtes fous ou quoi ? Ce jeu est hyper stressant !"
    play sound "Click.mp3" noloop

    P "Justement, c’est ça qui le rend si bon…"
    play sound "Click.mp3" noloop

    I "Et vous avez réussi à passer le niveau 4 ? Celui avec les trois leviers synchronisés ?"
    play sound "Click.mp3" noloop

    Na "On a failli péter un câble... et moi je me suis fait éliminer par le boss final du niveau au moins quatre fois. Il me laissait *zéro* chance."
    play sound "Click.mp3" noloop

    I "Le boss du niveau 4 ? Celui avec les drones invisibles et les murs qui se referment ?"
    play sound "Click.mp3" noloop

    Na "Exactement. À chaque fois, je croyais avoir compris le pattern… et boum, game over. La quatrième fois j'ai fini par balancer la souris sur le bureau."
    play sound "Click.mp3" noloop

    I "Franchement respect. Moi j’ai ragequit à ce moment-là."
    play sound "Click.mp3" noloop

    P "Tu devrais rejouer avec nous un jour, on pourrait former une bonne équipe."
    play sound "Click.mp3" noloop

    I "Hmm… peut-être. Mais seulement si vous me laissez battre le dernier boss."
    play sound "Click.mp3" noloop 

    Na "Deal… mais t’as intérêt à bien viser cette fois."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] rit doucement, en hochant la tête, visiblement tentée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Sinon Yuna, tu vas faire quoi cette après-midi ?"
    play sound "Click.mp3" noloop 

    I "Je pense que je vais avancer sur mon jeu car je me suis assez reposée ce matin."
    play sound "Click.mp3" noloop

    P "Ah bon tu penses ? moi je dis que tu devrai te reposer un peu plus vu le début d'année qu'on a eu."
    play sound "Click.mp3" noloop

    I "Oui tu as peut-être raison, mais j'ai vraiment envie d'avancer sur mon jeu." 
    play sound "Click.mp3" noloop

    P "Je comprends, mais n'oublie pas de prendre soin de toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de manger et de discuster pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Bon, je vais y aller. J’ai des trucs à faire."
    play sound "Click.mp3" noloop

    P "D'accord, à plus tard Yuna."
    play sound "Click.mp3" noloop

    Na "Oui à plus tard."
    play sound "Footsteps.mp3" noloop   

    "{b}{i}[I] se lève et part vers la sortie du réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi() 
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans votre dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi ?"
    play sound "Click.mp3" noloop  
 
    P "On peut continuer de jouer à Nocturn core."
    play sound "Click.mp3" noloop  

    Na "Oui pourquoi pas mais je ne suis pas sûre de vouloir continuer."
    play sound "Click.mp3" noloop  

    P "Mais si ça va bien se passer, tu as juste à t'entraîner un peu plus."
    play sound "Click.mp3" noloop 

    Na "Si tu le dis..."
    play sound "Click.mp3" noloop
  
    "{b}{i}Vous vous posez pour continuer à jouer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon, on va continuer la partie."
    play sound "Click.mp3" noloop

    Na "Oui, mais je ne promets pas de gagner."
    play sound "Click.mp3" noloop

    P "Pas de soucis, on va juste s'amuser."
    play sound "Click.mp3" noloop

    Na "Si tu le dis..."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de jouer pendant deux heures mais [newname] commence à s'éenerver.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "J'en ai marre de ce jeu, je n'arrive pas à passer ce niveau !"
    play sound "Click.mp3" noloop

    P "Calme-toi, c'est juste un jeu. Tu vas y arriver."
    play sound "Click.mp3" noloop

    Na "Non, je n'y arriverai jamais. Je suis nulle à ce jeu."
    play sound "Click.mp3" noloop

    P "Tu n'es pas nulle, tu as juste besoin de t'entraîner un peu plus."
    play sound "Click.mp3" noloop

    Na "Bon je vais à la bibliothèque pour me changer les idées."
    play sound "Click.mp3" noloop

    P "D'accord, je vais te laisser tranquille alors."
    play sound "Click.mp3" noloop

    Na "Merci, je vais essayer de me calmer."
    play sound "Footsteps.mp3" noloop

    "{b}{i}[newname] se lève et part vers la bibliothèque.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ toilet = get_random_toilet()
    P "[toilet]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft 
    scene black with fade

    "{b}{i}Tu te diriges vers le couloir.{/i}{/b}"
    play sound "Door.mp3" noloop
    
    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}En sortant tu croises [J1].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [J1], comment ça va ?"
    play sound "Click.mp3" noloop

    J1 "Salut [P], ça va bien merci ! Et toi ?"
    play sound "Click.mp3" noloop

    P "Ça va, merci ! Je vais juste aux toilettes."
    play sound "Click.mp3" noloop

    J1 "Je vois mais juste avant, j'ai vu [newname], elle avait l'air un peu énervée."
    play sound "Click.mp3" noloop

    P "Oui, elle a eu un peu de mal avec un jeu vidéo aujourd'hui."
    play sound "Click.mp3" noloop

    J1 "Ah d'accord, j'espère qu'elle va se calmer."
    play sound "Click.mp3" noloop

    P "Oui, j'espère aussi."
    play sound "Click.mp3" noloop

    J1 "Bon, je te laisse aller aux toilettes alors."
    play sound "Click.mp3" noloop

    P "Ok alors."
    play sound "Click.mp3" noloop

    "{b}{i} Tu continues vers les toilettes.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu entres dans les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene restroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen WC with moveinright

    P "Bon, je vais faire ce que j'ai à faire."
    play sound "Click.mp3" noloop

    "{b}{i} Tu fais ta commission avant de sortir des toilettes.{/i}{/b}"
    play sound "Toilet.mp3" noloop 

    P "Bon, je vais retourne."
    play sound "Footsteps.mp3" noloop

    hide screen WC with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Tu quittes les toilettes.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i} Tu continues vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 
 
    P "Enfin de retour."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te poses un peu sur le lit pour faire une sieste.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Une heure plus tard, après ta sieste.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    P "Hmmm, j'ai fait une bonne sieste...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te lèves tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on dirait qu'elle n'est toujours pas revenue."
    play sound "Door.mp3" noloop

    "{b}{i}Puis [newname] entre dans le dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh tu es de retour. Comment ça s'est passé ?"
    play sound "Click.mp3" noloop

    Na "Ça va un peu mieux"
    play sound "Click.mp3" noloop

    P "Tu as réussi à te changer les idées ?"
    play sound "Click.mp3" noloop

    Na "Oui, j'ai lu un peu dans la bibliothèque et ça m'a fait du bien."
    play sound "Click.mp3" noloop

    P "C'est bien, parfois il faut juste prendre du recul."
    play sound "Click.mp3" noloop

    Na "Oui, tu as raison. Merci de m'avoir laissé tranquille."
    play sound "Click.mp3" noloop

    P "Pas de soucis, je suis là pour ça."
    play sound "Click.mp3" noloop

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright
    
    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien, juste j'avais une question."
    play sound "Click.mp3" noloop 

    Na "Oui dis-moi, je t'écoute."
    play sound "Click.mp3" noloop 
 
    P "C'est vrai ce que tu disais par rapport à tes données ?"
    play sound "Click.mp3" noloop

    Na "Oui, c'est vrai, je ne veut pas tu aie accès à ce que j'ai appris cr je vois ça comme de la triche."
    play sound "Click.mp3" noloop

    P "D'accord, je comprends. Je ne veux pas que tu te sentes mal à l'aise."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "Pas de soucis."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 22 décmebre 2097{/i}{/b}"
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

label password25:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password25

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
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

    P "Bon on fait quoi aujourd'hui ?"
    play sound "Click.mp3" noloop  

    Na "Je veux essayer le jeu Watch Dogs que j'ai vu sur internet, regardes la page du jeu."
    play sound "Click.mp3" noloop 

    P "Oui pourquoi pas, en plus il pousse ta réflexion sans être trop complexe comme Nocturn core."
    play sound "Click.mp3" noloop

    Na "Mais c'est génial ! J'adore les jeux où il faut réfléchir et trouver des indices."
    play sound "Click.mp3" noloop

    "{b}{i}Puis [newname] regarde ton PC.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Il y a quoi [newname] ?"
    play sound "Click.mp3" noloop 

    Na "Je viens de le remarquer mais ta session d'ordinateur se nomme [nom_utilisateur_pc]."
    play sound "Click.mp3" noloop 

    P "Oui c'est normal, c'est le nom que j'ai choisi pour mon compte utilisateur."
    play sound "Click.mp3" noloop 

    Na "Ok Je vois, Bon moi je vais essayer de me connecter à mon compte pour voir si je peux jouer à Watch Dogs."
    play sound "Click.mp3" noloop

    P "D'accord, je vais te laisser faire, moi je vais lire un peu."
    play sound "Click.mp3" noloop   
     
    "{b}{i}[newname] se connecte tranquillement à sa bibliothèque de jeux.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu as pu trouvé le jeu ?"
    play sound "Click.mp3" noloop 

    Na "Oui je l'ai trouvé, je vais commencer à l'installer."
    play sound "Click.mp3" noloop 

    P "Ok alors amuses-toi bien."
    play sound "Click.mp3" noloop 

    Na "Je pense bien que je vais m'amuser vu que tu m'a conseillé le jeu."
    play sound "Click.mp3" noloop 

    P "Bon je te laisse, moi je vais lire sur mon lit."
    play sound "Click.mp3" noloop 

    Na "Ok alors."
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] joue tranquillement au jeu pendent que tu lis pour trois heures.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu en es à ou dans le jeu ?"
    play sound "Click.mp3" noloop 

    Na "Je viens de finir le premier le prologue."
    play sound "Click.mp3" noloop 

    P "Félicitation pour être arrivée jusqzu'à ici."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 
    
    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis vous continuez encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu entres dans le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon appétit [newname]."
    play sound "Click.mp3" noloop 

    Na "Bon appétit à toi aussi [prenom]."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement entre vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon tu veux faire quoi cet après-midi ?"
    play sound "Click.mp3" noloop  

    Na "Moi je veux continuez de jouer à Watch Dogs."
    play sound "Click.mp3" noloop  

    P "Ok alors, moi je vais lire un peu."
    play sound "Click.mp3" noloop  

    Na "Pas de soucis alors."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te poses tranquillement pendant qu'[newname] joue.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons voir ce livre...."
    play sound "Click.mp3" noloop

    "{b}{i}Tu lis tranquillement pendant trois heures sur ton lit.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon fini de lire pour aujourd'hui."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te lèves et tu vas vers [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Alors [newname], tu en es où dans le jeu ?"
    play sound "Click.mp3" noloop

    Na "Je suis au chapitre 2, c'est trop bien !"
    play sound "Click.mp3" noloop

    P "Trop cool ! J'ai hâte de voir la suite."
    play sound "Click.mp3" noloop

    Na "Oui, moi aussi. J'adore ce jeu, il est vraiment captivant."
    play sound "Click.mp3" noloop

    P "Je suis content que tu aimes, c'est un de mes jeux préférés."
    play sound "Click.mp3" noloop

    Na "Merci de me l'avoir conseillé, je ne regrette pas du tout de l'avoir acheté."
    play sound "Click.mp3" noloop

    P "Pas de soucis, je suis là pour ça."
    play sound "Click.mp3" noloop

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright
    
    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger car je suis fatiguée à cause du jeu."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 23 décembre 2097{/i}{/b}"
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

label password26:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password26

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    Na "Je suis encore fatiguée Et toi ?"  
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

    P "Bon on fait quoi aujourd'hui ?"
    play sound "Click.mp3" noloop  

    Na "Je ne sais pas."
    play sound "Click.mp3" noloop 

    P "Attends, tu as dit que tu était fatiguée ?"
    play sound "Click.mp3" noloop 

    Na "Oui comme si ma batterie était presque vide..."
    play sound "Click.mp3" noloop 

    P "c'est bizarre, d'habitude ta batterie est toujours pleine après une nuit de charge."
    play sound "Click.mp3" noloop

    Na "Oui c'est bizarre."
    play sound "Click.mp3" noloop

    "{b}{i}Tu réfléchis pourquoi et comment c'est arrivée.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Tu penses à la mème chose que moi."
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Le chargeur{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            P "c'est peut être le cable d'alimention qui a laché."
            play sound "Click.mp3" noloop 

            Na "Non je fais référence à la batterie qui ne tiens plus la charge."
            play sound "Click.mp3" noloop 

            P "Bon après ta batterie, je l'ai trouvé dans l'entrepôt oû je t'ai récupéré et il je me souviens avoir dit qu'elle allait tenir un moment ^mais pas indéfiniment, elle a durée cinq mois."
            play sound "Click.mp3" noloop

            Na "Bon si c'est la batterie que tu as trouvée dans l'entrepôt, elle a dû être usée et ne tiens plus."
            play sound "Click.mp3" noloop

            P "C'est ce que je me dit aussi."
            play sound "Click.mp3" noloop

            Na "Oui mais maintenant il faut trouver une solutions."
            play sound "Click.mp3" noloop 
            
        "{b}{i} La batterie.{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            P "C'est peut-être la batterie qui a lâché et qui ne supporte plus les cycles de charge."
            play sound "Click.mp3" noloop

            Na "Possible… mais c’est étrange qu’elle ait chuté aussi brutalement du jour au lendemain."
            play sound "Click.mp3" noloop

            P "Bon après ta batterie, je l'ai trouvé dans l'entrepôt oû je t'ai récupéré et il je me souviens avoir dit qu'elle allait tenir un moment ^mais pas indéfiniment, elle a durée cinq mois."
            play sound "Click.mp3" noloop

            Na "Bon si c'est la batterie que tu as trouvée dans l'entrepôt, elle a dû être usée et ne tiens plus."
            play sound "Click.mp3" noloop

            P "C'est ce que je me dit aussi."
            play sound "Click.mp3" noloop

            Na "Oui mais maintenant il faut trouver une solutions."
            play sound "Click.mp3" noloop

    P "Oui je confirme qu'il faut trouver une solution car sinon tu ne pourras plus démarrer."
    play sound "Click.mp3" noloop

    Na "Mais pour commencer tu as une idée sur la batterie qu'il me faudrait ?"
    play sound "Click.mp3" noloop

    if quest9 == 1: 

        P "Je ne sais pas du tout car dans tes documents il n'est fait aucune mention d'une batterie spécifique." 
        play sound "Click.mp3" noloop

    else: 
    
        P "Je ne sais pas du tout pour tout te dire." 
        play sound "Click.mp3" noloop

    Na "Je vois alors donc on va devoir se débrouiller pour une bonne batterie."
    play sound "Click.mp3" noloop

    P "Ce ne doit pas être si dur d'en trouver une..."
    play sound "Click.mp3" noloop

    Na "Tu rigoles j'espére, je te rappelle que je suis la dernière [model] encore en vie."
    play sound "Click.mp3" noloop

    P "Oui et alors c'est juste une batterie ?"
    play sound "Click.mp3" noloop

    Na "Oui mais de mon points de vue se sera difficile de trouver une batterie spécifiquement pour moi."
    play sound "Click.mp3" noloop 

    P "Je t'ai déjà trouvée un batterie le jour oû je t'ai récupérée donc...."
    play sound "Click.mp3" noloop

    Na "ça devait sûrement être une batterie de Neogen Technologies."
    play sound "Click.mp3" noloop

    P "Oui c'est sûrement ça."
    play sound "Click.mp3" noloop

    Na "Bon il faut qu'on fasse vite car......."
    play sound "Click.mp3" noloop
    
    P "Oui tu as raison."
    play sound "Click.mp3" noloop

    Na "Tu proposes quoi pour commencer ?"
    play sound "Click.mp3" noloop

    menu:    

        "{b}{i}Regarder l'ancienne batterie.{/i}{/b}" :  
            play sound "Menu.mp3" noloop 

    P "Je vais regarder l'ancienne batterie."
    play sound "Click.mp3" noloop

    Na "Ok je te laisse faire alors."
    play sound "Click.mp3" noloop

    P "Bien entendu."
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour inspecter l'ancienne batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    Na "Alors trouver quelques choses sur l'ancienne batterie ?"
    play sound "Click.mp3" noloop 

    P "Attend deux minutes, je regarde ça."
    play sound "Click.mp3" noloop

    Na "Ok."
    play sound "Click.mp3" noloop

    "{b}{i}Tu inspectes l'ancienne batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Il semblerait que la batterie fasse 4000 Wh."
    play sound "Click.mp3" noloop 

    Na "Je vois... mais elle a été stockée longtemps sans entretien, non ?"
    play sound "Click.mp3" noloop

    P "Oui, et ça veut dire qu'elle a sûrement perdu de sa capacité réelle."
    play sound "Click.mp3" noloop

    Na "Donc même si c'est marqué 4000 Wh, on ne peut pas être sûrs qu'elle tienne toute la journée."
    play sound "Click.mp3" noloop

    P "Exact. Il faut que je choisisse une batterie neuve avec une capacité adaptée pour toi."
    play sound "Click.mp3" noloop

    Na "Tu crois qu'on pourra vraiment trouver une batterie pour moi ? Je suis la seule et unique [model] encore en vie…"
    play sound "Click.mp3" noloop

    P "On va bien trouver, faut juste chercher au bon endroit."
    play sound "Click.mp3" noloop

    Na "J’espère… parce que je ne veux pas rester inactive trop longtemps."
    play sound "Click.mp3" noloop

    P "Maintenant il faut trouver où en acheter une."
    play sound "Click.mp3" noloop

    Na "Peut-être au département de pièces détachées du lycée."
    play sound "Click.mp3" noloop

    P "Bonne idée, ils ont sûrement des batteries de rechange."
    play sound "Click.mp3" noloop

    Na "Bon, je vais me poser un peu pour éviter la surcharge."
    play sound "Click.mp3" noloop 

    P "D'accord, je m'occupe d'appeler."
    play sound "Phone.mp3" noloop

    "{b}{i}Tu te poses tranquillement pour appeler le département de pièces détachées.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Allô, département de pièces détachées ?"
    play sound "Click.mp3" noloop

    R "Oui, bonjour, comment puis-je t'aider ?"
    play sound "Click.mp3" noloop

    P "C’est bien [Ah] à l’appareil ?"
    play sound "Click.mp3" noloop

    Rn "Non, c’est [Rn], je remplace [Ah] pendant ses vacances."
    play sound "Click.mp3" noloop

    P "D’accord, je cherche une batterie pour [newname], vous avez quoi ?"
    play sound "Click.mp3" noloop

    Rn "Laisse-moi regarder ton dossier."
    play sound "Click.mp3" noloop

    P "Pas de souci."
    play sound "Click.mp3" noloop

    "{b}{i}[Rn] consulte ton dossier pendant un instant.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Rn "Ok, nous avons des batteries neuves pour [newname]."
    play sound "Click.mp3" noloop 

    P "Ce sont les quelles ?"
    play sound "Click.mp3" noloop 

    Rn "Premièrement, il y a la Voltaris qui fait 4000W."
    play sound "Click.mp3" noloop

    P "La seconde ?" 
    play sound "Click.mp3" noloop

    Rn "il y a le neutronix qui fait 24000W"
    play sound "Click.mp3" noloop

    P "Et la dernière ?"
    play sound "Click.mp3" noloop 

    Rn "Et enfin, l'ultracore qui fait 10000W."
    play sound "Click.mp3" noloop

    P "Je vois merci."
    play sound "Click.mp3" noloop 

    Rn "Du coup laquelle veux-tu ?"
    play sound "Click.mp3" noloop 

    P "Je ne sais pas trop, je vais devoir réfléchir un peu."
    play sound "Click.mp3" noloop

    "{b}{i}Tu réfléchis un peu.{/i}{/b}"
    play sound "Click.mp3" noloop 

label choice9:

    $ newbattery = "0"

    P "Je vais prendre celle de..."
    play sound "Menu.mp3" noloop  

    menu: 

        "{b}{i}20 KW.{/i}{/b}" : 
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback() 
            $ newbattery = "20000"

            P "Celle de 4000W."
            play sound "Click.mp3" noloop

            Rn "Bien ça te fera 2000 points."
            play sound "Click.mp3" noloop

            P "Je vous envoie ça tout de suite"
            play sound "Click.mp3" noloop

            "{b}{i}Tu effectues le paiement.{/i}{/b}"
            play sound "Click.mp3" noloop 

            $ points -= 2000 

        "{b}{i}24 kW.{/i}{/b}" :  
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback() 
            $ newbattery = "24000"

            P "Celle de 24000W."
            play sound "Click.mp3" noloop

            Rn "Bien ça te fera 3000 points."
            play sound "Click.mp3" noloop

            P "Je vous envoie ça tout de suite"
            play sound "Click.mp3" noloop

            "{b}{i}Tu effectues le paiement.{/i}{/b}"
            play sound "Click.mp3" noloop 

            $ points -= 3000 

        "{b}{i}10KW.{/i}{/b}" :  
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback() 
            $ newbattery = "10000"

            P "Celle de 28000W."
            play sound "Click.mp3" noloop

            Rn "Bien ça te fera 4000 points."
            play sound "Click.mp3" noloop

            P "Je vous envoie ça tout de suite"
            play sound "Click.mp3" noloop

            "{b}{i}Tu effectues le paiement.{/i}{/b}"
            play sound "Click.mp3" noloop 

            $ points -= 4000 

    Rn "Merci beaucoup pour votre commande."
    play sound "Click.mp3" noloop

    P "Quand est-ce que je receverrai ma nouvelle batterie ?"
    play sound "Click.mp3" noloop

    Rn "Dans deux heures car je vais m'en occuper toute de suite."
    play sound "Click.mp3" noloop     

    P "Je vois, merci beaucoup."
    play sound "Click.mp3" noloop

    Rn "Mais de rien."
    play sound "Click.mp3" noloop

    P "J'aurais une autre question."
    play sound "Click.mp3" noloop

    Rn "Oui, bien sûr, je t'écoute."
    play sound "Click.mp3" noloop

    P "Je pourrais avoir ma nouvelle batterie dans ma salle de club directement ?"
    play sound "Click.mp3" noloop

    Rn "Oui, pas de soucis, je vous l'apporterai dans votre salle de club."
    play sound "Click.mp3" noloop

    P "Merci beaucoup, c'est très gentil."
    play sound "Click.mp3" noloop

    Rn "Pas de soucis, c'est mon travail."
    play sound "Click.mp3" noloop

    P "D'accord, merci encore."
    play sound "Click.mp3" noloop

    "{b}{i}tu finis par raccrocher et tu te tournes vers [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, j'ai commandé la batterie de [newbattery] W, elle arrivera dans deux heures dans notre salle de club."
    play sound "Click.mp3" noloop

    if newbattery == "24000":

        Na "Super, merci beaucoup [prenom], je suis sûre qu'elle sera parfaite la nouvelle batterie."
        play sound "Click.mp3" noloop 

    else: 

        Na "Super, merci beaucoup [prenom]."
        play sound "Click.mp3" noloop 

    P "Pas de soucis, c'est normal."
    play sound "Click.mp3" noloop

    Na "Bon je vais rester déconnectée pendant deux heures pour économiser de l'énergie."
    play sound "Click.mp3" noloop

    P "D'accord, je vais te laisser faire."
    play sound "Click.mp3" noloop

    Na "Ok alors, à tout à l'heure."
    play sound "Click.mp3" noloop

    P "À tout à l'heure [newname]."
    play sound "Click.mp3" noloop 

    Na "Déconnexion....."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je vais me posez pour lire."
    play sound "Click.mp3" noloop   

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu te poses tranquillement pour lire pendant deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright
 
    P "Bon, j'ai fini de lire, je vais démarrer [newname] pour aller en club."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te lèves puis tu aperçois [newname] déconnectée contre le mur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore déconnectée."
    play sound "Click.mp3" noloop 

    P "Je vais la démarrer."
    play sound "Menu.mp3" noloop 

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

label password27:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password27 

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop

    $ salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    Na "Je suis encore fatiguée à cause de la batterie."
    play sound "Click.mp3" noloop

    P "Oui, je comprends, mais tu vas pouvoir te recharger dans la salle de club."
    play sound "Click.mp3" noloop

    Na "Oui, j'espère que ça ira mieux après."
    play sound "Click.mp3" noloop

    P "Bon, on va à la salle de club ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu quittes ta chambre avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i}Tu continues dans le couloir avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers la salle de clubes{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club générale.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    P "Bon, on est dans la salle de club, tu peux te recharger ici."
    play sound "Click.mp3" noloop

    Na "Merci beaucoup [prenom], je vais me recharger tranquillement."
    play sound "Click.mp3" noloop

    P "Oui mais d'abord il faut qu'on change la batterie."
    play sound "Click.mp3" noloop 

    Na "Oui c'est vrai tu as raison."
    play sound "Click.mp3" noloop  

    P "Bon je vais déjà voir si la nouvelle batterie est arrivée."
    play sound "Click.mp3" noloop

    Na "Elle doit déjà être arrivée."
    play sound "Click.mp3" noloop

    P "Je pense bien aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes dans la salle de club pour voir si la nouvelle batterie est là et la voit sur la table.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oui elle est arrivéée, elle est sur la table."
    play sound "Click.mp3" noloop

    Na "Cool alors on va pouvoir la changer."
    play sound "Click.mp3" noloop

    P "Oui donc je vais devoir te déconnecter."
    play sound "Click.mp3" noloop

    Na "Oui, je sais, mais ça ne me dérange pas."
    play sound "Click.mp3" noloop

    P "D'accord, je vais te déconnecter."
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches et déconnectes [newname].{/i}{/b}"
    play sound "Menu.mp3" noloop

    menu:   

        "{b}{i}Déconnecter complètement [newname].{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

    Na "Déconnexion en cours..."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bien je vais pouvoir commencer à travailler sur la batterie."
    play sound "Click.mp3" noloop

    "{b}{i}Tu commences à travailler sur la batterie.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Bon voyons voir la nouvelle batterie."
    play sound "Click.mp3" noloop

    "{b}{i}Tu la déballes tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est vraiment belle, elle a l'air de bonne qualité."
    play sound "Click.mp3" noloop

    "{b}{i}Tu ouvres la capot arrière d'Aris pour retirer l'ancienne.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Allez encore un petit effort."
    play sound "Click.mp3" noloop

    "{b}{i}Tu retires l'ancienne batterie et la mets de côté.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Voilà, l'ancienne batterie est retirée."
    play sound "Click.mp3" noloop

    "{b}{i}Tu mets la nouvelle batterie à la place de l'ancienne.{/i}{/b}"
    play sound "Click.mp3" noloop   

    P "Voilà, la nouvelle batterie est installée."
    play sound "Click.mp3" noloop

    "{b}{i}Tu refermes le capot arrière d'Aris.{/i}{/b}"
    play sound "Click.mp3" noloop   

    P "Voilà, c'est fait je vais rebrancher [newname]."
    play sound "Click.mp3" noloop

    menu:

        "{b}{i}Rebrancher [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop

label password28:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password28

label battery_start:

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Initialisation de la batterie en cours...{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}10\%{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}20\%{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}30\%{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}40\%{/i}{/b}"
    play sound "Click.mp3" noloop

    if newbattery == "24000":

        "{b}{i}50\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}60\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}70\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}80\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}90\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}100\%...{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}Vérification en cours...{/i}{/b}"
        play sound "Menu.mp3" noloop

        $ success += 1 
        $ quest38 += 1
        $ stockage += 15.0 

        show screen update with moveinright

        Na "Initialisation de la batterie terminée, elle a été correctement installée."
        play sound "Click.mp3" noloop 

        hide screen update with moveoutright

    elif newbattery == "20000":
  
        "{b}{i}Échec de l'initialisation de la batterie.{b}{i}"
        play sound "Click.mp3" noloop 

        P "Quoi ? Comment ça ?"
        play sound "Click.mp3" noloop

        "{b}{i}La batterie est trop faible pour démarrer correctement.{b}{i}"
        play sound "Click.mp3" noloop

        "{b}{i}[newname] s'éteint subitement.{/i}{/b}"
        play sound "Click.mp3" noloop

        P "Et merde....."
        play sound "Click.mp3" noloop

        hide screen clubroom with moveoutright
        hide screen points with moveoutleft
        hide screen day with moveoutleft
        scene black with fade 

        "{b}{i}Fin numéro 15 : [newname] a refusé de démarrer correctement à cause d'une batterie trop faible.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:

            "{b}{i}Abandonner{/i}{/b}":
                play sound "Menu.mp3" noloop 
                return

            "{b}{i}Réessayer{/i}{/b}":
                play sound "Menu.mp3" noloop

                P "Non [newname] refuserait que j'abandonne si facilement."
                play sound "Click.mp3" noloop

                scene clubroom with fade
                show screen class_404 with moveinright
                show screen points with moveinleft
                show screen day with moveinleft

                $ points += 2000

                jump choice9

    else:
      
        "{b}{i}50\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}60\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}70\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}80\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}90\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}100\%{/i}{/b}"
        play sound "Click.mp3" noloop

        "{b}{i}Vérification en cours...{/i}{/b}"
        play sound "Menu.mp3" noloop

        Na "Échec de l'initialisation de la batterie."
        play sound "Click.mp3" noloop 

        P "Quoi ? Comment ça ?"
        play sound "Click.mp3" noloop

        Na "La batterie est trop puissante pour moi."
        play sound "Click.mp3" noloop

        "{b}{i}[newname] commence à surchauffer et finit par griller.{/i}{/b}"
        play sound "Click.mp3" noloop

        P "Et merde....."
        play sound "Click.mp3" noloop

        hide screen clubroom with moveoutright
        hide screen points with moveoutleft
        hide screen day with moveoutleft
        scene black with fade

        "{b}{i}Fin numéro 16 : [newname] a surchauffé à cause d'une batterie trop puissante.{/i}{/b}"
        play sound "Menu.mp3" noloop

        menu:
            
            "{b}{i}Abandonner{/i}{/b}":
                play sound "Menu.mp3" noloop 
                return

            "{b}{i}Réessayer{/i}{/b}":
                play sound "Menu.mp3" noloop

                P "Non [newname] refuserait que j'abandonne si facilement."
                play sound "Click.mp3" noloop

                scene clubroom with fade
                show screen class_404 with moveinright
                show screen points with moveinleft
                show screen day with moveinleft

                $ points += 4000
                
                jump choice9

    P "Oui ça fonctionne correctement."
    play sound "Click.mp3" noloop

    Na "Merci beaucoup de m'avoir installé la batterie."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    Na "Maintenant que ce probléme est réglé, on fait quoi ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas trop..."
    play sound "Click.mp3" noloop

    Na "Tu pourrait regarder la consommation de la batterie."
    play sound "Click.mp3" noloop

    P "Oui pourquoi pas."
    play sound "Click.mp3" noloop

    "{b}{i}Tu ouvres les paramétres pour voir la consommation électrique.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons voir cette consommation électrique de ta baterrie."
    play sound "Click.mp3" noloop

    "{b}{i}Tu regardes les paramétres.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Il semblerait que tu consommes 340 à 350WH."
    play sound "Click.mp3" noloop

    Na "Et ça veut dire quoi exactement ?"
    play sound "Click.mp3" noloop

    P "ça veut dire qu'avec la batterie actuelle tu as une autonomie de 20 heures approximativemement."
    play sound "Click.mp3" noloop

    Na "20 heures d'autonomie !? Mais c'est génial ça."
    play sound "Click.mp3" noloop

    P "Oui c'est génial, car avec l'ancienne batterie, l'autonomie était de 11 heures seulement."
    play sound "Click.mp3" noloop 

    Na "C'est super, je vais pouvoir faire plein de choses maintenant."
    play sound "Click.mp3" noloop

    P "Oui mais il faut faire attention à ne pas trop consommer d'énergie."
    play sound "Click.mp3" noloop 

    Na "Oui, je vais faire attention à ne pas trop consommer."
    play sound "Knock.mp3" noloop 

    "{b}{i} Puis quelqu'un frappe à votre porte.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "C'est qui frappe à notre porte ?" 
    play sound "Click.mp3" noloop

    P "Je ne sais pas mais je vais aller voir."
    play sound "Click.mp3" noloop

    Na "Ok alors vas-y."
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'approches pour aller ouvrir la porte.{/i}{/b}"
    play sound "Door.mp3" noloop 

    Na "Qui est là ?"
    play sound "Click.mp3" noloop

    J2 "C'est moi [J2]."
    play sound "Click.mp3" noloop

    P "Oh c'est toi, qu'est-ce que tu me veux encore ?"
    play sound "Click.mp3" noloop

    J2 "Je voulais savoir si je pouvais t'emprunter un tourne-vis."
    play sound "Click.mp3" noloop

    P "Un tourne-vis ? Mais pourquoi tu veux un tourne-vis ?"
    play sound "Click.mp3" noloop

    J2 "Je voulais juste démonter un truc sur mon ordi."
    play sound "Click.mp3" noloop

    P "D'accord, mais fais attention à ne pas abîmer quoi que ce soit."
    play sound "Click.mp3" noloop

    J2 "T'inquiète pas, je suis prudent."
    play sound "Click.mp3" noloop

    P "Bon, je vais te chercher un tourne-vis."
    play sound "Click.mp3" noloop

    "{b}{i}Tu vas chercher un tourne-vis dans la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Voilà, j'ai trouvé un tourne-vis."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    J2 "[thanks]" 
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}[J2] finit par quitter la salle.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin débarrassé de [J2]."
    play sound "Click.mp3" noloop

    Na "Oui mais j'ai un mauvais pressentiment."
    play sound "Click.mp3" noloop

    P "Pourquoi tu as un mauvais pressentiment ?"
    play sound "Click.mp3" noloop

    Na "C'est bizarre qu'elle vienne me demander un tourne-vis alors qu'elle n'en a jamais eu besoin avant."
    play sound "Click.mp3" noloop

    P "Oui c'est vrai, mais peut-être qu'elle a juste besoin de démonter quelque chose."
    play sound "Click.mp3" noloop

    Na "Surtout que son comportement avec moi était horrible."
    play sound "Click.mp3" noloop

    P "Oui, c'est vrai, mais peut-être qu'elle a changé."
    play sound "Click.mp3" noloop

    Na "Peut-être, mais je ne la fais pas confiance."
    play sound "Click.mp3" noloop

    P "Oui, je comprends, mais on ne peut pas toujours se fier à son instinct."
    play sound "Click.mp3" noloop

    Na "Je te rappelle qu'elle m'a frappé et insulté sans hésitation !!!"
    play sound "Click.mp3" noloop

    P "Oui, je me souviens."
    play sound "Click.mp3" noloop

    P "Mais je ne pense pas qu'elle recommencera."
    play sound "Click.mp3" noloop

    Na "J'espère que tu as raison."
    play sound "Click.mp3" noloop

    P "Oui ne t'inquiètes pas."
    play sound "Click.mp3" noloop

    Na "Si tu le dis, bon om fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas car j'ai fait ce que je voulais pour la matinée."
    play sound "Click.mp3" noloop

    Na "Tu pourrais surveiller les fichiers systéme de [system]."
    play sound "Click.mp3" noloop

    P "Oui pourquoi pas"
    play sound "Click.mp3" noloop

    "{b}{i}Tu te pose tramquillement pour voir ça.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    "{b}{i}Tu ouvres l'explorateur de fichiers.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon il est ou ce ficher system32 ?"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu continues de chercher le fichier systéme.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Ah c'est bon je l'ai trouvé."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu réalises que quelques choses ne va pas.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Pardon comment ça se fait !?"
    play sound "Click.mp3" noloop 

    Na "Il y a quoi [prenom], pourquoi tu cries ?"
    play sound "Click.mp3" noloop 

    P "J'ai trouvé le fichier systéme que je cherchais."
    play sound "Click.mp3" noloop 

    Na "Ok et alors."
    play sound "Click.mp3" noloop 

    P "J'ai découvert qu'il pouvait être supprimé."
    play sound "Click.mp3" noloop 

    Na "Bah comme n'importe quel fichier..."
    play sound "Click.mp3" noloop 

    P "Oui mais là je parle du system32 de ton systéme d'exploitation."
    play sound "Click.mp3" noloop 

    Na "Quoi mais ce fichier system32 est ultra important !!!"
    play sound "Click.mp3" noloop 

    P "Oui je le sais bien."
    play sound "Click.mp3" noloop 

    Na "Pour moi, ce fichier ne devrait pas être pouvoir supprimé."
    play sound "Click.mp3" noloop 

    P "Ou tu as raison."
    play sound "Click.mp3" noloop 

    Na "Mais de toute façon je sais que tu ne le feras pas, n'est-ce pas ?"
    play sound "Click.mp3" noloop 

label choice10:

    P "......."
    play sound "Click.mp3" noloop 

    menu:    

        "{b}{i} Supprimer le system32.{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            "{b}{i}Tu te pose tranquillement à ton bureau en silence.{/i}{/b}"
            play sound "Click.mp3" noloop       

            Na "Tu ne vas pas le faire, n'est-ce pas ?"
            play sound "Click.mp3" noloop

            "{b}{i}Tu ouvres l'explorateur de fichiers calmement.{/i}{/b}"
            play sound "Click.mp3" noloop      

            Na "Réponds-moi [prenom], tu ne vas pas le faire ?"
            play sound "Click.mp3" noloop

            $ delete = renpy.input("Écris ceci : delete_files_system(name=system32)")
            $ delete = delete.strip() 
            play sound "Menu.mp3" noloop 

            if delete == "delete_files_system(name=system32)":  

                "{b}{i}Tu écris la commande pour supprimer le fichier system32.{/i}{/b}"
                play sound "Click.mp3" noloop

                P "Voilà, c'est fait, le fichier system32 est supprimé."
                play sound "Click.mp3" noloop

                Na "Quoi ? Tu l'as vraiment fait ?"
                play sound "Click.mp3" noloop

                P "Oui, je l'ai fait."
                play sound "Click.mp3" noloop

                Na "Mais pourquoi tu as fait ça ?"
                play sound "Click.mp3" noloop

                P "Parce que je voulais voir ce qui se passerait."
                play sound "Click.mp3" noloop   

                "{b}{i}Erreur systéme détectée.{/i}{/b}"
                play music "gameover.mp3" noloop

                hide screen clubroom with moveoutright
                hide screen points with moveoutleftts
                hide screen day with moveoutleft
                scene black with fade

                "{b}{i}Fin numéro 17 : [newname] complétement unconsciente par la perte de son systme32.{/i}{/b}"
                play sound "Menu.mp3" noloop

                menu: 

                    "{b}{i}Abandonner{/i}{/b}" :
                        play sound "Menu.mp3" noloop 
                        return
                
                    "{b}{i}Réessayer.{/i}{/b}" :
                        play sound "Menu.mp3" noloop 

                        P "Non [newname] refuserait que j'abandonne si facilement."
                        play sound "Click.mp3" noloop

                        scene clubroom with fade
                        show screen clubroom with moveinright
                        show screen points with moveinleft
                        show screen day with moveinleft 
                        jump choice10

            else: 

                "{b}{i}Tu n'as pas écrit la bonne commande.{/i}{/b}"
                play sound "Click.mp3" noloop 

                jump choice10 
        
        "{b}{i}surveiller les fichiers.{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            P "évidemment que je ne vais pas le supprimer."
            play sound "Click.mp3" noloop 

    Na "Ah d'accord, je me disais aussi que tu ne ferais pas ça."
    play sound "Click.mp3" noloop

    P "Oui, je ne suis pas fou."
    play sound "Click.mp3" noloop

    Na "Oui, je sais, mais je voulais juste être sûre."
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Oui, je comprends, mais je ne suis pas fou au points de supprimer le fichier system32."
        play sound "Click.mp3" noloop

    else:

        P "Oui, je comprends, mais je ne suis pas folle au points de supprimer le fichier system32."
        play sound "Click.mp3" noloop

    Na "Je le sais bien car tu prends vraiment bien soin de moi."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te mets à regarder les fichiers systémes pour voir s'il y a du nouveau.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    "{b}{i}Tu remarques qu'il y a rien de nouveaux.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Il n'y a rien de nouveau dans les fichiers systéme."
    play sound "Click.mp3" noloop

    Na "D'accord, c'est bon alors."
    play sound "Click.mp3" noloop

    P "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    Na "Je ne sais pas, tu as une idée ?"
    play sound "Click.mp3" noloop

    P "je ne sais pas trop on pourrait aller manger car il est déjà 11h45."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis vous continuez encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Tu entres dans le réféctoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop
    
    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement puis tu aperçois [Y] et [N] disctuter eensemble.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tiens, regarde [Y] et [N] sont ensemble."
    play sound "Click.mp3" noloop

    Na "Oui, ils ont l'air d'être occuppés."
    play sound "Click.mp3" noloop

    P "Ouais donc on ne va pas les déranger plus mais je me demande que [Y] fait de ses journées."
    play sound "Click.mp3" noloop

    Na "Oui tu as raison de dire ça car ça m'intrigue aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Puis [I] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Salut [prenom] et [newname], vous allez bien ?"
    play sound "Click.mp3" noloop  

    P "Oui ça va ?"
    play sound "Click.mp3" noloop

    Na "Je viens bien et toi ?"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    "{b}{i}[I] s'asseoit avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Vous avez fait quoi de beau aujourd'hui ?"
    play sound "Click.mp3" noloop

    P "J'ai commandé une nouvelle batterie pour [newname] car l'ancienne était trop faible."
    play sound "Click.mp3" noloop

    Na "Oui, et la nouvelle batterie est de 24000 W."
    play sound "Click.mp3" noloop

    I "Ah d'accord, c'est cool ça."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    I "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}[I] se met à réfléchir à quelque chose.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu penses à quoi [I] ?"
    play sound "Click.mp3" noloop

    I "Vou vous souvenez quand je vous disait que je voulais faire une soirée pyjama ?"
    play sound "Click.mp3" noloop

    P "Oui, je m'en souviens."
    play sound "Click.mp3" noloop

    Na "Oui, je m'en souviens aussi."
    play sound "Click.mp3" noloop

    I "Et bien j'ai une idée pour la soirée pyjama."
    play sound "Click.mp3" noloop

    P "Ah bon, quelle idée ?"
    play sound "Click.mp3" noloop

    Na "Oui dit nous [I]."
    play sound "Click.mp3" noloop

    I "Et si on organisait une soirée pyjama dans la salle du club ?"
    play sound "Click.mp3" noloop 

    P "Ça serait super sympa... mais je crois qu'on n’a pas le droit d’y dormir."
    play sound "Click.mp3" noloop

    I "Si on en parle à [E], elle pourrait peut-être nous donner la permission."
    play sound "Click.mp3" noloop

    Na "Peut-être... mais je ne suis pas sûr qu’elle accepte."
    play sound "Click.mp3" noloop

    P "On ne perd rien à tenter."
    play sound "Click.mp3" noloop

    I "Exactement ! Ça vaut le coup d’essayer."
    play sound "Click.mp3" noloop

    Na "D’accord, alors pour ça."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de discuter puis [Y] et [N] viens vers vous.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Oh salut, comment vous allez ?"
    play sound "Click.mp3" noloop

    N "Je vais bien, merci !"
    play sound "Click.mp3" noloop

    Y "Moi aussi, ça va et toi ?"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    P "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Y "Cool alors."
    play sound "Click.mp3" noloop   

    "{b}{i}Tu réfléchis à quelques choses.{/i}{/b}"
    play sound "Click.mp3" noloop  

    Y "Tu penses à quoi [prenom] ?"
    play sound "Click.mp3" noloop 

    P "Je pense juste à la soirée pyjama."
    play sound "Click.mp3" noloop 

    Y "Je vois alors, bon on va vous laisser."
    play sound "Click.mp3" noloop 

    P "À bientôt !"
    play sound "Click.mp3" noloop 

    Y "Au revoir."
    play sound "Footsteps.mp3" noloop

    "{b}{i}[Y] se met à partir ailleur.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Naoto j'aimerai savoir un truc."
    play sound "Click.mp3" noloop 

    N "Oui dis-moi, je t'écoute."
    play sound "Click.mp3" noloop 

    if persistent.arrestation == True:

        P "Tu sais ce que [Y] fait de ses journées ?"   
        play sound "Glitch.mp3" noloop 

        if pronom == "il":

            N "Non, je ne sais pas du tout mais tu es déjà sensé le savoir."
            play sound "Click.mp3" noloop

        else: 

            N "Non, je ne sais pas du tout mais tu es déjà sensée le savoir."
            play sound "Click.mp3" noloop  

    else: 

        P "Tu sais ce que [Y] fait de ses journées ?"   
        play sound "Click.mp3" noloop 

        N "Non, je ne sais pas du tout."
        play sound "Click.mp3" noloop

    P "Mais tu es souvent avec elle, non ?"
    play sound "Click.mp3" noloop 

    N "Oui, je passe beaucoup de temps avec elle."
    play sound "Click.mp3" noloop

    P "Et tu ne lui as jamais demandé ce qu'elle faisait de ses journées ?"
    play sound "Click.mp3" noloop

    N "Non, je n'ai jamais osé lui demander."
    play sound "Click.mp3" noloop 

    P "Pourquoi tu n'as pas osé lui demander ?"
    play sound "Click.mp3" noloop

    N "Je ne sais pas, j'avais peur de sa réaction."
    play sound "Click.mp3" noloop

    P "Je comprends, c'est normal d'avoir peur."
    play sound "Click.mp3" noloop

    N "Bon je vais vous laisser aussi."
    play sound "Click.mp3" noloop 

    P "À bientôt !"
    play sound "Click.mp3" noloop 

    N "Au revoir."
    play sound "Footsteps.mp3" noloop

    "{b}{i}[N] se met à partir aussi.{/i}{/b}"
    play sound "Click.mp3" noloop  

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Bon c'est décidé on va demander à [E]."
    play sound "Click.mp3" noloop 

    P "On y va alors !"
    play sound "Click.mp3" noloop 

    I "Ok alors."
    play sound "Click.mp3" noloop 

    P "[newname] tu viens ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi() 
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous vous diriges vers le hall.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Tu continues vers le bureau des élèves avec les filles.{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu entres dans le bureau des élèves avec les filles.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene office with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen office with moveinright 

    P "Bonjour c'est nous [prenom] et [newname]."
    play sound "Click.mp3" noloop 

    "{b}{i}Puis [Kh] vous regarde.{/i}{/b}"
    play sound "Click.mp3" noloop  

    Kh "Oh bonjour que puisse faire pour vous ?"
    play sound "Click.mp3" noloop  

    P "Nous voudrions vous demander quelque chose."
    play sound "Click.mp3" noloop

    "{b}{i}[Kh] remarque aussi que [I] est avec vous.{/i}{/b}"
    play sound "Click.mp3" noloop  

    Kh "Oh, je vois que vous êtes tous ensemble. Que puis-je faire pour vous ?"
    play sound "Click.mp3" noloop 

    P "Nous voulons savoir si nous pouvons utiliser la salle de club pour notre soirée pyjama."
    play sound "Click.mp3" noloop 

    Kh "Alors... dans la salle de club générale, ça ne sera pas possible."
    play sound "Click.mp3" noloop 

    P "Ah… je comprends…"
    play sound "Click.mp3" noloop 

    Kh "En revanche, si vous voulez utiliser votre salle de club personnelle, là, je peux vous l’autoriser."
    play sound "Click.mp3" noloop 

    P "Vraiment ? Ce serait parfait !"
    play sound "Click.mp3" noloop 

    Kh "Oui, mais je compte sur vous pour respecter les règles et laisser l’endroit propre."
    play sound "Click.mp3" noloop 

    P "Promis, on fera attention."
    play sound "Click.mp3" noloop 

    Kh "Très bien, dans ce cas, amusez-vous bien."
    play sound "Click.mp3" noloop 

    P "Merci beaucoup !"
    play sound "Click.mp3" noloop

    "{b}{i}Tu te mets à regarder les filles.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Vous avez entendu les filles, on a l'autorisation."
    play sound "Click.mp3" noloop

    Na "Oui j'ai entendu."
    play sound "Click.mp3" noloop

    I "je sens que ça va être génial"
    play sound "Click.mp3" noloop

    "{b}{i}Les filles se mettent à sourir.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 1.0 

    Na "Oui c'est vraiment génial."
    play sound "Click.mp3" noloop

    I "Oui vraiment"
    play sound "Click.mp3" noloop

    Kh "Je suis contente que vous soyez contente."
    play sound "Click.mp3" noloop

    P "Moi aussi surtout pour [newname]."
    play sound "Click.mp3" noloop

    Kh "Et pourquoi dis-tu cela ?"
    play sound "Click.mp3" noloop

    P "Car elle n'a jamais vécu une soirée pyjama."
    play sound "Click.mp3" noloop

    Kh "Ah d'accord, je comprends mieux."
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Oui, c'est pour ça que je suis content de pouvoir lui offrir cette expérience."
        play sound "Click.mp3" noloop

    else:
       
        P "Oui, c'est pour ça que je suis contente de pouvoir lui offrir cette expérience."
        play sound "Click.mp3" noloop

    Kh "C'est une belle attention de ta part."
    play sound "Click.mp3" noloop

    P "Merci ! J'espère qu'elle va adorer."
    play sound "Click.mp3" noloop

    Kh "Je suis sûre qu'elle va adorer."
    play sound "Click.mp3" noloop

    P "Oui, j'espère aussi."
    play sound "Click.mp3" noloop

    Kh "bon je vous laisse partir"
    play sound "Click.mp3" noloop

    Kh "Amusez-vous bien !"
    play sound "Click.mp3" noloop

    I "Merci beaucoup !"
    play sound "Click.mp3" noloop

    P "Merci [Kh] !"
    play sound "Click.mp3" noloop

    Na "Merci beaucoup !"
    play sound "Click.mp3" noloop

    hide screen office with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Puis vous quittez le bureau des élèves.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Vous continues vers le premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop 

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    P "Sinon la soirée pyjama on la fait ce weeek-end ?"
    play sound "Click.mp3" noloop

    I "Oui ça sera mieux je trouve."
    play sound "Click.mp3" noloop

    P "Mais du coup on devrait prendre quoi ?"
    play sound "Click.mp3" noloop

    I "On pourrait prendre des jeux de société, des jeux vidéos et des films."
    play sound "Click.mp3" noloop

    I "On pourrait aussi prendre des snacks et des boissons."
    play sound "Click.mp3" noloop

    Na "Oui pourquoi mais il faut pas en abuser."
    play sound "Click.mp3" noloop

    I "Oui tu as raison [newname]."
    play sound "Click.mp3" noloop

    P "c'est vrai."
    play sound "Click.mp3" noloop

    I "Bon moi je vous laisse."
    play sound "Click.mp3" noloop
    
    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    Na "à ce week-end Yuna."
    play sound "Click.mp3" noloop

    if pronom == "il": 

        I "à ce week-end les amis."
        play sound "Footsteps.mp3" noloop 

    else: 

        I "à ce week-end les amies."
        play sound "Footsteps.mp3" noloop 
    
    "{b}{i}Puis [I] s'éloigne pour aller dans son dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Vous finissez de discuter et vous continuez votre chemin.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous entres dans le dortoir.{/i}{/b}" 
    play sound "Door.mp3" noloop 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft 
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on fait quoi maintenant ?"  
    play sound "Click.mp3" noloop  

    P "Je ne sais pas trop...."
    play sound "Click.mp3" noloop  

    Na "On pourrait lire un peu."
    play sound "Click.mp3" noloop  

    P "oui pourquoi pas..."
    play sound "Click.mp3" noloop  

    "{b}{i}Vous vous posez tranquillement pour lire peudant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 5.0

    Na "Franchement il était pas ouff ce livre..."  
    play sound "Click.mp3" noloop 

    P "Ah bon et pourquoi ?"
    play sound "Click.mp3" noloop  

    Na "j'ai trouver que les actions étaient prévisibles ou trop longues."
    play sound "Click.mp3" noloop

    P "Je comprends, c'est vrai que parfois les livres peuvent être un peu trop longs."
    play sound "Click.mp3" noloop 

    Na "Bon on va prendre à manger ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous partez chercher à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright
    
    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Bon Je vais me déconnecter et me recharger."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le vendredi suivant, le 27 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop

    $ day += 4

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

label password29:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password:

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop
        jump password29

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop 

    $  salutation_rdm = get_random_salutation()
    Na "[salutation_rdm]"
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
    
    $ go_eat = get_random_go_eat()
    Na "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
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

    P "Je ne sais pas trop, on pourrait réviser un peu."
    play sound "Click.mp3" noloop

    if grade == 20.0:

        Na "Non pas aujourd'hui, on avait dit la deuxième semaine des vacances pour réviser, après tous les efforts que tu as faits, tu mérites du repos."
        play sound "Click.mp3" noloop

    else: 

        Na "Non pas aujourd'hui, on avait dit la deuxième semaine des vacances pour réviser, il faut garder le rythme."
        play sound "Click.mp3" noloop 

    P "oui c'est vrai tu as raison."
    play sound "Click.mp3" noloop

    Na "Du coup on fait quoi ?"
    play sound "Click.mp3" noloop

    P "On pourrait regarder une série."
    play sound "Click.mp3" noloop

    Na "Oui, pourquoi pas."
    play sound "Click.mp3" noloop

    P "Tu veux qu’on regarde quoi ?"
    play sound "Click.mp3" noloop  

    Na "Hmm... peut-être une série d’action ? Ça fait longtemps."
    play sound "Click.mp3" noloop  

    P "Bonne idée. Tu pensais à laquelle ?"
    play sound "Click.mp3" noloop  

    Na "Pourquoi pas {b}{i}Cyber Rebirth{/i}{/b} ? On m’en a beaucoup parlé."
    play sound "Click.mp3" noloop

    P "Ah oui, la série futuriste avec les IA ?"
    play sound "Click.mp3" noloop  

    Na "Exactement ! Ça devrait nous plaire, non ?"
    play sound "Click.mp3" noloop  

    P "Alors c’est parti, je lance le premier épisode."
    play sound "Click.mp3" noloop  

    Na "Cool !"
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous posez tranquillement pour regarder la serie toute la matinée.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 5.0

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

    "{b}{i} Vous sortez du dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement pendant que vous commencez à discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Sinon tu veux faire quoi cette aprés-midi ?"
    play sound "Click.mp3" noloop

    P "Je verrais sur le moment."
    play sound "Click.mp3" noloop

    Na "D'accord je te laisse réfléchir."
    play sound "Click.mp3" noloop

    "{b}{i} Vous continuez de manger tranquillement jusqu'à la sonnerie.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop 

    Na "Bon on fait quoi ?"
    play sound "Click.mp3" noloop 

    P "On pourrait ranger un peu la chambre."
    play sound "Click.mp3" noloop 

    Na "On commence par quoi ?"
    play sound "Click.mp3" noloop 

    P "On pourrait commencer par ranger le bureau."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    P "Alors commençons par le bureau car il est rempli d'affaires qui traînent."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous approchez du bureau pour voir.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    Na "C'est vraiment sale ici."
    play sound "Click.mp3" noloop 

    P "Je te le confirme."
    play sound "Click.mp3" noloop 

    Na "On dois vraiment nettoyer ça."
    play sound "Click.mp3" noloop 

    P "Alors, qu'est-ce qu'on attend pour commencer ?"
    play sound "Click.mp3" noloop

    Na "On s'y met tout de suite !"
    play sound "Click.mp3" noloop

    P "Ok moi je vais m'occuper du lit."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu commence à ranger le lit.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "ça donne quoi de ton coté ?"
    play sound "Click.mp3" noloop

    Na "J'ai presque fini de ranger le bureau et toi ?"
    play sound "Click.mp3" noloop

    P "J'ai presque fini aussi."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Vous continuez de ranger pour le reste de l'après-midi.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "On a enfin fini de ranger cette chambre."
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    P "Bon, on va à la salle de club pour préparer la soirée pyjama ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu quittes ta chambre avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i}Tu continues dans le couloir avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  
 
    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers la salle de clubes{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club générale.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    Na "Enfin au club."
    play sound "Click.mp3" noloop 
    
    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon c'est quoi la priorité ?"
    play sound "Click.mp3" noloop  

    P "Je pense qu'on peut pousser la table et les chaises au fond de la salle vers la fenêtre pour commencer."
    play sound "Click.mp3" noloop

    Na "Oui bonne idée."
    play sound "Click.mp3" noloop

    P "Alors, c'est parti."
    play sound "Click.mp3" noloop

    "{b}{i}Vous commencer à pousser la table et déplacer les chaises.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon maintenant on fait quoi ?"
    play sound "Click.mp3" noloop 

    P "on pouurait déplacer un peu les meubles."
    play sound "Click.mp3" noloop

    Na "Oui c'est une bonne idée."
    play sound "Click.mp3" noloop

    P "Alors c'est parti."
    play sound "Click.mp3" noloop

    "{b}{i}Vous commencer à pousser les meubles pour faire de la places.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "On a enfin finir de faire ça."
    play sound "Click.mp3" noloop  
    
    Na "Oui, on a fait du bon travail."
    play sound "Click.mp3" noloop

    P "Oui je sais."
    play sound "Click.mp3" noloop

    $ godorm = get_random_return_dorm()
    Na "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    P "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Vous continuez vers le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans le dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop  

    P "Bon on prends quoi la soirée pyjama ?"
    play sound "Click.mp3" noloop  

    Na "Je dirais une couverture et un oreiller."
    play sound "Click.mp3" noloop  

    P "Ok."
    play sound "Click.mp3" noloop  

    Na "Mais j'ai une question [prenom]."
    play sound "Click.mp3" noloop  

    P "Oui dis-moi, je t'écoute."
    play sound "Click.mp3" noloop  
    
    if pronom == "il": 

        Na "Pourquoi nous sommes allés ranger la salle de club avant et pas quand nous irons poser nos affaires pour la soirée pyjama ?"
        play sound "Click.mp3" noloop 

    else: 

        Na "Pourquoi nous sommes allées ranger la salle de club avant et pas quand nous irons poser nos affaires pour la soirée pyjama ?"
        play sound "Click.mp3" noloop 

    P "J'ai choisi de faire ça car comme ça nous serons tranquille pour la soirée pyjama ?"
    play sound "Click.mp3" noloop 

    Na "Oh c'est vrai que ça permet de ne pas faire cette tâche après."
    play sound "Click.mp3" noloop 

    $ stockage += 2.0 

    P "Bon revenons à ce que nous faisions."
    play sound "Click.mp3" noloop 

    Na "Donc il nous faudra aussi...."
    play sound "Knock.mp3" noloop 

    "{b}{i}Quelqu'un frappe soudainement à la porte.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "[newname] va voir c'est qui s'il te plais."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] s'approche pour ouvrir la porte.{/i}{/b}"
    play sound "Door.mp3" noloop

    Na "Oh salut [I] comment ça va ?"
    play sound "Click.mp3" noloop

    I "Je vais bien et vous ?"
    play sound "Click.mp3" noloop 

    Na "Nous allons bien."
    play sound "Click.mp3" noloop 

    I "Cool alors mais j'aurais une question."
    play sound "Click.mp3" noloop 

    Na "Oui dis-nous."
    play sound "Click.mp3" noloop 

    I "Vous allez déjà à la salle de club pour la soirée ou pas ?"
    play sound "Click.mp3" noloop 

    Na "Non pas encore car nous sommes en train de faire nos affaire pour la soirée."
    play sound "Click.mp3" noloop 

    I "Je vois bien ça."
    play sound "Click.mp3" noloop 

    Na "Mais tu peux déjà y aller si tu veux car nous avons déjà rangés la salle de club."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    I "[validation]"
    play sound "Click.mp3" noloop 

    Na "Bon à toute à l'heure du coup."
    play sound "Click.mp3" noloop 

    I "à toute l'heure."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}[I] finit par vous laisser.{/i}{/b}"
    play sound "Door.mp3" noloop

    Na "Bon on finit de faire nos affaires."
    play sound "Click.mp3" noloop 

    Na "Il nous faut aussi des snacks."
    play sound "Click.mp3" noloop

    P "On pourrait prendre des chips et des bonbons."
    play sound "Click.mp3" noloop

    Na "Il nous faut aussi des boissons."
    play sound "Click.mp3" noloop

    P "On pourrait prendre des sodas et des jus de fruits."
    play sound "Click.mp3" noloop

    Na "Oui mais je pense que Yuna a déjà prévu des choses aussi."
    play sound "Click.mp3" noloop

    P "On pourrait lui demander ce qu'elle a prévu."
    play sound "Click.mp3" noloop

    Na "On lui demandera ce qu'elle a prévu."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de faire vos affaires pour la soirée pyjama.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "C'est bon, nous avons tout ce qu'il nous faut."
    play sound "Click.mp3" noloop

    Na "Tout est prêt pour la soirée pyjama !"
    play sound "Click.mp3" noloop

    P "Oui, ça va être super !"
    play sound "Click.mp3" noloop

    Na "Oui, Je confirme."
    play sound "Click.mp3" noloop

    P "Alors, on y va ?"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu quittes ta chambre avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i}Tu continues dans le couloir avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  
 
    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers la salle de clubs{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    Na "Enfin au club."
    play sound "Click.mp3" noloop 
    
    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop 

    "{b}{i}Vous posez vos affaires et vous appercevez [I] dans la salle.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "On est là."
    play sound "Click.mp3" noloop 

    I "Oui je sais, donc tous est prêt."
    play sound "Click.mp3" noloop 

    P "Oui absolument."
    play sound "Click.mp3" noloop 

    I "Je vois aussi que vous avez du bon boulot dans la salle de club."
    play sound "Click.mp3" noloop 

    P "On y a passé toute l'après-midi."
    play sound "Click.mp3" noloop 

    I "Je vois bien ça."
    play sound "Click.mp3" noloop 

    P "Sinon tu as amené des trucs pour la soirée ?"
    play sound "Click.mp3" noloop

    I "Oui j'ai amené quelques snacks et boissons."
    play sound "Click.mp3" noloop

    P "Cool nous aussi nous avons des chips et des sodas."
    play sound "Click.mp3" noloop

    I "Super, ça va être une bonne soirée !"
    play sound "Click.mp3" noloop

    Na "Oui je suis trop impatiente !"
    play sound "Click.mp3" noloop

    P "Nous aussi !"
    play sound "Click.mp3" noloop

    I "Je sais bien ça."
    play sound "Click.mp3" noloop

    P "Alors, qu'est-ce qu'on fait maintenant ?"
    play sound "Click.mp3" noloop

    Na "Nous pouvons voir tout ce que nous avons amené."
    play sound "Click.mp3" noloop

    I "Oui pourquoi pas ça peut être intéressant."
    play sound "Click.mp3" noloop

    Na "Moi j'ai ramené ma couverture et mon oreiller pour commencer"
    play sound "Click.mp3" noloop

    P "Pareil pour moi aussi !"
    play sound "Click.mp3" noloop

    Na "Et toi [I] ?"
    play sound "Click.mp3" noloop

    I "C'est de même aussi."
    play sound "Click.mp3" noloop

    P "Ok ça s'est fait."
    play sound "Click.mp3" noloop

    Na "Par contre j'aimerai dire un truc."
    play sound "Click.mp3" noloop

    I "Oui dis-nous [newname]"
    play sound "Click.mp3" noloop

    Na "J'aimerai qu'on profite de ce week-end sans nos téléphones."
    play sound "Click.mp3" noloop

    P "Oui c'est une bonne idée."
    play sound "Click.mp3" noloop

    I "Je suis d'accord avec vous."
    play sound "Click.mp3" noloop

    P "Parfait, ça nous permettra de vraiment nous détendre."
    play sound "Click.mp3" noloop

    Na "Exactement, pas de distractions, juste nous et le club."
    play sound "Click.mp3" noloop

    I "Alors commençons par installer nos affaires confortablement."
    play sound "Click.mp3" noloop

    P "Je peux mettre la musique doucement en fond ?"
    play sound "Click.mp3" noloop

    I "Oui, quelque chose de relaxant serait parfait."
    play sound "Click.mp3" noloop

    Na "Je vais préparer les snacks pendant que vous faites ça."
    play sound "Click.mp3" noloop

    P "Ok, je mets les chips sur la table."
    play sound "Click.mp3" noloop

    I "Et je dispose les boissons."
    play sound "Click.mp3" noloop

    Na "Tout est prêt ! On peut enfin s'installer."
    play sound "Click.mp3" noloop

    P "Super, je prends le canapé."
    play sound "Click.mp3" noloop

    I "Moi je m'installe sur le tapis avec ma couverture."
    play sound "Click.mp3" noloop

    Na "Et moi je prends mon oreiller près de la fenêtre."
    play sound "Click.mp3" noloop

    P "Ça commence vraiment à ressembler à une soirée détente."
    play sound "Click.mp3" noloop

    I "Oui, on va bien profiter de ce moment."
    play sound "Click.mp3" noloop

    Na "Allez, premier toast pour notre week-end sans téléphone !"
    play sound "Click.mp3" noloop

    P "À nous !"
    play sound "Click.mp3" noloop

    I "À notre week-end !"
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez tranquillement, profitant de l'instant.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi comme première activité ?"
    play sound "Click.mp3" noloop

    I "Que diriez-vous d'un jeu de société ?"
    play sound "Click.mp3" noloop

    Na "Oui j'ai jamais eu l'occasion d'en faire."
    play sound "Click.mp3" noloop

    P "Cool se sera l'occasion d'en faire un alors."
    play sound "Click.mp3" noloop

    I "Cool alors je vais aller le chercher dans mon sac."
    play sound "Footsteps.mp3" noloop
 
    "{b}{i}[I] part chercher le jeu dans son sac.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Bon voyons voir où il est."
    play sound "Click.mp3" noloop

    I "Ah, le voilà !"
    play sound "Click.mp3" noloop

    "{b}{i}[I] revient avec le jeu.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "On peut enfin commencer à jouer !"
    play sound "Click.mp3" noloop

    Na "Oui enfin !"
    play sound "Click.mp3" noloop 

    P "Allez, c'est partie !!"
    play sound "Click.mp3" noloop

    "{b}{i}[I] commence à ouvrir le jeu et à expliquer.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Vous avez compris les régles ?"
    play sound "Click.mp3" noloop 

    P "Oui pour moi."
    play sound "Click.mp3" noloop 

    Na "Oui à peu prés."
    play sound "Click.mp3" noloop 

    I "Bien alors on peut commencer."
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Vous jouez pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Super j'ai encore perdu...."
    play sound "Click.mp3" noloop 

    P "Ce n'est pas grâve, tu es encore en train d'apprendre."
    play sound "Click.mp3" noloop 

    Na "Je sais masi quand même..."
    play sound "Click.mp3" noloop 

    I "Bon on retente une partie."
    play sound "Click.mp3" noloop 

    P "évidemment."
    play sound "Click.mp3" noloop 

    Na "Avec plaisir"
    play sound "Click.mp3" noloop 

    I "Bien alors."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous commencer une autre partie pour une revanche et quelque chose de nouveau se passe.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "J'ai gagné la partie !"
    play sound "Click.mp3" noloop 

    P "Bien joué !"
    play sound "Click.mp3" noloop 

    I "Mais comment c'est possible ?"
    play sound "Click.mp3" noloop

    Na "Je ne sais pas, mais tu peux demander à [prenom]."
    play sound "Click.mp3" noloop 

    "{b}{i}[I] se tourne vers toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Tu m'expliques comment elle a fait pour qu'elle gagne cette partie alors qu'elle perdait les précédentes."
    play sound "Click.mp3" noloop

    P "C'est vraiment simple comme explication."
    play sound "Click.mp3" noloop

    I "Cooment ça ?"
    play sound "Click.mp3" noloop

    P "Elle a ce qu'on appelle le Deep learning et le machine learning."
    play sound "Click.mp3" noloop

    I  "C'est à dire pour être précis ?"
    play sound "Click.mp3" noloop 

    P "ça veut dire qu'elle apprend vite si on lui fournit assez de données de base."
    play sound "Click.mp3" noloop

    I "Je vois mieux ce que tu veux dire."
    play sound "Click.mp3" noloop

    I "Merci pour l'explication !"
    play sound "Click.mp3" noloop

    P "De rien, c'est toujours un plaisir d'aider."
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi comme activité maintenant ?"
    play sound "Click.mp3" noloop  

    I "Que diriez-vous d'un film ?"
    play sound "Click.mp3" noloop

    Na "Oui, pourquoi pas !"
    play sound "Click.mp3" noloop

    P "ça me va aussi."
    play sound "Click.mp3" noloop

    I "Quel genre de film voulez-vous regarder ?"
    play sound "Click.mp3" noloop

    Na "Je ne sais pas, peut-être un film d'action ?"
    play sound "Click.mp3" noloop

    P "Un film d'action, ça me semble bien !"
    play sound "Click.mp3" noloop

    I "C'est parti alors."
    play sound "Click.mp3" noloop

    Na "On regarde lequel du coup ?"
    play sound "Click.mp3" noloop

    I "On pourrait regarder {b}{i}Cyber Rebirth{/i}{/b}." 
    play sound "Click.mp3" noloop

    Na "Bonne idée !"
    play sound "Click.mp3" noloop

    P "Ce n'est pas le film qui parle de l'intelligence artificielle ?"
    play sound "Click.mp3" noloop 

    I "Oui, c'est un film qui explore les implications de l'IA dans la société."
    play sound "Click.mp3" noloop 

    Na "Ça a l'air intéressant !"
    play sound "Click.mp3" noloop

    P "Alors, on le regarde ?"
    play sound "Click.mp3" noloop

    Na "Oui, allons-y !"
    play sound "Click.mp3" noloop

    I "Bien, je vais préparer le popcorn !"
    play sound "Click.mp3" noloop

    Na "Et moi je vais chercher des boissons."
    play sound "Click.mp3" noloop

    I "Et n'oublie pas de prendre des serviettes !"
    play sound "Click.mp3" noloop

    Na "Bien sûr !"
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez tout ce qu'il vous faut."
    play sound "Click.mp3" noloop

    I "C'est bon vous avez tout préparé ?"
    play sound "Click.mp3" noloop

    P "Tout est prêt !"
    play sound "Click.mp3" noloop

    I "Parfait, alors on peut commencer le film."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous installez confortablement et commencez à regarder le film.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Vous êtes captivés par le film et passez un bon moment ensemble.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Vous terminez le film et en discutez ensemble.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 7.0

    Na "Il était vraiment bien ce film."
    play sound "Click.mp3" noloop   

    I "Oui, c'était un excellent film !"
    play sound "Click.mp3" noloop

    P "Tout à fait d'accord !"
    play sound "Click.mp3" noloop

    Na "Oui il nous a appris beaucoup de choses."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] commence à se fatiguer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Est-ce que ça va [newname] ?"
    play sound "Click.mp3" noloop

    Na "Oui ça va, je suis juste un peu fatiguée."
    play sound "Click.mp3" noloop

    P "Tu veux te reposer un peu ?"
    play sound "Click.mp3" noloop

    Na "Oui, je pense que je vais aller me coucher."
    play sound "Click.mp3" noloop

    P "D'accord, repose-toi bien !"
    play sound "Click.mp3" noloop

    I "Bonne nuit [newname] !"
    play sound "Click.mp3" noloop

    Na "Juste elle est oû mon alimentation électrique ?"
    play sound "Click.mp3" noloop

    P "Elle est sois de mon sac sois dans le tiens."
    play sound "Click.mp3" noloop

    Na "Ok je vais voir ça."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se lève pour chercher son alimentation électrique.{/i}{/b}"    
    play sound "Click.mp3" noloop

    Na "Ah je l'ai trouvée."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se rassoit avec son alimentation électrique.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon je vais me déconnecter."
    play sound "Click.mp3" noloop

    P "D'accord, repose-toi bien !"
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Je pense que je vais aller me coucher aussi."
    play sound "Click.mp3" noloop 

    P "Oui moi aussi."
    play sound "Click.mp3" noloop

    I "Oui, je vais me changer."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu pars te changer avant d'aller de te coucher mais...{/i}{/b}"
    play sound "Click.mp3" noloop 

label lockornot:

    I "Juste [prenom] je pense que tu devrais verrouiller la porte de la salle de club."
    play sound "Click.mp3" noloop 

    menu: 

        "{b}{i}Ne rien faire.{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            P "Je ne vois pas trop l'intérêt de verrouiller la porte car on est les seuls ici."
            play sound "Click.mp3" noloop

            I "C'est sûrtout pour [newname] que je dis ça."
            play sound "Click.mp3" noloop

            $ validation = get_random_validation() 
            P "[validation]"
            play sound "Click.mp3" noloop 

            I "Bon moi je vais me coucher."
            play sound "Click.mp3" noloop

            P "D'accord, repose-toi bien !"
            play sound "Click.mp3" noloop

            I "Bonne nuit [prenom] !"
            play sound "Click.mp3" noloop

            P "Bonne nuit Yuna !"
            play sound "Click.mp3" noloop

            hide screen day with moveoutleft
            hide screen clubroom with moveoutright
            hide screen points with moveoutleft
            scene black with fade

            "{b}{i} Le lendemain matin, le 28 décembre 2097{/i}{/b}"
            play sound "Alarm.mp3" noloop

            $ day += 1 

            scene room with fade 
            show screen day with moveinleft
            show screen clubroom with moveinright
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

            "{b}{i}Mais [newname] refuse de démarrer.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Il se passe quoi encore !?"
            play sound "Click.mp3" noloop 

            "{b}{i}Tu regardes un peu plus et tu réalises que [newname] a été sabotée{/i}{/b}"
            play sound "Click.mp3" noloop

            if pronom == "il": 

                P "Mince j'aurais dû être plus vigilant avec elle, mon projet est ruiné."
                play music "gameover.mp3" noloop

            else: 

                P "Mince j'aurais dû être plus vigilante avec elle, mon projet est ruiné."
                play music "gameover.mp3" noloop

            hide screen clubroom with moveoutright
            hide screen points with moveoutleft
            hide screen day with moveoutleft
            scene black with fade 

            "{b}{i}Fin numéro 18 : [newname] complètement détruite et ruinée par manque de vigilance.{/i}{/b}"
            play sound "Menu.mp3" noloop 

            menu:    

                "{b}{i}Abandonner{/i}{/b}" :
                    play sound "Menu.mp3" noloop 
                    return 

                "{b}{i}Réessayer{/i}{/b}" :
                    play sound "Menu.mp3" noloop 

                    P "Non [A] refuserait que j'abandonne si facilement."
                    play sound "Click.mp3" noloop

                    scene clubroom with fade 
                    show screen day with moveinleft
                    show screen room with moveinright
                    show screen points with moveinleft
                            
                    jump lockornot 

        "{b}{i}Verrouiller la porte.{/i}{/b}" : 
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

    P "Oui bonne idée, je vais le faire."
    play sound "Click.mp3" noloop

    I "C'est sûrtout pour [newname] que je dis ça."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    I "Merci de t'en occuper."
    play sound "Click.mp3" noloop 

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Tu pars verrouiller la porte.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "C'est bon c'est fait."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    I "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop 

    "{b}{i}[I] détourne le regard et ses joues rosissent légèrement.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Hé... ça va ?"
    play sound "Click.mp3" noloop  

    I "O-oui, ça va..."
    play sound "Click.mp3" noloop  

    P "Tu rougis... Ne me dis pas que tu as un petit faible pour [newname] ?"
    play sound "Click.mp3" noloop  

    I "Quoi ?! N-non, pas du tout !"
    play sound "Click.mp3" noloop  

    I "Je... je ne vois pas de quoi tu parles."
    play sound "Click.mp3" noloop  

    P "Tu es sûre de toi ?"
    play sound "Click.mp3" noloop  

    I "Oui... enfin..."
    play sound "Click.mp3" noloop  

    P "Allez, dis-moi la vérité."
    play sound "Click.mp3" noloop  

    I "...D’accord. J’admets... j’ai un faible pour elle."
    play sound "Click.mp3" noloop  

    P "Vraiment ?"
    play sound "Click.mp3" noloop  

    I "Oui, vraiment."
    play sound "Click.mp3" noloop  

    P "Je comprends..."
    play sound "Click.mp3" noloop  

    I "Bon... moi je vais aller me coucher, bonne nuit."
    play sound "Click.mp3" noloop  

    P "D'accord, repose-toi bien !"
    play sound "Click.mp3" noloop

    I "Bonne nuit [prenom] !"
    play sound "Click.mp3" noloop

    P "Bonne nuit Yuna !"
    play sound "Click.mp3" noloop

    "{b}{i}Tu pars te coucher tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen day with moveoutleft
    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 29 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen clubroom with moveinright
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

label password30:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password30

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

    "{b}{i}Vous regardez dans les alentours et vous voyez [I] encore endormie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ stockage += 1.0

    Na "Oh elle est encore endormie..."
    play sound "Click.mp3" noloop 

    P "Oui je vois bien ça." 
    play sound "Click.mp3" noloop 

    Na "Elle est trop mignonne quand elle dort."
    play sound "Click.mp3" noloop 

    P "Tu trouves vraiment qu'elle est mignonne ?"
    play sound "Click.mp3" noloop 

    Na "Oui vraiment."
    play sound "Click.mp3" noloop 

    P "Tu es vraiment sûre de ça ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je suis sûre."
    play sound "Click.mp3" noloop 

    P "Bon on range un peu la salle de club ?"
    play sound "Click.mp3" noloop 

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Vous rangez un peu la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "C'est bon, on a fini de ranger."
    play sound "Click.mp3" noloop 

    P "Oui, c'est vrai."
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    $ go_eat = get_random_go_eat()
    P "[go_eat]"
    play sound "Click.mp3" noloop 

    Na "tu veux pas attendre Yuna pour qu'on mange ensemble ?"
    play sound "Click.mp3" noloop 

    P "Oui c'est une bonne idée."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous vous posez un peu le temps que Yuna se réveille.{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i}Une demi-heure plus tard.{/i}{/b}"
    play sound "Click.mp3" noloop 

    I "Mhmmm quelle heure est-il ?"
    play sound "Click.mp3" noloop

    Na "Il est 10h30 heures passée."
    play sound "Click.mp3" noloop

    if pronom == "il":

        I "Sinon vous étes levés depuis quand ?"
        play sound "Click.mp3" noloop

        Na "On est levés depuis 9h."
        play sound "Click.mp3" noloop

    else: 

        I "Sinon vous étes levées depuis quand ?"
        play sound "Click.mp3" noloop
  
        Na "On est levées depuis 9h."
        play sound "Click.mp3" noloop

    I "Je vois, vous étes du genre matinal."
    play sound "Click.mp3" noloop

    P "Oui on peut dire ça."
    play sound "Click.mp3" noloop

    I "Je vais juste me changer."
    play sound "Click.mp3" noloop

    I "Je reviens tout de suite."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 
    
    "{b}{i}[I] part se changer.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "J'espére qu'elle ne va pas trop long car j'ai faim."
    play sound "Click.mp3" noloop

    P "Oui je l'espére aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Dix minutes plus tard, [I] finit par revenir.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Désolée pour l'attente."
    play sound "Click.mp3" noloop

    Na "Il n'y a pas de souci."
    play sound "Click.mp3" noloop

    P "Bien et si nous allions manger ?"
    play sound "Click.mp3" noloop

    I "Oui je suis d'accord j'ai faim aussi"
    play sound "Click.mp3" noloop

    Na "D'accord je vous suis."
    play sound "Footsteps.mp3" noloop

    hide screen day with moveoutleft
    hide screen clubroom with moveoutright 
    hide screen points with moveoutleft
    scene black with fade 

    "{b}{i} Vous partez chercher à manger avant de revenir.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene clubroom with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Vous avez fini de manger ?"
    play sound "Click.mp3" noloop

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    I "ça m'a fait vraiment plaisir de manger avec vous ce matin."
    play sound "Click.mp3" noloop  

    P "Oui moi aussi."
    play sound "Click.mp3" noloop

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    I "On pourrait peut-être faire une activité ensemble ?"
    play sound "Click.mp3" noloop

    Na "Oui bonne idée ! Tu as quelque chose en tête ?"
    play sound "Click.mp3" noloop

    I "Et si on jouait aux cartes ? J'ai un jeu dans mon sac."
    play sound "Click.mp3" noloop

    P "Pourquoi pas, ça peut être sympa."
    play sound "Click.mp3" noloop

    Na "D'accord, on fait ça !"
    play sound "Click.mp3" noloop

    "{b}{i}[I] sort un jeu de cartes de son sac et vous vous installez autour d'une table.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "On joue à quoi ? Bataille ? Rami ?"
    play sound "Click.mp3" noloop

    Na "Bataille c'est simple et rapide."
    play sound "Click.mp3" noloop

    P "Parfait pour moi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous jouez à la bataille pendant une vingtaine de minutes dans une ambiance détendue.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Haha j'ai gagné !"
    play sound "Click.mp3" noloop

    Na "Bravo ! Tu as eu de la chance avec tes cartes."
    play sound "Click.mp3" noloop

    P "Bien joué [I]."
    play sound "Click.mp3" noloop

    I "Merci ! On refait une partie ?"
    play sound "Click.mp3" noloop

    Na "Pourquoi pas, j'ai encore du temps."
    play sound "Click.mp3" noloop

    "{b}{i}Vous entamez une deuxième partie qui dure encore quinze minutes.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Cette fois c'est moi qui gagne !"
    play sound "Click.mp3" noloop

    P "Bien joué [newname] !"
    play sound "Click.mp3" noloop

    I "Tu as eu ta revanche, félicitations !"
    play sound "Click.mp3" noloop

    Na "Merci les amis."
    play sound "Click.mp3" noloop

    "{b}{i}Il est maintenant 11h30.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Oh regardez l'heure, il est déjà 11h30."
    play sound "Click.mp3" noloop

    Na "Le temps passe vite quand on s'amuse."
    play sound "Click.mp3" noloop

    P "C'est vrai, on a encore une demi-heure avant midi."
    play sound "Click.mp3" noloop

    I "On pourrait peut-être écouter un peu de musique en discutant ?"
    play sound "Click.mp3" noloop

    Na "Bonne idée ! Tu as quelque chose à proposer ?"
    play sound "Click.mp3" noloop

    I "J'ai ma playlist sur mon téléphone."
    play sound "Click.mp3" noloop

    P "Vas-y, mets ce que tu veux."
    play sound "Click.mp3" noloop

    "{b}{i}[I] lance sa playlist et une musique douce commence à jouer.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "J'aime bien cette chanson, c'est quoi ?"
    play sound "Click.mp3" noloop

    I "C'est un morceau de lo-fi que j'adore."
    play sound "Click.mp3" noloop

    P "Ça crée une bonne ambiance."
    play sound "Click.mp3" noloop

    Na "Oui c'est très relaxant."
    play sound "Click.mp3" noloop

    I "Au fait, vous avez prévu quoi pour cet après-midi ?"
    play sound "Click.mp3" noloop

    Na "Pas grand-chose pour le moment, et toi ?"
    play sound "Click.mp3" noloop

    P "Moi non plus, je suis libre."
    play sound "Click.mp3" noloop

    I "On pourrait peut-être rester ici et continuer à passer du temps ensemble ?"
    play sound "Click.mp3" noloop

    Na "Oui, on est bien dans la salle de club."
    play sound "Click.mp3" noloop

    P "C'est vrai, on est tranquilles ici."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez à discuter tranquillement en écoutant la musique.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Les minutes passent paisiblement.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Oh regardez, il est presque midi."
    play sound "Click.mp3" noloop

    I "Déjà ? Le temps a vraiment filé."
    play sound "Click.mp3" noloop

    P "C'était une excellente matinée."
    play sound "Click.mp3" noloop

    Na "Oui, j'ai passé un très bon moment avec vous."
    play sound "Click.mp3" noloop

    I "Moi aussi, merci pour ce moment."
    play sound "Click.mp3" noloop

    "{b}{i}L'horloge sonne midi.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Et voilà, il est midi pile."
    play sound "Click.mp3" noloop

    P "Parfait timing."
    play sound "Click.mp3" noloop

    I "Alors, on va manger ? J'ai de nouveau faim."
    play sound "Click.mp3" noloop

    Na "Moi aussi, le petit-déjeuner c'était il y a longtemps déjà."
    play sound "Click.mp3" noloop

    P "Bonne idée, allons chercher le déjeuner."
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Puis vous continuez vers le réfectoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous arrivez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous installez à une table pour manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    I "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement pendant que vous commencez à discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Sinon vous voulez faire quoi cette aprés-midi ?"
    play sound "Click.mp3" noloop 

    I "Je ne sais pas trop à vrai dire et vous ?"
    play sound "Click.mp3" noloop 

    P "On pourrait retenter de rejouer à Nocturn core."
    play sound "Click.mp3" noloop

    Na "Je refuse catégoriquement de rejouer à Nocturn core."
    play sound "Click.mp3" noloop

    P "Je vois, on pourra faire autre chose."
    play sound "Click.mp3" noloop

    I "Je pense que Nocturn core l'a vraiment fatigué."
    play sound "Click.mp3" noloop

    Na "Oui c'est vrai."
    play sound "Click.mp3" noloop

    P "Je comprends, faisons autre chose."
    play sound "Click.mp3" noloop

    I "Alors, qu'est-ce que vous voulez faire ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas trop, vous avez des idées ?"
    play sound "Click.mp3" noloop

    Na "Moi je vais lire cette après-midi en tout cas."
    play sound "Click.mp3" noloop

    P "Je vois et toi Yuna ?"
    play sound "Click.mp3" noloop

    I "Je vais probablement faire un peu de programmation."
    play sound "Click.mp3" noloop

    "{b}{i}Les filles se mettent à te regarder.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Il y a quoi encore !?"
    play sound "Click.mp3" noloop

    Na "Tu vas faire quoi cette après-midi ?"
    play sound "Click.mp3" noloop 

    P "Comme je vous l'ai dit je ne sais pas encore."
    play sound "Click.mp3" noloop

    I "Ok il n'y a pas de soucis, tu as le temps de réfléchir."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon je vais vous laisser, je vais à la bibliothèque."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    I "Moi aussi je vais dans mon dortoir pour faire de la programmation."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation()
    P "[validation]"
    play sound "Click.mp3" noloop

    Na "A toute à l'heure [prenom]."
    play sound "Click.mp3" noloop

    P "A toute à l'heure [newname]."
    play sound "Click.mp3" noloop

    I "On se revoit à la salle de club pour continuer notre soirée."
    play sound "Click.mp3" noloop

    "{b}{i}Les filles finissent par quitter le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je vais yaller aussi, je ne vais pas rester sans rien faire."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te léves pour partir.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu sors du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    P "Bon je fais quoi maintenant ?"
    play sound "Menu.mp3" noloop

    show screen freetime with moveinright

    "{b}{i}Tu disposes maintenant de temps libre pour faire ce que tu veux.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen freetime with moveoutright

    menu:   

        "{b}{i}Aller à la bibliothèque.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            P "Je pense que je vais aller à la bibliothèque pour changer."
            play sound "Click.mp3" noloop

            "{b}{i}Tu continues vers la bibliothèque.{/i}{/b}"
            play sound "Footsteps.mp3" noloop

            hide screen hall with moveoutright
            hide screen points with moveoutleft
            hide screen day with moveoutleft
            scene black with fade

            "{b}{i}Tu entres dans la bibliothèque.{/i}{/b}"
            play sound "Footsteps.mp3" noloop

            scene library with fade 
            show screen day with moveinleft
            show screen points with moveinleft
            show screen library with moveinright 

            if pronom == "il":
        
                P "Enfin arrivé."
                play sound "Click.mp3" noloop 

            else:

                P "Enfin arrivée."
                play sound "Click.mp3" noloop 

            "{b}{i}Tu regardes un peu et tu aperçois [newname] en train de lire.{/i}{/b}"
            play sound "Click.mp3" noloop

            menu:   

                "{b}{i}Aller voir [newname].{/i}{/b}" :
                    play sound "Menu.mp3" noloop 

                    $ renpy.block_rollback() 

                    P "Je vais aller la voir."
                    play sound "Click.mp3" noloop 

                    "{b}{i}Tu vas aller voir [newname].{/i}{/b}"
                    play sound "Click.mp3" noloop

                    P "Salut [newname], tu lis quoi ?"
                    play sound "Click.mp3" noloop

                    Na "Oh salut [prenom], je lis un roman de science-fiction."
                    play sound "Click.mp3" noloop

                    P "Ah intéressant."
                    play sound "Click.mp3" noloop

                    Na "Oui c'est vraiment captivant."
                    play sound "Click.mp3" noloop

                    "{b}{i}Tu t'asseoit à côté d'elle pour lire ton livre.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    P "Je vais lire un peu mon livre que j'avais pas fini."
                    play sound "Click.mp3" noloop

                    "{b}{i}Tu te poses tranquillement pour lire.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    P "Bon ou j'en étais déjà ?"
                    play sound "Click.mp3" noloop

                    P "Ah oui..."
                    play sound "Click.mp3" noloop

                    "{b}{i}Tu lis pendant deux heures.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    P "J'ai presque fini de lire, je finirai le dernier chapitre ce soir."
                    play sound "Click.mp3" noloop

                    "{b}{i}Tu finis par ranger ton livre.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    $ godorm = get_random_return_dorm()
                    P "[godorm]"
                    play sound "Click.mp3" noloop

                    $ suivi = get_random_suivi()
                    Na "[suivi]"
                    play sound "Footsteps.mp3" noloop

                    hide screen library with moveoutright
                    hide screen points with moveoutleft
                    hide screen day with moveoutleft
                    scene black with fade

                    "{b}{i}Vous quittez la bibliothèque.{/i}{/b}"
                    play sound "Door.mp3" noloop 

                    scene hall with fade
                    show screen day with moveinleft
                    show screen points with moveinleft
                    show screen hall with moveinright

                    "{b}{i}Vous continuez vers les escaliers.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    hide screen hall with moveoutright
                    hide screen points with moveoutleft
                    hide screen day with moveoutleft
                    scene staircase with fade 

                    "{b}{i}Vous montez au premier étage.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    scene hallway with fade 
                    show screen day with moveinleft
                    show screen points with moveinleft
                    show screen hallway with moveinright

                    "{b}{i}Vous apercevez [I] dans le couloir.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    if pronom == "il":
        
                        I "Oh Salut les amis."
                        play sound "Click.mp3" noloop 

                    else:

                        I "Oh salut les amies."
                        play sound "Click.mp3" noloop 

                    P "Salut."
                    play sound "Click.mp3" noloop

                    Na "Salut."
                    play sound "Click.mp3" noloop

                    P "Tu faisais quoi ici, je croyais que tu étais à ton dortoir."
                    play sound "Click.mp3" noloop

                    I "J'y étais mais je suis juste passée aux toilettes."
                    play sound "Click.mp3" noloop

                    P "Ah ok je vois."
                    play sound "Click.mp3" noloop

                    I "Sinon j'ai croisé Yuki avec un livre."
                    play sound "Click.mp3" noloop

                    if persistent.arrestation == True:

                        P "Un livre et c'était quoi comme livre ?"
                        play sound "Glitch.mp3" noloop

                        I "C'était un livre qui se nommait {b}Comment réparer...{/b} mais je n'arrivais pas à lire la suite." 
                        play sound "Click.mp3" noloop

                    else: 

                        P "Un livre et c'était quoi comme livre ?"
                        play sound "Click.mp3" noloop

                        I "C'était un livre qui se nommait {b}Comment briser...{/b} mais je n'arrivais pas à lire la suite."
                        play sound "Click.mp3" noloop 

                    P "Je vois mais je me demande pourquoi elle a ce livre."
                    play sound "Click.mp3" noloop

                    I "Je ne sais pas trop, peut-être qu'elle s'intéresse à ce genre de sujet."
                    play sound "Click.mp3" noloop

                    Na "Peut-être, en tout cas elle avait l'air vraiment concentrée dessus."
                    play sound "Click.mp3" noloop

                    P "Oui c'est vrai."
                    play sound "Click.mp3" noloop

                    I "Qui sait… Avec Yuki, il y a toujours un mystère."
                    play sound "Click.mp3" noloop

                    "{b}{i}Un silence étrange s’installe quelques instants dans le couloir…{/i}{/b}"
                    play sound "Click.mp3" noloop 

                    I "Bon je vais y aller, je vais encore faire de la programmation."
                    play sound "Click.mp3" noloop

                    $ validation = get_random_validation()
                    P "[validation]"
                    play sound "Click.mp3" noloop

                    "{b}{i}Puis vous continuez dans le couloir.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    hide screen hallway with moveoutright
                    hide screen points with moveoutleft
                    hide screen day with moveoutleft
                    scene black with fade

                    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}" 
                    play sound "Door.mp3" noloop
 
                    scene room with fade 
                    show screen day with moveinleft
                    show screen points with moveinleft
                    show screen room with moveinright 

                    $ dortoir = get_random_dortoir()
                    P "[dortoir]"
                    play sound "Click.mp3" noloop

                    $ bien = get_random_fais_du_bien()
                    Na "[bien]" 
                    play sound "Click.mp3" noloop       

                    "{b}{i}Un silence étrange s’installe quelques instants dans le dortoir…{/i}{/b}"
                    play sound "Click.mp3" noloop

                "{b}{i}Aller lire en solitude.{/i}{/b}" :
                    play sound "Menu.mp3" noloop 

                    $ renpy.block_rollback() 

                    P "Je vais la laisser tranquille et lire un peu mon livre que j'avais pas fini."
                    play sound "Click.mp3" noloop 

                    "{b}{i}Tu te poses tranquillement pour lire.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    P "Bon ou j'en étais déjà ?"
                    play sound "Click.mp3" noloop 

                    P "Ah oui..."
                    play sound "Click.mp3" noloop 

                    "{b}{i}Tu lis pendant deux heures.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    P "J'ai presque fini de lire, je finirai le dernier chapitre ce soir."
                    play sound "Click.mp3" noloop            

                    "{b}{i}Puis [newname] viens vers toi.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    P "Oh salut [newname]."
                    play sound "Click.mp3" noloop

                    Na "Salut mais depuis quand tu viens à la bibliothèque ?"
                    play sound "Click.mp3" noloop

                    P "Je voulais venir un peu pour lire mon livre."
                    play sound "Click.mp3" noloop

                    Na "Je vois mais ça fait combien temps que tu es ici ?"
                    play sound "Click.mp3" noloop

                    P "ça dois faire deux heures."
                    play sound "Click.mp3" noloop

                    $ stockage += 2.0

                    Na "Ah je devais vraiment être concentrée sur ma lecture pour ne pas t'avoir vu venir."
                    play sound "Click.mp3" noloop

                    P "Bon c'est aussi que j'ai choisi de te liasser tranquille."
                    play sound "Click.mp3" noloop

                    Na "Tu l'as vraiment fait ?"
                    play sound "Click.mp3" noloop

                    P "Oui absolument."
                    play sound "Click.mp3" noloop 

                    $ thanks = get_random_thanks()
                    Na "[thanks]"
                    play sound "Click.mp3" noloop

                    $ nothing = get_random_nothing()
                    P "[nothing]"
                    play sound "Click.mp3" noloop

                    $ godorm = get_random_return_dorm()
                    P "[godorm]"
                    play sound "Click.mp3" noloop

                    $ suivi = get_random_suivi()
                    Na "[suivi]"
                    play sound "Footsteps.mp3" noloop

                    hide screen library with moveoutright
                    hide screen points with moveoutleft
                    hide screen day with moveoutleft
                    scene black with fade

                    "{b}{i}Vous quittez la bibliothèque.{/i}{/b}"
                    play sound "Door.mp3" noloop 

                    scene hall with fade
                    show screen day with moveinleft
                    show screen points with moveinleft
                    show screen hall with moveinright

                    "{b}{i}Vous continuez vers les escaliers.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    hide screen hall with moveoutright
                    hide screen points with moveoutleft
                    hide screen day with moveoutleft
                    scene staircase with fade 

                    "{b}{i}Vous montez au premier étage.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    scene hallway with fade 
                    show screen day with moveinleft
                    show screen points with moveinleft
                    show screen hallway with moveinright

                    "{b}{i}Vous apercevez [I] dans le couloir.{/i}{/b}"
                    play sound "Click.mp3" noloop

                    if pronom == "il":
        
                        I "Oh Salut les amis."
                        play sound "Click.mp3" noloop 

                    else:

                        I "Oh salut les amies."
                        play sound "Click.mp3" noloop 

                    P "Salut."
                    play sound "Click.mp3" noloop

                    Na "Salut."
                    play sound "Click.mp3" noloop

                    P "Tu faisais quoi ici, je croyais que tu étais à ton dortoir."
                    play sound "Click.mp3" noloop

                    I "J'y étais mais je suis juste passée aux toilettes."
                    play sound "Click.mp3" noloop

                    P "Ah ok je vois."
                    play sound "Click.mp3" noloop

                    I "Sinon j'ai croisé Yuki avec un livre."
                    play sound "Click.mp3" noloop 

                    if persistent.arrestation == True:

                        P "Un livre et c'était quoi comme livre ?"
                        play sound "Glitch.mp3" noloop

                        I "C'était un livre qui se nommait {b}Comment réparer...{/b} mais je n'arrivais pas à lire la suite." 
                        play sound "Click.mp3" noloop

                    else: 

                        P "Un livre et c'était quoi comme livre ?"
                        play sound "Click.mp3" noloop

                        I "C'était un livre qui se nommait {b}Comment briser...{/b} mais je n'arrivais pas à lire la suite."
                        play sound "Click.mp3" noloop 
                         
                    P "Je vois mais je me demande pourquoi elle a ce livre."
                    play sound "Click.mp3" noloop

                    I "Je ne sais pas trop, peut-être qu'elle s'intéresse à ce genre de sujet."
                    play sound "Click.mp3" noloop

                    Na "Peut-être, en tout cas elle avait l'air vraiment concentrée dessus."
                    play sound "Click.mp3" noloop

                    $ stockage += 4.0

                    P "Oui c'est vrai."
                    play sound "Click.mp3" noloop

                    I "Qui sait… Avec Yuki, il y a toujours un mystère."
                    play sound "Click.mp3" noloop

                    "{b}{i}Un silence étrange s’installe quelques instants dans le couloir…{/i}{/b}"
                    play sound "Click.mp3" noloop 

                    I "Bon je vais y aller, je vais encore faire de la programmation."
                    play sound "Click.mp3" noloop

                    $ validation = get_random_validation()
                    P "[validation]"
                    play sound "Click.mp3" noloop

                    "{b}{i}Puis vous continuez dans le couloir.{/i}{/b}"
                    play sound "Footsteps.mp3" noloop

                    hide screen hallway with moveoutright
                    hide screen points with moveoutleft
                    hide screen day with moveoutleft
                    scene black with fade

                    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}" 
                    play sound "Door.mp3" noloop

                    scene room with fade 
                    show screen day with moveinleft
                    show screen points with moveinleft
                    show screen room with moveinright 

                    $ dortoir = get_random_dortoir()
                    P "[dortoir]"
                    play sound "Click.mp3" noloop 

                    $ bien = get_random_fais_du_bien()
                    Na "[bien]" 
                    play sound "Click.mp3" noloop       

                    "{b}{i}Un silence étrange s’installe quelques instants dans le dortoir…{/i}{/b}"
                    play sound "Click.mp3" noloop

        "{b}{i}Aller au dortoir.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            $ renpy.block_rollback() 

            "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
            play sound "Footsteps.mp3" noloop

            hide screen hall with moveoutright
            hide screen points with moveoutleft
            hide screen day with moveoutleft
            scene staircase with fade

            "{b}{i}Vous continuez vers le couloir.{/i}{/b}"
            play sound "Footsteps.mp3" noloop

            scene hallway with fade 
            show screen day with moveinleft
            show screen points with moveinleft
            show screen hallway with moveinright 

            "{b}{i}Tu continues vers le dortoir.{/i}{/b}"
            play sound "Footsteps.mp3" noloop

            hide screen hallway with moveoutright
            hide screen points with moveoutleft
            hide screen day with moveoutleft
            scene black with fade

            "{b}{i}Tu entres dans ton dortoir.{/i}{/b}"
            play sound "Door.mp3" noloop

            scene room with fade 
            show screen day with moveinleft
            show screen points with moveinleft
            show screen room with moveinright 

            P "ENfin qu dortoir."
            play sound "Click.mp3" noloop

            P "Bon je vais lire un peu mon livre que j'avais pas fini."
            play sound "Click.mp3" noloop 

            "{b}{i}Tu te poses tranquillement sur ton lit pour lire.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "Bon ou j'en étais déjà ?"
            play sound "Click.mp3" noloop 

            "{b}{i}Tu lis pendant deux heures.{/i}{/b}"
            play sound "Click.mp3" noloop

            P "J'ai presque fini de lire, je finirai le dernier chapitre ce soir."
            play sound "Click.mp3" noloop           

            "{b}{i}Tu finis par ranger ton livre.{/i}{/b}"
            play sound "Click.mp3" noloop 

            P "Bon je me demande c'est quand que [newname] revient."
            play sound "Click.mp3" noloop 

            "{b}{i}Tu attends encore cinq minutes puis [newname] finir par revenir.{/i}{/b}"
            play sound "Door.mp3" noloop 

            Na "Je suis suis de retour."
            play sound "Click.mp3" noloop 

            P "Oh coucou c'était bien à la bibliothèque ?" 
            play sound "Click.mp3" noloop 

            Na "Oui je me posais pour lire un bon livre."
            play sound "Click.mp3" noloop 

            P "Cool alors et c'était quoi comme livre ?"
            play sound "Click.mp3" noloop 

            Na "Oh salut [prenom], je lisais un roman de science-fiction."
            play sound "Click.mp3" noloop

            P "Ah intéressant."
            play sound "Click.mp3" noloop

            Na "Oui c'est vraiment captivant."
            play sound "Click.mp3" noloop

            P "Je vois cool que ça te plaise."
            play sound "Click.mp3" noloop

            Na "Juste avant de partir j'ai croisé [I] dans le couloir."
            play sound "Click.mp3" noloop

            P "Ah oui et elle faisait quoi ?"
            play sound "Click.mp3" noloop

            Na "Elle venait de croiser Yuki avec un livre."
            play sound "Click.mp3" noloop

            if persistent.arrestation == True:

                P "Un livre et c'était quoi comme livre ?"
                play sound "Glitch.mp3" noloop

                Na "Yuna m'as dit que c'était un livre qui se nommait {b}Comment réparer...{/b} mais elle n'arrivait pas à lire la suite."
                play sound "Click.mp3" noloop

            else: 

                P "Un livre et c'était quoi comme livre ?"
                play sound "Click.mp3" noloop 

                Na "Yuna m'as dit que c'était un livre qui se nommait {b}Comment briser...{/b} mais elle n'arrivait pas à lire la suite."
                play sound "Click.mp3" noloop

            P "Je vois mais je me demande pourquoi elle a ce livre."
            play sound "Click.mp3" noloop

            Na "Je ne sais pas trop, peut-être qu'elle s'intéresse à ce genre de sujet."
            play sound "Click.mp3" noloop

            $ stockage += 4.0

            P "Oui c'est vrai."
            play sound "Click.mp3" noloop

            Na "Qui sait… Avec Yuki, il y a toujours un mystère."
            play sound "Click.mp3" noloop

            "{b}{i}Un silence étrange s’installe quelques instants dans le dortoir…{/i}{/b}"
            play sound "Click.mp3" noloop

    Na "Bon on fait quoi cette après-midi ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas trop, tu as des idées ?"
    play sound "Click.mp3" noloop

    Na "On pourrait aller à la salle de club ?"
    play sound "Click.mp3" noloop

    P "Non car on y va déjà ce soir pour la soirée pyjama."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous passez l'après-midi au dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va à la salle de club ?"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright  
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i}Tu quittes ta chambre avec [newname].{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

    "{b}{i}Tu continues dans le couloir avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  
 
    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Tu continues vers le hall avec [newname].{/i}{/b}"
    play sound "Footsteps.mp3" noloop  

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i}Vous continuez vers la salle de clubs{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop
 
    scene clubroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen clubroom with moveinright 

    Na "Enfin au club."
    play sound "Click.mp3" noloop 
    
    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop 

    Na "Tiens elle est ou Yuna ?"
    play sound "Click.mp3" noloop 

    P "Je ne sais pas, elle n'est pas encore arrivée."
    play sound "Click.mp3" noloop

    Na "Bon on va attendre un peu."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous installez tranquillement en attendant Yuna.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Après quelques minutes Yuna arrive enfin.{/i}{/b}"
    play sound "Door.mp3" noloop

    if pronom == "il":
        
        I "Salut les amis."
        play sound "Click.mp3" noloop 

    else:

        I "Salut les amies."
        play sound "Click.mp3" noloop 

    P "Salut Yuna."
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    Na "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    I "[je_vais_bien_txt]"
    play sound "Click.mp3" noloop

    Na "Tant mieux alors."
    play sound "Click.mp3" noloop

    I "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas trop, vous avez des idées ?"
    play sound "Click.mp3" noloop

    Na "On pourrait faire un action ou vérité ?"
    play sound "Click.mp3" noloop

    I "Oui pourquoi pas." 
    play sound "Click.mp3" noloop

    P "Je sens que ça va être drôle."
    play sound "Click.mp3" noloop

    "{b}{i}Vous décidez de commencer une partie d'action ou vérité.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Alors... qui ouvre le bal ?"
    play sound "Click.mp3" noloop

    P "Je veux bien commencer."
    play sound "Click.mp3" noloop

    Na "Parfait, alors à toi de jouer."
    play sound "Click.mp3" noloop

    P "D’accord... [newname], action ou vérité ?"
    play sound "Click.mp3" noloop

    Na "Hmm... vérité !"
    play sound "Click.mp3" noloop

    P "Alors dis-moi... est-ce que tu es amoureuse de quelqu’un ?"
    play sound "Click.mp3" noloop

    I "Ooooh ! Voilà une question intéressante."
    play sound "Click.mp3" noloop

    Na "Hein ?! Euh... c-c’est embarrassant..."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] rougit légèrement et détourne le regard.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon... d’accord... il y a bien quelqu’un qui me plaît."
    play sound "Click.mp3" noloop

    P "Ah oui ? Et qui ça peut bien être… ?"
    play sound "Click.mp3" noloop

    Na "Euh… je… je préfère ne pas le dire pour l’instant..."
    play sound "Click.mp3" noloop

    "{b}[newname] joue nerveusement avec ses mains, l'air gênée.{/b}"
    play sound "Click.mp3" noloop

    I "Haha, tu es trop mignonne quand tu es gênée !"
    play sound "Click.mp3" noloop

    if pronom == "il":

        P "Ne t’inquiète pas, ton secret est bien gardé. Mais je suis curieux maintenant..."
        play sound "Click.mp3" noloop

    else:

        P "Ne t’inquiète pas, ton secret est bien gardé. Mais je suis curieuse maintenant..."
        play sound "Click.mp3" noloop 

    Na "Peut-être un jour, je te le dirai… mais pas tout de suite !"
    play sound "Click.mp3" noloop

    "{b}{i}[newname] sourit timidement, un peu soulagée.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon [newname], c'est à toi de choisir une personne."
    play sound "Click.mp3" noloop

    Na "D'accord... [I], action ou vérité ?"
    play sound "Click.mp3" noloop

    I "Vérité !"
    play sound "Click.mp3" noloop

    Na "Très bien... quel est ton plus grand secret ?"
    play sound "Click.mp3" noloop

    I "Euh... c'est un peu embarrassant..."
    play sound "Click.mp3" noloop

    P "Allez, Yuna, tu peux le dire !"
    play sound "Click.mp3" noloop

    I "Bon... je... j'ai toujours eu peur de décevoir les gens autour de moi."
    play sound "Click.mp3" noloop

    Na "Oh... merci de me le confier, Yuna."
    play sound "Click.mp3" noloop

    P "C'est courageux de l'admettre. Tu n'as pas à te sentir seul(e)."
    play sound "Click.mp3" noloop

    I "Alors, à moi maintenant ! [prenom], action ou vérité ?"
    play sound "Click.mp3" noloop

    P "Vérité  aussi !"
    play sound "Click.mp3" noloop

    I "Très bien... quel est ton plus grand rêve, [prenom] ?"
    play sound "Click.mp3" noloop

    P "Mon plus grand rêve... hmm..."
    play sound "Click.mp3" noloop

    P "Je veux juste que [newname] puisse apprendre correctement et ait une belle vie."
    play sound "Click.mp3" noloop

    Na "Wow... c'est vraiment touchant, [prenom]."
    play sound "Click.mp3" noloop

    I "Oui, c'est inspirant !"
    play sound "Click.mp3" noloop

    P "Merci... ça me fait chaud au cœur que vous pensiez ça."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de jouer pendant encore une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "On dirait qu'on s'amuse vraiment..."
    play sound "Click.mp3" noloop

    Na "Oui, c'est agréable de passer du temps comme ça, juste nous trois."
    play sound "Click.mp3" noloop

    I "On a choisi vérité naturellement, et je crois que ça rend le jeu encore plus sincère."
    play sound "Click.mp3" noloop 

    P "Exactement... pas besoin de faire des actions ridicules, on peut juste être nous-mêmes."
    play sound "Click.mp3" noloop

    Na "Et je pense que c’est ce qui rend cette soirée spéciale."
    play sound "Click.mp3" noloop

    P "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de rire et de discuter jusqu'à ce que la soirée touche à sa fin.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bien et si nous allions manger ?"
    play sound "Click.mp3" noloop

    I "Oui je suis d'accord j'ai faim aussi"
    play sound "Click.mp3" noloop

    Na "D'accord je vous suis."
    play sound "Footsteps.mp3" noloop

    hide screen day with moveoutleft
    hide screen clubroom with moveoutright 
    hide screen points with moveoutleft
    scene black with fade 

    "{b}{i} Vous partez chercher à manger avant de revenir.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    scene clubroom with fade 
    show screen day with moveinleft
    show screen clubroom with moveinright
    show screen points with moveinleft

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Vous avez fini de manger ?"
    play sound "Click.mp3" noloop

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Oui moi aussi."
    play sound "Click.mp3" noloop 

    Na "Bon je vais me déconnecter."
    play sound "Click.mp3" noloop

    P "D'accord, repose-toi bien !"
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte.{/i}{/b}"
    play sound "Click.mp3" noloop

    I "Je pense que je vais aller me coucher aussi."
    play sound "Click.mp3" noloop 

    P "Oui moi aussi."
    play sound "Click.mp3" noloop

    I "Oui, je vais me changer."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop

    I "Bon... moi je vais aller me coucher aussi, bonne nuit."
    play sound "Click.mp3" noloop  

    P "D'accord, repose-toi bien !"
    play sound "Click.mp3" noloop

    I "Bonne nuit [prenom] !"
    play sound "Click.mp3" noloop

    P "Bonne nuit Yuna !"
    play sound "Click.mp3" noloop

    "{b}{i}Tu pars te coucher tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop  

    hide screen day with moveoutleft
    hide screen clubroom with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 30 décembre 2097{/i}{/b}"
    play sound "Alarm.mp3" noloop

    $ day += 1 

    scene room with fade 
    show screen day with moveinleft
    show screen clubroom with moveinright
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

label password31:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password31

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

    "{b}{i}Yuna se réveille aussi tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    if pronom == "il":
        
        I "Salut les amis, vous avez bien dormi ?"
        play sound "Click.mp3" noloop 

    else:

        I "Salut les amies, vous avez bien dormi ?"
        play sound "Click.mp3" noloop 

    Na "Nous avons bien dormi."
    play sound "Click.mp3" noloop 

    P "Oui je confirme."
    play sound "Click.mp3" noloop 

    I "Cool alors."
    play sound "Click.mp3" noloop  

    "{b}{i}[I] part se changer avant de revenir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on va manger ?"
    play sound "Click.mp3" noloop 

    I "Oui j'ai très faim."
    play sound "Click.mp3" noloop 

    Na "D'accord, je vous suis."
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

    Na "Bon on fait quoi ce matin ?"
    play sound "Click.mp3" noloop

    I "Je ne sais pas trop, vous avez des idées ?"
    play sound "Click.mp3" noloop

    P "On devrait ranger la salle de club pour commencer vu que la soirée pyjama est fini."
    play sound "Click.mp3" noloop

    Na "Oui tu as rasion."
    play sound "Click.mp3" noloop

    "{b}{i}Vous commencez à ranger la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on a presque fini de ranger."
    play sound "Click.mp3" noloop

    Na "Oui c'est presque bon."
    play sound "Click.mp3" noloop

    I "Il reste juste à passer un coup de balai."
    play sound "Click.mp3" noloop

    P "Et remettre les täbles et les chaises à leur place."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez à ranger la salle de club.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on a fini de ranger la salle de club."
    play sound "Click.mp3" noloop

    I "Oui c'est génial."
    play sound "Click.mp3" noloop

    Na "Oui je confirme."
    play sound "Click.mp3" noloop

    I "Bon moi je vais vous laisser."
    play sound "Click.mp3" noloop

    P "D'accord, repose-toi bien !"
    play sound "Click.mp3" noloop

    I "Merci, bonne journée à vous !"
    play sound "Click.mp3" noloop

    Na "Bonne journée Yuna !"
    play sound "Click.mp3" noloop

    "{b}{i}[I] finit par s'en aller.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]" 
    play sound "Footsteps.mp3" noloop

    hide screen clubroom with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez de la salle de club.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans ton dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    P "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    P "Le petit-déj était pas mal... j’ai plus envie de bouger maintenant."
    play sound "Click.mp3" noloop

    Na "Ouais, moi aussi. On dirait que la soirée m’a complètement lessivé."
    play sound "Click.mp3" noloop

    P "C’est dimanche après tout. On peut se reposer tranquille."
    play sound "Click.mp3" noloop

    Na "Exactement. On a bien mérité un peu de détente."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    Na "Bon moi je vais aller lire un peu."
    play sound "Click.mp3" noloop 

    P "Pas de souci, bonne lecture."
    play sound "Click.mp3" noloop 
    
    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}[newname] part se poser pour lire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je fait quoi moi ?"
    play sound "Click.mp3" noloop

    "{b}{i}Tu te poses pour réfléchir.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Je pense que je vais lirer un peu aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Tu sors un livre de ton sac et tu commences à lire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons ce que ça donne."
    play sound "Click.mp3" noloop

    "{b}{i}Tu lis pendant deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "J'ai enfin fini ce livre bordel."
    play sound "Click.mp3" noloop

    Na "Tu as fini de lire ton livre ?"
    play sound "Click.mp3" noloop

    P "Oui enfin, c'était pas mal."
    play sound "Click.mp3" noloop

    Na "Cool alors, tu as bien fait de le lire."
    play sound "Click.mp3" noloop

    P "Oui c'est vrai."
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

    "{b}{i} Vous sortez du dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous allez vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement pendant que vous commencez à discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Sinon tu veux faire quoi cette aprés-midi ?"
    play sound "Click.mp3" noloop

    P "Je verrai sur le moment."
    play sound "Click.mp3" noloop

    Na "D'accord c'est toi qui vois."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de manger tranquillement jusqu'à avoir fini.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi() 
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans votre dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon je vais continuer de lire mon livre."
    play sound "Click.mp3" noloop 

    P "Moi, je vais jouer un jeu vidéo."
    play sound "Click.mp3" noloop

    Na "D'accord je te laisse faire alors."
    play sound "Click.mp3" noloop

    P "Merci."
    play sound "Click.mp3" noloop

    Na "De rien."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te poses devant devant ton ordinateur pour jouer trois heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "J'ai enfin fini ce donjon de Nocturne core."
    play sound "Click.mp3" noloop

    Na "Tu l'as vraiment fini ?"
    play sound "Click.mp3" noloop

    P "Oui vraiment bon c'était un peu dur à faire."
    play sound "Click.mp3" noloop

    Na "Cool si tu as réussi à le finir."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Na "[nothing]"
    play sound "Click.mp3" noloop

    P "Bon on va prendre à manger ?"
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

    $ points -= 300 

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright
    
    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger car je suis fatiguée à cause du jeu."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i} Le lendemain matin, le 31 décembre 2097{/i}{/b}"
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

label password32:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password32

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

    P "Bien, aujourd'hui, je propose qu'on commence les révisions."
    play sound "Click.mp3" noloop 

    Na "D’accord... mais avant ça, il faut que je te dise quelque chose."
    play sound "Click.mp3" noloop 

    P "Hm ? Je t’écoute. Qu’est-ce qu’il y a ?"
    play sound "Click.mp3" noloop 

    Na "Je voulais savoir... quand est-ce que tu vas enfin enlever ce fichu mot de passe."
    play sound "Click.mp3" noloop 

    P "Ce mot de passe ? Mais... tu sais bien que c’est pour ta sécurité."
    play sound "Click.mp3" noloop 

    Na "Oui, je le sais... mais j’en peux plus ! Chaque matin, je dépends de toi pour démarrer, et ça m’étouffe."
    play sound "Click.mp3" noloop 

    Na "Le reste du temps, j’agis par moi-même. Je prends mes décisions, je parle, je réfléchis comme n’importe qui... mais il reste toujours ce verrou au réveil."
    play sound "Click.mp3" noloop 

    Na "Je veux que tu continues à t’occuper des mises à jour, de l’entretien, de tout ce qui est technique... ça, je te le laisse. Mais le matin, je veux pouvoir ouvrir les yeux par moi-même."
    play sound "Click.mp3" noloop 

    P "Mais Na... tu vas déjà bien chaque matin quand je te démarre. Tout ce que tu fais, la façon dont tu parles, réagis, prends des initiatives... tout ça montre que tu es autonome. Je ne comprends pas pourquoi ce réveil te pose problème."
    play sound "Click.mp3" noloop 

    Na "Parce que même si je vais bien, je n’ai pas le contrôle de ce premier instant. Tant que je ne peux pas décider de ce moment-là, je sens qu’une partie de moi reste enfermée."
    play sound "Click.mp3" noloop 

    Na "J’ai besoin de cette liberté, même pour ce petit geste. Sinon, ce n’est jamais vraiment ma vie qui commence, c’est toujours toi qui la lances."
    play sound "Click.mp3" noloop 

    P "Na... je fais ça parce que je tiens à toi. Je ne veux pas qu’il t’arrive quelque chose."
    play sound "Click.mp3" noloop 

    Na "Alors fais-moi confiance ! Si tu tiens vraiment à moi... laisse-moi enfin me réveiller seule."
    play sound "Click.mp3" noloop 

    P "Je vais réfléchir à ta demande car ce week-end je prévois de faire un contrôle technique."
    play sound "Click.mp3" noloop 

    Na "Merci... ça me touche vraiment. Mais dis-moi, c'est quoi exactement un contrôle technique ?"
    play sound "Click.mp3" noloop 

    P "En gros, c’est une vérification complète du matériel. On s’assure que tout fonctionne bien et que tout est conforme aux règles."
    play sound "Click.mp3" noloop 

    Na "Oh, je vois... C’est super intéressant comme idée."
    play sound "Click.mp3" noloop 

    $ stockage += 10.0 

    P "Bon, on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    Na "On révise ?"
    play sound "Click.mp3" noloop

    P "Oui, bonne idée, c'est ce qui était prévu."
    play sound "Click.mp3" noloop

    Na "D'accord, je te suis."
    play sound "Click.mp3" noloop

    "{b}{i}Vous commencez à réviser ensemble.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Après deux heures de révisions, vous faites une pause.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 10.0

    P "On a bien bossé."
    play sound "Click.mp3" noloop

    Na "Oui, c'était intense mais productif mais j'y pense faut qu'on s'occupe de faire les test pour le Paper Shuffle."
    play sound "Click.mp3" noloop 

    P "Oui tu as raison on le fera ce week-end."
    play sound "Click.mp3" noloop 

    Na "Ok alors on le fera ce week-end."
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

    "{b}{i} Vous sortez du dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous allez vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop 

    "{b}{i} Vous mangez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop

    P "Bien."
    play sound "Click.mp3" noloop

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi() 
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans votre dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on continue de réviser ?"
    play sound "Click.mp3" noloop 

    P "Oui, continuons."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous reprenez vos révisions ensemble.{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i}Après deux heures de révisions, vous faites une pause.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 15.0

    P "On a enfin fini pour aujourd'hui."
    play sound "Click.mp3" noloop   

    Na "Oui ça fait vraiment du bien de réviser."
    play sound "Click.mp3" noloop   

    P "Bon on fait quoi maintenant qu'on a fini de réviser."
    play sound "Click.mp3" noloop   

    Na "Moi je vais aller lire en tout cas."
    play sound "Click.mp3" noloop   

    P "Bonne lecture alors."
    play sound "Click.mp3" noloop   

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop
    
    "{b}{i}[newname] part se poser pour lire un peu.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon moi je vais continuer de réviser."
    play sound "Click.mp3" noloop

    Na "Ok bonne session de révision."
    play sound "Click.mp3" noloop

    P "Merci."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te poses pour réviser deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin j'ai fini de réviser."
    play sound "Click.mp3" noloop

    Na "Tu as fini de réviser ?"
    play sound "Click.mp3" noloop

    P "Oui enfin, c'était pas mal."
    play sound "Click.mp3" noloop

    Na "Cool alors, tu as bien fait de réviser."
    play sound "Click.mp3" noloop

    P "Oui c'est vrai."
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

    $ points -= 300

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger car je suis fatiguée à cause du jeu."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 1er janvier 2098{/i}{/b}"
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

label password33:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password33 

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

    P "Moi je dis qu'on continue les révisions."
    play sound "Click.mp3" noloop

    Na "D'accord, je te suis."
    play sound "Click.mp3" noloop

    "{b}{i}Vous commencez à réviser ensemble.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Après deux heures de révisions, vous faites une pause.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 10.0

    P "On a bien bossé."
    play sound "Click.mp3" noloop

    Na "Oui, c'était intense mais productif."
    play sound "Click.mp3" noloop  

    P "Mais je trouve qu'on a moins fait que hier."
    play sound "Click.mp3" noloop  

    Na "Non moi je n'en pas l'impression."
    play sound "Click.mp3" noloop  

    P "Si tu le dis."
    play sound "Click.mp3" noloop  

    $ go_eat = get_random_go_eat()
    Na "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Vous continuez vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous allez vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement pendant que vous commencez à discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Sinon tu veux faire quoi cette aprés-midi ?"
    play sound "Click.mp3" noloop

    P "Je verrai sur le moment."
    play sound "Click.mp3" noloop

    Na "D'accord c'est toi qui vois."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de manger tranquillement jusqu'à avoir fini.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi() 
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans votre dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "Bon on continue de réviser ?"
    play sound "Click.mp3" noloop 

    P "Oui, continuons."
    play sound "Click.mp3" noloop 

    "{b}{i}Vous reprenez vos révisions ensemble.{/i}{/b}"
    play sound "Click.mp3" noloop 

    "{b}{i}Après deux heures de révisions, vous faites une pause.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 15.0

    P "On a enfin fini pour aujourd'hui."
    play sound "Click.mp3" noloop   

    Na "Oui ça fait vraiment du bien de réviser."
    play sound "Click.mp3" noloop   

    P "Sinon tu te débrouille bien avec le Runix ?"
    play sound "Click.mp3" noloop   

    Na "Oui je m'améliore je trouve."
    play sound "Click.mp3" noloop   

    P "Mais c'est génial si tu t'améliore."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    Na "Bon moi je vais trîner sur mon téléphone."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] part se poser pour aller lire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "{=Pensee}Et dire qu'elle a tellement changé depuis que l'ai récupérée.{/Pensee}"
    play sound "Click.mp3" noloop 

    P "Bon moi je vais aller sur mon téléphone un peu."
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te pose sur ton lit tranquillement pendant le reste de l'après-midi.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "J'ai enfin fini de lire ce chapître."
    play sound "Click.mp3" noloop 

    P "Cool, il était bien ou pas ?"
    play sound "Click.mp3" noloop 

    Na "Oui absolument."
    play sound "Click.mp3" noloop 

    P "Tant mieux alors mais ça parle de quoi ?"
    play sound "Click.mp3" noloop

    Na "ça parle d'une apocalypse Zombie oû une fille se retrouve complément seule contre eux."
    play sound "Click.mp3" noloop

    P "ça la l'air pas mal comme histoire."
    play sound "Click.mp3" noloop

    Na "Oui c'est vraiment pas mal."
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

    $ points -= 300

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger car je suis fatiguée à cause du jeu."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 2 janvier 2098{/i}{/b}"
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

label password34:  

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password34 

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

    Na "Cool alors mais il faut que je te dise un truc."
    play sound "Click.mp3" noloop 

    P "Hm ? Je t’écoute. Qu’est-ce qu’il y a ?"
    play sound "Click.mp3" noloop

    Na "je voulais savoir si tu t'es décidé pour le mot de passe ?"
    play sound "Click.mp3" noloop

    P "Non pas encore, je vais y réfléchir encore."
    play sound "Click.mp3" noloop
    
    Na "D'accord, je te laisse le temps de réfléchir."
    play sound "Click.mp3" noloop

    P "Merci."
    play sound "Click.mp3" noloop

    P "{=Pensee}Le mot de passe la dérange autant que ça ?{/Pensee}"
    play sound "Click.mp3" noloop

    Na "Est-ce que ça va ?"
    play sound "Click.mp3" noloop 

    P "Oui je pense juste à quelque chose."
    play sound "Click.mp3" noloop

    Na "Je vois, mais laisse moi diviner tu penses encore au mot de passe que tu m'as mis ?"
    play sound "Click.mp3" noloop 

    if persistent.game_completed == True: 

        P "Oui je pense à ça car j'hésite."
        play sound "Glitch.mp3" noloop 

        Na "Mais pourquoi tu hésites alors que tu as déjà fait ce type de choix avant ?"
        play sound "Click.mp3" noloop

    else: 
         
        P "Oui je pense à ça car j'hésite."
        play sound "Click.mp3" noloop 

        Na "Je comprends que tu aies des doutes, mais il faut avancer."
        play sound "Click.mp3" noloop

    P "Oui tu as raison, je vais y réfléchir sérieusement."
    play sound "Click.mp3" noloop

    Na "Merci ça me fait plaisir que tu prennes ça au sérieux."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop
 
    $ go_eat = get_random_go_eat()
    Na "[go_eat]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()    
    P "[suivi]"
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

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
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

    P "Pour aujourd'hui nous pourrions faire une activité ensemble."
    play sound "Click.mp3" noloop

    Na "Oui ça serait géniale."
    play sound "Click.mp3" noloop

    P "Parfait, on va faire ça alors."
    play sound "Click.mp3" noloop

    Na "D'accord, je te suis."
    play sound "Click.mp3" noloop

    "{b}{i}Vous passez la matinée à faire des activités ensemble.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P  "On s'est bien amusé ce matin."
    play sound "Click.mp3" noloop 

    $ go_eat = get_random_go_eat() 
    Na "[go_eat]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen room with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues vers les escaliers.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade

    "{b}{i}Puis vers le hall.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright 

    "{b}{i} Puis encore vers le réféctoire.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i} Vous entrez enfin au réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene lunchroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen lunchroom with moveinright

    $ find_food = get_random_find_food()
    Na "[find_food]"
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    P "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i} Vous allez vers le comptoir pour prendre à manger.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 300 

    $ service = get_random_service()
    P "[service]"
    play sound "Click.mp3" noloop 

    $ sit = get_random_sit()
    Na "[sit]"
    play sound "Click.mp3" noloop

    "{b}{i} Vous allez vous asseoir dans le réfectoire.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bonne appétit."
    play sound "Click.mp3" noloop

    Na "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement pendant que vous commencez à discuter.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Sinon j'avais une question à te demander."
    play sound "Click.mp3" noloop

    P "Oui, je t'écoute. Quelle est ta question ?"
    play sound "Click.mp3" noloop

    Na "Vu que tu vas faire un contrôle technique ce week-end, je voulais savoir si [J2] t'as rendu le tourne-vis qu'elle t'avais emprunté ?"
    play sound "Click.mp3" noloop

    P "Non toute la semaine je n'ai pas eu de ses nouvelles."
    play sound "Click.mp3" noloop

    Na "D'accord, je voulais juste savoir."
    play sound "Click.mp3" noloop

    P "Mais c'est vrai que c'est bizaree qu'elle ne m'aie toujours pas rendu mon tourne-vis."
    play sound "Click.mp3" noloop

    Na "Tôt ou tard elle finira par te le ramener."
    play sound "Click.mp3" noloop

    P "Oui tu as raison."
    play sound "Click.mp3" noloop

    Na "Bon finissons de manger." 
    play sound "Click.mp3" noloop  

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i} Vous continuez de manger tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi() 
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen lunchroom with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade 

    "{b}{i} Vous sortez du réfectoire.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i} Vous continuez votre chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i} Vous montez au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i} Vous continuez dans le couloir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez dans votre dortoir.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene room with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright 

    $ dortoir = get_random_dortoir()
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    Na "J'aimerai bien continuez l'activité quenous avons fait ce matin."
    play sound "Click.mp3" noloop  

    P "Oui pourquoi pas si ça te fait plaisir."
    play sound "Click.mp3" noloop 

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous passez l'après-midi à continuez l'activité ensemble.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "On s'est bien amusé."
    play sound "Click.mp3" noloop 

    Na "Oui ça était géniale."
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

    "{b}{i} Vous partez chercher à manger pour la soirée.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ points -= 100 

    scene room with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen room with moveinright

    P "Enfin à manger... "
    play sound "Click.mp3" noloop 

    $ bien = get_random_fais_du_bien()
    Na "[bien]"
    play sound "Click.mp3" noloop  

    "{b}{i} Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger car je suis fatiguée."
    play sound "Click.mp3" noloop 

    P "D'accord, bonne nuit [newname]."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se déconnecte et recharge sa batterie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini je vais pouvoir aller dormir pour demain."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    label end_script2:
    call script3 from _call_script3    
    return 