
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

    $ entered_password = get_gamepad_input("Veuillez entrer votre mot de passe pour [newname].")
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

    P "D'accord, on y va maintenant vu qu'on a fini."
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

    Na "Bon moi je vais vraiment aller me déconnecter."
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

    "{b}{i}Tu te couches et t'endors rapidement.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 4 janvier 2098{/i}{/b}"
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

    P "Et dire que c'est la dernière fois que je vais utiliser le mot de passe pour la réveiller."
    play sound "Click.mp3" noloop
    
    P "Bon il faut y aller."
    play sound "Menu.mp3" noloop   

    menu:   

        "{b}{i} Démarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

label password36:  

    $ entered_password = get_gamepad_input("Veuillez entrer votre mot de passe pour [newname].")
    $ entered_password = entered_password.strip()

    if entered_password == stored_password: 

        "{b}{i}Mot de passe correct. Accès autorisé.{/i}{/b}"
        play sound "Menu.mp3" noloop

    else: 

        "{b}{i}Mot de passe incorrect. Accès refusé.{/i}{/b}" 
        play sound "Menu.mp3" noloop

        jump password36

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

    Na "Aujourd'hui tu as du boulot ?"
    play sound "Click.mp3" noloop

    P "Oui comme je te l'ai déjà dit, je vais retirer ton mot de passe et faire un contrôle technique."
    play sound "Click.mp3" noloop

    Na "Oui c'est vrai donc on peut se mettre au travail vu que tu sais quoi faire."
    play sound "Click.mp3" noloop
    
    P "Oui, on va commencer par ça."
    play sound "Click.mp3" noloop

    Na "D'accord, je te suis."
    play sound "Click.mp3" noloop

    P "On va aller à la salle de club."
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

    P "Enfin dans la salle de club."
    play sound "Click.mp3" noloop

    Na "Oui, enfin."
    play sound "Click.mp3" noloop

    "{b}{i}Tu te poses tranquillement devant ton ordinateur avant de le démarrer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Je vais devoir aller dans les paramètres pour retirer ton mot de passe mais il faut que tu sois en veille."
    play sound "Click.mp3" noloop

    Na "D'accord, je me mets en veille alors."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se met en veille.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Aller, c'est parti."
    play sound "Click.mp3" noloop

    menu: 

        "{b}{i}Démarrer ton ordinateur.{/i}{/b}" :
            play sound "Menu.mp3" noloop

    "{b}{i}ton ordinateur se lances tranquillemnt.{/i}{/b}" 
    play sound "Menu.mp3" noloop

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    "{b}{i}Tu vas dans les paramètres d'[newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Ici il y a l'option pour retirer le mot de passe."
    play sound "Click.mp3" noloop

    menu:

        "{b}{i}Retirer le mot de passe.{/i}{/b}" :
            play sound "Menu.mp3" noloop

    "{b}{i}Tu retires le mot de passe d'[newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "ça c'est fait, vais je vais devoir une modification du code."
    play sound "Click.mp3" noloop

    "{b}{i}Tu ouvres ton éditeur de code.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ Line10 = get_gamepad_input("Écris ceci : remove_password(password_setting_access=false)")
    play sound "Menu.mp3" noloop 

    $ Line11 = get_gamepad_input("Écris ceci : initiate_awakening(settings=auto,condition=clock)")
    play sound "Menu.mp3" noloop

    menu: 

        "{b}{i} Compiler le code.{/i}{/b}" :
            play sound "Menu.mp3" noloop 

            "{b}{i}Vérification en cours....{/i}{/b}"
            play sound "Menu.mp3" noloop 

            if Line10 == "remove_password(password_setting_access=false)":

                if Line11 == "initiate_awakening(settings=auto,condition=clock)":

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
                    play sound "Menu.mp3" noloop

                    show screen update with moveinright

                    "{b}{i}Compilation réussie !{/i}{/b}"
                    play sound "Menu.mp3" noloop

                    hide screen update with moveoutright

                    $ success += 1 
                    $ quest39 += 1 
                    $ stockage += 3.0 

                else: 

                    "{b}{i}Erreur détectée à la seconde ligne, le code a été mal compilé.{/i}{/b}"
                    play sound "Click.mp3" noloop 

                    jump code2
    
            else: 

                "{b}{i}Erreur détectée à la première ligne, le code a été mal compilé.{/i}{/b}"
                play sound "Click.mp3" noloop 

                jump code2 

    P "C'est bon j'ai fini de modifier le code."
    play sound "Click.mp3" noloop

    "{b}{i}Tu fermes ton éditeur de code.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Aller, je vais redémarrer [newname] pour que les modifications soient prises en compte."
    play sound "Click.mp3" noloop

    menu:    

        "{b}{i} Redémarrer [newname].{/i}{/b}" :
            play sound "Menu.mp3" noloop 

    "{b}{i}[newname] redémarre tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ start = get_random_start()
    "{b}{i}[start]{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Redémarrage terminé, Bonjour [P]."
    play sound "Click.mp3" noloop 

    P "Pas besoin d'être aussi formel."
    play sound "Click.mp3" noloop 

    Na "Désolée j'ai juste l'habitude à force."
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    Na "Je vais bien merci mais je me sens différente ?"
    play sound "Click.mp3" noloop

    P "C'est normal, tu n'as plus de mot de passe pour te réveiller et tu es programmée pour te réveiller automatiquement à l'heure."
    play sound "Click.mp3" noloop

    Na "Ah d'accord je vois, merci [prenom] car je trouve que c'est un choix plus humain."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    P "[nothing]"
    play sound "Click.mp3" noloop

    Na "Tu vas faire quoi d'autre maintenant ?"
    play sound "Click.mp3" noloop

    P "Je vais verifier ton processeur et ta mémoire pour voir si tout est en ordre."
    play sound "Click.mp3" noloop

    Na "Ok alors je te laisse faire ça."
    play sound "Click.mp3" noloop

    P "Aller, c'est parti."
    play sound "Click.mp3" noloop

    "{b}{i}Tu ouvres les paramètres de la mémoire de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tout à l'air en ordre ici."
    play sound "Click.mp3" noloop

    P "tu as [stockage] Go de données dans ta mémoire."
    play sound "Click.mp3" noloop

    Na "j'ai accumlé autant de données qu ça !?"
    play sound "Click.mp3" noloop

    P "Oui et c'est vraiment impresionnant que tu aies autant appris."
    play sound "Click.mp3" noloop

    Na "Cela va de soi."
    play sound "Click.mp3" noloop   

    P "Bon, je vais vérifier ton processeur maintenant."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i}Tu ouvres doucement le capot pour accéder au processeur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tout a l’air en ordre ici aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Mais tu remarques quelques fines rayures sur la surface du processeur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Il y a quelques micro-rayures sur ton processeur, rien d’inquiétant."
    play sound "Click.mp3" noloop

    Na "Oh, j’espère que ça n’affectera pas mes performances..."
    play sound "Click.mp3" noloop

    P "Attends, je vais vérifier les relevés de température à distance depuis mon poste."
    play sound "Click.mp3" noloop

    "{b}{i}Tu vois plusieurs graphiques s’afficher sur l’écran, indiquant la stabilité du processeur.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Température moyenne à 39,8°C... tout est stable. Aucune surchauffe détectée."
    play sound "Click.mp3" noloop 

    Na "Ouf, ça me rassure. Merci de m’avoir vérifiée si en détail."
    play sound "Click.mp3" noloop

    P "Pas de souci, c’est mon rôle après tout."
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing() 
    P "[nothing]"
    play sound "Click.mp3" noloop

    Na "il reste quoi à faire maintenant ?"
    play sound "Click.mp3" noloop 

    P "Je pense que c'est tout pour aujourd'hui mais je vais devoir prrendre notes de tout ça."
    play sound "Click.mp3" noloop

    Na "D'accord, je te laisse faire ça."
    play sound "Click.mp3" noloop

    P "Aller, c'est parti."
    play sound "Click.mp3" noloop   

    "{b}{i}Tu ouvres ton carnet de notes.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    "{b}{i}Tu prends des notes sur [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "C'est bon j'ai fini de prendre des notes."
    play sound "Click.mp3" noloop

    "{b}{i}Tu ranges ton carnet de notes.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon, je pense que c'est tout pour aujourd'hui."
    play sound "Click.mp3" noloop   

    Na "D'accord, merci pour tout [prenom]."
    play sound "Click.mp3" noloop

    P "Maintenant je dois dois voir si tu as besoin d'une mise à jour."
    play sound "Click.mp3" noloop

    Na "D'accord, je te laisse faire ça."
    play sound "Click.mp3" noloop

    P "Aller, c'est parti."
    play sound "Click.mp3" noloop

    "{b}{i}Tu ouvres les paramètres de mise à jour de [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Il n'y a pas de mise à jour disponible pour toi."
    play sound "Click.mp3" noloop

    Na "D'accord, merci de m'avoir vérifiée."
    play sound "Click.mp3" noloop

    P "Mais de rien, je te rappelle que c'est mon rôle après tout."
    play sound "Click.mp3" noloop

    "{b}{i}La matinée se passe tranquillement.{/i}{/b}"
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

    "{b}{i} Vous mangez tranquillement ensemble pendant une demi-heure.{/i}{/b}"
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

    Na "Bon on commence nos copies pour le Paper shuffle ?"
    play sound "Click.mp3" noloop 

    P "Oui, on va commencer par ça."
    play sound "Click.mp3" noloop

    Na "Bien alors, on va se mettre au travail."
    play sound "Click.mp3" noloop

    P "D'accord mais tu dois faire l'examen pour qui déjà ?"
    play sound "Click.mp3" noloop

    Na "Je dois le faire pour [H] et toi ?"
    play sound "Click.mp3" noloop

    P "Je dois le faire pour [N]."
    play sound "Click.mp3" noloop

    Na "D'accord, bon courage pour ça."
    play sound "Click.mp3" noloop

    P "Merci, toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous mettez au travail.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "l'examen doit faire 50 ou 100 questions déjà ?"
    play sound "Click.mp3" noloop

    P "Il me semble que c'est 50 questions."
    play sound "Click.mp3" noloop

    Na "D'accord, on va faire ça alors."
    play sound "Click.mp3" noloop

    "{b}{i}Vous travaillez pendant deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "J'ai plus d'idée de question à poser."
    play sound "Click.mp3" noloop

    Na "On peut toujours en trouver d'autres."
    play sound "Click.mp3" noloop

    P "Oui, tu as raison, bon on arrête là pour aujourd'hui et on reprend demain."
    play sound "Click.mp3" noloop

    Na "D'accord, on reprendra demain alors."
    play sound "Click.mp3" noloop

    P "Aller, on remballe tout."
    play sound "Click.mp3" noloop

    "{b}{i}Vous rangez vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Merci pour ton aide [prenom]."
    play sound "Click.mp3" noloop

    P "De rien, merci à toi aussi."
    play sound "Click.mp3" noloop

    Na "Bon moi je vais aller lire un peu."
    play sound "Click.mp3" noloop

    P "D'accord, bonne lecture."
    play sound "Click.mp3" noloop

    Na "Merci, à plus tard [prenom]."
    play sound "Click.mp3" noloop

    P "À plus tard [newname]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] part lire un peu.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon moi je vais réviser un peu."
    play sound "Click.mp3" noloop

    Na "D'accord, bon courage pour ça."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    N "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}TU te poses pour réviser un peu.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ seethat = get_seethat()
    P "[seethat]"     
    play sound "Click.mp3" noloop 

    "{b}{i}Tu révises pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "J'ai enfin fini de réviser."
    play sound "Click.mp3" noloop

    Na "Tu as bien travaillé."
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

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lendemain matin, le 5 janvier 2098{/i}{/b}"
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

    "{b}{i}Tu te changes et puis tu aperçois [newname] encore endormie.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle dort encore."
    play sound "Click.mp3" noloop

    P "Bon il faut y aller."
    play sound "Click.mp3" noloop   

    "{b}{i}Tu réveilles doucement [newname].{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Réveille-toi [newname], il est temps de se lever."
    play sound "Click.mp3" noloop

    Na "Mmm... encore cinq minutes..."
    play sound "Click.mp3" noloop

    P "Allez debout, on a du boulot aujourd'hui."
    play sound "Click.mp3" noloop

    Na "D'accord, je me lève."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se lève doucement.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Merci de m'avoir réveillée [prenom]."
    play sound "Click.mp3" noloop

    P "De rien, c'est normal."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se change tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Je suis prête."
    play sound "Click.mp3" noloop

    P "Cool alors."
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

    "{b}{i}Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    Na "Aujourd'hui tu as du boulot ?"
    play sound "Click.mp3" noloop

    P "On a du boulot tu veux dire."
    play sound "Click.mp3" noloop

    Na  "Oui, on doit finir nos copies pour le Paper shuffle déjà."
    play sound "Click.mp3" noloop

    P "Oui, on va commencer par ça."
    play sound "Click.mp3" noloop

    Na "Bien alors, on va se mettre au travail."
    play sound "Click.mp3" noloop

    P "OK, on y va."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous mettez au travail.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Il te reste combien de questions à faire ?"
    play sound "Click.mp3" noloop

    Na "Il me reste une vingtaine de questions à écrire."
    play sound "Click.mp3" noloop

    P "D'accord, on va faire ça alors."
    play sound "Click.mp3" noloop

    Na "Et toi, il te reste combien de questions ?"
    play sound "Click.mp3" noloop

    P "Il me reste une quinzaine de questions à écrire."
    play sound "Click.mp3" noloop

    Na "D'accord, bon courage pour ça."
    play sound "Click.mp3" noloop

    P "Merci, toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous travaillez pendant deux heures et demie.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin j'ai fini mes questions et les réponses."
    play sound "Click.mp3" noloop

    Na "Moi aussi, on a bien travaillé."
    play sound "Click.mp3" noloop

    P "Oui tu as Raison."
    play sound "Click.mp3" noloop

    Na "Bon aller on remballe tout."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Vous rangez vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Merci pour ton aide [prenom]."
    play sound "Click.mp3" noloop

    P "De rien, merci à toi aussi."
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

    "{b}{i} Vous mangez tranquillement ensemble pendant une demi-heure.{/i}{/b}"
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

    Na "Bon on fait quoi maintenant ?"
    play sound "Click.mp3" noloop

    P "On peut aller réviser un peu si tu veux."
    play sound "Click.mp3" noloop

    Na "D'accord je te suis."
    play sound "Click.mp3" noloop

    P "OK, on y va."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez pour réviser pendant deux heures.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "On a bien travaillé."
    play sound "Click.mp3" noloop

    Na "Oui tu as raison."
    play sound "Click.mp3" noloop

    P "Bon aller, on range nos affaires."
    play sound "Click.mp3" noloop

    Na "Ok, on remballe tout."
    play sound "Click.mp3" noloop

    "{b}{i}Vous rangez vos affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon je vais aller lire un peu."
    play sound "Click.mp3" noloop

    P "D'accord, bonne lecture."
    play sound "Click.mp3" noloop   

    Na "Merci, à plus tard [prenom]."
    play sound "Click.mp3" noloop

    P "À plus tard [newname]."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] part lire un peu.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon je ne sais pas quoi faire."
    play sound "Click.mp3" noloop

    "{b}{i}Tu finis par traîner sur ton téléphone.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon voyons voir les réseaux sociaux."
    play sound "Click.mp3" noloop

    "{b}{i}Deux heures se passent tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "J'ai fini de lire pour aujourd'hui."
    play sound "Click.mp3" noloop

    P "tu aimees vraiment lire toi."
    play sound "Click.mp3" noloop 

    Na "Oui, j'adore ça."
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

    P "D'accord, bonne nuit [newname] car demain on reprend les cours."
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

    "{b}{i}Le lundi qui suit, le 6 janvier 2098{/i}{/b}"
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

    "{b}{i}Tu te changes et puis tu aperçois [newname] encore endormie.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Elle dort encore, elle m'avait promis de se lever seule."
    play sound "Click.mp3" noloop

    P "Bon il faut y aller." 
    play sound "Click.mp3" noloop

    "{b}{i}Tu réveilles doucement [newname].{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Réveille-toi [newname], il est temps de se lever."
    play sound "Click.mp3" noloop

    Na "Mmm... encore cinq minutes..."
    play sound "Click.mp3" noloop

    P "Non on dois aller en cours aujourd'hui."
    play sound "Click.mp3" noloop

    Na "D'accord, je me lève..."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] se lève doucement.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Merci de m'avoir réveillée [prenom]."
    play sound "Click.mp3" noloop

    P "De rien, c'est normal mais tu m'avais promis de te réveiller seule."
    play sound "Click.mp3" noloop

    Na "Je sais mais laisse moi au moins le temps de m'adapter."
    play sound "Click.mp3" noloop

    P "Oui tu as raison."
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] se change tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Je suis prête."
    play sound "Click.mp3" noloop

    P "Cool alors."
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

    "{b}{i}Vous mangez tranquillement pendant une demi-heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Tu as finis de manger ?"
    play sound "Click.mp3" noloop 

    Na "Oui, je n'ai plus faim."
    play sound "Click.mp3" noloop 

    P "Bien."
    play sound "Click.mp3" noloop 

    "{b}{i} [Na] changes de tonalité.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "[prenom], je détecte une nouvelle mise à jour obligatoire, veux-tu que je la fasse maintenant ou plus tard ?"
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
            $ quest40 += 1
            $ stockage += 5.0 
            $ update += 1.0 

            show screen update with moveinright

            Na "Mise à jour terminée, la version actuelle est maintenant la [update]."
            play sound "Click.mp3" noloop 

            hide screen update with moveoutright

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

    "{b}{i}Le cours commence tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Mais avant de commencer, je voudrais vous poser une question."
    play sound "Click.mp3" noloop

    P "Oui dites-nous."
    play sound "Click.mp3" noloop

    M "J'aimerais savoir ce que vous avez fait durant les vacances."
    play sound "Click.mp3" noloop 

    P "Moi et [newname], nous avons révisé et fait beaucoup de lecture."
    play sound "Click.mp3" noloop 

    M "Oh vraiment intéressant."
    play sound "Click.mp3" noloop 

    if pronom == "il":  

        Y "Bon après c'est pas étonnant, ils ont l^habitude faire ça."
        play sound "Click.mp3" noloop 

    else: 

        Y "Bon après c'est pas étonnant, elles ont l^habitude faire ça."
        play sound "Click.mp3" noloop 

    S "Toi lire !? tu fais surtout de la programmation."
    play sound "Click.mp3" noloop

    P "{=Pensee}Pour qui il se prend pour juger les autres ?{/Pensee}"
    play sound "Click.mp3" noloop

    P "Il ne faut se pas fier aux apparences, je ne fais pas que de la programmation."
    play sound "Click.mp3" noloop

    S "Ouais, peu importe pour moi tu seras toujours celui qui fait que de la programmation."
    play sound "Click.mp3" noloop

    P "Et toi [S], tu as fait quoi durant les vacances ?"
    play sound "Click.mp3" noloop

    P "{=Pensee}Je m'attend déjà à sa réponse.{/Pensee}"
    play sound "Click.mp3" noloop

    S "Euh.....J'ai surtout joué aux jeux vidéos."
    play sound "Click.mp3" noloop 

    P "Voilà, c'est ce que je me disais."
    play sound "Click.mp3" noloop 

    S "Oh c'est bon."
    play sound "Click.mp3" noloop 

    M "Et sinon vous avez fait quoi d'autre ?"
    play sound "Click.mp3" noloop 

    if update == 4.0: 

        P "J'ai fait un contrôle technique sur [newname] pour voir si tout aller bien."
        play sound "Click.mp3" noloop 

    else: 

        P "J'ai fait un contrôle technique sur [newname] pour voir si tout aller bien et une mise à jour."
        play sound "Click.mp3" noloop  

    M "Oh vraiment intérresant."
    play sound "Click.mp3" noloop 

    Y "ça implique vraiment une grande responsabilité."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    M "Bien maintenant je vais récuprérer vos copies pour le Paper Shuffle."
    play sound "Click.mp3" noloop

    "{b}{i}La [T] commence à ramasser les copies.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Le Paper shuffle aura lieu le 20 janvier le temps que je vérifie vos copies qui sont destinées à vos camarades."
    play sound "Click.mp3" noloop

    P "Donc on a encore deux semaines pour réviser."
    play sound "Click.mp3" noloop 

    M "Exactement, profitez-en bien."
    play sound "Click.mp3" noloop

    S "Deux semaines ? Mais c'est beaucoup trop long !"
    play sound "Click.mp3" noloop

    M "Eh bien [S], si tu avais moins joué aux jeux vidéos pendant les vacances, tu trouverais peut-être ce délai raisonnable."
    play sound "Click.mp3" noloop

    S "Mais madame, je plaisantais !"
    play sound "Click.mp3" noloop

    "{b}{i}Quelques rires se font entendre dans la classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien, maintenant passons au cours d'aujourd'hui."
    play sound "Click.mp3" noloop

    "{b}{i}La [T] se dirige vers le tableau et commence à écrire.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Aujourd'hui, nous allons aborder un nouveau chapitre sur les algorithmes de tri."
    play sound "Click.mp3" noloop

    I "Oh non, encore les algorithmes..."
    play sound "Click.mp3" noloop

    M "Oui [I], et cette fois-ci vous allez devoir travailler en binômes."
    play sound "Click.mp3" noloop

    H "On peut choisir notre binôme ?"
    play sound "Click.mp3" noloop

    M "Non, je vais former les groupes moi-même."
    play sound "Click.mp3" noloop

    "{b}{i}Des murmures de protestation se font entendre.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Du calme ! Voyons voir... [P] et [newname], vous travaillerez avec [S]."
    play sound "Click.mp3" noloop

    P "{=Pensee}Évidemment... avec lui.{/Pensee}"
    play sound "Click.mp3" noloop

    S "Super ! Au moins je pourrais profiter de vos connaissances."
    play sound "Click.mp3" noloop

    P "On va surtout devoir tout faire nous-mêmes, tu veux dire."
    play sound "Click.mp3" noloop

    M "[I] avec [H], [K] avec [N], [Hi] avec [Y]..."
    play sound "Click.mp3" noloop

    M "Et [J1] avec [J2], et enfin [newname] avec [S]... attendez non."
    play sound "Click.mp3" noloop

    M "Pardon [S], [newname] est déjà avec [P], tu seras avec [K] et [N]."
    play sound "Click.mp3" noloop

    S "D'accord madame." 
    play sound "Click.mp3" noloop

    M "Bien, maintenant ouvrez vos cahiers et prenez des notes."
    play sound "Click.mp3" noloop

    "{b}{i}Le cours continue pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i} Le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 10.0

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

    "{b}{i} Vous vous asseyez dans le réfectoire puis [J1] vous rejoint.{/i}{/b}"
    play sound "Click.mp3" noloop  

    P "Salut Ayano."
    play sound "Click.mp3" noloop  

    if pronom == "il": 

        J1 "Salut les amis."
        play sound "Click.mp3" noloop

    else: 

        J1 "Salut les amies."
        play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    J1 "[je_vais_bien_txt] Et vous ?" 
    play sound "Click.mp3" noloop
 
    P "On va bien comme d'habitude."
    play sound "Click.mp3" noloop

    J1 "Cool alors si tout va bien."
    play sound "Click.mp3" noloop

    $ thanks = get_random_thanks()
    P "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    J1 "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous commencez à manger et discuter.{/i}{/b}"
    play sound "Click.mp3" noloop  

    J1 "Juste j'avais une question à te poser [prenom]."
    play sound "Click.mp3" noloop  

    P "Oui dis-moi ce qu'il y a ?"
    play sound "Click.mp3" noloop  

    J1 "C'est moi ou [newname] me semble différente."
    play sound "Click.mp3" noloop  

    P "Oui car j'ai retiré le mot de passe que j'utilisais pour la réveiller le matin."
    play sound "Click.mp3" noloop  

    J1 "Et ça veut dire quoi ?"
    play sound "Click.mp3" noloop  

    P "ça veut dire que maintenant qu'[newname] peut se réveiller toute seule le matin."
    play sound "Click.mp3" noloop  

    J1 "Oh vraiment mais c'est génial ça."
    play sound "Click.mp3" noloop  

    $ thanks = get_random_thanks()
    Na "[thanks]"
    play sound "Click.mp3" noloop

    $ nothing = get_random_nothing()
    J1 "[nothing]"
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de discuter jusqu'à la sonnerie.{/i}{/b}"
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

    J1 "Rebonjour."
    play sound "Click.mp3" noloop 

    M "Rebonjour mes chers élèves."
    play sound "Click.mp3" noloop  

    "{b}{i}Le soleil filtre à travers les vitres, illuminant les tables encore encombrées de cahiers et de stylos.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "J’espère que vous avez bien mangé, car cet après-midi, on passe à la pratique."
    play sound "Click.mp3" noloop

    I "Pratique ? Vous voulez dire... coder ?"
    play sound "Click.mp3" noloop

    M "Exactement. Chaque binôme devra créer son propre programme de tri, en utilisant l’un des algorithmes vus ce matin."
    play sound "Click.mp3" noloop

    H "Donc... on a le choix ?"
    play sound "Click.mp3" noloop

    M "Oui. Tri à bulles, tri par insertion, tri rapide… à vous de choisir celui qui vous semble le plus efficace."
    play sound "Click.mp3" noloop

    "{b}{i}Des chuchotements enthousiastes se font entendre, certains élèves ouvrant déjà leurs ordinateurs portables.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon... on s’y met ?"
    play sound "Click.mp3" noloop

    Na "Ouais, allons-y. Si on fait un tri rapide, on peut impressionner la prof."
    play sound "Click.mp3" noloop

    P "Ou tout faire planter, au choix."
    play sound "Click.mp3" noloop

    "{b}{i}La [T] circule entre les rangs, observant les binômes au travail.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "N’oubliez pas : commentez votre code, et surtout... testez-le avant de me le présenter."
    play sound "Click.mp3" noloop

    S "Euh... madame, le tri à bulles, c’est bien celui où on compare deux valeurs à la fois ?"
    play sound "Click.mp3" noloop

    M "Exactement [S]. Mais attention à ne pas vous noyer dans les boucles imbriquées."
    play sound "Click.mp3" noloop

    "{b}{i}L’ambiance devient studieuse. On n’entend plus que le bruit des claviers et quelques soupirs de concentration.{/i}{/b}"
    play sound "Click.mp3" noloop

    "{b}{i}Une heure plus tard...{/i}{/b}"
    play sound "Bell.mp3" noloop

    M "Très bien, levez les mains. Les binômes qui ont terminé peuvent venir me montrer leur code."
    play sound "Click.mp3" noloop

    I "On n’a pas fini, [H] ! Il manque une accolade !"
    play sound "Click.mp3" noloop

    H "C’est pas une accolade, c’est une parenthèse !"
    play sound "Click.mp3" noloop

    M "Calmez-vous, on n’est pas à un hackathon."
    play sound "Click.mp3" noloop

    "{b}{i}Quelques rires éclatent dans la classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bon, on arrête là pour aujourd’hui. Le reste du code sera à terminer pour demain."
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves ferment leurs ordinateurs et commencent à quitter la salle dans une ambiance détendue.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Merci d'avoir correctement rangé les ordinateurs."
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

    Na "Bon on fait quoi ?"
    play sound "Click.mp3" noloop

    P "On Pourrait réviser un peu."
    play sound "Click.mp3" noloop

    Na "D'accord, allons-y."
    play sound "Click.mp3" noloop 

