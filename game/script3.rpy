
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

    $ entered_password = renpy.input("Veuillez entrer votre mot de passe pour [newname].")
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

    $ Line10 = renpy.input("Écris ceci : remove_password(password_setting_access=false)")
    play sound "Menu.mp3" noloop 

    $ Line11 = renpy.input("Écris ceci : initiate_awakening(settings=auto,condition=clock)")
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

        $ reboot = renpy.input("Écris ceci : control_access(user_rights=user)")
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

    Na "Oui tu as raison."
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

    M "Je vais commencer par ramasser les codes que je vous ai demandé de finir."
    play sound "Click.mp3" noloop

    M "Merci de me les remettre."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i}Tout le monde a rendu leur travail.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Parfait, maintenant nous allons passer à la suite du cours."
    play sound "Click.mp3" noloop

    M "Aujourd'hui, nous allons analyser différents codes de tri que vous avez fait."
    play sound "Click.mp3" noloop

    P "Intéressant de savoir comment les autres ont fait."
    play sound "Click.mp3" noloop

    M "Exactement, c'est important de voir différentes approches."
    play sound "Click.mp3" noloop

    M "Commençons par le groupe de [I] et [H]. Pouvez-vous nous montrer votre code ?"
    play sound "Click.mp3" noloop

    I "Oui madame. Nous avons utilisé un tri par sélection."
    play sound "Click.mp3" noloop

    M "Très bien. Expliquez-nous le principe."
    play sound "Click.mp3" noloop

    H "On cherche le plus petit élément et on le place au début, puis on recommence avec le reste."
    play sound "Click.mp3" noloop

    M "Parfait. Et quelle est la complexité de cet algorithme ?"
    play sound "Click.mp3" noloop

    I "O(n²) dans tous les cas, madame."
    play sound "Click.mp3" noloop

    P "{=Pensee}Classique, mais pas très optimisé...{/Pensee}"
    play sound "Click.mp3" noloop

    M "Exact. Pouvez-vous nous montrer votre code au tableau ?"
    play sound "Click.mp3" noloop

    I "Bien sûr."
    play sound "Click.mp3" noloop

    "{b}{i}[I] se lève et écrit le code au tableau.{/i}{/b}"
    play sound "Click.mp3" noloop

    H "On a utilisé deux boucles imbriquées. La première parcourt le tableau..."
    play sound "Click.mp3" noloop

    I "Et la deuxième cherche le minimum dans la partie non triée."
    play sound "Click.mp3" noloop

    M "Bien expliqué. Quelqu'un voit des points à améliorer ?"
    play sound "Click.mp3" noloop

    "{b}{i}La classe reste silencieuse quelques instants.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "On pourrait éviter les échanges inutiles si l'élément est déjà à sa place."
    play sound "Click.mp3" noloop

    M "Excellente remarque, [newname]. C'est ce genre d'optimisation qui fait la différence."
    play sound "Click.mp3" noloop

    I "Ah oui, on n'y avait pas pensé."
    play sound "Click.mp3" noloop

    M "Ce n'est pas grave, l'important est d'apprendre. Maintenant, [P] et [newname], montrez-nous votre approche."
    play sound "Click.mp3" noloop

    P "Nous avons implémenté un tri rapide avec partition."
    play sound "Click.mp3" noloop

    S "Évidemment qu'ils ont fait le plus compliqué...."
    play sound "Click.mp3" noloop

    M "Intéressant. Et pourquoi ce choix ?"
    play sound "Click.mp3" noloop

    P "Parce que la complexité moyenne est O(n log n), bien meilleure que O(n²)."
    play sound "Click.mp3" noloop

    M "Excellent raisonnement. Pouvez-vous expliquer le principe à la classe ?"
    play sound "Click.mp3" noloop

    P "Le tri rapide fonctionne par division. On choisit un pivot et on partitionne le tableau."
    play sound "Click.mp3" noloop

    Na "Les éléments plus petits que le pivot vont à gauche, les plus grands à droite."
    play sound "Click.mp3" noloop

    P "Ensuite on applique récursivement le même principe sur chaque partie."
    play sound "Click.mp3" noloop

    M "Très clair. Et vous avez mentionné des optimisations ?"
    play sound "Click.mp3" noloop

    Na "Oui, pour les petits tableaux de moins de 10 éléments, on bascule sur un tri par insertion."
    play sound "Click.mp3" noloop

    M "Pourquoi cette approche ?"
    play sound "Click.mp3" noloop

    P "Parce que le tri par insertion est plus rapide sur de petites données, malgré sa complexité O(n²)."
    play sound "Click.mp3" noloop

    M "Exactement. La théorie de la complexité ne fait pas tout, les constantes comptent aussi."
    play sound "Click.mp3" noloop

    Hi "Et comment vous avez choisi le pivot ?"
    play sound "Click.mp3" noloop

    Na "On prend la médiane de trois valeurs : premier, milieu et dernier élément."
    play sound "Click.mp3" noloop

    M "Technique classique pour éviter le pire cas. Bien pensé."
    play sound "Click.mp3" noloop

    S "Ils ont vraiment pensé à tout ces deux-là..."
    play sound "Click.mp3" noloop

    M "Maintenant, [K], [N] et [S], à vous."
    play sound "Click.mp3" noloop

    S "Nous... on a fait un tri à bulles, madame."
    play sound "Click.mp3" noloop

    "{b}{i}Quelques rires étouffés se font entendre dans la classe.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Du calme ! Le tri à bulles n'est pas ridicule s'il est bien implémenté."
    play sound "Click.mp3" noloop

    K "Avec quelques optimisations quand même !"
    play sound "Click.mp3" noloop

    N "On arrête si le tableau est déjà trié en vérifiant s'il y a eu des échanges."
    play sound "Click.mp3" noloop

    M "C'est une bonne idée d'optimisation. Expliquez-nous."
    play sound "Click.mp3" noloop

    S "Si pendant un passage complet on n'a fait aucun échange, c'est que le tableau est trié."
    play sound "Click.mp3" noloop

    M "Exactement. Et quelle est la complexité dans le meilleur cas avec cette optimisation ?"
    play sound "Click.mp3" noloop

    K "O(n) si le tableau est déjà trié !"
    play sound "Click.mp3" noloop

    M "Très bien. Vous voyez, même un algorithme simple peut être amélioré."
    play sound "Click.mp3" noloop

    P "{=Pensee}Au moins ils ont essayé d'optimiser... Mais ça reste du tri à bulles.{/Pensee}"
    play sound "Click.mp3" noloop

    M "Continuons avec [Hi] et [Y]. Qu'avez-vous fait ?"
    play sound "Click.mp3" noloop

    Hi "Nous avons implémenté un tri par insertion, madame."
    play sound "Click.mp3" noloop

    Y "On a trouvé que c'était un bon compromis entre simplicité et efficacité."
    play sound "Click.mp3" noloop

    M "Intéressant. Développez votre pensée."
    play sound "Click.mp3" noloop

    Hi "Le tri par insertion est simple à comprendre et à coder."
    play sound "Click.mp3" noloop

    Y "Et il est très efficace sur des tableaux presque triés ou de petite taille."
    play sound "Click.mp3" noloop

    M "Excellent point. C'est d'ailleurs pour ça que [P] et [newname] l'utilisent dans leur optimisation."
    play sound "Click.mp3" noloop

    P "C'est vrai, le tri par insertion a son utilité dans certains contextes."
    play sound "Click.mp3" noloop

    Hi "Merci. On a aussi remarqué qu'il est stable, contrairement au tri rapide."
    play sound "Click.mp3" noloop

    M "Quelqu'un peut expliquer ce qu'est la stabilité d'un tri ?"
    play sound "Click.mp3" noloop

    Na "C'est quand deux éléments égaux gardent leur ordre relatif après le tri."
    play sound "Click.mp3" noloop

    M "Parfait. Et pourquoi est-ce important ?"
    play sound "Click.mp3" noloop

    Y "Si on trie des données déjà triées par un autre critère, on ne perd pas cet ordre."
    play sound "Click.mp3" noloop

    M "Exactement. Par exemple, des étudiants triés par classe puis par nom."
    play sound "Click.mp3" noloop

    P "{=Pensee}C'est vrai que je n'avais pas pensé à la stabilité...{/Pensee}"
    play sound "Click.mp3" noloop

    M "Passons maintenant à [J1] et [J2]. Montrez-nous votre travail."
    play sound "Click.mp3" noloop

    J1 "On a fait un tri par fusion, madame."
    play sound "Click.mp3" noloop

    J2 "C'est un peu comme le tri rapide mais en divisant toujours en deux parties égales."
    play sound "Click.mp3" noloop

    M "Bonne description. Quelle est la différence principale ?"
    play sound "Click.mp3" noloop

    J1 "Le tri rapide divise selon un pivot, le tri fusion divise simplement au milieu."
    play sound "Click.mp3" noloop

    J2 "Et la fusion se fait après, en combinant deux sous-tableaux triés."
    play sound "Click.mp3" noloop

    M "Très bien. Et quels sont les avantages ?"
    play sound "Click.mp3" noloop

    J1 "La complexité est toujours O(n log n), même dans le pire cas."
    play sound "Click.mp3" noloop

    J2 "Et c'est un tri stable !"
    play sound "Click.mp3" noloop

    M "Excellent. Y a-t-il des inconvénients ?"
    play sound "Click.mp3" noloop

    P "Il nécessite de la mémoire supplémentaire pour la fusion."
    play sound "Click.mp3" noloop

    M "Exactement, [P]. La complexité spatiale est O(n)."
    play sound "Click.mp3" noloop

    J1 "Oui, on a dû créer des tableaux temporaires."
    play sound "Click.mp3" noloop

    M "C'est le compromis. Performance garantie contre utilisation mémoire."
    play sound "Click.mp3" noloop

    S "Tous ces algorithmes différents... C'est compliqué."
    play sound "Click.mp3" noloop

    M "Bien, nous avons vu plusieurs approches. Quelle est la conclusion ?"
    play sound "Click.mp3" noloop

    P "Il n'y a pas de meilleur algorithme universel."
    play sound "Click.mp3" noloop

    M "Développez."
    play sound "Click.mp3" noloop

    P "Ça dépend du contexte : taille des données, si elles sont presque triées, mémoire disponible..."
    play sound "Click.mp3" noloop

    Na "Et aussi si on a besoin de stabilité ou pas."
    play sound "Click.mp3" noloop

    M "Parfaitement résumé. C'est exactement ce que je voulais que vous compreniez."
    play sound "Click.mp3" noloop

    M "Un bon programmeur connaît plusieurs outils et sait choisir le bon selon la situation."
    play sound "Click.mp3" noloop

    I "Donc notre tri par sélection n'est pas nul finalement ?"
    play sound "Click.mp3" noloop

    M "Absolument pas. Il est simple, ne nécessite pas de mémoire supplémentaire et fait peu d'écritures."
    play sound "Click.mp3" noloop

    H "Peu d'écritures ?"
    play sound "Click.mp3" noloop

    M "Oui, au maximum n échanges. C'est utile quand les écritures sont coûteuses, comme sur certains supports."
    play sound "Click.mp3" noloop

    I "Ah, je comprends mieux !"
    play sound "Click.mp3" noloop

    M "Bien. Pour le prochain cours, je veux que vous réfléchissiez à d'autres algorithmes."
    play sound "Click.mp3" noloop

    M "Faites des recherches sur le tri par tas et le tri par comptage."
    play sound "Click.mp3" noloop

    P "{=Pensee}Le tri par tas, ça va être intéressant...{/Pensee}"
    play sound "Click.mp3" noloop

    S "Madame, on doit les implémenter ?"
    play sound "Click.mp3" noloop

    M "Non, juste comprendre leur principe et leurs cas d'usage. On les codera ensemble la semaine prochaine."
    play sound "Click.mp3" noloop

    K "Ouf, ça nous laisse le temps de comprendre."
    play sound "Click.mp3" noloop

    M "Exactement. La compréhension avant l'implémentation."
    play sound "Bell.mp3" noloop

    "{b}{i}La sonnerie retentit.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien, c'est tout pour aujourd'hui. Bon travail à tous !"
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

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bonne appétit."
    play sound "Click.mp3" noloop

    P "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i} Vous mangez tranquillement puis [K] viens vers vous en mode sérieux.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Oh salut."
    play sound "Click.mp3" noloop

    K "Salut, tu vas bien ?"
    play sound "Click.mp3" noloop

    P "Oui et toi ?"
    play sound "Click.mp3" noloop

    K "Ça va, merci."
    play sound "Click.mp3" noloop

    P "Sinon quoi de neuf ?"
    play sound "Click.mp3" noloop

    K "Je vais te parler de ce qu'il s'est passé hier en fin d'après-midi, après les cours."
    play sound "Click.mp3" noloop

    P "Si tu parles de l'attaque qu'il y a eu hier après les cours, je suis au courant."
    play sound "Click.mp3" noloop 

    K "Bien et il s'est passé quoi de ton coté ?"
    play sound "Click.mp3" noloop 

    if quest40 == 1:

        P "Rien de spécial car [newname] était à jour niveau sécurité."
        play sound "Click.mp3" noloop   

        K "Ah cool alors si rien de spécial ne s'est passé."
        play sound "Click.mp3" noloop

        P "Oui, heureusement d'ailleurs."
        play sound "Click.mp3" noloop 

    else: 

        P "Elle a failli se faire pirater par quelqu'un qui connaissait les privilèges administrateur."
        play sound "Click.mp3" noloop 

        K "Ah bon, il a réussi ?"
        play sound "Click.mp3" noloop

        P "Non, j'ai récupéré les droits derrière son dos avant qu'il n'aille plus loin."
        play sound "Click.mp3" noloop 

        K "Ouf, heureusement que tu étais là pour l'aider."
        play sound "Click.mp3" noloop

    P "Sinon, de ton coté, quoi de neuf ?"
    play sound "Click.mp3" noloop

    K "Eh bien, après les cours, j'ai remarqué quelque chose d'étrange sur le réseau."
    play sound "Click.mp3" noloop

    P "Quoi donc ?"
    play sound "Click.mp3" noloop

    K "Il y avait beaucoup de requétes venant de l'addresse IP {b}{i}201.125.114.115.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Encore cette addresse IP ? C'est celle qui a essayé de pirater [newname] ?"
    play sound "Click.mp3" noloop

    K "Oui, c'est ça."
    play sound "Click.mp3" noloop

    P "C'est vraiment bizarre que cette addresse IP revienne tout le temps."
    play sound "Click.mp3" noloop

    K "Je ne sais pas, mais ça m'inquiète un peu."
    play sound "Click.mp3" noloop

    P "Oui tu as raison de t'inquiéter sur ça."
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

    "{b}{i}Tout le monde s'asseoit à sa place et le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 10.0

    P "[newname] on va en permanence pour réviser ?"
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

    "{b}{i}Vous vous dirigez vers la salle de permanence.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen perm with moveinright

    "{b}{i}Vous vous installez à une place.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon, par quoi on commence ?"
    play sound "Click.mp3" noloop

    P "Par ce qu'on a vu en classe aujourd'hui."
    play sound "Click.mp3" noloop

    Na "Alors oui poourquoi pas"
    play sound "Click.mp3" noloop

    "{b}{i}Puis Les jumelles et [S] entre ici.{/i}{/b}"
    play sound "Click.mp3" noloop

    J2 "Oh c'est vous...salut."
    play sound "Click.mp3" noloop   

    P "Salut..."
    play sound "Click.mp3" noloop

    P "{=Pensee}Je me demande aussi ce qu'ils font ici...{/Pensee}"
    play sound "Click.mp3" noloop

    S "Salut..."
    play sound "Click.mp3" noloop 

    Na "Salut Vous venez réviser aussi ?"
    play sound "Click.mp3" noloop 

    J1 "Oui, on a besoin de réviser pour le prochain contrôle."
    play sound "Click.mp3" noloop

    S "Mouais, je suis là parce que je révise avec elles."
    play sound "Click.mp3" noloop 

    if pronom == "il":

        P "{=Pensee}Ça promet d'être sympa cette séance de révision... mais il faut que je lui demande un truc pour être sûr.{/Pensee}"
        play sound "Click.mp3" noloop 

    else: 

        P "{=Pensee}Ça promet d'être sympa cette séance de révision... mais il faut que je lui demande un truc pour être sûre.{/Pensee}"
        play sound "Click.mp3" noloop 

    menu:  

        "{b}{i}Poser un affront à [S]{/i}{/b}":
            play sound "Menu.mp3" noloop

            $ renpy.block_rollback()

    P "Au fait [S], j'ai une question à te poser !"
    play sound "Click.mp3" noloop

    S "Oui quoi encore ?"
    play sound "Click.mp3" noloop

    P "Tu étais ou hier après les cours !?"
    play sound "Click.mp3" noloop

    Na "Tu ne va pas recommencer avec ça !"
    play sound "Click.mp3" noloop

    P "Mais il faut que je sache ce qu'il faisait."
    play sound "Click.mp3" noloop

    S "De quoi vous parlez ?"
    play sound "Click.mp3" noloop

    P "Je te demande juste où tu étais hier après les cours."
    play sound "Click.mp3" noloop

    S "Pour répondre à ta question, j'étais en permanence en train d'étudier."
    play sound "Click.mp3" noloop

    P "Ah bon et il y a quelqu'un pour confirmer ton affirmation ?"
    play sound "Click.mp3" noloop

    S "Oui il y a les jumelles qui peuvent confirmer."
    play sound "Click.mp3" noloop

    J1 "Oui c'est vrai, [S] était avec nous en permanance."
    play sound "Click.mp3" noloop

    J2 "Oui, on a révisé ensemble après les cours et alors."
    play sound "Click.mp3" noloop

    if quest40 == 1:

        P "Je demande car hier il y a eu une tentative d'intrusion dans le système de [newname] avec une commande administrateur."
        play sound "Click.mp3" noloop

    else:

        P "Je demande car hier il y a eu une attaque informatique contre [newname] avec une commande administrateur."
        play sound "Click.mp3" noloop

    J2 "Hey pourquoi tu nous accuses toute de suite sans preuve ?"
    play sound "Click.mp3" noloop

    P "Je tiens à rappeller que tu as insulté et frappé [newname] sous mes yeux !"
    play sound "Click.mp3" noloop

    J2 "Je t'assure que ce n'est pas nous !!"
    play sound "Click.mp3" noloop

    S "Oui c'est vrai, on n'a rien fait du tout."
    play sound "Click.mp3" noloop

    P "Je vois alors si vous le dites."
    play sound "Click.mp3" noloop

    P "{=Pensee}Pourquoi j'ai l'impression qu'il y a un truc qui cloche ?{/Pensee}"
    play sound "Click.mp3" noloop

    "{b}{i}Puis ils finissent par aller s'installer pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon, on se met au travail maintenant, [prenom]."
    play sound "Click.mp3" noloop

    P "Oui, tu as raison."
    play sound "Click.mp3" noloop

    Na "On a du pain sur la planche."
    play sound "Click.mp3" noloop

    "{b}{i}Vous révisez tranquillement pendant une heure et demi.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Enfin fini de réviser."
    play sound "Click.mp3" noloop

    Na "On peut enfin se détendre un peu."
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen perm with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous quittez la salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

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
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i}Vous posez calmement votre sac à dos sur le bureau.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon..."
    play sound "Click.mp3" noloop

    "{b}{i}[newname] change soudainement de ton.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Il faut qu’on parle de ce qu’il s’est passé en permanence."
    play sound "Click.mp3" noloop

    P "Je m’en doutais..."
    play sound "Click.mp3" noloop

    Na "Pourquoi tu les as accusés de front comme ça !?"
    play sound "Click.mp3" noloop

    P "Je voulais simplement connaître la vérité sur ce qu’il s’était passé."
    play sound "Click.mp3" noloop

    Na "Franchement... quand tu as une idée en tête, tu deviens irrécupérable."
    play sound "Click.mp3" noloop

    P "Peut-être... mais si je ne dis rien, personne ne le fera à ma place."
    play sound "Click.mp3" noloop

    Na "Tu aurais pu leur parler calmement au lieu de les accuser comme ça."
    play sound "Click.mp3" noloop

    P "Peut-être que tu as raison..."
    play sound "Click.mp3" noloop

    Na "Bon, on se pose tranquillement ?"
    play sound "Click.mp3" noloop

    P "Oui, bonne idée."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "ça fait du bien un peu de repos."
    play sound "Click.mp3" noloop

    P "Oui, surtout après cette journée bien chargée."
    play sound "Click.mp3" noloop

    "{b}{i}Vous trainez sur vos téléphones pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Il se fait tard non ?"
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

    "{b}{i}Le lendemain matin, le 8 janvier 2098{/i}{/b}"
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

    "{b}{i}Tu te changes et puis tu aperçois [newname] se lever doucement aussi.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop  

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    P "Cool alors si tu vas bien et pour une fois tu as réussi à te réveiller seule depuis que que j'ai fait le changement."
    play sound "Click.mp3" noloop

    Na "Oui c'est vrai."
    play sound "Click.mp3" noloop

    P "Tu as bien dormi ?"
    play sound "Click.mp3" noloop

    Na "Oui très bien merci et toi ?"
    play sound "Click.mp3" noloop

    P "Moi aussi, j'ai bien dormi."
    play sound "Click.mp3" noloop

    Na "Cool alors, bon moi je vais aller me changer."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] part se changer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "[newname], tu es prête ?"
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

    M "Nous allons approfondire le cour les différents type de tri"
    play sound "Click.mp3" noloop   

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Le cours de tri continue sans problème.{/i}{/b}"
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

    M "Reprenons le cours là où nous l'avions laissé."
    play sound "Click.mp3" noloop

    "{b}{i} Le cours continue tranquillement pour la matinée.{/i}{/b}"
    play sound "Bell.mp3" noloop

    "{b}{i}La sonnerie retentit.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien, c'est tout pour ce matin. Bon travail à tous !"
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

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bonne appétit."
    play sound "Click.mp3" noloop

    P "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous mangez tranquillement pendant quarante-cinq minutes.{/i}{/b}"
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

    "{b}{i}Tout le monde s'asseoit à sa place et le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    $ endlesson = get_random_endlesson()
    M "[endlesson]"
    play sound "Click.mp3" noloop 

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 10.0

    P "[newname] on va en permanence pour réviser ?"
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

    "{b}{i}Vous vous dirigez vers la salle de permanence.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen perm with moveinright

    "{b}{i}Vous vous installez à une place.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on se pose pour réviser."
    play sound "Click.mp3" noloop

    Na "Oui, il faut qu'on révise."
    play sound "Click.mp3" noloop

    "{b}{i}EN même temps, les jumelles et [S] entre aussi pour réviser.{/i}{/b}"
    play sound "Click.mp3" noloop

    if pronom == "il": 

        J1 "Salut les amis."
        play sound "Click.mp3" noloop

    else: 

        J1 "Salut les amies."
        play sound "Click.mp3" noloop

    S "Salut [prenom] et [newname]..."
    play sound "Click.mp3" noloop

    P "Salut..."
    play sound "Click.mp3" noloop

    Na "Salut Vous étes venus réviser ?"
    play sound "Click.mp3" noloop

    J1 "Oui on est à fons sur ça en ce moment."
    play sound "Click.mp3" noloop 

    P "Ah bah oui avec les nouveaux sujets et le Paper Shuffle."
    play sound "Click.mp3" noloop

    Na "Oui c'est clair."
    play sound "Click.mp3" noloop

    J1 "Bon on vous laisse réviser tranquille."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}Ils s'éloignent pour aller réviser de leur côté.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bon, on se met au travail maintenant, [prenom]."
    play sound "Click.mp3" noloop

    P "Oui, tu as raison."
    play sound "Click.mp3" noloop

    "{b}{i}Vous révisez tranquillement pendant une heure et demi.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Enfin fini de réviser."
    play sound "Click.mp3" noloop

    Na "On peut enfin se détendre un peu."
    play sound "Click.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen perm with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous quittez la salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

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
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i}Vous posez calmement votre sac à dos sur le bureau.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Bon, on se pose tranquillement ?"
    play sound "Click.mp3" noloop

    P "Oui, bonne idée."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "ça fait du bien un peu de repos."
    play sound "Click.mp3" noloop

    P "Oui, surtout après cette journée bien chargée."
    play sound "Click.mp3" noloop

    "{b}{i}Vous trainez sur vos téléphones pendant une heure.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Il se fait tard non ?"
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

    P "Enfin fini je vais pouvoir aller dormir."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}le vendredi qui suit, le 10 janvier 2098{/i}{/b}"
    play sound "Alarm.mp3" noloop

    $ day += 2
    $ points -= 1200

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft 

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes et puis tu aperçois [newname] se lever doucement aussi.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop  

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    P "Tu as bien dormi ?"
    play sound "Click.mp3" noloop

    Na "Oui très bien merci et toi ?"
    play sound "Click.mp3" noloop

    P "Moi aussi, j'ai bien dormi."
    play sound "Click.mp3" noloop

    Na "Cool alors, bon moi je vais aller me changer."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] part se changer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "[newname], tu es prête ?"
    play sound "Click.mp3" noloop

    Na "Je suis prête."
    play sound "Click.mp3" noloop

    P "Cool alors."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, on va en cours avant d'être en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Click.mp3" noloop 

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

    $ validation = get_random_validation() 
    Na "[validation]"
    play sound "Click.mp3" noloop

    "{b}{i} Le cours se passe tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    "{b}{i}La sonnerie retentit.{/i}{/b}"
    play sound "Click.mp3" noloop

    M "Bien, c'est tout pour ce matin. Bon travail à tous !"
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

    "{b}{i} Vous asseyez à une table.{/i}{/b}"
    play sound "Click.mp3" noloop 

    Na "Bonne appétit."
    play sound "Click.mp3" noloop

    P "Bonne appétit à toi aussi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous mangez tranquillement pendant quarante-cinq minutes.{/i}{/b}"
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

    "{b}{i}Tout le monde s'asseoit à sa place et le cours continue tranquillement.{/i}{/b}"
    play sound "Bell.mp3" noloop

    M "Bien je ferais un petit test lundi pour conclure ce sujet."
    play sound "Click.mp3" noloop 

    H "C'est noté madame."
    play sound "Click.mp3" noloop

    P "Compris"
    play sound "Click.mp3" noloop 
 
    Na "Compris."
    play sound "Click.mp3" noloop

    "{b}{i}Les élèves commencent à ranger leurs affaires.{/i}{/b}"
    play sound "Click.mp3" noloop

    $ stockage += 10.0 

    P "[newname] on va en permanence pour réviser ?"
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

    "{b}{i}Vous vous dirigez vers la salle de permanence.{/i}{/b}"
    play sound "Footsteps.mp3" noloop

    hide screen hallway with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous entrez en salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene classroom with fade
    show screen day with moveinleft
    show screen points with moveinleft
    show screen perm with moveinright

    "{b}{i}Vous vous installez à une place.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "Bon on se pose pour réviser."
    play sound "Click.mp3" noloop

    Na "Oui, il faut qu'on révise."
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

    "{b}{i}Vous prenez vos sac à dos.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ godorm = get_random_return_dorm()
    P "[godorm]"
    play sound "Click.mp3" noloop

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    hide screen perm with moveoutright
    hide screen points with moveoutleft
    hide screen day with moveoutleft
    scene black with fade

    "{b}{i}Vous quittez la salle de permanence.{/i}{/b}"
    play sound "Door.mp3" noloop

    scene hallway with fade 
    show screen day with moveinleft
    show screen points with moveinleft
    show screen hallway with moveinright

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
    Na "[dortoir]"
    play sound "Click.mp3" noloop

    $ bien = get_random_fais_du_bien()
    P "[bien]" 
    play sound "Click.mp3" noloop  

    "{b}{i}Vous posez calmement votre sac à dos sur le bureau.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "J'aimerais bien qu'on se pose pour lire"
    play sound "Click.mp3" noloop

    P "Bonne idée, j'ai justement un livre avec moi."
    play sound "Click.mp3" noloop

    "{b}{i}Vous vous posez tranquillement pour lire.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "C'est agréable de lire un bon livre."
    play sound "Click.mp3" noloop

    P "Oui, ça change des écrans."
    play sound "Click.mp3" noloop

    "{b}{i}Vous lisez pendant une heure et demi.{/i}{/b}"
    play sound "Click.mp3" noloop

    Na "Il se fait tard non ?"
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

    P "Enfin fini je vais pouvoir aller dormir."
    play sound "Click.mp3" noloop  

    "{b}{i}Tu te changes avant d'aller de te coucher.{/i}{/b}"
    play sound "Click.mp3" noloop

    hide screen day with moveoutleft
    hide screen room with moveoutright
    hide screen points with moveoutleft
    scene black with fade

    "{b}{i}Le lundi, le 13 janvier 2098{/i}{/b}"
    play sound "Alarm.mp3" noloop

    $ day += 3
    $ points -= 1800

    scene room with fade 
    show screen day with moveinleft
    show screen room with moveinright
    show screen points with moveinleft 

    "{b}{i}Tu te réveilles tranquillement.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ line = get_random_morning_line()
    P "[line]"
    play sound "Click.mp3" noloop 

    "{b}{i}Tu te changes et puis tu aperçois [newname] se lever doucement aussi.{/i}{/b}"
    play sound "Click.mp3" noloop 

    $ comment_ca_va = get_random_comment_ca_va()
    P "[comment_ca_va]"
    play sound "Click.mp3" noloop  

    $ je_vais_bien_txt = get_random_je_vais_bien() 
    Na "[je_vais_bien_txt]" 
    play sound "Click.mp3" noloop

    P "Tu as bien dormi ?"
    play sound "Click.mp3" noloop

    Na "Oui très bien merci et toi ?"
    play sound "Click.mp3" noloop

    P "Moi aussi, j'ai bien dormi."
    play sound "Click.mp3" noloop

    Na "Cool alors, bon moi je vais aller me changer."
    play sound "Click.mp3" noloop

    $ validation = get_random_validation() 
    P "[validation]"
    play sound "Click.mp3" noloop 

    "{b}{i}[newname] part se changer.{/i}{/b}"
    play sound "Click.mp3" noloop

    P "[newname], tu es prête ?"
    play sound "Click.mp3" noloop

    Na "Je suis prête."
    play sound "Click.mp3" noloop

    P "Cool alors."
    play sound "Click.mp3" noloop

    "{b}{i}Vous continuez de discuter.{/i}{/b}"
    play sound "Click.mp3" noloop 

    P "Bon, on va en cours avant d'être en retard."
    play sound "Click.mp3" noloop 

    $ suivi = get_random_suivi()
    Na "[suivi]"
    play sound "Footsteps.mp3" noloop

    "{b}{i}Vous prenez d'abord vos sac à dos.{/i}{/b}"
    play sound "Click.mp3" noloop 

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

    label end_script3:
    call script4 from _call_script4    
    return   