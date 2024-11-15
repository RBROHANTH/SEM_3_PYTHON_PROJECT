import pygame
import sys
pygame.init()

WIDTH, HEIGHT = 1300, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Zoro's Adventure - A One Piece Story")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)

pygame.mixer.init()
pygame.mixer.music.load('mic.mp3')
pygame.mixer.music.play(loops=-1)

title_font = pygame.font.Font(None, 60)  
regular_font = pygame.font.Font(None, 40)  
zoro_font = pygame.font.Font(None, 40)
intro_3bg= pygame.transform.scale( pygame.image.load("zoro12.png").convert_alpha(), (WIDTH, HEIGHT))
intro_0bg= pygame.transform.scale( pygame.image.load("intro_0.png").convert_alpha(), (WIDTH, HEIGHT))
intro_1bg= pygame.transform.scale( pygame.image.load("intro_1.png").convert_alpha(), (WIDTH, HEIGHT))
intro_2bg= pygame.transform.scale( pygame.image.load("intro_2.png").convert_alpha(), (WIDTH, HEIGHT))
accept_luffybg= pygame.transform.scale( pygame.image.load("morgan_defeat.png").convert_alpha(), (WIDTH, HEIGHT))
reject_luffybg= pygame.transform.scale( pygame.image.load("zoro_death.png").convert_alpha(), (WIDTH, HEIGHT))
buggy_teambg= pygame.transform.scale( pygame.image.load("buggy_team.png").convert_alpha(), (WIDTH, HEIGHT))
intro_to_orangetownbg= pygame.transform.scale( pygame.image.load("intro_buggy.png").convert_alpha(), (WIDTH, HEIGHT))
orangetown_0bg= pygame.transform.scale( pygame.image.load("zoro_vs_buggy.png").convert_alpha(), (WIDTH, HEIGHT))
orangetown_1bg= pygame.transform.scale( pygame.image.load("zoro_defeating_cabaji.png").convert_alpha(), (WIDTH, HEIGHT))
orangetown_2bg= pygame.transform.scale( pygame.image.load("nami.png").convert_alpha(), (WIDTH, HEIGHT))
orange_TO_syrupbg= pygame.transform.scale( pygame.image.load("ussop_marry.png").convert_alpha(), (WIDTH, HEIGHT))
syrup_TO_barateebg= pygame.transform.scale( pygame.image.load("mihawk_split.png").convert_alpha(), (WIDTH, HEIGHT))
baratee0bg= pygame.transform.scale( pygame.image.load("mihawk_entrance.png").convert_alpha(), (WIDTH, HEIGHT))
baratee1bg= pygame.transform.scale( pygame.image.load("mihawk_choice.png").convert_alpha(), (WIDTH, HEIGHT))
baratee2bg= pygame.transform.scale( pygame.image.load("mihawk_disrespect.png").convert_alpha(), (WIDTH, HEIGHT))
baratee3bg= pygame.transform.scale( pygame.image.load("mihawk_stopped_zoro.png").convert_alpha(), (WIDTH, HEIGHT))
baratee4bg=  pygame.transform.scale( pygame.image.load("mihawk_chest_stab.png").convert_alpha(), (WIDTH, HEIGHT))
baratee5bg =  pygame.transform.scale( pygame.image.load("mihawk_yoru.png").convert_alpha(), (WIDTH, HEIGHT))
baratee_f1bg =  pygame.transform.scale( pygame.image.load("zoro_cries2.png").convert_alpha(), (WIDTH, HEIGHT))
baratee_f2bg =  pygame.transform.scale( pygame.image.load("mihawk_kills_zoro2.png").convert_alpha(), (WIDTH, HEIGHT))
baratee_f3bg =  pygame.transform.scale( pygame.image.load("mihawk_killing_zoro.jpg").convert_alpha(), (WIDTH, HEIGHT))
baratee6bg =  pygame.transform.scale( pygame.image.load("zoro_win.png").convert_alpha(), (WIDTH, HEIGHT))
def draw_text(text, x, y, font=regular_font):
    rendered_text = font.render(text, True, RED)
    screen.blit(rendered_text, (x, y))

