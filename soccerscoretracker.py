""" 
Final Project SDEV140 - Intro to Software Development
Ben Vuko
Version 2.1
Due 5/14
Purpose: To Create A Program To Track Score Of A Soccer Game
"""

"""import tkinter for obvious reasons"""
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

#Define as a class
class FootballScoreTracker:\
    #define the initializer
    def __init__(self, root):
        """ 
        Set team names and scores to default values
        Set title of program to Soccer Score Tracker
        Run main window function to start program
        """
        self.root = root
        self.root.title("Soccer Score Tracker")
        
        self.team1_name = ""
        self.team2_name = ""
        self.team1_score = 0
        self.team2_score = 0
        
        self.create_main_window()
    
    def create_main_window(self):
        """ 
        Creates main frame 
        Creates Labels and entry boxes to get team names
        Creats a start game button and an exit button to leave
        """
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=20, pady=20)
        
        #Home Team
        self.team1_label = tk.Label(self.main_frame, text="Home Team Name:")
        self.team1_label.grid(row=0, column=0)
        self.team1_entry = tk.Entry(self.main_frame)
        self.team1_entry.grid(row=0, column=1)
        
        #Away Team
        self.team2_label = tk.Label(self.main_frame, text="Away Team Name:")
        self.team2_label.grid(row=1, column=0)
        self.team2_entry = tk.Entry(self.main_frame)
        self.team2_entry.grid(row=1, column=1)
        
        # Soccer Ball Image
        soccerball_image = Image.open("soccerball.jpg")
        soccerball_image = soccerball_image.resize((100, 100), Image.LANCZOS)
        self.soccerball_img = ImageTk.PhotoImage(soccerball_image)
        self.soccerball_label = tk.Label(self.main_frame, image=self.soccerball_img, text="Soccer Ball Image")
        self.soccerball_label.grid(row=2, columnspan=2, padx=10, pady=10)
        
        # Start Game Button
        self.start_button = tk.Button(self.main_frame, text="Start Game", command=self.start_game)
        self.start_button.grid(row=3, columnspan=2, padx=5, pady=5)
        
        # Exit Button
        self.exit_button = tk.Button(self.main_frame, text="Exit", command=self.root.destroy)
        self.exit_button.grid(row=4, columnspan=2, padx=5, pady=5)
    
    def create_scoring_window(self):
        """ 
        Creates second window of actual game tracker
        Creates Labels with teams scores
        Creates buttons to add goals to each team
        Creates an exit button for this window
        """
        self.scoring_window = tk.Toplevel(self.root)
        self.scoring_window.title("Scoring Window")
        
        # Clock Image
        clock_image = Image.open("clock.jpg")
        clock_image = clock_image.resize((200, 200), Image.LANCZOS)
        self.clock_img = ImageTk.PhotoImage(clock_image)
        self.clock_label = tk.Label(self.scoring_window, image=self.clock_img, text="Clock Image")
        self.clock_label.grid(row=0, columnspan=2, padx=10, pady=10)

        # Team score labels
        self.team1_score_label = tk.Label(self.scoring_window, text=self.team1_name + " Score: 0")
        self.team1_score_label.grid(row=1, column=0, padx=10, pady=10)

        self.team2_score_label = tk.Label(self.scoring_window, text=self.team2_name + " Score: 0")
        self.team2_score_label.grid(row=1, column=1, padx=10, pady=10)

        # Goal buttons
        self.team1_button = tk.Button(self.scoring_window, text="Goal for " + self.team1_name, command=self.add_goal_team1)
        self.team1_button.grid(row=2, column=0, padx=5, pady=5)

        self.team2_button = tk.Button(self.scoring_window, text="Goal for " + self.team2_name, command=self.add_goal_team2)
        self.team2_button.grid(row=2, column=1, padx=5, pady=5)

        # Exit button
        self.exit_button_scoring = tk.Button(self.scoring_window, text="Exit", command=self.root.destroy)
        self.exit_button_scoring.grid(row=3, columnspan=2, padx=5, pady=5)
    
    def validate_input(self, team_name):
        """ 
        Makes sure there is no numbers or spaces in name and pops up an error if there are any
        """
        if team_name.isalpha():
            return True
        else:
            messagebox.showwarning("Error", "Please enter a valid team name.")
            return False
    
    def start_game(self):
        """ 
        Gets input for team names
        Checks if both teams are validated using validate_input function
        If they both pass it opens the scoring window and starts game and closes main window
        """
        team1_name = self.team1_entry.get()
        team2_name = self.team2_entry.get()
    
        if self.validate_input(team1_name) and self.validate_input(team2_name):
            self.team1_name = team1_name
            self.team2_name = team2_name
            self.create_scoring_window()
            self.root.withdraw()


    def add_goal_team1(self):
        """ 
        When ran it adds score to team 1 or home team
        """
        self.team1_score += 1
        self.team1_score_label.config(text=self.team1_name + " Score: " + str(self.team1_score))

    def add_goal_team2(self):
        """ 
        When ran it adds score to team 2 or away team
        """
        self.team2_score += 1
        self.team2_score_label.config(text=self.team2_name + " Score: " + str(self.team2_score))

""" Runs the main window """
root = tk.Tk()
app = FootballScoreTracker(root)
root.mainloop()
