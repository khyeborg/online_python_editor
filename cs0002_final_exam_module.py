print("CSCI-UA.0002 Final Exam Module")
print()

class person():
    def __init__(self,name,birthyear,father,mother,sex):
        self.name=name
        self.birthyear=birthyear
        self.father=father
        self.mother=mother
        self.sex=sex
def print_tree(person,generation=0):
    if generation<3:
        print(person.name,person.father.name,
              person.mother.name,person.birthyear,person.sex, generation)
        print_tree(person.mother,generation+1) 
        print_tree(person.father,generation+1) 
    else:
        print(person.name, person.birthyear,person.sex, generation)

def gen_person(name,generation,sex):
    birthyear=1980-30*generation+(len(name)%5)
    if generation==3:
        father=None
        mother=None
    else:
        father_name=male_names.pop()
        mother_name=female_names.pop()
        father=gen_person(father_name,generation+1,"male")
        mother=gen_person(mother_name,generation+1,"female")
    return person(name,birthyear,father,mother,sex)

male_names = ['Liam', 'Noah', 'Oliver', 'Elijah', 'William', 'James', 'Benjamin', 'Lucas', 'Henry', 'Alexander', 'Mason', 'Michael', 'Ethan', 'Daniel', 'Jacob', 'Logan', 'Jackson', 'Levi', 'Sebastian', 'Mateo', 'Jack', 'Owen', 'Theodore', 'Aiden', 'Samuel', 'Joseph', 'John', 'David', 'Wyatt', 'Matthew', 'Luke', 'Asher', 'Carter', 'Julian', 'Grayson', 'Leo', 'Jayden', 'Gabriel', 'Isaac', 'Lincoln', 'Anthony', 'Hudson', 'Dylan', 'Ezra', 'Thomas', 'Charles', 'Christopher', 'Jaxon', 'Maverick', 'Josiah', 'Isaiah', 'Andrew', 'Elias', 'Joshua', 'Nathan', 'Caleb', 'Ryan', 'Adrian', 'Miles', 'Eli', 'Nolan', 'Christian', 'Aaron', 'Cameron', 'Ezekiel', 'Colton', 'Luca', 'Landon', 'Hunter', 'Jonathan', 'Santiago', 'Axel', 'Easton', 'Cooper', 'Jeremiah', 'Angel', 'Roman', 'Connor', 'Jameson', 'Robert', 'Greyson', 'Jordan', 'Ian', 'Carson', 'Jaxson', 'Leonardo', 'Nicholas', 'Dominic', 'Austin', 'Everett', 'Brooks', 'Xavier', 'Kai', 'Jose', 'Parker', 'Adam', 'Jace', 'Wesley', 'Kayden', 'Silas', 'Bennett', 'Declan', 'Waylon', 'Weston', 'Evan', 'Emmett', 'Micah', 'Ryder', 'Beau', 'Damian', 'Brayden', 'Gael', 'Rowan', 'Harrison', 'Bryson', 'Sawyer', 'Amir', 'Kingston', 'Jason', 'Giovanni', 'Vincent', 'Ayden', 'Chase', 'Myles', 'Diego', 'Nathaniel', 'Legend', 'Jonah', 'River', 'Tyler', 'Cole', 'Braxton', 'George', 'Milo', 'Zachary', 'Ashton', 'Luis', 'Jasper', 'Kaiden', 'Adriel', 'Gavin', 'Bentley', 'Calvin', 'Zion', 'Juan', 'Maxwell', 'Max', 'Ryker', 'Carlos', 'Emmanuel', 'Jayce', 'Lorenzo', 'Ivan', 'Jude', 'August', 'Kevin', 'Malachi', 'Elliott', 'Rhett', 'Archer', 'Karter', 'Arthur', 'Luka', 'Elliot', 'Thiago', 'Brandon', 'Camden', 'Justin', 'Jesus', 'Maddox', 'King', 'Theo', 'Enzo', 'Matteo', 'Emiliano', 'Dean', 'Hayden', 'Finn', 'Brody', 'Antonio', 'Abel', 'Alex', 'Tristan', 'Graham', 'Zayden', 'Judah', 'Xander', 'Miguel', 'Atlas', 'Messiah', 'Barrett', 'Tucker', 'Timothy', 'Alan', 'Edward', 'Leon', 'Dawson', 'Eric', 'Ace', 'Victor', 'Abraham', 'Nicolas', 'Jesse', 'Charlie', 'Patrick', 'Walker', 'Joel', 'Richard', 'Beckett', 'Blake', 'Alejandro', 'Avery', 'Grant', 'Peter', 'Oscar', 'Matias', 'Amari', 'Lukas', 'Andres', 'Arlo', 'Colt', 'Adonis', 'Kyrie', 'Steven', 'Felix', 'Preston', 'Marcus', 'Holden', 'Emilio', 'Remington', 'Jeremy', 'Kaleb', 'Brantley', 'Bryce', 'Mark', 'Knox', 'Israel', 'Phoenix', 'Kobe', 'Nash', 'Griffin', 'Caden', 'Kenneth', 'Kyler', 'Hayes', 'Jax', 'Rafael', 'Beckham', 'Javier', 'Maximus', 'Simon', 'Paul', 'Omar', 'Kaden', 'Kash', 'Lane', 'Bryan', 'Riley', 'Zane', 'Louis', 'Aidan', 'Paxton', 'Maximiliano', 'Karson', 'Cash', 'Cayden', 'Emerson', 'Tobias', 'Ronan', 'Brian', 'Dallas', 'Bradley', 'Jorge', 'Walter', 'Josue', 'Khalil', 'Damien', 'Jett', 'Kairo', 'Zander', 'Andre', 'Cohen', 'Crew', 'Hendrix', 'Colin', 'Chance', 'Malakai', 'Clayton', 'Daxton', 'Malcolm', 'Lennox', 'Martin', 'Jaden', 'Kayson', 'Bodhi', 'Francisco', 'Cody', 'Erick', 'Kameron', 'Atticus', 'Dante', 'Jensen', 'Cruz', 'Finley', 'Brady', 'Joaquin', 'Anderson', 'Gunner', 'Muhammad', 'Zayn', 'Derek', 'Raymond', 'Kyle', 'Angelo', 'Reid', 'Spencer', 'Nico', 'Jaylen', 'Jake', 'Prince', 'Manuel', 'Ali', 'Gideon', 'Stephen', 'Ellis', 'Orion', 'Rylan', 'Eduardo', 'Mario', 'Rory', 'Cristian', 'Odin', 'Tanner', 'Julius', 'Callum', 'Sean', 'Kane', 'Ricardo', 'Travis', 'Wade', 'Warren', 'Fernando', 'Titus', 'Leonel', 'Edwin', 'Cairo', 'Corbin', 'Dakota', 'Ismael', 'Colson', 'Killian', 'Major', 'Tate', 'Gianni', 'Elian', 'Remy', 'Lawson', 'Niko', 'Nasir', 'Kade', 'Armani', 'Ezequiel', 'Marshall', 'Hector', 'Desmond', 'Kason', 'Garrett', 'Jared', 'Cyrus', 'Russell', 'Cesar', 'Tyson', 'Malik', 'Donovan', 'Jaxton', 'Cade', 'Romeo', 'Nehemiah', 'Sergio', 'Iker', 'Caiden', 'Jay', 'Pablo', 'Devin', 'Jeffrey', 'Otto', 'Kamari', 'Ronin', 'Johnny', 'Clark', 'Ari', 'Marco', 'Edgar', 'Bowen', 'Jaiden', 'Grady', 'Zayne', 'Sullivan', 'Jayceon', 'Sterling', 'Andy', 'Conor', 'Raiden', 'Royal', 'Royce', 'Solomon', 'Trevor', 'Winston', 'Emanuel', 'Finnegan', 'Pedro', 'Luciano', 'Harvey', 'Franklin', 'Noel', 'Troy', 'Princeton', 'Johnathan', 'Erik', 'Fabian', 'Oakley', 'Rhys', 'Porter', 'Hugo', 'Frank', 'Damon', 'Kendrick', 'Mathias', 'Milan', 'Peyton', 'Wilder', 'Callan', 'Gregory', 'Seth', 'Matthias', 'Briggs', 'Ibrahim', 'Roberto', 'Conner', 'Quinn', 'Kashton', 'Sage', 'Santino', 'Kolton', 'Alijah', 'Dominick', 'Zyaire', 'Apollo', 'Kylo', 'Reed', 'Philip', 'Kian', 'Shawn', 'Kaison', 'Leonidas', 'Ayaan', 'Lucca', 'Memphis', 'Ford', 'Baylor', 'Kyson', 'Uriel', 'Allen', 'Collin', 'Ruben', 'Archie', 'Dalton', 'Esteban', 'Adan', 'Forrest', 'Alonzo', 'Isaias', 'Leland', 'Jase', 'Dax', 'Kasen', 'Gage', 'Kamden', 'Marcos', 'Jamison', 'Francis', 'Hank', 'Alexis', 'Tripp', 'Frederick', 'Jonas', 'Stetson', 'Cassius', 'Izaiah', 'Eden', 'Maximilian', 'Rocco', 'Tatum', 'Keegan', 'Aziel', 'Moses', 'Bruce', 'Lewis', 'Braylen', 'Omari', 'Mack', 'Augustus', 'Enrique', 'Armando', 'Pierce', 'Moises', 'Asa', 'Shane', 'Emmitt', 'Soren', 'Dorian', 'Keanu', 'Zaiden', 'Raphael', 'Deacon', 'Abdiel', 'Kieran', 'Phillip', 'Ryland', 'Zachariah', 'Casey', 'Zaire', 'Albert', 'Baker', 'Corey', 'Kylan', 'Denver', 'Gunnar', 'Jayson', 'Drew', 'Callen', 'Jasiah', 'Drake', 'Kannon', 'Braylon', 'Sonny', 'Bo', 'Moshe', 'Huxley', 'Quentin', 'Rowen', 'Santana', 'Cannon', 'Kenzo', 'Wells', 'Julio', 'Nikolai', 'Conrad', 'Jalen', 'Makai', 'Benson', 'Derrick', 'Gerardo', 'Davis', 'Abram', 'Mohamed', 'Ronald', 'Raul', 'Arjun', 'Dexter', 'Kaysen', 'Jaime', 'Scott', 'Lawrence', 'Ariel', 'Skyler', 'Danny', 'Roland', 'Chandler', 'Yusuf', 'Samson', 'Case', 'Zain', 'Roy', 'Rodrigo', 'Sutton', 'Boone', 'Saint', 'Saul', 'Jaziel', 'Hezekiah', 'Alec', 'Arturo', 'Jamari', 'Jaxtyn', 'Julien', 'Koa', 'Reece', 'Landen', 'Koda', 'Darius', 'Sylas', 'Ares', 'Kyree', 'Boston', 'Keith', 'Taylor', 'Johan', 'Edison', 'Sincere', 'Watson', 'Jerry', 'Nikolas', 'Quincy', 'Shepherd', 'Brycen', 'Marvin', 'Dariel', 'Axton', 'Donald', 'Bodie', 'Finnley', 'Onyx', 'Rayan', 'Raylan', 'Brixton', 'Colby', 'Shiloh', 'Valentino', 'Layton', 'Trenton', 'Landyn', 'Alessandro', 'Ahmad', 'Gustavo', 'Ledger', 'Ridge', 'Ander', 'Ahmed', 'Kingsley', 'Issac', 'Mauricio', 'Tony', 'Leonard', 'Mohammed', 'Uriah', 'Duke', 'Kareem', 'Lucian', 'Marcelo', 'Aarav', 'Leandro', 'Reign', 'Clay', 'Kohen', 'Dennis', 'Samir', 'Ermias', 'Otis', 'Emir', 'Nixon', 'Ty', 'Sam', 'Fletcher', 'Wilson', 'Dustin', 'Hamza', 'Bryant', 'Flynn', 'Lionel', 'Mohammad', 'Cason', 'Jamir', 'Aden', 'Dakari', 'Justice', 'Dillon', 'Layne', 'Zaid', 'Alden', 'Nelson', 'Devon', 'Titan', 'Chris', 'Khari', 'Zeke', 'Noe', 'Alberto', 'Roger', 'Brock', 'Rex', 'Quinton', 'Alvin', 'Cullen', 'Azariah', 'Harlan', 'Kellan', 'Lennon', 'Marcel', 'Keaton', 'Morgan', 'Ricky', 'Trey', 'Karsyn', 'Langston', 'Miller', 'Chaim', 'Salvador', 'Amias', 'Tadeo', 'Curtis', 'Lachlan', 'Amos', 'Anakin', 'Krew', 'Tomas', 'Jefferson', 'Yosef', 'Bruno', 'Korbin', 'Augustine', 'Cayson', 'Mathew', 'Vihaan', 'Jamie', 'Clyde', 'Brendan', 'Jagger', 'Carmelo', 'Harry', 'Nathanael', 'Mitchell', 'Darren', 'Ray', 'Jedidiah', 'Jimmy', 'Lochlan', 'Bellamy', 'Eddie', 'Rayden', 'Reese', 'Stanley', 'Joe', 'Houston', 'Douglas', 'Vincenzo', 'Casen', 'Emery', 'Joziah', 'Leighton', 'Marcellus', 'Atreus', 'Aron', 'Hugh', 'Musa', 'Tommy', 'Alfredo', 'Junior', 'Neil', 'Westley', 'Banks', 'Eliel', 'Melvin', 'Maximo', 'Briar', 'Colten', 'Lance', 'Nova', 'Trace', 'Axl', 'Ramon', 'Vicente', 'Brennan', 'Caspian', 'Remi', 'Deandre', 'Legacy', 'Lee', 'Valentin', 'Ben', 'Louie', 'Westin', 'Wayne', 'Benicio', 'Grey', 'Zayd', 'Gatlin', 'Mekhi', 'Orlando', 'Bjorn', 'Harley', 'Alonso', 'Rio', 'Aldo', 'Byron', 'Eliseo', 'Ernesto', 'Talon', 'Thaddeus', 'Brecken', 'Kace', 'Kellen', 'Enoch', 'Kiaan', 'Lian', 'Creed', 'Rohan', 'Callahan', 'Jaxxon', 'Ocean', 'Crosby', 'Dash', 'Gary', 'Mylo', 'Ira', 'Magnus', 'Salem', 'Abdullah', 'Kye', 'Tru', 'Forest', 'Jon', 'Misael', 'Madden', 'Braden', 'Carl', 'Hassan', 'Emory', 'Kristian', 'Alaric', 'Ambrose', 'Dario', 'Allan', 'Bode', 'Boden', 'Juelz', 'Kristopher', 'Genesis', 'Idris', 'Ameer', 'Anders', 'Darian', 'Kase', 'Aryan', 'Dane', 'Guillermo', 'Elisha', 'Jakobe', 'Thatcher', 'Eugene', 'Ishaan', 'Larry', 'Wesson', 'Yehuda', 'Alvaro', 'Bobby', 'Bronson', 'Dilan', 'Kole', 'Kyro', 'Tristen', 'Blaze', 'Brayan', 'Jadiel', 'Kamryn', 'Demetrius', 'Maurice', 'Arian', 'Kabir', 'Rocky', 'Rudy', 'Randy', 'Rodney', 'Yousef', 'Felipe', 'Robin', 'Aydin', 'Dior', 'Kaiser', 'Van', 'Brodie', 'London', 'Eithan', 'Stefan', 'Ulises', 'Camilo', 'Branson', 'Jakari', 'Judson', 'Yahir', 'Zavier', 'Damari', 'Jakob', 'Jaxx', 'Bentlee', 'Cain', 'Niklaus', 'Rey', 'Zahir', 'Aries', 'Blaine', 'Kyng', 'Castiel', 'Henrik', 'Joey', 'Khalid', 'Bear', 'Graysen', 'Jair', 'Kylen', 'Darwin', 'Alfred', 'Ayan', 'Kenji', 'Zakai', 'Avi', 'Cory', 'Fisher', 'Jacoby', 'Osiris', 'Harlem', 'Jamal', 'Santos', 'Wallace', 'Brett', 'Fox', 'Leif', 'Maison', 'Reuben', 'Adler', 'Zev', 'Calum', 'Kelvin', 'Zechariah', 'Bridger', 'Mccoy', 'Seven', 'Shepard', 'Azrael', 'Leroy', 'Terry', 'Harold', 'Mac', 'Mordechai', 'Ahmir', 'Cal', 'Franco', 'Trent', 'Blaise', 'Coen', 'Dominik', 'Marley', 'Davion', 'Jeremias', 'Riggs', 'Jones', 'Will', 'Damir', 'Dangelo', 'Canaan', 'Dion', 'Jabari', 'Landry', 'Salvatore', 'Kody', 'Hakeem', 'Truett', 'Gerald', 'Lyric', 'Gordon', 'Jovanni', 'Kamdyn', 'Alistair', 'Cillian', 'Foster', 'Terrance', 'Murphy', 'Zyair', 'Cedric', 'Rome', 'Abner', 'Colter', 'Dayton', 'Jad', 'Xzavier', 'Rene', 'Vance', 'Duncan', 'Frankie', 'Bishop', 'Davian', 'Everest', 'Heath', 'Jaxen', 'Marlon', 'Maxton', 'Reginald', 'Harris', 'Jericho', 'Keenan', 'Korbyn', 'Wes', 'Eliezer', 'Jeffery', 'Kalel', 'Kylian', 'Turner', 'Willie', 'Rogeli', 'Ephraim']
female_names = ['Olivia', 'Emma', 'Ava', 'Charlotte', 'Sophia', 'Amelia', 'Isabella', 'Mia', 'Evelyn', 'Harper', 'Camila', 'Gianna', 'Abigail', 'Luna', 'Ella', 'Elizabeth', 'Sofia', 'Emily', 'Avery', 'Mila', 'Scarlett', 'Eleanor', 'Madison', 'Layla', 'Penelope', 'Aria', 'Chloe', 'Grace', 'Ellie', 'Nora', 'Hazel', 'Zoey', 'Riley', 'Victoria', 'Lily', 'Aurora', 'Violet', 'Nova', 'Hannah', 'Emilia', 'Zoe', 'Stella', 'Everly', 'Isla', 'Leah', 'Lillian', 'Addison', 'Willow', 'Lucy', 'Paisley', 'Natalie', 'Naomi', 'Eliana', 'Brooklyn', 'Elena', 'Aubrey', 'Claire', 'Ivy', 'Kinsley', 'Audrey', 'Maya', 'Genesis', 'Skylar', 'Bella', 'Aaliyah', 'Madelyn', 'Savannah', 'Anna', 'Delilah', 'Serenity', 'Caroline', 'Kennedy', 'Valentina', 'Ruby', 'Sophie', 'Alice', 'Gabriella', 'Sadie', 'Ariana', 'Allison', 'Hailey', 'Autumn', 'Nevaeh', 'Natalia', 'Quinn', 'Josephine', 'Sarah', 'Cora', 'Emery', 'Samantha', 'Piper', 'Leilani', 'Eva', 'Everleigh', 'Madeline', 'Lydia', 'Jade', 'Peyton', 'Brielle', 'Adeline', 'Vivian', 'Rylee', 'Clara', 'Raelynn', 'Melanie', 'Melody', 'Julia', 'Athena', 'Maria', 'Liliana', 'Hadley', 'Arya', 'Rose', 'Reagan', 'Eliza', 'Adalynn', 'Kaylee', 'Lyla', 'Mackenzie', 'Alaia', 'Isabelle', 'Charlie', 'Arianna', 'Mary', 'Remi', 'Margaret', 'Iris', 'Parker', 'Ximena', 'Eden', 'Ayla', 'Kylie', 'Elliana', 'Josie', 'Katherine', 'Faith', 'Alexandra', 'Eloise', 'Adalyn', 'Amaya', 'Jasmine', 'Amara', 'Daisy', 'Reese', 'Valerie', 'Brianna', 'Cecilia', 'Andrea', 'Summer', 'Valeria', 'Norah', 'Ariella', 'Esther', 'Ashley', 'Emerson', 'Aubree', 'Isabel', 'Anastasia', 'Ryleigh', 'Khloe', 'Taylor', 'Londyn', 'Lucia', 'Emersyn', 'Callie', 'Sienna', 'Blakely', 'Kehlani', 'Genevieve', 'Alina', 'Bailey', 'Juniper', 'Maeve', 'Molly', 'Harmony', 'Georgia', 'Magnolia', 'Catalina', 'Freya', 'Juliette', 'Sloane', 'June', 'Sara', 'Ada', 'Kimberly', 'River', 'Ember', 'Juliana', 'Aliyah', 'Millie', 'Brynlee', 'Teagan', 'Morgan', 'Jordyn', 'London', 'Alaina', 'Olive', 'Rosalie', 'Alyssa', 'Ariel', 'Finley', 'Arabella', 'Journee', 'Hope', 'Leila', 'Alana', 'Gemma', 'Vanessa', 'Gracie', 'Noelle', 'Marley', 'Elise', 'Presley', 'Kamila', 'Zara', 'Amy', 'Kayla', 'Payton', 'Blake', 'Ruth', 'Alani', 'Annabelle', 'Sage', 'Aspen', 'Laila', 'Lila', 'Rachel', 'Trinity', 'Daniela', 'Alexa', 'Lilly', 'Lauren', 'Elsie', 'Margot', 'Adelyn', 'Zuri', 'Brooke', 'Sawyer', 'Lilah', 'Lola', 'Selena', 'Mya', 'Sydney', 'Diana', 'Ana', 'Vera', 'Alayna', 'Nyla', 'Elaina', 'Rebecca', 'Angela', 'Kali', 'Alivia', 'Raegan', 'Rowan', 'Phoebe', 'Camilla', 'Joanna', 'Malia', 'Vivienne', 'Dakota', 'Brooklynn', 'Evangeline', 'Camille', 'Jane', 'Nicole', 'Catherine', 'Jocelyn', 'Julianna', 'Lena', 'Lucille', 'Mckenna', 'Paige', 'Adelaide', 'Charlee', 'Mariana', 'Myla', 'Mckenzie', 'Tessa', 'Miriam', 'Oakley', 'Kailani', 'Alayah', 'Amira', 'Adaline', 'Phoenix', 'Milani', 'Annie', 'Lia', 'Angelina', 'Harley', 'Cali', 'Maggie', 'Hayden', 'Leia', 'Fiona', 'Briella', 'Journey', 'Lennon', 'Saylor', 'Jayla', 'Kaia', 'Thea', 'Adriana', 'Mariah', 'Juliet', 'Oaklynn', 'Kiara', 'Alexis', 'Haven', 'Aniyah', 'Delaney', 'Gracelynn', 'Kendall', 'Winter', 'Lilith', 'Logan', 'Amiyah', 'Evie', 'Alexandria', 'Gracelyn', 'Gabriela', 'Sutton', 'Harlow', 'Madilyn', 'Makayla', 'Evelynn', 'Gia', 'Nina', 'Amina', 'Giselle', 'Brynn', 'Blair', 'Amari', 'Octavia', 'Michelle', 'Talia', 'Demi', 'Alaya', 'Kaylani', 'Izabella', 'Fatima', 'Tatum', 'Makenzie', 'Lilliana', 'Arielle', 'Palmer', 'Melissa', 'Willa', 'Samara', 'Destiny', 'Dahlia', 'Celeste', 'Ainsley', 'Rylie', 'Reign', 'Laura', 'Adelynn', 'Gabrielle', 'Remington', 'Wren', 'Brinley', 'Amora', 'Lainey', 'Collins', 'Lexi', 'Aitana', 'Alessandra', 'Kenzie', 'Raelyn', 'Elle', 'Everlee', 'Haisley', 'Hallie', 'Wynter', 'Daleyza', 'Gwendolyn', 'Paislee', 'Ariyah', 'Veronica', 'Heidi', 'Anaya', 'Cataleya', 'Kira', 'Avianna', 'Felicity', 'Aylin', 'Miracle', 'Sabrina', 'Lana', 'Ophelia', 'Elianna', 'Royalty', 'Madeleine', 'Esmeralda', 'Joy', 'Kalani', 'Esme', 'Jessica', 'Leighton', 'Ariah', 'Makenna', 'Nylah', 'Viviana', 'Camryn', 'Cassidy', 'Dream', 'Luciana', 'Maisie', 'Stevie', 'Kate', 'Lyric', 'Daniella', 'Alicia', 'Daphne', 'Frances', 'Charli', 'Raven', 'Paris', 'Nayeli', 'Serena', 'Heaven', 'Bianca', 'Helen', 'Hattie', 'Averie', 'Mabel', 'Selah', 'Allie', 'Marlee', 'Kinley', 'Regina', 'Carmen', 'Jennifer', 'Jordan', 'Alison', 'Stephanie', 'Maren', 'Kayleigh', 'Angel', 'Annalise', 'Jacqueline', 'Braelynn', 'Emory', 'Rosemary', 'Scarlet', 'Amanda', 'Danielle', 'Emelia', 'Ryan', 'Carolina', 'Astrid', 'Kensley', 'Shiloh', 'Maci', 'Francesca', 'Rory', 'Celine', 'Kamryn', 'Zariah', 'Liana', 'Poppy', 'Maliyah', 'Keira', 'Skyler', 'Noa', 'Skye', 'Nadia', 'Addilyn', 'Rosie', 'Eve', 'Sarai', 'Edith', 'Jolene', 'Maddison', 'Meadow', 'Charleigh', 'Matilda', 'Elliott', 'Madelynn', 'Holly', 'Leona', 'Azalea', 'Katie', 'Mira', 'Ari', 'Kaitlyn', 'Danna', 'Cameron', 'Kyla', 'Bristol', 'Kora', 'Armani', 'Nia', 'Malani', 'Dylan', 'Remy', 'Maia', 'Dior', 'Legacy', 'Alessia', 'Shelby', 'Maryam', 'Sylvia', 'Yaretzi', 'Lorelei', 'Madilynn', 'Abby', 'Helena', 'Jimena', 'Elisa', 'Renata', 'Amber', 'Aviana', 'Carter', 'Emmy', 'Haley', 'Alondra', 'Elaine', 'Erin', 'April', 'Emely', 'Imani', 'Kennedi', 'Lorelai', 'Hanna', 'Kelsey', 'Aurelia', 'Colette', 'Jaliyah', 'Kylee', 'Macie', 'Aisha', 'Dorothy', 'Charley', 'Kathryn', 'Adelina', 'Adley', 'Monroe', 'Sierra', 'Ailani', 'Miranda', 'Mikayla', 'Alejandra', 'Amirah', 'Jada', 'Jazlyn', 'Jenna', 'Jayleen', 'Beatrice', 'Kendra', 'Lyra', 'Nola', 'Emberly', 'Mckinley', 'Myra', 'Katalina', 'Antonella', 'Zelda', 'Alanna', 'Amaia', 'Priscilla', 'Briar', 'Kaliyah', 'Itzel', 'Oaklyn', 'Alma', 'Mallory', 'Novah', 'Amalia', 'Fernanda', 'Alia', 'Angelica', 'Elliot', 'Justice', 'Mae', 'Cecelia', 'Gloria', 'Ariya', 'Virginia', 'Cheyenne', 'Aleah', 'Jemma', 'Henley', 'Meredith', 'Leyla', 'Lennox', 'Ensley', 'Zahra', 'Reina', 'Frankie', 'Lylah', 'Nalani', 'Reyna', 'Saige', 'Ivanna', 'Aleena', 'Emerie', 'Ivory', 'Leslie', 'Alora', 'Ashlyn', 'Bethany', 'Bonnie', 'Sasha', 'Xiomara', 'Salem', 'Adrianna', 'Dayana', 'Clementine', 'Karina', 'Karsyn', 'Emmie', 'Julie', 'Julieta', 'Briana', 'Carly', 'Macy', 'Marie', 'Oaklee', 'Christina', 'Malaysia', 'Ellis', 'Irene', 'Anne', 'Anahi', 'Mara', 'Rhea', 'Davina', 'Dallas', 'Jayda', 'Mariam', 'Skyla', 'Siena', 'Elora', 'Marilyn', 'Jazmin', 'Megan', 'Rosa', 'Savanna', 'Allyson', 'Milan', 'Coraline', 'Johanna', 'Melany', 'Chelsea', 'Michaela', 'Melina', 'Angie', 'Cassandra', 'Yara', 'Kassidy', 'Liberty', 'Lilian', 'Avah', 'Anya', 'Laney', 'Navy', 'Opal', 'Amani', 'Zaylee', 'Mina', 'Sloan', 'Romina', 'Ashlynn', 'Aliza', 'Liv', 'Malaya', 'Blaire', 'Janelle', 'Kara', 'Analia', 'Hadassah', 'Hayley', 'Karla', 'Chaya', 'Cadence', 'Kyra', 'Alena', 'Ellianna', 'Katelyn', 'Kimber', 'Laurel', 'Lina', 'Capri', 'Braelyn', 'Faye', 'Kamiyah', 'Kenna', 'Louise', 'Calliope', 'Kaydence', 'Nala', 'Tiana', 'Aileen', 'Sunny', 'Zariyah', 'Milana', 'Giuliana', 'Eileen', 'Elodie', 'Rayna', 'Monica', 'Galilea', 'Journi', 'Lara', 'Marina', 'Aliana', 'Harmoni', 'Jamie', 'Holland', 'Emmalyn', 'Lauryn', 'Chanel', 'Tinsley', 'Jessie', 'Lacey', 'Elyse', 'Janiyah', 'Jolie', 'Ezra', 'Marleigh', 'Roselyn', 'Lillie', 'Louisa', 'Madisyn', 'Penny', 'Kinslee', 'Treasure', 'Zaniyah', 'Estella', 'Jaylah', 'Khaleesi', 'Alexia', 'Dulce', 'Indie', 'Maxine', 'Waverly', 'Giovanna', 'Miley', 'Saoirse', 'Estrella', 'Greta', 'Rosalia', 'Mylah', 'Teresa', 'Bridget', 'Kelly', 'Adalee', 'Aubrie', 'Lea', 'Harlee', 'Anika', 'Itzayana', 'Hana', 'Kaisley', 'Mikaela', 'Naya', 'Avalynn', 'Margo', 'Sevyn', 'Florence', 'Keilani', 'Lyanna', 'Joelle', 'Kataleya', 'Royal', 'Averi', 'Kallie', 'Winnie', 'Baylee', 'Martha', 'Pearl', 'Alaiya', 'Rayne', 'Sylvie', 'Brylee', 'Jazmine', 'Ryann', 'Kori', 'Noemi', 'Haylee', 'Julissa', 'Celia', 'Laylah', 'Rebekah', 'Rosalee', 'Aya', 'Bria', 'Adele', 'Aubrielle', 'Tiffany', 'Addyson', 'Kai', 'Bellamy', 'Leilany', 'Princess', 'Chana', 'Estelle', 'Selene', 'Sky', 'Dani', 'Thalia', 'Ellen', 'Rivka', 'Amelie', 'Andi', 'Kynlee', 'Raina', 'Vienna', 'Alianna', 'Livia', 'Madalyn', 'Mercy', 'Novalee', 'Ramona', 'Vada', 'Berkley', 'Gwen', 'Persephone', 'Milena', 'Paula', 'Clare', 'Kairi', 'Linda', 'Paulina', 'Kamilah', 'Amoura', 'Hunter', 'Isabela', 'Karen', 'Marianna', 'Sariyah', 'Theodora', 'Annika', 'Kyleigh', 'Nellie', 'Scarlette', 'Keyla', 'Kailey', 'Mavis', 'Lilianna', 'Rosalyn', 'Sariah', 'Tori', 'Yareli', 'Aubriella', 'Bexley', 'Bailee', 'Jianna', 'Keily', 'Annabella', 'Azariah', 'Denisse', 'Promise', 'August', 'Hadlee', 'Halle', 'Fallon', 'Oakleigh', 'Zaria', 'Jaylin', 'Paisleigh', 'Crystal', 'Ila', 'Aliya', 'Cynthia', 'Giana', 'Maleah', 'Rylan', 'Aniya', 'Denise', 'Emmeline', 'Scout', 'Simone', 'Noah', 'Zora', 'Meghan', 'Landry', 'Ainhoa', 'Lilyana', 'Noor', 'Belen', 'Brynleigh', 'Cleo', 'Meilani', 'Karter', 'Amaris', 'Frida', 'Iliana', 'Violeta', 'Addisyn', 'Nancy', 'Denver', 'Leanna', 'Braylee', 'Kiana', 'Wrenley', 'Barbara', 'Khalani', 'Aspyn', 'Ellison', 'Judith', 'Robin', 'Valery', 'Aila', 'Deborah', 'Cara', 'Clarissa', 'Iyla', 'Lexie', 'Anais', 'Kaylie', 'Nathalie', 'Alisson', 'Della', 'Addilynn', 'Elsa', 'Zoya', 'Layne', 'Marlowe', 'Jovie', 'Kenia', 'Samira', 'Jaylee', 'Jenesis', 'Etta', 'Shay', 'Amayah', 'Avayah', 'Egypt', 'Flora', 'Raquel', 'Whitney', 'Zola', 'Giavanna', 'Raya', 'Veda', 'Halo', 'Paloma', 'Nataly', 'Whitley', 'Dalary', 'Drew', 'Guadalupe', 'Kamari', 'Esperanza', 'Loretta', 'Malayah', 'Natasha', 'Stormi', 'Ansley', 'Carolyn', 'Corinne', 'Paola', 'Brittany', 'Emerald', 'Freyja', 'Zainab', 'Artemis', 'Jillian', 'Kimora', 'Zoie', 'Aislinn', 'Emmaline', 'Ayleen', 'Queen', 'Jaycee', 'Murphy', 'Nyomi', 'Elina', 'Hadleigh', 'Marceline', 'Marisol', 'Yasmin', 'Zendaya', 'Chandler', 'Emani', 'Jaelynn', 'Kaiya', 'Nathalia', 'Violette', 'Joyce', 'Paityn', 'Elisabeth', 'Emmalynn', 'Luella', 'Yamileth', 'Aarya', 'Luisa', 'Zhuri', 'Araceli', 'Harleigh', 'Madalynn', 'Melani', 'Laylani', 'Magdalena', 'Mazikeen', 'Belle', 'Kadence']
sex="Female"
n=0
while (len(female_names)>=8) and (len(male_names)>=8):
    n+=1
    if sex=="Female":
        exec(f"p{str(n)}=gen_person(female_names.pop(),0,\"female\")")
        sex="Male"
    else:
        exec(f"p{str(n)}=gen_person(male_names.pop(),0,\"male\")")
        sex="Female"