def intro_0():
    screen.blit(intro_3bg, (0, 0))  
    draw_text("Zoro is a swordsman who wants to be the strongest swordsman ", 100, 100, zoro_font)#
    draw_text("in the world", 100, 150, zoro_font)
    draw_text("He was famous throughout the lands as The Pirate Hunter Zoro.", 100, 200, zoro_font)
    draw_text("Press 1 to start Zoro's journey", 100, 400)
    draw_text("Press 2 to exit", 100, 500)
    pygame.display.flip()

def intro_1():
    screen.blit(intro_1bg, (0, 0))
    draw_text("Zoro was held in crucifixion as he challenged Hellmeppo", 100, 450, zoro_font)
    draw_text("the son of marine captain Axe-hand Morgan.", 100, 500, zoro_font)
    draw_text("But Hellmeppo and Axe-hand Morgan wanted to execute Zoro.", 100, 550, zoro_font)
    draw_text("press 1 to next", 100, 600, zoro_font)
    pygame.display.flip()

def intro_2():
    screen.blit(intro_2bg, (0, 0))
    draw_text("Suddenly a boy named Monkey D.Luffy appeared in front of", 100, 400, zoro_font)
    draw_text("Zoro and asked him to join his Pirate crew.", 100, 450, zoro_font)
    draw_text("Luffy is a Devil fruit user which allows him to turn ", 100, 500, zoro_font)
    draw_text("his body into Rubber. Luffy has a dream of becoming the king of the Pirates", 100, 550, zoro_font)
    draw_text("press 1 to next", 100, 600, zoro_font)
    pygame.display.flip()

def intro_3():
    screen.blit(intro_2bg, (0, 0))
    draw_text("press 1 To Accept Luffy's offer and become a Pirate.", 100, 450, zoro_font)
    draw_text("press 2 To Reject Luffy's offer and continue solo.", 100, 500, zoro_font)
    pygame.display.flip()

def accept_luffy():
    screen.blit(accept_luffybg, (0, 0))
    draw_text("As Zoro,now joined Luffy's crew as his first crewmate.", 100, 450, zoro_font)
    draw_text("Luffy and Zoro defeted Axe-hand Morgan using thier", 100, 500, zoro_font)
    draw_text("Rubber powers and sword skills.", 100, 550, zoro_font)
    draw_text("press 1 to next", 100, 600, zoro_font)
    pygame.display.flip()    

def reject_luffy():
    screen.blit(reject_luffybg, (0, 0))
    draw_text("As Zoro,Rejected Luffy's offer.Luffy left Zoro alone.", 100, 450, zoro_font)
    draw_text("Thus Zoro was killed by Axe-hand Morgan.", 100, 500, zoro_font)
    draw_text("press 1 to Restart the game", 100, 550, zoro_font)
    draw_text("press ESC to exit the game", 100, 600, zoro_font)
    pygame.display.flip()

def intro_to_orangetown():
    screen.blit(intro_to_orangetownbg, (0, 0))
    draw_text("As Zoro and Luffy set sail into the sea and reached Orange town.", 100, 400, zoro_font)
    draw_text("Where they had to fight captain Buggy.", 100, 450, zoro_font)
    draw_text("Captain Buggy is also a devil fruit user that makes his body", 100, 500, zoro_font)
    draw_text("immune to sword attacks as he can split his body apart at will.", 100, 550, zoro_font)
    draw_text("press 1 to next", 100, 600, zoro_font)
    pygame.display.flip()     

def orangetown_0():
    screen.blit(orangetown_0bg, (0, 0))
    draw_text("Luffy fights Cabaji (Buggy's swordsman).", 100, 400, zoro_font)
    draw_text("Zoro fights Buggy. Zoro cannot cut Buggy due to his devil fruit powers.", 100, 450, zoro_font)
    draw_text("press 1 To continue fighting.", 100, 550, zoro_font)
    draw_text("press 2 To switch opponents with Luffy", 100, 600, zoro_font)
    pygame.display.flip()

