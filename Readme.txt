1.-First day of the 100day challenge:
	-Create and configure the GIT repository.
	-Download all the content and PDFs.
	-Create a PDF creator/modificator.
	-Create the band name generator.
	-Downloaded the IDE "Thonny" -> It is very useful for beginners.
	-Set everything up for day 2 (which will actually be still in day 1 since I want to move forward).
2.-Second day of the 100day challenge:
	Warm up:
		-2 digit addition.
		-BMI Calculator.
		-Age calculator (This is the simplest version: when you JUST turned that age, not even one day after).
	Day 2 code:
		-Tip calculator.
3.-Third day of the 100day challenge:
	Warm up:
		-Even or Odd calculator.
		-Leap year calculator.
		-Rollercoaster ride calculator.
		-Pizza delivery program.
		-Love calculator.
	Day 3 code:
		-Choose your own story.
4.-Fourth day of the 100day challenge:
	Warm up:
		-Random number generator.
		-Coin Toss.
		-Treasure map.
	Day 4 code:
		-Rock, paper, scissors.
5.-Fifth day of the 100day challenge:
	Warm up:
		-Student heights average.
		-Highest exam score.
		-Addition of all the even numbers in a range of numbers.
		-FizzBuzz game.
	Day 5 code:
		-Password generator.
