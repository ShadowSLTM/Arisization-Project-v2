## Clavier virtuel pour manette - À placer dans controller.rpy

init python:
    import pygame
    
    def is_gamepad_connected():
        """Vérifie si une manette est connectée"""
        try:
            pygame.joystick.init()
            return pygame.joystick.get_count() > 0
        except:
            return False
    
    class GamepadKeyboard:
        """Clavier virtuel navigable à la manette"""
        
        def __init__(self):
            # Disposition du clavier AZERTY avec caractères spéciaux
            self.layouts = {
                'minuscules': [
                    ['a', 'z', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                    ['q', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm'],
                    ['w', 'x', 'c', 'v', 'b', 'n', ',', '.', ';', ':'],
                    ['123', 'MAJ', 'ESPACE', 'SUPPR', 'OK']
                ],
                'majuscules': [
                    ['A', 'Z', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                    ['Q', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M'],
                    ['W', 'X', 'C', 'V', 'B', 'N', '!', '?', ';', ':'],
                    ['123', 'min', 'ESPACE', 'SUPPR', 'OK']
                ],
                'chiffres': [
                    ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                    ['(', ')', '_', '=', 'ABC', 'ESPACE', 'SUPPR', 'OK']
                ]
            }
            
            self.current_layout = 'minuscules'
            self.cursor_x = 0
            self.cursor_y = 0
            self.text = ""
            self.max_length = 100
            self.last_action_time = 0
            self.action_delay = 0.15
            self.prompt = ""
            
        def get_current_layout(self):
            return self.layouts[self.current_layout]
        
        def move_cursor(self, dx, dy):
            """Déplace le curseur sur le clavier"""
            import time
            current_time = time.time()
            
            if current_time - self.last_action_time < self.action_delay:
                return
            
            self.last_action_time = current_time
            layout = self.get_current_layout()
            self.cursor_y = (self.cursor_y + dy) % len(layout)
            self.cursor_x = (self.cursor_x + dx) % len(layout[self.cursor_y])
        
        def get_current_key(self):
            """Retourne la touche actuellement sélectionnée"""
            layout = self.get_current_layout()
            return layout[self.cursor_y][self.cursor_x]
        
        def press_key(self):
            """Appuie sur la touche sélectionnée"""
            import time
            current_time = time.time()
            
            if current_time - self.last_action_time < self.action_delay:
                return 'CONTINUE'
            
            self.last_action_time = current_time
            key = self.get_current_key()
            
            if key == 'OK':
                return 'DONE'
            elif key == 'ESPACE':
                if len(self.text) < self.max_length:
                    self.text += ' '
            elif key == 'SUPPR':
                if self.text:
                    self.text = self.text[:-1]
            elif key == 'MAJ':
                self.current_layout = 'majuscules'
                self.cursor_x = 0
                self.cursor_y = 0
            elif key == 'min':
                self.current_layout = 'minuscules'
                self.cursor_x = 0
                self.cursor_y = 0
            elif key == 'ABC':
                self.current_layout = 'minuscules'
                self.cursor_x = 0
                self.cursor_y = 0
            elif key == '123':
                self.current_layout = 'chiffres'
                self.cursor_x = 0
                self.cursor_y = 0
            else:
                if len(self.text) < self.max_length:
                    self.text += key
            
            return 'CONTINUE'
        
        def reset(self, prompt="", default="", max_length=100):
            """Réinitialise le clavier"""
            import time
            self.text = default
            self.max_length = max_length
            self.cursor_x = 0
            self.cursor_y = 0
            self.current_layout = 'minuscules'
            self.last_action_time = time.time()
            self.prompt = prompt

default gamepad_kb = GamepadKeyboard()

init python:
    def get_gamepad_input(prompt="Entrez votre texte:", default="", max_length=100):
        """Affiche le clavier virtuel et retourne le texte saisi"""
        if not is_gamepad_connected():
            return get_gamepad_input(prompt, default=default, length=max_length)
        
        gamepad_kb.reset(prompt, default, max_length)
        gamepad_kb.prompt = prompt
        
        while True:
            result = renpy.call_screen("gamepad_keyboard", 
                                      max_length=max_length)
            
            if result == 'DONE':
                return gamepad_kb.text
            elif result == 'CANCEL':
                return None

screen gamepad_keyboard(max_length=100):
    
    modal True
    
    key "pad_leftshoulder_press" action Function(gamepad_kb.move_cursor, -1, 0)
    key "pad_rightshoulder_press" action Function(gamepad_kb.move_cursor, 1, 0)
    key "pad_dpleft_press" action Function(gamepad_kb.move_cursor, -1, 0)
    key "pad_dpright_press" action Function(gamepad_kb.move_cursor, 1, 0)
    key "pad_dpup_press" action Function(gamepad_kb.move_cursor, 0, -1)
    key "pad_dpdown_press" action Function(gamepad_kb.move_cursor, 0, 1)
    key "pad_leftx_pos" action Function(gamepad_kb.move_cursor, 1, 0)
    key "pad_leftx_neg" action Function(gamepad_kb.move_cursor, -1, 0)
    key "pad_lefty_pos" action Function(gamepad_kb.move_cursor, 0, 1)
    key "pad_lefty_neg" action Function(gamepad_kb.move_cursor, 0, -1)
    key "pad_a_press" action Return(gamepad_kb.press_key())
    key "pad_b_press" action Return(gamepad_kb.press_key())
    key "pad_back_press" action Return('CANCEL')
    key "pad_y_press" action Return('CANCEL')
    
    frame:
        xalign 0.5
        yalign 0.5
        xsize 1200
        ysize 800
        
        vbox:
            spacing 20
            xalign 0.5
            
            text "[gamepad_kb.prompt!q]" size 30 xalign 0.5
            
            frame:
                xsize 1100
                ysize 80
                xalign 0.5
                background "#333"
                
                text "[gamepad_kb.text!q]_" size 28 xalign 0.5 yalign 0.5
            
            text "[gamepad_kb.text!q] / [max_length]" size 20 xalign 0.5
            
            vbox:
                spacing 10
                xalign 0.5
                
                python:
                    current_layout = gamepad_kb.get_current_layout()
                
                for row_idx in range(len(current_layout)):
                    hbox:
                        spacing 10
                        xalign 0.5
                        
                        python:
                            current_row = current_layout[row_idx]
                        
                        for col_idx in range(len(current_row)):
                            python:
                                key = current_row[col_idx]
                                is_selected = (gamepad_kb.cursor_x == col_idx and gamepad_kb.cursor_y == row_idx)
                                key_width = 200 if key in ['ESPACE', 'SUPPR', 'MAJ', 'min', 'ABC', '123', 'OK'] else 80
                                key_bg = "#4CAF50" if is_selected else "#666"
                                key_size = 20 if len(key) > 2 else (24 if len(key) > 1 else 32)
                            
                            button:
                                xsize key_width
                                ysize 80
                                background key_bg
                                
                                text key:
                                    size key_size
                                    xalign 0.5
                                    yalign 0.5
                                    color "#FFF"
                                    substitute False
                                
                                action Return(gamepad_kb.press_key())
            
            text "Manette: D-Pad/Stick = naviguer | A/Croix = valider | Back = annuler" size 18 xalign 0.5

label exemple_utilisation:
    
    if is_gamepad_connected():
        "Manette détectée !"
    else:
        "Clavier/Souris détecté."
    
    $ code_saisi = get_gamepad_input("Entrez le code:", "", 10)
    
    if code_saisi is None:
        "Saisie annulée."
    elif code_saisi == "1234":
        "Code correct !"
    else:
        "Code incorrect: [code_saisi]"
    
    return

screen gamepad_status():
    frame:
        xalign 0.98
        yalign 0.02
        background "#000000AA"
        padding (10, 10)
        
        python:
            manette_connectee = is_gamepad_connected()
        
        if manette_connectee:
            text "🎮 Manette" size 18 color "#4CAF50"
        else:
            text "⌨️ Clavier" size 18 color "#FFA500"