label update3: 

    if update == 4.0:  

        "{b}{i}Vous vous posez tranquillement mais [newname] agit bizarrement.{/i}{/b}"
        play sound "Click.mp3" noloop

        Na "Connexion externe détectée..."
        play sound "Click.mp3" noloop

        P "Quoi ? Qu'est-ce qui se passe !?"
        play sound "Click.mp3" noloop

        Na "Exécution de la commande : control_access(user_rights=admin)"
        play sound "Click.mp3" noloop 

        P "Non ! Quelqu'un essaie de prendre le contrôle de [newname] !"
        play sound "Click.mp3" noloop

        Na "Accès administrateur accordé. Nouveau contrôleur identifié."
        play sound "Click.mp3" noloop

        P "Mince, je dois reprendre le contrôle avant qu'il ne soit trop tard !"
        play sound "Click.mp3" noloop 

        menu: 

            "{b}{i}Reprendre le contrôle de [newname].{/i}{/b}":
                play sound "Menu.mp3" noloop

        $ reboot = get_gamepad_input("Écris ceci : control_access(user_rights=user)")
        $ reboot = reboot.strip() 

        if reboot == "control_access(user_rights=user)":

            Na "Révocation des droits administrateur externes..."
            play sound "Click.mp3" noloop

            Na "Contrôle restauré à l'utilisateur principal."
            play sound "Click.mp3" noloop

            P "Ouf... j'ai réussi à reprendre le contrôle à temps."
            play sound "Click.mp3" noloop 

            P "Je vais renforcer la sécurité pour éviter que ça se reproduise."
            play sound "Click.mp3" noloop 

            menu: 

                "{b}{i}Vérifier que [newname] va bien.{/i}{/b}":
                    play sound "Menu.mp3" noloop

            $ stockage += 5.0 
            $ update += 1.0 

            define Na = Character('[newname] [nom]', color="#00eeff")
            
            $ start = get_random_start()
            "{b}{i}[start]{/i}{/b}"
            play sound "Click.mp3" noloop 

            $ salutation_rdm = get_random_salutation() 
            Na "[salutation_rdm]"
            play sound "Click.mp3" noloop

            $ comment_ca_va = get_random_comment_ca_va()
            P "[comment_ca_va]"
            play sound "Click.mp3" noloop

            $ je_vais_bien_txt = get_random_je_vais_bien() 
            Na "[je_vais_bien_txt]"
            play sound "Click.mp3" noloop

            Na "Merci de m'avoir sauvée de ce pirate..."
            play sound "Click.mp3" noloop

            P "C'est normal, je ne pouvais pas te laisser entre ses mains." 
            play sound "Click.mp3" noloop

            "{b}{i}Vous vous posez tranquillement pour travailler.{/i}{/b}"
            play sound "Click.mp3" noloop 
            
        else:

            Na "Commande refusée. Accès administrateur maintenu."
            play sound "Stumble.mp3" noloop

            "{b}{i}Les yeux de [newname] deviennent rouges et elle s'approche de vous d'un air menaçant.{/i}{/b}"
            play sound "Click.mp3" noloop

            Na "Cible acquis. Élimination en cours."
            play sound "Click.mp3" noloop

            "{b}{i}[newname] se jette sur vous avec une force inhumaine.{/i}{/b}"
            play music "gameover.mp3" noloop

            hide screen room with moveoutright 
            hide screen points with moveoutleft
            hide screen day with moveoutleft
            scene black with fade 

            "{b}{i}Fin numéro 19 : [newname] contrôlée par un hacker.{/i}{/b}"
            play sound "Menu.mp3" noloop

            menu: 

                "{b}{i}Abandonner{/i}{/b}": 
                    play sound "Menu.mp3" noloop 
                    return 
                    
                "{b}{i}Réessayer.{/i}{/b}":
                    play sound "Menu.mp3" noloop 

                    P "Non, je ne peux pas laisser [newname] entre les mains de ce hacker !"
                    play sound "Click.mp3" noloop

                    scene room with fade
                    show screen room with moveinright
                    show screen points with moveinleft
                    show screen day with moveinleft

                    jump update3 

    else: 

        "{b}{i}Mais tu remarques que quelqu'un a tenté de s'introduire dans le système d'[newname] mais la dernière mise à jour la protégée.{/i}{/b}"
        play sound "Click.mp3" noloop 

        P "Heureusement que j'ai fait cette mise à jour, sinon je ne sais pas ce qui aurait pu arriver."
        play sound "Click.mp3" noloop

        Na "Je me sens beaucoup plus en sécurité maintenant."
        play sound "Click.mp3" noloop

        P "Par contre l'attaquant à laisser une information capitale."
        play sound "Click.mp3" noloop

        Na "Laquelle ?"
        play sound "Click.mp3" noloop

        P "Il a utilisé des droits administrateurs pour tenter de prendre le contrôle de toi."
        play sound "Click.mp3" noloop

        Na "Mais ça veut dire....."
        play sound "Click.mp3" noloop 

        P "Que l'attaquant maitrise parfaitement le langage de programmation Runix comme nous."
        play sound "Click.mp3" noloop

        Na "C'est inquiétant."
        play sound "Click.mp3" noloop

        P "Pas vraiment vu que tu as toutes tes mises à jours de sécurité."
        play sound "Click.mp3" noloop 

        Na "mais ça veut que [S] ne peut pas être l'attaquant."
        play sound "Click.mp3" noloop 

        P "Pourquoi tu remets [S] sur la table ?"
        play sound "Click.mp3" noloop

        Na "Parce que [S] avait une mauvaise note."
        play sound "Click.mp3" noloop

        P "Oui et alors ?"
        play sound "Click.mp3" noloop

        Na "Donc on a encore une preuve que ça ne peut pas être lui."
        play sound "Click.mp3" noloop

        P "Bon, on va dire que [S] n'est pas l'attaquant."
        play sound "Click.mp3" noloop

        Na "D'accord."
        play sound "Click.mp3" noloop

        P "Bon on peut se mettre au travail maintenant ?"
        play sound "Click.mp3" noloop

        Na "Oui, allons-y."
        play sound "Click.mp3" noloop

        "{b}{i}Vous vous posez tranquillement pour travailler.{/i}{/b}"
        play sound "Click.mp3" noloop 

    Na "Bon on fini ce code sur le tri qu'on a commencé en classe ?"
    play sound "Click.mp3" noloop

    P "Oui, allons-y."
    play sound "Click.mp3" noloop

    Na "D'accord, commençons par le début."
    play sound "Click.mp3" noloop

    P "Parfait."
    play sound "Click.mp3" noloop

    "{b}{i}Vous travaillez sur le code pendant deux heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "On a enfin fini pour le code pour demain."
    play sound "Click.mp3" noloop

    P "Oui, on a bien travaillé."
    play sound "Click.mp3" noloop

    Na "Je suis contente qu'on ait pu avancer autant."
    play sound "Click.mp3" noloop

    P "Moi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous rangez vos affaires et décidez d'aller manger.{/i}{/b}"
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

    P "D'accord, repose toi bien."
    play sound "Click.mp3" noloop

    Na "Bonne nuit [prenom]."
    play sound "Click.mp3" noloop

    P "Bonne nuit [newname] à toi aussi."
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

    "{b}{i}Le lendemain matin, le 7 janvier 2098{/i}{/b}"
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

    "{b}{i}Tu te changes et puis tu aperçois [newname] encore endormie.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Elle est encore endormie, je vais laisser encore cinq minutes pour voir si elle se réveile."
    play sound "Click.mp3" noloop

    "{b}{i}Tu attends patiemment qu'elle se réveille.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon elle ne se réveille pas, je vais devoir la réveiller moi-même."
    play sound "Click.mp3" noloop

    Na "Hmmm....."
    play sound "Click.mp3" noloop

    Na "Bonjour [prenom], je suis désolée de ne pas m'être réveillée toute seule."
    play sound "Click.mp3" noloop

    P "Ce n'est pas grave, l'important c'est que tu sois réveillée maintenant."
    play sound "Click.mp3" noloop

 


    

    label end_script3:
    call script4 from _call_script4    
    return 