6.-Sixth day of the 100day challenge:
	Warm up:
		-Hurdle 1 (Reeborg's World).
		-Hurdle 2 (Reeborg's World).
		-Hurdle 3 (Reeborg's World).
		-Hurdle 4 (Reeborg's World).
	Day 6 code:
		-Maze runner (Reeborg's World).
7.-Seventh day of the 100day challenge:
	Day 7 code:
		-Hangman (My way)
		-Hangman (Professor's way)
8.-Eigth day of the 100day challenge:
	Warm up:
		-Functions with arguments, and keyword arguments.
	Day 8 code:
		-Caesar Cipher (1).
		-Caesar Cipher (2).
		-Caesar Cipher (3).
9.-Nineth day of the 100day challenge:
	Warm up:
		-How to use dictionaries.
		-How to use one of the dictionary methods, plus dictionary unpacking.
		-Nesting lists and dictionaries.
		-Function that add new countries to the old list of dictionaries.
	Day 9 code:
		-Blind auction: It asks the user for their name, their bid, and if there
		 is another user. If there is, then the entire process starts again.
		 After every iteration, the code updates a dictionary with "names" and "bid"
		 prices values.
	 -A little over complicated at the end, but it does the job correctly: outputs
	  the auctions winner. (wins the highest price).
	 -Teachers way of solving it: Even though the 2 versions of code are mostly
    different, in core logic, none of them are wrong or incorrect. They just
		tackle the problem differently. Maybe you want the keys and the values as
		lists, to later refferencing and indexing a list; choice 1. Or maybe you
		just needed a key value pair, where the keys are all the names and the
		values are all the bid prices; choice 2. Either is correct, it just depends
		on what you need afterwards. At the end, both versions output the same
		correct answer.
10.-Tenth day of the 100day challenge:
	Warm up:
		-How to write a function that returns a value (I already did that in many
		 of my previous codes, but this is officially the first one).
		-This is how you have multiple returns inside a function.
		-This is the same 'leap year' program I coded earlier, but now it has multiple
		 functions with multiple return statements.
		 -How to make DocStrings.
	Day 10 code:
		-I am trying to get used to log every new working change in the code. So,
		 right now the only thing that is coded are the functions and all the tests
		 for debugging purposes.
		-Problem solved: Now it does not ask for the input operator twice (I forgot
		 to add it to the read me). The code loops twice the code with a 'for loop'
		 and works as intended: Asks the user for 2 numbers, what operation to use
		 and outputs the results. Then asks if the user wants to use the old result
		 for a new operation and starts the loop again.
		 Now I realize I should have also added how the code worked without a loop,
		 for referencing. Good to know for next time.
		-Works better with a while loop.
		-If the user inputs the wrong special character, then the calculator closes.
		-Final code (My way).
		-I forgot to add the 'clear()' function.
		-The professor gave us a way to calling functions inside dictionaries. I
		 had never seen that before, and it is EXTREMELY clever.
		-This is incredible... The calculator function now has a 'switch' inside
		 that decides what operation to use. AND it is faster than if statements
		 because it is a hash table.... Amazing...
		-This is the professor's way of solving the challenge. (if the user types
		 'n' then the entire program closes).
		-New concept: Recursion.
		-I just added an escape flag in order to exit the recursion. Otherwise, you
		 would either have to close the IDE or the program in order to finish it.
11.-Eleventh day of the 100day challenge:
	First Capstone Project:
		-BlackJack Game:
			-All the cards are created, the art module is added, and the different
			 directories are in place. Everything is ready to go.
			-The art module is taking more than I expected to complete. I forgot there
			 are 53 cards, therefore 53 artworks.. I will finish it later. I am going
			 to focus on the program first, then in the GUI.
			-Now I am forgetting to update the read my file... But in summary, The
			 'Deck()', 'Ace()', 'Jack()', 'King()' and 'Queen()' classes are created,
			 debugged and ready to go. The class 'Deck()' creates one card of each
			 suit, for a total of 52 cards. Which are instances of their own
			 different classes.
			-Right now the game works as expected: The computer deals 2 cards to the
			 player, and one card to itself. Prints the suits and values of all the
			 cards, plus their addition.
			-It deals two rounds. If the user wants a card, then he/she gets one, and
			 and the computer also gets one. Then the total for both is printed. (Now
			 for loops are implemented to print the cards and the totals, since they
			 are stored in new 'list' variables).
			-Everything works as intended, and I am proud it is not crashing or ouputing
			 anything wrong in any way. But I still have to work on the code; it works
			 but it is EXTREMELY badly written. I will implement while and for loops
			 next.
			-Better written code: 'while' and 'for' loops implemented. I will see if I
			 can clean the code a little more before going to the GUI part of the game.
			-I forgot to check: If the player's or the computer's hand is 12+,
			 decide to draw a card, and get an 'Ace', then its value would be '1'
			 instead of '10'.
			-Artwork for all the 10s.
			-Artwork for all the 9s.
			-Artwork for all the 8s.
			-Artwork for all the 7s.
			-Artwork for all the 6s.
			-Artwork for all the 5s.
			-Artwork for all the 4s.
			-Artwork for all the 3s.
			-Artwork for all the 2s.
			-'numbers' module debugged and ready to use.
			-Game fully developed. It can be ran in IDEs or Consoles; just change the
			 paths at the beginning of each module. I know there might be a way to
			 avoid this, but that is for future improvements.
			-A little house keeping: King and Queen of Diamonds did not have the correct
			 artwork. Plus, the 'clear()' function is implemented for console games.
			 (Clear does not work with Hydrogen - Atom IDE).
			-Final touch: The dealer (computer) has an upside down card at the beginning
			 of the first round. That is how BlackJack is played, and I forgot to add
			 that upside down card. (It is simply aesthetics for now. Just for GUI; the
			 code still is the same. That blank card does not add or substracts anything
			 more than graphics).
			-Clean up for the first calculations: It is impossible to have more than 20
			 in the first hand, then get an 'Ace' and not being BlackJack. So the code
			 is simpler there. PLUS I added the main rule for BlackJack (I did not
			 know it existed): if you get a 10 value card, plus an "Ace", in any order,
			 then you have a BlackJack. Neat rule.
			-If you get BlackJack, and you decide to stop playing. You automatically
			 win, and the computer does not flip its upside down card.
			-Recursion implemented: Now the game can restart if the player decides to.
			-DocStrings for the different functions.
			-The computer can now have a BlackJack also. And there was a weird debug
			 where if you typed "(N)o" to end the game after a few rounds of playing,
			 the game would not stop (until you went through as many games as answers
			 "(N)o" you gave. It is a recursive problem, where you don't end a game,
			 and start another one.. I feel like I am in Inception)
			-Professor's way of solving the BlackJack way.
			-I believe these are the last changes: I added >> if __name__ == '__main__': <<
			 This is very useful when creating a bunch of games in an arcade, for example.
			 If you are running 'blackjack.py' as a stand alone program. it will run
			 the 'play()' function. If it was imported, then it would not run the play
			 method. I also added the '__init__.py' to the main directory and the
			 sub-directories so Python can know to treat everything as a package.
			-I left out the magic/dunder methods, which I should not. So I went back
			 and added them, while doing a little housekeeping in the imports: It is
			 not about running the code in an IDE or Console... But about where you
			 run the code. If you open the Day_11 directory as a project, then everything
			 will run smoothly.
12.-Twelfth day of the 100day challenge:

	Warm Up:
		-I got carried away and forgot to log the changes in readme. But the warm ups
		 are codes that give examples about what variable scope is and how to correctly
		 use it.
  Guessing game:
		-All the functions are ready to be used and debugged. And a little bit of the
		 logic is laid out.
		-All the logic for the generation and storage of the random number is ready.
		 The code checks if the answer from the user is equal to the random generated
		 number, and outputs if the number from the user is 'correct', 'too high' or
		 'too low' and substracts 1 remaining attempt from the total.
		-Use the remaining attempts to keep looping until there are no attempts left
		 or the user gets the correct number. If the user keeps giving the wrong
		 answer and runs out of attempts, then it is game over. I also changed the
		 structure of the if statement. It is easier to read.
		-Recursion: If the player wants to play again, they can. Plus, the clear
		 function is added.
		-DocStrings.
		-The game might be a little more readable. I added a function for keeping
		 track of the attempts lost.
		-The professor's way is very interesting. It is highly suggested you take
		 a look at it since she is writing it better. From watching her, I realized
		 most of the times you have an 'if statement', it is good to enclose it in
		 a function. Also, you can use the 'return' in your advantage. See line 48
		 in the professor's file.
13.-Thirteenth day of the 100day challenge:
	Warm up + Debugging:
		-I got carried away debugging that I forgot to add every step to the log...
		 Well, I caught myself in the first debugging of the actual coding challenge:
		 Where you should not assign the value "0", but compare it instead > "==".
		-You should be turning the answer into an "int". Right now it is a "str".
		- 1.-The final print is printing a number inside a list.
		  2.-You should be using 'elif' to make one big condition, and not a bunch of small ones.
		  3.-You should use "and" instead of "or".
14.-Fourteenth day of the 100day challenge:
	-Higher or lower game:
		-All the modules are imported and ready to use.
		-Game with only one iteration debugged and ready to go.
		-First function "score()": This function takes 4 arguments: The first and
		 second random choice the computer makes, the answer from the user, and the
		 current score to calculate if the user was right or wrong. Then updates
		 the score accordingly.
		-I ended up using a way simpler function "right_choice()" -> This function
		 takes 2 arguments: the first and the second choice, and returns which one
		 has bigger follower counts, or in other words, the correct answer.
		-Recursion: The player can now play again if he/she wants to. The only thing
		 left is to clear the screen, and add the artwork.
		-The function to clear the screen is added, and the artwork is also added.
		-Works exactly as the professor, but it is very messy.
		-Cleaner version: much better way of organizing the functions.
		-I did not realize there was a rule that stated "the winner of the 2
		 will go to the next round, and be compared to someone/something else." Now
		 it takes that rule into consideration. It is a small (but clever) change.
		 turning the output from "right_choice()" into a tuple of 2 outputs instead
		 of only 1.
		-The professor gave me an idea to solve one of the issues I saw happening:
		 Every now and then, the random generation of names would generate exactly
		 the same name twice, therefore, making the user lose due to both answers
		 being equal. (neither will be higher than the opponent).
		-It never occurred to me to format the data for printing. Thanks to the
		 professor I can start doing it.
		-Professor's way of solving the challenge.
15.-Fifteenth day of the 100day challenge:
	-Cofee machine:
		-Some of the logic is layed out: The machine asks the user what they want to do,
		 (M)ake coffee, or print the (R)eport. Depending the answer, it outputs a report
		 of the ingredients, or prompts the user to choose what type of coffee they want.
		 There is a hidden answer "off" that turns off the machine. If the user inserts
		 more money than needed, then the machine gives them change and the coffee.
		 If they insert less than the total cost, then tells the user that it is not
		 enough, and returns the money. If they insert the exact amount, then the
		 machine dispenses the coffee.
		-I created, tested and debugged all the functions: calculations(), ingredients(),
		 espresso(), latte(), cappuccino(). I also added 'money' to the resources
		 dictionary, so the output of all the coffee functions would be added to
		 the total money as 'profit'.
		-Better organized: 'brew_profit()' function has been added to get the profit
		 from brewing the coffee, so it would be easier to added to the resources
		 dictionary
		-The ingredients used are now substracted from the initial total.
		-The machine now checks if the user inserted enough money for a certain coffee.
		 if they did, then checks if there are enough ingredients to make that coffee,
		 and if there is not, then it outputs what is running out: water, milk, etc.
		 I also did a little house cleaning: 'ingredients()' now prints things with
		 less white spaces in between words.
		-A way out of the infinite loop if the machine runs out of ingredients.
		-Final function 'play()' for repeatability and to finish off the program.
		 The rest is just housekeeping and DocStrings.
		-While adding the DocStrings, I realized that the functions for making the
		 different coffees were also checking if enough water was in the reservoir.
		 This is not needed because it is already taken care of by 'brew()'. So, those
		 lines were removed.
		-I also forgot to round the numbers to the nearest 2 decimal places before
		 returning the change to the user. The printing in the UI is also better formatted.
		-Artwork added.
		-The option should be 'off' not 'o'.
		-Adding the units to the quantities.
		-Professor's solution to the challenge.
16.-Sixteenth day of the 100day challenge:

	-Warm up:
		-How to use OOP and PrettyTable as an example.
	-Coffee machine OOP:
		-Extraction of all the files.
		-Getting my old template of the coffee machine.
		-Everything ready and debugged. I know I should not have done it all in one swoop,
		 but I felt if I stopped to record something, I would lose my train of thought.
		 If I got stuck somewhere, then I would have recorded it. I also did minor modifications
		 to the Day_15 'coffee_machine.py' mainly in the last print statements, so they look
		 nicer on screen, and also ending the entire program when typing "off" or a wrong
		 answer. (Before it would ask 'Hello! type (A)gain to go to main menu, or (E)xit:', then
		 do something).
		-Last DocString.
		-There was a tinny bug I did not see at first. previous logic: If the user does not have enough
		 money to brew the coffee, it returns the money AND brews the coffee. Now, if the user does not
		 insert enough money, then the machine does not brew the coffee.
		-Her way is much more condensed, and it matches her previous way of tackling the challenge.
17.-Seventeenth day of the 100day challenge:
	-Warm up:
		-Creating a class, and adding its first attributes.
		-Adding the first method.
	-Questionnaire game:
		-First class and its attributes.
		-Changes made to 'data.py'
		-Question bank created. And '__init__.py' created.
		-'next_question()' is created.
		-'next_question()' is implement in 'main.py'.
		-'still_has_questions()' is created and implemented in 'main.py'.
		-'check_answer()' is created and implemented in 'main.py'.
		 Final version of the code is finished; It checks and outputs how many
		 correct answers the user had out of the total.
18.-Eighteenth day of the 100day challenge:

	-Warm up:
		-Tim the turtle drawing a square.
		-Tim the turtle drawing a dotted line.
		-Draw 7 shapes.
		-Change colors.
		-Random walk.
		-Spirograph.
		-Spirograph 2.0.
	-Hirst Painting:
		-Ready.
		-Colorgram module imported, and 40 colors extracted from the picture.
		-Timmy draws 10 circles at the bottom of the screen.
		-Draws 10 circles with different colors from the list of 40 colors extracted.
		-It draws a 10x10 matrix of circles, with different color each. Every circle
		 is 20units is diameter and with a distance of 50units of each other. I still
		 have to clean up the code, but it works.
		-Much cleaner code: Everything is now in functions and the computer asks
		 how many dots the user wants on the canvas.
		-DocString.
		-Two of the extremely light colors were removed.
		-For running it on cmd.
		-Faster to run, and it only shows the dots.
		-Professor's way.
19.-Nineteenth day of the 100day challenge:

	-Etch a sketch.
	-Turtle race: All the turtles are racing, but they always end up in the same
	 places. I think it is because I should model the game in terms of real physics;
	 speed = distance/time. Right now I only change how fast the game renders/updates
	 each turtle.
	-All the turtles have different speed. The only thing is that when 2 turtles are
	 within a few paces of the finish line, and 2 or any combination of turtles, crosses
	 the line, then all of them win (even though it clearly states who crosses first).
	-Apparently this will solve it. (I am not completely convinced, but I do not want
	 to run more iterations of the game)
20.-Twentieth day of the 100day challenge:
	-Snake game:
		-Starting 3 segments in the snake game.
		-All the segments move as one, and they turn where the head turns.
		-Start of the OOP process.
		-Cleaner and slightly better written code.
		-To do list.
		-Up, Left, Down, and Right turns implemented.
		-Failsafe in case you are facing one way, and want to go the exact opposite way.
		 (You should not be able to do it. Otherwise, you would be going over yourself).
		-Better way of accessing the head of the snake in the 'snake.py' module.
		-Also, better way of accessing the directions; as constants.
21.-Twenty first day of the 100day challenge:
	-Warm up:
		-Inheritance.
	-Snake game (continuation):
		-The food for the snake is randomly generated on the screen. The food has its
		 own module and belongs to a class.
		-Every time the snake hits the food, it automatically changes location.
		-Have a scoreboard that updates every time the user eats a dot.
		-The game stops if the snake collides with any wall.
		-If the user hits a wall, then the game stops, and the text "GAME OVER"
		 appears in the middle.
		-If the snake eats a dot, then it gets bigger by 1 link/turtle.
		-If the snake eats itself, then it is game over.
		-Faster gameplay, and better written 'for loop' when eating itself.
22.-Twenty second day of the 100day challenge:
	-Pong game:
		-Everything ready to go.
		-A ball is created and placed in the middle of the screen.
		-The ball bounces off the walls in the correct directions.
		-There is a method that holds the direction of bouncing. And there is also a
		 small bug: since the ball moves at a certain speed, then checks if it inside
		 certain boundaries (walls), then it behaves like a ghost. It can go through
		 a wall, realizes it went through it and change direction as if bouncing. So
		 if the ball went BEYOND what it could cover in the next step, it sees itself
		 still trapped in the wall, therefore changing direction again. It seems
		 as if it changed directions twice in a row, "mid-air" without touching a wall.
		-This should solve the problem for now: every time the ball hits a wall, it
		 takes a tiny step, then begins the process of checking once more.
		-The ball is correctly instantiated and accessed in the 'Ball()'. And the
		 module for the dotted line in the middle of the screen is added.
		-Scoreboard module implemented: 2 scoreboards are printed on the screen.
		-Paddle modules implemented: 2 paddles are added to the screen, and positioned
		 on either side of the board. (This module is an adaptation of the 'snake'
		 module. Therefore, it still needs modifications). I also changed the 'scoreboard'
		 module so it would be better written. And the 'middle_line' module was modified
		 so the shape and color of the turtles remained constants.
		-Updated 'To Do' list.
		-Paddles move up or down: the paddle methods for going up and down are now
		 correctly implemented, and the 'move()' method from the 'snake' module has
		 been adapted. Now there are 2 methods; one for moving up and the other
		 for moving down. The 'up()' and 'down()' methods have been adapted for the
		 paddle class too.
		-DocStrings for the paddle class.
		-Movement for the second player is added.
		-Small logic for GAME OVER is added.
		-The ball now bounces off the 2 player's paddles.
		-Updated 'To Do' list.
		-The scores are now being kept.
		-The paddles and the ball are now reset once a player loses a game.
		-Fully functional game. I just have to do some housekeeping.
		-Pong module separated into functions.
		-The users have a little bit more time between game resets, and they can also
		 choose how many games to play (currently 'lives' has to be changed in the code).
		-Now the game asks the user how many games the player wants to play. It also
		 checks if the players are in a tie, if they are, then they can play one last
		 round: SUDDEN DEATH. I also separated the functions to make it easier to
		 navigate.
		-The rest of the DocStrings.
		-Some comments for better readability.
		-The paddles may run faster if instead of 8 turtle objects for the body, you
		 make only one object, and stretch it vertically. It also makes the logic
		 MUCH more simpler.
23.-Twenty third day of the 100day challenge:
	-Cross the road:
		-Starting files and To Do list.
		-A blue turtle is created, placed at the bottom of the screen, and can move
		 up or down with the 'w' or 's' key respectively. Scoreboard is also implemented,
		 and is taken and adapted from the pong module.
		-A scoreboard is created. It is also an adaptation from the 'pong' game.
		-The module car is created, and implemented in the game.
		-The car object now can appear in a random location that does not touch the
		 turtle either at the beginning, or at the safe zone all the way at the end.
		 It can cover a random distance between 5 and 10 pixels at a time. The function
		 for creating multiple cars is also codded, but not implemented yet.
		-The 'Y' coordinates for the car object were wrong before. The cars can have
		 different colors when they are instantiated.
		-Updated 'ToDo' list.
		-The car objects go back to the initial 'X' axis location, but with a random
		 'Y' location and color thanks to the 'new_location()' in the car module.
		 Timmy the turtle also goes back to its origin after reaching the upper wall.
		-10 cars are created with random different colors, distance coverage, and location.
		 and the 'car' module was also modified so it would take the random locations,
		 and distance coverage correctly.
		-The cars would pick a random location and color, but would keep the same distance
		 coverage once they reset. Now they also get a new distance coverage, making
		 the game completely random in all aspects.
		-The player loses, and the game stops if Timmy gets hit by a car.
		-The distance between Timmy the turtle and the cars is a little bit smaller,
		 making the hit-box smaller. And after the player beats a level, the cars get
		 faster by a small amount.
		-Timmy module and class have been created.
		-The class Timmy has been updated for correct logic execution, and also
		 implemented in the 'cross_the_road' game.
		-Final touches before making the DocStrings.
		-DocStrings ready.
		-The cars needed to be generated off the screen. Therefore, more cars needed
		 to be added in order to make it a decent game.
		-'back_to_start()' method has been added to make a cleaner and less repetitive
		 code.
		-Final DocString.
24.-Twenty fourth day of the 100day challenge:
	-How to write to files:
		-The initial files are created.
		-End of the intro to writing and reading files.
	-Snake game 2.0:
		-All the files are copied to today's directory.
		-The Game Over method was deleted from the scoreboard module, and it was replaced
		 with the reset method. It takes the score of the current game, and checks it if
		 it is higher than the previous higher score. If it is, then updates the high
		 score. (The snake module needs to be updated also, since it does not stop once
		 it hits a wall).
		-The reset method has been added to the snake class. It deletes all the
		 segments previously obtained by the snake (deletes all the objects in the list),
		 then creates a new snake from scratch and sets it up in the middle of the screen.
		 (the snake reset is properly working, but I need to delete the turtle objects
		 that are left over from the previous game)."
		-The snake's links are now shipped elsewhere on the screen, so the game can
		 start from a clean screen every time. (This might not be the best way to tackle
		 it since the turtle objects will be pilling up every time the game restarts)"
		-The score is now being kept by saving it into a '.txt' file. So, even if the
		 game is closed, it will always have the highest score. The file that contains
		 the 'reading files' code has been modified to show the difference between
		 'absolute path' and 'relative path'.
	-Mail merge:
		-All files ready.
		-Getting all the names into a list.
		-Creates all the letters with their respective person as the title of the
		 letter, and also in the receivers name inside the letter.
		-Professor's way of solving the challenge.
		-Final DocStrings for the Snake 2.0 game.
25.-Twenty fifth day of the 100day challenge:
	-Warm up:
		-Pandas crash course.
		-The 'weather.py' file was in the wrong directory.
	-Squirrel census:
		-All the files are in place.
		-It is printing the correct information, but in the wrong way. I have to create
		 two dictionaries of lists, not a single dictionary.
		-Problem solved.
		-I feel like it is a better implementation.
		-I was writing everything in a wrong file.
	-U.S States Game:
		-Everything is set up.
		-Setting up the screen.
		-To do list.
		-The module and class 'pin' have been added in order to place the pin
		 location of the different states on the map.
		-Everything works as intended. The only thing left is to check the actual
		 game and see if there are any other rules I missed. Plus, do some
		 housecleaning, and DocStrings.
		-If the person answers the 50 states right, then the game ends. Also, there
		 is a command that would end the game right away 'exit'.
		-I re-arranged the code a bit and put the functions on top, that way it is
		 easier to read. Now the game keeps track of the states that that person
		 missed when the game ended, and writes it in a 'csv' file. The file only
		 has the name of the states: no coordinates or anything else.
		-Professor's way of solving the challenge.
26.-Twenty sixth day of the 100day challenge:
	-Warm up:
		-Series of warmups.
		-The last one is tricky and it was great to solve.
		-List comprehension for the 'states' game made by the professor. My version
		 of the code does not use that kind of 'for loop' therefore, rendering unsuitable.
		-Dictionary comprehension.
		-Dictionary comprehension 2.
		-Dictionary comprehension 3.
		-Loop through a Pandas data frame.
	-Nato alphabet:
		-Starting logic.
		-Final code.
27.-Twenty sixth day of the 100day challenge:
	-Warm up:
		-Creating our first GUI program.
		-Labels.
		-*args.
		-Alternative way of solving it.
		-**kwargs.
		-class + **kwargs.
		-Way around accessing keys that do not exist in a dictionary. (**kwargs)
		-This is how you would update the text in a label.
		-Buttons.
		-Event listeners for buttons.
		-Entry: (It basically is an input field).
		-All the different widgets.
		-Changing the layout and positioning of the widgets with 'place()'.
		-Changing the layout and positioning of the widgets with 'grid()'.
		-Add padding. (A little wiggle room on the edges. Like a frame).
		-Or add padding to a specific widget.
	-Miles to Kilometers:
		-Initial code.
		-User input.
		-First label: Miles.
		-Second label: is equal to.
		-Third label: result of calculation.
		-Function for calculating miles to kilometers.
		-Kilometers label.
		-Button.
		-If the input is an integer, then the calculation should end up being an
		 integer. That is why I changed the input to float, so the calculation can
		 be more precise.
		-Better layout.
28.-Twenty eigth day of the 100day challenge:
	-Pomodoro clock:
		-Starting files and code.
		-Background color changed.
		-Added the 'Timer' text on top of the tomato. And also put everything into
		 a grid layout.
		-Added the buttons 'Start' and 'Reset' to the GUI."
		-Added the 'check mark' label.
		-Actual layout (The positioning was incorrect).
		-No edge around the buttons.
		-Updating some variables.
		-Countdown Mechanism.
		-Timer Mechanism.
		-Making a timer in minutes.
		-Now it looks like an actual timer when the number is "00".
		-How  to set a new timer after the old one expired.
		-Just a little more and the logic is finished.
		-Working idea. Needs final implementation.
		-Now with variables (closer to how it should look like at the end).
		-Working implementation. Needs refinement.
		-REPS was a global variable, and it was created as 'rep'.
		-The check marks are now updating, but in odd intervals.
		-A token variable is created and initialized to '0' to keep track of how
		 many times the person studied for 25mins straight. That token is passed
		 down as an argument to the 'count_down()' function, so it knows when to
		 print the check marks. The check marks label starts off empty. Then it
		 follows this formula 'reps-token' where 'reps' is the total number of
		 repetitions the 'for loop' did; which is stored in REPS, and it is also
		 passed down as an argument, hence 'reps'. When the last iteration comes,
		 it simply prints 4 check marks, and lets the person take a break for 20mins.
		-The rest of the debugging code has been commented out.
		-I was missing the labels for the 'work', 'short break' and 'long break'.
		-Labels now change color accordingly to the pomodoro state they are at.
		-The 'reset' button now stops the timer and resets the screen. Due to the
		 fact that the code is designed to create all the timers at once, making
		 each one of them wait for their turn, a layer of complexity was added. At
		 the moment the timers are created, they HAVE to be saved in SEPARATED
		 variables, otherwise, later on it would be impossible to stop all of them.
		 To solve this problem, a global dictionary 'TIMER_DICT' has been implemented,
		 which holds all the '.after()' iterations, rendering possible to access and
		 stop them one by one.
		-Now, when the user hits 'start' again, after resetting the timer, it
		 correctly starts a brand new timer.
		-Back to the original timeframes: the program is finished.
29.-Twenty nineth day of the 100day challenge:
	-Password Manager:
		-Starting files and code.
		-Lock image.
		-Labels.
		-Text boxes.
		-Buttons added and alignment of all the widgets.
		-I just switched the way the '**kwargs' are passed. It resembles 'Pandas'
		 dataframes.
		-A little more wiggle room for aesthetics.
		-Autoinitialize the email text box with '@gmail.com'.
		-Places the cursor to the website text box as soon as the program runs, and
		 initialize the email text box with '@gmail.com'."
		-The text boxes are actually 'entry' boxes.
		-The entry boxes' layout also changed. They needed to be wider.
		-If the user hits the 'add' button, then the code saves all the typed
		 information in a new line to a '.txt' file. If the file does not exist, it
		 creates it.
		-Now it deletes credentials on screen, so new ones can be typed.
		-Then challenge states that the function should be called 'save'.
		-A pop-up window appears, and asks the user if the information entered is
		 correct before actually saving it into the '.txt' file.
		-If the person leaves any field empty, then a warning pops up saying so.
		-Password generator function: It takes the source code from 'Day_5' and
		 adapts it, so whenever the person hits the 'Generate password' button, it
		 generates a strong random password.
		-A more pythonic approach to creating the final password string.
		-Amazingly clever way to copy the freshly generated password into the
		 clipboard, so it can be used or pasted anywhere.
30.-Thirtieth day of the 100day challenge:
	-Warm up:
		-Error handling: FileNotFoundError.
		-This is how you would most likely solve problem #1.
		-And this is how you would most likely solve problem #2.
		-You can also be more specific and get a hold to that error and print it.
		-In case all the 'try' succeed.
		-This will execute no matter what.
		-This is how you would raise your own exceptions.
		-Exercise 1.
		-Exercise 2.
		-Exercise 3.
		-Starting files for today's challenge.
		-How to save everything as a '.json' file.
		-This is how it actually should look like at the end. (better written code).
		-Search button, plus layout update.
		-'find_password()' implemented and added to de button 'Search'.
		-Pop up window + 'try ... except ... else' to catch 'FileNotFoundError'
		 and 'KeyError'.
		-I forgot to put the warning when there is no '.json' file inside a pop up
		 window. It just printed the message to the command line.
31.-Thirty-first day of the 100day challenge:
	-Flash card:
		-Starting directories, files and code.
		-Front and back images, and buttons.
		-Title and word of the flashcard.
		-It is better having the words as a constant list.
		-The card's tittle is supposed to start off as 'language', then change.
		-I added a new button to start the game. Otherwise, it would have started
		 as soon as the program executed. Now the user has the choice when to start
		 the game. Whenever any of the buttons is pressed, a 3sec counter starts,
		 and after it is finished, the card flips and shows the translated word.
		 Right now it just flips without giving the answer. It has to do with the
		 way the random word is chosen from the list. (It is better to get hold of
		 he actual dictionary, then access the original word, that way I can pass
		 the dict to later access the translation).
		-Problem solved: get hold of the dictionary, then access the different words
		 in their respective languages, in their respective timeframes.
		-The card now changes color to green after flipping back to 'English'.
		-There was as word that did not have the alternative meaning.
		-The word cause was the shortened version of because.
		-The tilde was missing.
		-It did not have the alternative meaning.
		-It need context to have that meaning.
		-It did not have the alternative meaning.
		-It does not exist in spanish.
		-The program now keeps track of all the words the person knows, and takes
		 them out of the flash cards deck. You can access these known words by
		 printing the 'KNOWN_WORDS' list. The intention is to show all the words as
		 a panel in a new window, after clicking the 'Known' button on the top right
		 corner. The button exists, and creates a pop up window, but right now, the
		 window it is empty.
		-The user can now see all the words they know in a dedicated screen.
		-Everything is now in a 'try..except..else' to prevent the user from starting
		 the selection process before starting the game."
		-Greeting message instead of plain words.
		-Now the person gets a '.csv' file with all the words they need to focus on.
		 And there is a new counter in the known words, showing the total words they
		 know out of 860.
		-Simplify the code by adding 'next_card()'.
		-Re-arranging the functions for readability.
		-There is now a new window that shows the words that need focus. (csv + GUI).
		-Exception handling: FileNotFoundError.
		-Simple exception handling: I chose to do it this way since it can be tackled
		 with an 'if statement', and there is also no error it can possibly produce.
		-Bettere labeling for the pop up windows: They now state if the user is in
		 'known' or 'unknown' pop up window.
32.-Thirty-second day of the 100day challenge:
	-Warm up:
		-Starting files.
		-Sending an e-mail.
		-Motivational quote in email depending day of the week.
		-Change the name.
	-Birthday wisher:
		-Starting files.
		-I don't like 'main.py'.
		-Starting code.
		-'birthdays.csv' updated.
		-One birthday has to be today, otherwise it would be very hard to test the code.
		-I know I should have kept everything logged, as I have been doing. But I was
		 in a hurry and needed to finish fast. It will not happen again.
		-Alternative way of solving the challenge.
33.-Thirty-third day of the 100day challenge:
	-Warm up:
		-Initial code: API request.
		-API response meaning.
		-JSON file from API.
		-Latitude and Longitude as a tuple.
	-Kanye API:
		-Kanye API initial files and code.
		-End code. (it was not that complicated).
	-Sunset and sunrise API:
		-Initial code.
	-ISS Overhead notifier:
		-Starting file.
		-Final version.
		-The comparison can also be written like this. Very handy.
		-Should be 'or' not 'and'.
		-Alternative solution to the challenge.
34.-Thirty-fourth day of the 100day challenge:
===============================================================================
===============================================================================