def orangetown_1():
    screen.blit(orangetown_1bg, (0, 0))
    draw_text("Zoro defeated cabaji Captain Buggy's right handman while Luffy defeated Buggy", 100, 500, zoro_font)
    draw_text("press 1 To next", 100, 550, zoro_font)
    pygame.display.flip()     

def orangetown_2():
    screen.blit(buggy_teambg, (0, 0))
    draw_text("As Zoro,Didn't switch opponents with luffy.", 100, 450, zoro_font)
    draw_text("Captain Buggy killed Zoro with his devil fruit powers abilites.", 100, 500, zoro_font)
    draw_text("press 1 to Restart the game", 100, 550, zoro_font)
    draw_text("press ESC to exit the game", 100, 600, zoro_font)
    pygame.display.flip()     

def orangetown_3():
    screen.blit(orangetown_2bg, (0, 0))
    draw_text("A girl named Nami wants to join thier crew as a Navigator.", 100, 450, zoro_font)
    draw_text("press 1 To reject Nami.", 100, 500, zoro_font)
    draw_text("press 2 To Accept Nami.", 100, 550, zoro_font)
    pygame.display.flip() 

def orangetown_4():
    screen.blit(reject_luffybg, (0, 0))
    draw_text("As Luffy and Zoro don't have any navigation skills.", 100, 450, zoro_font)
    draw_text("They got lost in the seas and starved to Death.", 100, 500, zoro_font)
    draw_text("press 1 to Restart the game", 100, 550, zoro_font)
    draw_text("press ESC to exit the game", 100, 600, zoro_font)
    pygame.display.flip()
    

def orange_TO_syrup():
    screen.blit(orange_TO_syrupbg, (0, 0))
    draw_text("Nami, the navigator took the crew to a nearby village.", 100, 450, zoro_font)
    draw_text("And they meet a guy named Usopp,He became their crew member.", 100, 500, zoro_font)
    draw_text("Usopp provided a new ship for the crew.", 100, 550, zoro_font)
    draw_text("press 1 To next", 100, 600, zoro_font)
    pygame.display.flip()

def syrup_TO_baratee():
    screen.blit(syrup_TO_barateebg, (0, 0))
    draw_text("With Usopp the crew went to the foalting restorant Barattee.", 100, 450, zoro_font)
    draw_text("Where they encounted a powerful pirate ship with 100 men on it.", 100, 500, zoro_font)
    draw_text("And the ship was sliced up into two pieces suddenly.", 100, 550, zoro_font)
    draw_text("press 1 To next", 100, 600, zoro_font)
    pygame.display.flip()

def baratee0():
    screen.blit(baratee0bg, (0, 0))
    draw_text("As everyone was shocked about who was able to do that...", 100, 400, zoro_font)
    draw_text("Zoro knew exactly who it is.", 100, 450, zoro_font)
    draw_text("With fear and thrill, Zoro says that is", 100, 500, zoro_font)
    draw_text("the world's greatest swordsman \"Dracule Mihawk\"", 100, 550, zoro_font)
    draw_text("press 1 To next", 100, 600, zoro_font)
    pygame.display.flip()

def baratee1():
    screen.blit(baratee1bg, (0, 0))
    draw_text("press 1 To challenge Mihawk now.", 100, 450, zoro_font)
    draw_text("press 2 To train and fight Mihawk some time later.", 100, 500, zoro_font)
    pygame.display.flip()

def baratee2():
    screen.blit(baratee2bg, (0, 0))
    draw_text("Eventhough, Zoro challenged Mihack , Mihack took out the smallest knife", 100, 500, zoro_font)
    draw_text("He had to fight Zoro's three sorwds As a disrespect to Zoro", 100, 550, zoro_font)
    draw_text("press 1 To next", 100, 600, zoro_font)
    pygame.display.flip()

