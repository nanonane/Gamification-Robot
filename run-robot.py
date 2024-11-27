# run the Gamificaiton Robot with: python run-robot.py
# Author: Yinuo Zhu

import os
from Robot import Robot
from time import sleep


def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_init() -> None:
    clear_screen()
    print("""
  ________                  .__   _____ .__                   __   .__                 
 /  _____/ _____     _____  |__|_/ ____\|__|  ____  _____   _/  |_ |__|  ____    ____  
/   \  ___ \__  \   /     \ |  |\   __\ |  |_/ ___\ \__  \  \   __\|  | /  _ \  /    \ 
\    \_\  \ / __ \_|  Y Y  \|  | |  |   |  |\  \___  / __ \_ |  |  |  |(  <_> )|   |  \\
 \______  /(____  /|__|_|  /|__| |__|   |__| \___  >(____  / |__|  |__| \____/ |___|  /
        \/      \/       \/                      \/      \/                         \/ 
                
                        __________         ___.              __                                                
                        \______   \  ____  \_ |__    ____  _/  |_                                              
                         |       _/ /  _ \  | __ \  /  _ \ \   __\                                             
                         |    |   \(  <_> ) | \_\ \(  <_> ) |  |                                               
                         |____|_  / \____/  |___  / \____/  |__|                                               
                                \/              \/                                                             


                                Press Enter to continue...

""")
    input()


def draw_robot(game_robot: Robot) -> None:
    clear_screen()
    game_robot.draw()
    # if game_robot.is_whole():
    #     sleep(1)
    #     clear_screen()
    #     game_robot.draw_whole()


def main():
    draw_init()

    game_robot = Robot()
    draw_robot(game_robot)

    while True:
        command = input("> ").strip().lower()
        if command == 'q':
            break
        if command == 'help':
            print("Hello! This is a Gamification Robot!")
            print(
                "Use 'head', 'left_arm', 'right_arm', 'left_leg', 'right_leg', 'left_chest', 'right_chest' to check out each part.")
            print("Use 'q' to quit.")
        elif game_robot.is_part(command):
            clear_screen()
            game_robot.check_part(command)
            input()
            draw_robot(game_robot)
        else:
            print("Invalid command. Type 'help' for more information.")


if __name__ == "__main__":
    main()
