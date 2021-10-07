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
===============================================================================
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
===============================================================================