class CarModel001:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'AliceBlue'
        self.current_speed = 0
        self.top_speed = 483 # feet per second
        self.acceleration_rate = 106 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel002:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'AntiqueWhite'
        self.current_speed = 0
        self.top_speed = 455 # feet per second
        self.acceleration_rate = 110 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel003:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Aqua'
        self.current_speed = 0
        self.top_speed = 476 # feet per second
        self.acceleration_rate = 100 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel004:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Aquamarine'
        self.current_speed = 0
        self.top_speed = 463 # feet per second
        self.acceleration_rate = 102 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel005:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Azure'
        self.current_speed = 0
        self.top_speed = 458 # feet per second
        self.acceleration_rate = 120 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel006:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Beige'
        self.current_speed = 0
        self.top_speed = 414 # feet per second
        self.acceleration_rate = 109 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel007:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Bisque'
        self.current_speed = 0
        self.top_speed = 475 # feet per second
        self.acceleration_rate = 125 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel008:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Black'
        self.current_speed = 0
        self.top_speed = 407 # feet per second
        self.acceleration_rate = 113 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel009:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'BlanchedAlmond'
        self.current_speed = 0
        self.top_speed = 418 # feet per second
        self.acceleration_rate = 117 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel010:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Blue'
        self.current_speed = 0
        self.top_speed = 405 # feet per second
        self.acceleration_rate = 124 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel011:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'BlueViolet'
        self.current_speed = 0
        self.top_speed = 403 # feet per second
        self.acceleration_rate = 102 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel012:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Brown'
        self.current_speed = 0
        self.top_speed = 405 # feet per second
        self.acceleration_rate = 114 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel013:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'BurlyWood'
        self.current_speed = 0
        self.top_speed = 412 # feet per second
        self.acceleration_rate = 123 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel014:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'CadetBlue'
        self.current_speed = 0
        self.top_speed = 411 # feet per second
        self.acceleration_rate = 106 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel015:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Chartreuse'
        self.current_speed = 0
        self.top_speed = 436 # feet per second
        self.acceleration_rate = 120 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel016:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Chocolate'
        self.current_speed = 0
        self.top_speed = 421 # feet per second
        self.acceleration_rate = 130 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel017:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Coral'
        self.current_speed = 0
        self.top_speed = 445 # feet per second
        self.acceleration_rate = 114 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel018:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'CornflowerBlue'
        self.current_speed = 0
        self.top_speed = 492 # feet per second
        self.acceleration_rate = 115 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel019:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Cornsilk'
        self.current_speed = 0
        self.top_speed = 406 # feet per second
        self.acceleration_rate = 114 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel020:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Crimson'
        self.current_speed = 0
        self.top_speed = 435 # feet per second
        self.acceleration_rate = 118 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel021:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Cyan'
        self.current_speed = 0
        self.top_speed = 445 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel022:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkBlue'
        self.current_speed = 0
        self.top_speed = 482 # feet per second
        self.acceleration_rate = 117 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel023:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkCyan'
        self.current_speed = 0
        self.top_speed = 426 # feet per second
        self.acceleration_rate = 113 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel024:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkGoldenRod'
        self.current_speed = 0
        self.top_speed = 444 # feet per second
        self.acceleration_rate = 127 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel025:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkGray'
        self.current_speed = 0
        self.top_speed = 491 # feet per second
        self.acceleration_rate = 124 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel026:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkGrey'
        self.current_speed = 0
        self.top_speed = 483 # feet per second
        self.acceleration_rate = 123 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel027:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkGreen'
        self.current_speed = 0
        self.top_speed = 422 # feet per second
        self.acceleration_rate = 127 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel028:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkKhaki'
        self.current_speed = 0
        self.top_speed = 500 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel029:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkMagenta'
        self.current_speed = 0
        self.top_speed = 421 # feet per second
        self.acceleration_rate = 115 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel030:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkOliveGreen'
        self.current_speed = 0
        self.top_speed = 438 # feet per second
        self.acceleration_rate = 120 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel031:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkOrange'
        self.current_speed = 0
        self.top_speed = 431 # feet per second
        self.acceleration_rate = 125 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel032:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkOrchid'
        self.current_speed = 0
        self.top_speed = 413 # feet per second
        self.acceleration_rate = 124 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel033:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkRed'
        self.current_speed = 0
        self.top_speed = 409 # feet per second
        self.acceleration_rate = 128 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel034:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkSalmon'
        self.current_speed = 0
        self.top_speed = 445 # feet per second
        self.acceleration_rate = 114 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel035:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkSeaGreen'
        self.current_speed = 0
        self.top_speed = 439 # feet per second
        self.acceleration_rate = 107 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel036:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkSlateBlue'
        self.current_speed = 0
        self.top_speed = 434 # feet per second
        self.acceleration_rate = 116 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel037:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkSlateGray'
        self.current_speed = 0
        self.top_speed = 439 # feet per second
        self.acceleration_rate = 103 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel038:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkSlateGrey'
        self.current_speed = 0
        self.top_speed = 471 # feet per second
        self.acceleration_rate = 108 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel039:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkTurquoise'
        self.current_speed = 0
        self.top_speed = 424 # feet per second
        self.acceleration_rate = 115 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel040:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DarkViolet'
        self.current_speed = 0
        self.top_speed = 473 # feet per second
        self.acceleration_rate = 130 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel041:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DeepPink'
        self.current_speed = 0
        self.top_speed = 426 # feet per second
        self.acceleration_rate = 126 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel042:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DeepSkyBlue'
        self.current_speed = 0
        self.top_speed = 483 # feet per second
        self.acceleration_rate = 129 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel043:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DimGray'
        self.current_speed = 0
        self.top_speed = 420 # feet per second
        self.acceleration_rate = 118 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel044:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DimGrey'
        self.current_speed = 0
        self.top_speed = 411 # feet per second
        self.acceleration_rate = 113 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel045:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'DodgerBlue'
        self.current_speed = 0
        self.top_speed = 455 # feet per second
        self.acceleration_rate = 127 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel046:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'FireBrick'
        self.current_speed = 0
        self.top_speed = 462 # feet per second
        self.acceleration_rate = 104 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel047:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'FloralWhite'
        self.current_speed = 0
        self.top_speed = 461 # feet per second
        self.acceleration_rate = 110 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel048:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'ForestGreen'
        self.current_speed = 0
        self.top_speed = 428 # feet per second
        self.acceleration_rate = 101 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel049:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Fuchsia'
        self.current_speed = 0
        self.top_speed = 453 # feet per second
        self.acceleration_rate = 108 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel050:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Gainsboro'
        self.current_speed = 0
        self.top_speed = 457 # feet per second
        self.acceleration_rate = 104 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel051:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'GhostWhite'
        self.current_speed = 0
        self.top_speed = 440 # feet per second
        self.acceleration_rate = 109 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel052:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Gold'
        self.current_speed = 0
        self.top_speed = 456 # feet per second
        self.acceleration_rate = 112 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel053:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'GoldenRod'
        self.current_speed = 0
        self.top_speed = 467 # feet per second
        self.acceleration_rate = 129 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel054:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Gray'
        self.current_speed = 0
        self.top_speed = 413 # feet per second
        self.acceleration_rate = 103 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel055:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Grey'
        self.current_speed = 0
        self.top_speed = 489 # feet per second
        self.acceleration_rate = 117 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel056:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Green'
        self.current_speed = 0
        self.top_speed = 443 # feet per second
        self.acceleration_rate = 116 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel057:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'GreenYellow'
        self.current_speed = 0
        self.top_speed = 486 # feet per second
        self.acceleration_rate = 106 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel058:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'HoneyDew'
        self.current_speed = 0
        self.top_speed = 408 # feet per second
        self.acceleration_rate = 125 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel059:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'HotPink'
        self.current_speed = 0
        self.top_speed = 415 # feet per second
        self.acceleration_rate = 122 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel060:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'IndianRed'
        self.current_speed = 0
        self.top_speed = 465 # feet per second
        self.acceleration_rate = 122 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel061:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Indigo'
        self.current_speed = 0
        self.top_speed = 489 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel062:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Ivory'
        self.current_speed = 0
        self.top_speed = 439 # feet per second
        self.acceleration_rate = 117 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel063:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Khaki'
        self.current_speed = 0
        self.top_speed = 454 # feet per second
        self.acceleration_rate = 130 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel064:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Lavender'
        self.current_speed = 0
        self.top_speed = 402 # feet per second
        self.acceleration_rate = 109 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel065:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LavenderBlush'
        self.current_speed = 0
        self.top_speed = 454 # feet per second
        self.acceleration_rate = 127 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel066:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LawnGreen'
        self.current_speed = 0
        self.top_speed = 413 # feet per second
        self.acceleration_rate = 124 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel067:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LemonChiffon'
        self.current_speed = 0
        self.top_speed = 427 # feet per second
        self.acceleration_rate = 103 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel068:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightBlue'
        self.current_speed = 0
        self.top_speed = 415 # feet per second
        self.acceleration_rate = 106 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel069:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightCoral'
        self.current_speed = 0
        self.top_speed = 483 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel070:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightCyan'
        self.current_speed = 0
        self.top_speed = 485 # feet per second
        self.acceleration_rate = 108 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel071:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightGoldenRodYellow'
        self.current_speed = 0
        self.top_speed = 460 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel072:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightGray'
        self.current_speed = 0
        self.top_speed = 448 # feet per second
        self.acceleration_rate = 107 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel073:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightGrey'
        self.current_speed = 0
        self.top_speed = 452 # feet per second
        self.acceleration_rate = 123 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel074:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightGreen'
        self.current_speed = 0
        self.top_speed = 449 # feet per second
        self.acceleration_rate = 100 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel075:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightPink'
        self.current_speed = 0
        self.top_speed = 429 # feet per second
        self.acceleration_rate = 108 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel076:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightSalmon'
        self.current_speed = 0
        self.top_speed = 465 # feet per second
        self.acceleration_rate = 130 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel077:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightSeaGreen'
        self.current_speed = 0
        self.top_speed = 434 # feet per second
        self.acceleration_rate = 111 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel078:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightSkyBlue'
        self.current_speed = 0
        self.top_speed = 492 # feet per second
        self.acceleration_rate = 121 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel079:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightSlateGray'
        self.current_speed = 0
        self.top_speed = 428 # feet per second
        self.acceleration_rate = 124 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel080:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightSlateGrey'
        self.current_speed = 0
        self.top_speed = 467 # feet per second
        self.acceleration_rate = 114 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel081:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightSteelBlue'
        self.current_speed = 0
        self.top_speed = 445 # feet per second
        self.acceleration_rate = 126 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel082:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LightYellow'
        self.current_speed = 0
        self.top_speed = 405 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel083:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Lime'
        self.current_speed = 0
        self.top_speed = 448 # feet per second
        self.acceleration_rate = 111 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel084:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'LimeGreen'
        self.current_speed = 0
        self.top_speed = 497 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel085:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Linen'
        self.current_speed = 0
        self.top_speed = 416 # feet per second
        self.acceleration_rate = 114 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel086:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Magenta'
        self.current_speed = 0
        self.top_speed = 444 # feet per second
        self.acceleration_rate = 130 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel087:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Maroon'
        self.current_speed = 0
        self.top_speed = 442 # feet per second
        self.acceleration_rate = 116 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel088:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumAquaMarine'
        self.current_speed = 0
        self.top_speed = 435 # feet per second
        self.acceleration_rate = 130 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel089:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumBlue'
        self.current_speed = 0
        self.top_speed = 462 # feet per second
        self.acceleration_rate = 115 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel090:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumOrchid'
        self.current_speed = 0
        self.top_speed = 500 # feet per second
        self.acceleration_rate = 116 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel091:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumPurple'
        self.current_speed = 0
        self.top_speed = 480 # feet per second
        self.acceleration_rate = 128 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel092:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumSeaGreen'
        self.current_speed = 0
        self.top_speed = 437 # feet per second
        self.acceleration_rate = 121 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel093:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumSlateBlue'
        self.current_speed = 0
        self.top_speed = 481 # feet per second
        self.acceleration_rate = 112 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel094:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumSpringGreen'
        self.current_speed = 0
        self.top_speed = 418 # feet per second
        self.acceleration_rate = 127 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel095:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumTurquoise'
        self.current_speed = 0
        self.top_speed = 409 # feet per second
        self.acceleration_rate = 129 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel096:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MediumVioletRed'
        self.current_speed = 0
        self.top_speed = 483 # feet per second
        self.acceleration_rate = 106 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel097:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MidnightBlue'
        self.current_speed = 0
        self.top_speed = 406 # feet per second
        self.acceleration_rate = 114 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel098:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MintCream'
        self.current_speed = 0
        self.top_speed = 437 # feet per second
        self.acceleration_rate = 109 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel099:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'MistyRose'
        self.current_speed = 0
        self.top_speed = 460 # feet per second
        self.acceleration_rate = 100 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel100:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Moccasin'
        self.current_speed = 0
        self.top_speed = 465 # feet per second
        self.acceleration_rate = 111 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel101:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'NavajoWhite'
        self.current_speed = 0
        self.top_speed = 445 # feet per second
        self.acceleration_rate = 110 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel102:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Navy'
        self.current_speed = 0
        self.top_speed = 454 # feet per second
        self.acceleration_rate = 127 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel103:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'OldLace'
        self.current_speed = 0
        self.top_speed = 454 # feet per second
        self.acceleration_rate = 108 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel104:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Olive'
        self.current_speed = 0
        self.top_speed = 485 # feet per second
        self.acceleration_rate = 129 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel105:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'OliveDrab'
        self.current_speed = 0
        self.top_speed = 411 # feet per second
        self.acceleration_rate = 101 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel106:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Orange'
        self.current_speed = 0
        self.top_speed = 479 # feet per second
        self.acceleration_rate = 123 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel107:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'OrangeRed'
        self.current_speed = 0
        self.top_speed = 472 # feet per second
        self.acceleration_rate = 100 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel108:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Orchid'
        self.current_speed = 0
        self.top_speed = 473 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel109:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'PaleGoldenRod'
        self.current_speed = 0
        self.top_speed = 404 # feet per second
        self.acceleration_rate = 113 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel110:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'PaleGreen'
        self.current_speed = 0
        self.top_speed = 429 # feet per second
        self.acceleration_rate = 126 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel111:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'PaleTurquoise'
        self.current_speed = 0
        self.top_speed = 406 # feet per second
        self.acceleration_rate = 115 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel112:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'PaleVioletRed'
        self.current_speed = 0
        self.top_speed = 430 # feet per second
        self.acceleration_rate = 111 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel113:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'PapayaWhip'
        self.current_speed = 0
        self.top_speed = 475 # feet per second
        self.acceleration_rate = 123 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel114:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'PeachPuff'
        self.current_speed = 0
        self.top_speed = 401 # feet per second
        self.acceleration_rate = 103 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel115:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Peru'
        self.current_speed = 0
        self.top_speed = 438 # feet per second
        self.acceleration_rate = 113 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel116:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Pink'
        self.current_speed = 0
        self.top_speed = 409 # feet per second
        self.acceleration_rate = 106 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel117:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Plum'
        self.current_speed = 0
        self.top_speed = 497 # feet per second
        self.acceleration_rate = 122 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel118:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'PowderBlue'
        self.current_speed = 0
        self.top_speed = 469 # feet per second
        self.acceleration_rate = 103 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel119:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Purple'
        self.current_speed = 0
        self.top_speed = 412 # feet per second
        self.acceleration_rate = 119 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel120:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'RebeccaPurple'
        self.current_speed = 0
        self.top_speed = 408 # feet per second
        self.acceleration_rate = 101 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel121:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Red'
        self.current_speed = 0
        self.top_speed = 443 # feet per second
        self.acceleration_rate = 130 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel122:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'RosyBrown'
        self.current_speed = 0
        self.top_speed = 447 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel123:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'RoyalBlue'
        self.current_speed = 0
        self.top_speed = 485 # feet per second
        self.acceleration_rate = 101 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel124:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SaddleBrown'
        self.current_speed = 0
        self.top_speed = 428 # feet per second
        self.acceleration_rate = 106 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel125:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Salmon'
        self.current_speed = 0
        self.top_speed = 418 # feet per second
        self.acceleration_rate = 119 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel126:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SandyBrown'
        self.current_speed = 0
        self.top_speed = 494 # feet per second
        self.acceleration_rate = 102 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel127:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SeaGreen'
        self.current_speed = 0
        self.top_speed = 415 # feet per second
        self.acceleration_rate = 108 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel128:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SeaShell'
        self.current_speed = 0
        self.top_speed = 404 # feet per second
        self.acceleration_rate = 115 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel129:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Sienna'
        self.current_speed = 0
        self.top_speed = 444 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel130:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Silver'
        self.current_speed = 0
        self.top_speed = 411 # feet per second
        self.acceleration_rate = 118 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel131:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SkyBlue'
        self.current_speed = 0
        self.top_speed = 492 # feet per second
        self.acceleration_rate = 115 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel132:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SlateBlue'
        self.current_speed = 0
        self.top_speed = 489 # feet per second
        self.acceleration_rate = 104 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel133:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SlateGray'
        self.current_speed = 0
        self.top_speed = 423 # feet per second
        self.acceleration_rate = 110 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel134:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SlateGrey'
        self.current_speed = 0
        self.top_speed = 400 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel135:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Snow'
        self.current_speed = 0
        self.top_speed = 432 # feet per second
        self.acceleration_rate = 104 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel136:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SpringGreen'
        self.current_speed = 0
        self.top_speed = 424 # feet per second
        self.acceleration_rate = 112 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel137:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'SteelBlue'
        self.current_speed = 0
        self.top_speed = 417 # feet per second
        self.acceleration_rate = 124 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel138:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Tan'
        self.current_speed = 0
        self.top_speed = 493 # feet per second
        self.acceleration_rate = 125 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel139:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Teal'
        self.current_speed = 0
        self.top_speed = 425 # feet per second
        self.acceleration_rate = 102 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel140:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Thistle'
        self.current_speed = 0
        self.top_speed = 494 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel141:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Tomato'
        self.current_speed = 0
        self.top_speed = 402 # feet per second
        self.acceleration_rate = 128 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel142:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Turquoise'
        self.current_speed = 0
        self.top_speed = 418 # feet per second
        self.acceleration_rate = 113 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel143:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Violet'
        self.current_speed = 0
        self.top_speed = 437 # feet per second
        self.acceleration_rate = 101 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel144:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Wheat'
        self.current_speed = 0
        self.top_speed = 422 # feet per second
        self.acceleration_rate = 127 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel145:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'White'
        self.current_speed = 0
        self.top_speed = 402 # feet per second
        self.acceleration_rate = 116 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel146:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'WhiteSmoke'
        self.current_speed = 0
        self.top_speed = 467 # feet per second
        self.acceleration_rate = 105 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel147:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'Yellow'
        self.current_speed = 0
        self.top_speed = 437 # feet per second
        self.acceleration_rate = 109 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled


class CarModel148:
    # attributes of each car
    def __init__(self):
        self.paint_color = 'YellowGreen'
        self.current_speed = 0
        self.top_speed = 404 # feet per second
        self.acceleration_rate = 107 # feet per second
        self.distance_traveled = 0

    # move cars every fraction of a second
    def move(self):
        update_rate = 100 # fraction of a second
        if self.current_speed < self.top_speed:
            if (self.current_speed + self.acceleration_rate / update_rate) > self.top_speed:
                self.current_speed = self.top_speed
            else:
                self.current_speed += self.acceleration_rate / update_rate
        self.distance_traveled += self.current_speed / update_rate
    # report car color
    def color(self):
        return self.paint_color
    # report distance traveled
    def distance(self):
        return self.distance_traveled



# Generic PRNG class to generate random values in a predictable manner
# adapted from JavaScript algorithm:  https://gist.github.com/blixt/f17b47c62508be59987b
class Generic_PRNG:

    def __init__(self, seed):
        self.__seed = seed % 2147483647
        if (self.__seed <= 0):
            self.__seed += 2147483646
        self.next()

    # Returns a pseudo-random value between 1 and 2^32 - 2.
    def next(self):
        self.__seed = self.__seed * 16807 % 2147483647
        return self.__seed

    # Returns a pseudo-random floating point number in range [0, 1).
    def next_float(self):
        return (self.next() - 1) / 2147483646

    # Mirror the randint function in Python PRNG
    def randint(self, low, high):
        return int( self.next_float() * (high-low+1) + low )

    # Mirror the uniform function in Python PRNG
    def uniform(self, low, high):
        return self.next_float() * (high-low+1) + low

    # Mirror the choice function on Python PRNG
    def choice(self, seq):
        i = self.randint(0, len(seq)-1)
        return seq[i]