def baratee_fail1():
    screen.blit(baratee_f1bg, (0, 0))
    draw_text("As Zoro stepped back, instead of fighting Mihawk", 100, 450, zoro_font)
    draw_text("Zoro failed in his promise of being the strongest swordsman in the world", 100, 500, zoro_font)
    draw_text("press 1 to Restart the game", 100, 550, zoro_font)
    draw_text("press ESC to exit the game", 100, 600, zoro_font)
    pygame.display.flip()

def baratee3():
    screen.blit(baratee3bg, (0, 0))
    draw_text("Since Zoro was humiliated by Mihawk's action. He rushed towards Mihawk", 100, 450, zoro_font)
    draw_text("Using his Three Sword Style only to be stopped by the small knife.", 100, 500, zoro_font)
    draw_text("press 1 To escape from Mihawk", 100, 550, zoro_font)
    draw_text("press 2 To continue even after knowing the power gap", 100, 600, zoro_font)
    pygame.display.flip()

def baratee_fail2():
    screen.blit(baratee_f2bg, (0, 0))
    draw_text("As Zoro tried to escape the fight Mihawk killed Zoro instanlly.", 100, 500, zoro_font)
    draw_text("press 1 to Restart the game", 100, 550, zoro_font)
    draw_text("press ESC to exit the game", 100, 600, zoro_font)
    pygame.display.flip()

def baratee4():
    screen.blit(baratee4bg, (0, 0))
    draw_text("As Zoro continued fighting he was sttabed in his chest with the kinfe", 100, 450, zoro_font)
    draw_text("Mihawk gives two choices:", 100, 500, zoro_font)
    draw_text("press 1 To surrender", 100, 550, zoro_font)
    draw_text("press 2 To die ", 100, 600, zoro_font)
    pygame.display.flip()

def baratee_fail3():
    screen.blit(baratee_f3bg, (0, 0))
    draw_text("As Zoro surrendered to Mihawk easily, he felt Zoro was unworthy of being", 100, 450, zoro_font)
    draw_text("the world's greatest swordsman. Thus Mihawk killed Zoro.", 100, 500, zoro_font)
    draw_text("press 1 to Restart the game", 100, 550, zoro_font)
    draw_text("press ESC to exit the game", 100, 600, zoro_font)
    pygame.display.flip()

def baratee5():
    screen.blit(baratee5bg, (0, 0))
    draw_text("Mihawk, impressed by Zoro's will to die instead of giving up on", 100, 450, zoro_font)
    draw_text("his dreams, made Mihawk use his black blade Yoru.", 100, 500, zoro_font)
    draw_text("Zoro won Mihawk's Respect,thus Mihawk accepted Zoro as a Rival", 100, 550, zoro_font)
    draw_text("press 1 to next", 100, 600, zoro_font)
    pygame.display.flip() 

def baratee6():
    screen.blit(baratee6bg, (0, 0))
    pygame.display.flip()   

