
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

    "{b}{i}Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
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

    P "Bon je vais aller la voir pour voir."
    play sound "Footsteps.mp3" noloop 

    "{b}{i}Tu te diriges vers le dortoir d'[I] avant d'y parvenir.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Bon....."
    play sound "Knock.mp3" noloop 

    "{b}{i}Tu frappes à la porte d'[I] et patientes.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "{=Pensee}Tiens, on dirait qu'elle n'est pas là.{/Pensee}"
    play sound "Click.mp3" noloop

    P "{=Pensee}Bon, je vais revenir plus tard alors.{/Pensee}"
    play sound "Footsteps.mp3" noloop

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

    "{b}{i} Puis encore vers le bibliothèque.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveinright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu entres dans la bibliothèque.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene library with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen library with moveinright 

    "{b}{i}En entrant dans la bibliothèque, tu regardes autour de toi.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "On dirait qu'il n'y a personne..."
    play sound "Click.mp3" noloop 

    P "attends deux secondes, je crois voir quelqu'un là-bas..."
    play sound "Footsteps.mp3" noloop

    "{b}{i}Tu te diriges vers la personne.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut [I], tu es toute seule ?"
    play sound "Click.mp3" noloop

    I "Oh salut [prenom], oui je suis toute seule."
    play sound "Click.mp3" noloop

    P "Je voulais te parler d'un truc."
    play sound "Click.mp3" noloop

    I "Ah oui de quoi ?"
    play sound "Click.mp3" noloop

    P "C'est à propos de [newname]."
    play sound "Click.mp3" noloop

    I "Ah d'accord, qu'est-ce qu'il y a ?"
    play sound "Click.mp3" noloop

    P "Je voulais savoir si tu pouvais m'aider à mieux la comprendre."
    play sound "Click.mp3" noloop 

    I "Bien sûr, je peux t'aider. Que veux-tu savoir ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas trop par où commencer..."
    play sound "Click.mp3" noloop

    I "Pas de souci, on peut y aller étape par étape. Qu'est-ce que tu as remarqué chez elle jusqu'à présent ?"
    play sound "Click.mp3" noloop

    P "c'est concernant son mot de passe."
    play sound "Click.mp3" noloop

    I "Ah, je vois. Quel est le problème avec son mot de passe ?"
    play sound "Click.mp3" noloop

    P "J'ai fait un systéme de mot de passe pour elle pour la réveiller le matin, mais maintenant elle veut se réveiller toute seule."
    play sound "Click.mp3" noloop

    I "C'est intéressant. Peut-être qu'elle cherche à avoir plus d'autonomie. As-tu essayé de lui demander pourquoi elle veut se réveiller toute seule ?"
    play sound "Click.mp3" noloop

    P "Elle m'a dit qu'elle fait déjà tout le reste toute seule, alors pourquoi pas ça aussi."
    play sound "Click.mp3" noloop

    I "C'est une bonne raison. Peut-être qu'elle veut juste se sentir plus indépendante. Tu pourrais essayer de lui faire confiance et de la laisser gérer son propre réveil."
    play sound "Click.mp3" noloop

    P "Mais je dois toujours m'occuper de ses mises à jour et de son entretien technique donc pourquoi pas son mot de passe aussi comme je l'ai fait jusqu'à présent."
    play sound "Click.mp3" noloop   

    I "C'est vrai, mais peut-être que pour elle, le fait de se réveiller seule est un petit pas vers plus d'autonomie. Tu pourrais essayer de lui faire confiance sur ce point et voir comment ça se passe."
    play sound "Click.mp3" noloop

    P "Sachant que si je retire son mot de passe et elle sera complétment autonome, donc tu en penses quoi ?"
    play sound "Click.mp3" noloop

    I "Je pense que c'est une bonne idée. Si elle se sent prête à être autonome, pourquoi ne pas lui donner cette chance ?"
    play sound "Click.mp3" noloop

    P "D'accord, je vais lui en parler et voir ce qu'elle en pense car elle veux vraiment se réveiller toute seule le matin."
    play sound "Click.mp3" noloop

    I "Bonne idée. Tiens-moi au courant de ce qu'elle en pense."
    play sound "Click.mp3" noloop

    P "Pas de souci, merci pour ton aide [I]."
    play sound "Click.mp3" noloop

    I "De rien, à plus tard [prenom]."
    play sound "Click.mp3" noloop

    P "À plus tard."
    play sound "Footsteps.mp3" noloop

    hide screen library with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Tu quittes la bibliothèque.{/i}{/b}"
    play sound "Door.mp3" noloop 

    scene hall with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hall with moveinright

    "{b}{i}Tu continues ton chemin vers le dortoir.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hall with moveoutright 
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene staircase with fade 

    "{b}{i}Tu montes au premier étage.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    scene hallway with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright 

    "{b}{i}Tu continues dans le couloir.{/i}{/b}"
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

    Na "Re-bonjour [prenom], tu es déjà de retour ?"
    play sound "Click.mp3" noloop

    P "Oui, je suis déjà de retour."
    play sound "Click.mp3" noloop

    Na "Tu as l'air pensif, tout va bien ?"
    play sound "Click.mp3" noloop

    P "J'ai discuté avec [I] à la bibliothèque. car elle n'était pas à son dortoir."
    play sound "Click.mp3" noloop

    Na "Ah d'accord, et de quoi avez-vous parlé ?"
    play sound "Click.mp3" noloop

    P "Je lui ai parlé de toi et de ton envie de te réveiller toute seule le matin."    
    play sound "Click.mp3" noloop

    Na "Ah oui, et qu'est-ce qu'elle en a pensé ?"
    play sound "Click.mp3" noloop

    P "Elle m'a conseillé de te faire confiance et de te laisser gérer ton propre réveil."
    play sound "Click.mp3" noloop

    Na "C'est gentil de sa part. Je comprends que tu veuilles t'assurer que tout va bien pour moi, mais je pense que je suis prête à être plus autonome."
    play sound "Click.mp3" noloop

    P "Donc je vais m'en occuper ce demain."
    play sound "Click.mp3" noloop

    Na "Merci [prenom], je te promets que je ferai de mon mieux pour me réveiller à l'heure et seule."
    play sound "Click.mp3" noloop

    P "Je te fais confiance."
    play sound "Click.mp3" noloop

    Na "Merci [prenom], tu es vraiment gentil."
    play sound "Click.mp3" noloop

    P "De rien, c'est normal."
    play sound "Click.mp3" noloop

    Na "Bon, je vais aller lire un peu maintenant."
    play sound "Click.mp3" noloop

    P "D'accord, bonne lecture alors."
    play sound "Click.mp3" noloop

    Na "Merci, à plus tard [prenom]."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}[newname] part pour aller lire.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, je vais me poser un peu devant l'ordi."
    play sound "Click.mp3" noloop

    "{b}{i}Tu t'installes confortablement.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Aller, voyons voir les nouveautés sur le net."
    play sound "Click.mp3" noloop

    "{b}{i}Tu passes le reste de la matinée à naviguer sur internet.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "[newname] tu lis encore un peu à ce que je sache ?"
    play sound "Click.mp3" noloop

    Na "Oui d'ailleurs, je viens de finir le dernier chapitre."
    play sound "Click.mp3" noloop

    P "Et alors, qu'est-ce que tu en as pensé ?"
    play sound "Click.mp3" noloop

    Na "C'était vraiment intéressant, j'ai beaucoup aimé la fin."  
    play sound "Click.mp3" noloop

    P "Content que ça t'ait plu."
    play sound "Click.mp3" noloop

    Na "Merci encore de m'avoir conseillé ce livre."
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

    "{b}{i} Vous mangez tranquillement ensemble.{/i}{/b}"
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
    Na "[bien]" 
    play sound "Click.mp3" noloop 

    P "Bon moi je vais aller lire un peu."
    play sound "Click.mp3" noloop

    Na "D'accord, bonne lecture alors."
    play sound "Click.mp3" noloop

    P "Merci, à plus tard [newname]."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    Na "[nothing]"
    play sound "Click.mp3" noloop

    P "Et toi tu vas faire quoi ?"
    play sound "Click.mp3" noloop

    Na "je vais faire du dessin."
    play sound "Click.mp3" noloop

    P "Depuis quand tu dessines ?"
    play sound "Click.mp3" noloop

    Na "J'ai commencé à dessiner il y a quelques mois, c'est un passe-temps que j'apprécie."
    play sound "Click.mp3" noloop

    P "Tu dessines quoi comme style ?"  
    play sound "Click.mp3" noloop

    Na "J'aime bien dessiner des paysages et des portraits, mais j'essaie aussi d'explorer d'autres styles."
    play sound "Click.mp3" noloop

    P "C'est cool, j'aimerais bien voir tes dessins un jour."
    play sound "Click.mp3" noloop

    Na "Avec plaisir, je te montrerai ça un de ces jours."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te poses pour lire un livre.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Tu lis pendant une bonne heure mais quelqu'un vient frapper à la porte.{/i}{/b}"
    play sound "Knock.mp3" noloop

    Na "C'est qui à la porte ?"
    play sound "Click.mp3" noloop

    P "Je ne sais pas, je vais aller voir."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te lèves pour aller ouvrir la porte.{/i}{/b}"
    play sound "Door.mp3" noloop

    "{b}{i}Tu ouvres la porte.{/i}{/b}"
    play sound "Click.mp3" noloop

    J1 "Salut [prenom] !"
    play sound "Click.mp3" noloop

    P "Salut Ayano, qu'est-ce que tu fais ici ?"
    play sound "Click.mp3" noloop

    J1 "Je suis venue te ramener ton tourne-vis que ma soeur a oublié de te rendre."
    play sound "Click.mp3" noloop

    P "Ah d'accord, merci car ça fait une semaine que je lui ai prêté et j'en aurai besoin demain."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    J1 "[nothing]"
    play sound "Click.mp3" noloop

    P "Tu veux entrer ?"
    play sound "Click.mp3" noloop

    J1 "Oui, si ça ne te dérange pas sinon en dehors de ça vous allez comment ?"
    play sound "Click.mp3" noloop

    P "On va bien, merci. Et toi ?"
    play sound "Click.mp3" noloop

    J1 "Ça va, merci."
    play sound "Click.mp3" noloop

    P "Bon entre alors."
    play sound "Click.mp3" noloop

    "{b}{i}Tu laisses entrer Ayano dans ton dortoir.{/i}{/b}"
    play sound "Click.mp3" noloop

    J1 "Merci [prenom]."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    J1 "Au fait, [newname] est en train de faire quoi ?"
    play sound "Click.mp3" noloop

    P "Elle est en train de dessiner."
    play sound "Click.mp3" noloop

    J1 "Ah d'accord, elle dessine quoi ?"
    play sound "Click.mp3" noloop

    P "Des paysages et des portraits."
    play sound "Click.mp3" noloop

    J1 "Oh c'est cool ça. Tu pourrais lui demander de te montrer ses dessins un jour."
    play sound "Click.mp3" noloop

    P "Oui, c'est une bonne idée."
    play sound "Click.mp3" noloop

    J1 "Bon je vais devoir vous laisser."
    play sound "Click.mp3" noloop

    P "D'accord, merci encore pour le tourne-vis."
    play sound "Click.mp3" noloop

    J1 "De rien, à plus tard [prenom]."
    play sound "Footsteps.mp3" noloop

    "{b}{i}Ayano finit par partir et [newname] retire ses écouteurs.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "C'était qui à la porte car j'avais mes écouteurs ?"
    play sound "Click.mp3" noloop

    P "C'était Ayano, elle est venue me rendre un tourne-vis."
    play sound "Click.mp3" noloop

    Na "Ah d'accord, merci de me l'avoir dit donc demain tu vas t'occuper de moi ?"
    play sound "Click.mp3" noloop

    P "Oui, je vais m'en occuper demain." 
    play sound "Click.mp3" noloop

    Na "Cool alors, merci [prenom]."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}Puis l'après-midi continue tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Je suis fatiguée, j'ai beaucoup dessiné cette après-midi."
    play sound "Click.mp3" noloop

    P "Tu devrais te reposer un peu."
    play sound "Click.mp3" noloop

    Na "Non ça va aller, je veux juste aller chercher à manger."
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

    "{b}{i}Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop

    P "Bien."
    play sound "Click.mp3" noloop

    Na "Bon Je vais me déconnecter et me recharger car je suis fatiguée."
    play sound "Click.mp3" noloop 

    P "Attends, je voulais te dire un truc d'abord."
    play sound "Click.mp3" noloop

    Na "Oui dis-moi je t'écoute."
    play sound "Click.mp3" noloop

    P "Demain matin se sera la dernière fois que j'utiliserai le mot de passe pour te réveiller."
    play sound "Click.mp3" noloop

    Na "Oui merci beaucoup." 
    play sound "Click.mp3" noloop

    P "De rien car je pense que tu dois complétment être libre même si tu l'es déjà pratiqument à part ton réveil."
    play sound "Click.mp3" noloop

    Na " Bon moi je vais vraiment aller me déconnecter."
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




    label end_script3:
    call script4 from _call_script4  
    return 

# Aris la plus belle ###################    