def generate_maze():

    prng = Generic_PRNG(12345)
    monsters = ['goblin', 'troll', 'gnoll', 'drake', 'hobgoblin', 'dragon', 'gnome', 'elf', 'orc']

    class Room:
        def __init__(self):
            self.gold = prng.randint(0,100)
            self.monster = prng.choice(monsters)
            self.north = None
            self.south = None
            self.east = None
            self.west = None
        def get_monster(self):
            return self.monster
        def get_gold(self):
            return self.gold

    room_a = Room()
    room_b = Room()
    room_c = Room()
    room_d = Room()
    room_e = Room()
    room_f = Room()
    room_g = Room()
    room_h = Room()
    room_i = Room()
    room_j = Room()
    room_k = Room()
    room_l = Room()
    room_m = Room()

    room_h.west = room_g
    room_g.east = room_h
    room_g.south = room_f
    room_f.north = room_g
    room_f.sound = room_a
    room_a.north = room_f
    room_a.east = room_b
    room_b.west = room_a
    room_b.east = room_c
    room_b.south = room_k
    room_k.north = room_b
    room_k.south = room_l
    room_l.north = room_k
    room_l.east = room_m
    room_c.west = room_b
    room_c.east = room_d
    room_d.west = room_c
    room_d.east = room_e
    room_d.north = room_i
    room_e.west = room_d
    room_i.south = room_d
    room_i.north = room_j
    room_j.south = room_i

    return room_c