def handle_input(current_scene):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if current_scene == "intro_0":
                if event.key == pygame.K_1:
                    return "intro_1", None  
                elif event.key == pygame.K_2:
                    pygame.quit()
                    sys.exit()

            elif current_scene == "intro_1":
                if event.key == pygame.K_1:
                    return "intro_2", None
                
            elif current_scene == "intro_2":
                if event.key == pygame.K_1:
                    return "intro_3", None      
                
            elif current_scene == "intro_3":
                if event.key == pygame.K_1:
                    return "accept_luffy", None
                elif event.key == pygame.K_2:
                    return "reject_luffy", None 
                
            elif current_scene == "accept_luffy":
                if event.key == pygame.K_1:
                    return "intro_to_orangetown", None
                
            elif current_scene == "reject_luffy":
                if event.key == pygame.K_1:
                    return "intro_0", None
                
            elif current_scene == "intro_to_orangetown":
                if event.key == pygame.K_1:
                    return "orangetown_0", None
                
            elif current_scene == "orangetown_0":
                if event.key == pygame.K_1:
                    return "orangetown_2", None
                if event.key == pygame.K_2:
                    return "orangetown_1", None
                
            elif current_scene == "orangetown_2":
                if event.key == pygame.K_1:
                    return "intro_0", None
                
            elif current_scene == "orangetown_1":
                if event.key == pygame.K_1:
                    return "orangetown_3", None
                
            elif current_scene == "orangetown_3":
                if event.key == pygame.K_2:
                    return "orange_TO_syrup", None
                if event.key == pygame.K_1:
                    return "orangetown_4", None
                
            elif current_scene == "orangetown_4":
                if event.key == pygame.K_1:
                    return "intro_0", None
                
            elif current_scene == "orange_TO_syrup":
                if event.key == pygame.K_1:
                    return "syrup_TO_baratee", None 
                
            elif current_scene == "syrup_TO_baratee":
                if event.key == pygame.K_1:
                    return "baratee0", None    
                
            elif current_scene == "baratee0":
                if event.key == pygame.K_1:
                    return "baratee1", None  
                
            elif current_scene == "baratee1":
                if event.key == pygame.K_1:
                    return "baratee2", None  
                if event.key == pygame.K_2:
                    return "baratee_fail1", None 
                
            elif current_scene == "baratee2":
                if event.key == pygame.K_1:
                    return "baratee3", None  
                 
            elif current_scene == "baratee_fail1":
                if event.key == pygame.K_1:
                    return "intro_1", None 
                 
            elif current_scene == "baratee3":
                if event.key == pygame.K_2:
                    return "baratee4", None
                if event.key == pygame.K_1:
                    return "baratee_fail2", None
                
            elif current_scene == "baratee_fail2":
                if event.key == pygame.K_1:
                    return "intro_0", None
                
            elif current_scene == "baratee4":
                if event.key == pygame.K_2:
                    return "baratee5", None
                if event.key == pygame.K_1:
                    return "baratee_fail3", None
                
            elif current_scene == "baratee5":
                if event.key == pygame.K_1:
                    return "baratee6", None
            
            elif current_scene == "baratee_fail3":
                if event.key == pygame.K_1:
                    return "intro_0", None
    return current_scene, None 

current_scene = "intro_0"
battle_choice = None
while True:
    if current_scene == "intro_0":
        intro_0()
    elif current_scene == "intro_1":
        intro_1()
    elif current_scene == "intro_2":
        intro_2()
    elif current_scene == "intro_3":
        intro_3()
    elif current_scene == "accept_luffy":
        accept_luffy()
    elif current_scene == "reject_luffy":
        reject_luffy()
    elif current_scene == "intro_to_orangetown":
        intro_to_orangetown()
    elif current_scene == "orangetown_0":
        orangetown_0()
    elif current_scene == "orangetown_1":
        orangetown_1()
    elif current_scene == "orangetown_2":
        orangetown_2()
    elif current_scene == "orangetown_3":
        orangetown_3()
    elif current_scene == "orangetown_4":
        orangetown_4()
    elif current_scene == "orange_TO_syrup":
        orange_TO_syrup()
    elif current_scene == "syrup_TO_baratee":
        syrup_TO_baratee()
    elif current_scene == "baratee0" :
        baratee0()
    elif  current_scene == "baratee1" :
        baratee1()
    elif  current_scene == "baratee2" :
        baratee2()
    elif  current_scene == "baratee_fail1" :
        baratee_fail1()
    elif  current_scene == "baratee3" :
        baratee3()
    elif  current_scene == "baratee_fail2" :
        baratee_fail2()
    elif  current_scene == "baratee4" :
        baratee4()
    elif  current_scene == "baratee_fail3" :
        baratee_fail3()
    elif  current_scene == "baratee5" :
        baratee5()
    elif  current_scene == "baratee6" :
        baratee6()
    current_scene, battle_choice = handle_input(current_scene)
    pygame.display.update()