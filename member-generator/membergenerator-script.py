import random

male_first_names = ["David",
                    "John",
                    "Paul",
                    "Mark",
                    "James",
                    "Andrew",
                    "Scott",
                    "Steven",
                    "Robert",
                    "Stephen",
                    "William",
                    "Craig",
                    "Michael",
                    "Stuart",
                    "Christopher",
                    "Alan",
                    "Colin",
                    "Brian",
                    "Kevin",
                    "Gary",
                    "Richard",
                    "Derek",
                    "Martin",
                    "Thomas",
                    "Neil",
                    "Barry",
                    "Ian",
                    "Jason",
                    "Iain",
                    "Gordon",
                    "Alexander",
                    "Graeme",
                    "Peter",
                    "Darren",
                    "Graham",
                    "George",
                    "Kenneth",
                    "Allan",
                    "Simon",
                    "Douglas",
                    "Keith",
                    "Lee",
                    "Anthony",
                    "Grant",
                    "Ross",
                    "Jonathan",
                    "Gavin",
                    "Nicholas",
                    "Joseph",
                    "Stewart",
                    "Daniel",
                    "Edward",
                    "Matthew",
                    "Donald",
                    "Fraser",
                    "Garry",
                    "Malcolm",
                    "Charles",
                    "Duncan",
                    "Alistair",
                    "Raymond",
                    "Philip",
                    "Ronald",
                    "Ewan",
                    "Ryan",
                    "Francis",
                    "Bruce",
                    "Patrick",
                    "Alastair",
                    "Bryan",
                    "Marc",
                    "Jamie",
                    "Hugh",
                    "Euan",
                    "Gerard",
                    "Sean",
                    "Wayne",
                    "Adam",
                    "Calum",
                    "Alasdair",
                    "Robin",
                    "Greig",
                    "Angus",
                    "Russell",
                    "Cameron",
                    "Roderick",
                    "Norman",
                    "Murray",
                    "Gareth",
                    "Dean",
                    "Eric",
                    "Adrian",
                    "Gregor",
                    "Samuel",
                    "Gerald",
                    "Henry",
                    "Justin",
                    "Benjamin",
                    "Shaun",
                    "Callum",
                    "Campbell",
                    "Frank",
                    "Roy",
                    "Timothy",
                    "Glen",
                    "Marcus",
                    "Hamish",
                    "Niall",
                    "Barrie",
                    "Liam",
                    "Brendan",
                    "Terence",
                    "Greg",
                    "Leslie",
                    "Lindsay",
                    "Trevor",
                    "Vincent",
                    "Christian",
                    "Lewis",
                    "Rory",
                    "Antony",
                    "Fergus",
                    "Roger",
                    "Arthur",
                    "Dominic",
                    "Ewen",
                    "Jon",
                    "Owen",
                    "Gregory",
                    "Jeffrey",
                    "Terry",
                    "Damian",
                    "Geoffrey",
                    "Harry",
                    "Walter",
                    "Bernard",
                    "Desmond",
                    "Jack",
                    "Aaron",
                    "Archibald",
                    "Blair",
                    "Jeremy",
                    "Nathan",
                    "Alister",
                    "Dale",
                    "Dylan",
                    "Glenn",
                    "Julian",
                    "Leon",
                    "Allen",
                    "Martyn",
                    "Nigel",
                    "Alisdair",
                    "Denis",
                    "Drew",
                    "Evan",
                    "Phillip",
                    "Frazer",
                    "Guy",
                    "Laurence",
                    "Lawrence",
                    "Magnus",
                    "Crawford",
                    "Finlay",
                    "Frederick",
                    "Gregg",
                    "Karl",
                    "Kerr",
                    "Mohammed",
                    "Rodney",
                    "Victor",
                    "Carl",
                    "Daryl",
                    "Don",
                    "Edwin",
                    "Erik",
                    "Grahame",
                    "Ivan",
                    "Kyle",
                    "Leigh",
                    "Lorne",
                    "Maurice",
                    "Murdo",
                    "Nicolas",
                    "Steve",
                    "Allister",
                    "Clark",
                    "Darran",
                    "Dennis",
                    "Elliot",
                    "Leonard",
                    "Nairn",
                    "Scot",
                    "Stefan",
                    "Toby",
                    "Warren",
                    "Billy",
                    "Clive",
                    "Damien",
                    "Louis",
                    "Mohammad",
                    "Neill",
                    "Noel",
                    "Ralph",
                    "Sandy",
                    "Albert",
                    "Alun",
                    "Brett",
                    "Clifford",
                    "Eoin",
                    "Glyn",
                    "Imran",
                    "Ivor",
                    "Johnathan",
                    "Kevan",
                    "Neal",
                    "Oliver",
                    "Robbie",
                    "Roland",
                    "Stanley",
                    "Aidan",
                    "Antonio",
                    "Austin",
                    "Bradley",
                    "Cornelius",
                    "Darrin",
                    "Derrick",
                    "Innes",
                    "Kristian",
                    "Lachlan",
                    "Mathew",
                    "Moray",
                    "Nicol",
                    "Shane",
                    "Tony",
                    "Brent",
                    "Findlay",
                    "Forbes",
                    "Gilbert",
                    "Giles",
                    "Jay",
                    "Kelvin",
                    "Leighton",
                    "Marco",
                    "Omar",
                    "Roddy",
                    "Tom",
                    "Abdul",
                    "Alfred",
                    "Alick",
                    "Ashley",
                    "Bryce",
                    "Conrad",
                    "Darryl",
                    "Eugene",
                    "Harold",
                    "Harvey",
                    "Hector",
                    "Jody",
                    "Kieran",
                    "Kirk",
                    "Kris",
                    "Marshall",
                    "Muhammad",
                    "Ramsay",
                    "Ray",
                    "Rodger",
                    "Seumas",
                    "Tommy",
                    "Wai",
                    "Alex",
                    "Ali",
                    "Andrea",
                    "Archie",
                    "Daren",
                    "Derick",
                    "Gideon",
                    "Jan",
                    "Juan",
                    "Kerry",
                    "Kieron",
                    "Luke",
                    "Lyall",
                    "Manus",
                    "Marvin",
                    "Morgan",
                    "Muir",
                    "Myles",
                    "Ronnie",
                    "Rowan",
                    "Rupert",
                    "Spencer",
                    "Stephan",
                    "Struan",
                    "Torquil",
                    "Wallace",
                    "Aftab",
                    "Alain",
                    "Alec",
                    "Alvin",
                    "Anton",
                    "Arran",
                    "Arron",
                    "Austen",
                    "Aynsley",
                    "Benedict",
                    "Chad",
                    "Chun",
                    "Clarke",
                    "Damon",
                    "Danny",
                    "Darron",
                    "Declan",
                    "Deryck",
                    "Edmond",
                    "Edmund",
                    "Jacob",
                    "Johnston",
                    "Keiron",
                    "Kennedy",
                    "Khalil",
                    "Kristofer",
                    "Laurie",
                    "Lloyd",
                    "Mario",
                    "Max",
                    "Maxwell",
                    "Mitchell",
                    "Morris",
                    "Nathaniel",
                    "Naveed",
                    "Neville",
                    "Nickolas",
                    "Piers",
                    "Quentin",
                    "Rennie",
                    "Reuben",
                    "Riccardo",
                    "Roberto",
                    "Ruaraidh",
                    "Ruaridh",
                    "Stefano",
                    "Symon",
                    "Tobias",
                    "Todd",
                    "Abid",
                    "Adnan",
                    "Aeneas",
                    "Aiden",
                    "Ainslie",
                    "Ajay",
                    "Alessandro",
                    "Alyn",
                    "Anderson",
                    "Andre",
                    "Ashok",
                    "Asif",
                    "Atholl",
                    "Bjorn",
                    "Brandon",
                    "Brydon",
                    "Bryn",
                    "Caine",
                    "Calvin",
                    "Carlo",
                    "Ceri",
                    "Chris",
                    "Christien",
                    "Claudio",
                    "Clayton",
                    "Clint",
                    "Connell",
                    "Cyril",
                    "Damion",
                    "Darin",
                    "Dario",
                    "Darroch",
                    "Deryk",
                    "Dirk",
                    "Donovan",
                    "Dustin",
                    "Eamonn",
                    "Edgar",
                    "Elliott",
                    "Elton",
                    "Emlyn",
                    "Eoghan",
                    "Erlend",
                    "Farooq",
                    "Garth",
                    "Geoff",
                    "Gerrard",
                    "Gerry",
                    "Giancarlo",
                    "Gidon",
                    "Grierson",
                    "Hamilton",
                    "Hans",
                    "Hendry"]
female_first_names = ["Nicola",
                      "Karen",
                      "Fiona",
                      "Susan",
                      "Claire",
                      "Sharon",
                      "Angela",
                      "Gillian",
                      "Julie",
                      "Michelle",
                      "Jacqueline",
                      "Amanda",
                      "Tracy",
                      "Louise",
                      "Jennifer",
                      "Alison",
                      "Sarah",
                      "Donna",
                      "Caroline",
                      "Elaine",
                      "Lynn",
                      "Margaret",
                      "Elizabeth",
                      "Lesley",
                      "Deborah",
                      "Pauline",
                      "Lorraine",
                      "Laura",
                      "Lisa",
                      "Tracey",
                      "Carol",
                      "Linda",
                      "Lorna",
                      "Catherine",
                      "Wendy",
                      "Lynne",
                      "Yvonne",
                      "Pamela",
                      "Kirsty",
                      "Jane",
                      "Emma",
                      "Joanne",
                      "Heather",
                      "Suzanne",
                      "Anne",
                      "Diane",
                      "Helen",
                      "Victoria",
                      "Dawn",
                      "Mary",
                      "Samantha",
                      "Marie",
                      "Kerry",
                      "Ann",
                      "Hazel",
                      "Christine",
                      "Gail",
                      "Andrea",
                      "Clare",
                      "Sandra",
                      "Shona",
                      "Kathleen",
                      "Paula",
                      "Shirley",
                      "Denise",
                      "Melanie",
                      "Patricia",
                      "Audrey",
                      "Ruth",
                      "Jill",
                      "Lee",
                      "Leigh",
                      "Catriona",
                      "Rachel",
                      "Morag",
                      "Kirsten",
                      "Kirsteen",
                      "Katrina",
                      "Joanna",
                      "Lynsey",
                      "Cheryl",
                      "Debbie",
                      "Maureen",
                      "Janet",
                      "Aileen",
                      "Arlene",
                      "Zoe",
                      "Lindsay",
                      "Stephanie",
                      "Judith",
                      "Mandy",
                      "Jillian",
                      "Mhairi",
                      "Barbara",
                      "Carolyn",
                      "Gayle",
                      "Maria",
                      "Valerie",
                      "Christina",
                      "Marion",
                      "Frances",
                      "Michele",
                      "Lynda",
                      "Eileen",
                      "Janice",
                      "Kathryn",
                      "Kim",
                      "Allison",
                      "Julia",
                      "Alexandra",
                      "Mairi",
                      "Irene",
                      "Rhona",
                      "Carole",
                      "Katherine",
                      "Kelly",
                      "Nichola",
                      "Anna",
                      "Jean",
                      "Lucy",
                      "Rebecca",
                      "Sally",
                      "Teresa",
                      "Adele",
                      "Lindsey",
                      "Natalie",
                      "Sara",
                      "Lyn",
                      "Ashley",
                      "Brenda",
                      "Moira",
                      "Rosemary",
                      "Dianne",
                      "Kay",
                      "Eleanor",
                      "June",
                      "Geraldine",
                      "Marianne",
                      "Beverley",
                      "Evelyn",
                      "Leanne",
                      "Kirstie",
                      "Theresa",
                      "Agnes",
                      "Charlotte",
                      "Joan",
                      "Sheila",
                      "Clair",
                      "Hilary",
                      "Jayne",
                      "Sonia",
                      "Vivienne",
                      "Carla",
                      "Ellen",
                      "Emily",
                      "Morven",
                      "Debra",
                      "Janette",
                      "Gaynor",
                      "Rachael",
                      "Veronica",
                      "Vicky",
                      "Colette",
                      "Lyndsay",
                      "Maxine",
                      "Nicole",
                      "Sonya",
                      "Susanne",
                      "Alice",
                      "Georgina",
                      "Sheena",
                      "Leona",
                      "Tanya",
                      "Annette",
                      "Joyce",
                      "Ailsa",
                      "Avril",
                      "Iona",
                      "Isobel",
                      "Josephine",
                      "Kimberley",
                      "Sylvia",
                      "Lara",
                      "Linzi",
                      "Siobhan",
                      "Vanessa",
                      "Bernadette",
                      "Natasha",
                      "Monica",
                      "Esther",
                      "Hayley",
                      "Isabella",
                      "Rose",
                      "Roslyn",
                      "Tara",
                      "Adrienne",
                      "Carrie",
                      "Isabel",
                      "Jan",
                      "Janine",
                      "Justine",
                      "Kirstin",
                      "Norma",
                      "Rona",
                      "Shelley",
                      "Anne-Marie",
                      "Cara",
                      "Eilidh",
                      "Grace",
                      "Gwen",
                      "Isla",
                      "Vikki",
                      "Deirdre",
                      "Elspeth",
                      "Faye",
                      "Joy",
                      "Kara",
                      "Louisa",
                      "Naomi",
                      "Rosalind",
                      "Vicki",
                      "Amy",
                      "Hannah",
                      "Heidi",
                      "Leah",
                      "Lee-Ann",
                      "Lyndsey",
                      "Rhonda",
                      "Anita",
                      "Annie",
                      "April",
                      "Charmaine",
                      "Dorothy",
                      "Lynsay",
                      "Nadine",
                      "Penny",
                      "Sharron",
                      "Stacey",
                      "Charlene",
                      "Collette",
                      "Corinne",
                      "Kate",
                      "Katharine",
                      "Kerri",
                      "Kerrie",
                      "Linsey",
                      "Marjorie",
                      "Melissa",
                      "Helena",
                      "Jeanette",
                      "Marlene",
                      "Miranda",
                      "Roseann",
                      "Alana",
                      "Anthea",
                      "Morna",
                      "Andrina",
                      "Carol-Ann",
                      "Doreen",
                      "Juliet",
                      "Lauren",
                      "Nina",
                      "Nyree",
                      "Sarah-Jane",
                      "Sharlene",
                      "Simone",
                      "Beverly",
                      "Cindy",
                      "Diana",
                      "Dionne",
                      "Jacquelyn",
                      "Jenny",
                      "Johanne",
                      "Margo",
                      "Marina",
                      "Nancy",
                      "Trudy",
                      "Vivien",
                      "Wilma",
                      "Abigail",
                      "Alexis",
                      "Alyson",
                      "Angie",
                      "Ann-Marie",
                      "Annmarie",
                      "Belinda",
                      "Carolann",
                      "Carolanne",
                      "Eva",
                      "Eve",
                      "Glenda",
                      "Johanna",
                      "Karin",
                      "Kellie",
                      "Loraine",
                      "Lynette",
                      "Nadia",
                      "Penelope",
                      "Roberta",
                      "Tina",
                      "Gael",
                      "Gina",
                      "Ingrid",
                      "Lea",
                      "Marjory",
                      "Miriam",
                      "Philippa",
                      "Senga",
                      "Shonagh",
                      "Sophie",
                      "Catrina",
                      "Claudine",
                      "Constance",
                      "Edith",
                      "Erica",
                      "Katriona",
                      "Keli",
                      "Keri",
                      "Kristina",
                      "Laurie",
                      "Lucinda",
                      "Mari",
                      "Marlyn",
                      "Olivia",
                      "Paulene",
                      "Selina",
                      "Seonaid",
                      "Vivian",
                      "Williamina",
                      "Alexandria",
                      "Angeline",
                      "Antonia",
                      "Bridget",
                      "Candice",
                      "Carolyne",
                      "Cherie",
                      "Colleen",
                      "Connie",
                      "Daniella",
                      "Francesca",
                      "Gwendoline",
                      "Jessie",
                      "Jocelyn",
                      "Judy",
                      "Karina",
                      "Kaye",
                      "Kimberly",
                      "Lee-Anne",
                      "Lillian",
                      "Marian",
                      "Martha",
                      "May",
                      "Roisin",
                      "Shelagh",
                      "Sophia",
                      "Susanna",
                      "Aimee",
                      "Amanda-Jane",
                      "Amber",
                      "Beth",
                      "Caren",
                      "Claudia",
                      "Corrine",
                      "Euphemia",
                      "Jessica",
                      "Katie",
                      "Leeanne",
                      "Leila",
                      "Lilian",
                      "Liza",
                      "Madeleine",
                      "Marcia",
                      "Maree",
                      "Marilyn",
                      "Marisa",
                      "Myra",
                      "Olga",
                      "Sasha",
                      "Sharleen",
                      "Sian",
                      "Sonja",
                      "Tammy",
                      "Tania",
                      "Teri",
                      "Tessa",
                      "Toni",
                      "Tricia",
                      "Yasmin",
                      "Alexa",
                      "Amelia",
                      "Andrena",
                      "Annabel",
                      "Annemarie",
                      "Arleen",
                      "Carmen",
                      "Cecilia",
                      "Chloe",
                      "Corrie",
                      "Dana"]
last_names = ["SMITH",
              "JOHNSON",
              "WILLIAMS",
              "BROWN",
              "JONES",
              "GARCIA",
              "MILLER",
              "DAVIS",
              "RODRIGUEZ",
              "MARTINEZ",
              "HERNANDEZ",
              "LOPEZ",
              "GONZALEZ",
              "WILSON",
              "ANDERSON",
              "THOMAS",
              "TAYLOR",
              "MOORE",
              "JACKSON",
              "MARTIN",
              "LEE",
              "PEREZ",
              "THOMPSON",
              "WHITE",
              "HARRIS",
              "SANCHEZ",
              "CLARK",
              "RAMIREZ",
              "LEWIS",
              "ROBINSON",
              "WALKER",
              "YOUNG",
              "ALLEN",
              "KING",
              "WRIGHT",
              "SCOTT",
              "TORRES",
              "NGUYEN",
              "HILL",
              "FLORES",
              "GREEN",
              "ADAMS",
              "NELSON",
              "BAKER",
              "HALL",
              "RIVERA",
              "CAMPBELL",
              "MITCHELL",
              "CARTER",
              "ROBERTS",
              "GOMEZ",
              "PHILLIPS",
              "EVANS",
              "TURNER",
              "DIAZ",
              "PARKER",
              "CRUZ",
              "EDWARDS",
              "COLLINS",
              "REYES",
              "STEWART",
              "MORRIS",
              "MORALES",
              "MURPHY",
              "COOK",
              "ROGERS",
              "GUTIERREZ",
              "ORTIZ",
              "MORGAN",
              "COOPER",
              "PETERSON",
              "BAILEY",
              "REED",
              "KELLY",
              "HOWARD",
              "RAMOS",
              "KIM",
              "COX",
              "WARD",
              "RICHARDSON",
              "WATSON",
              "BROOKS",
              "CHAVEZ",
              "WOOD",
              "JAMES",
              "BENNETT",
              "GRAY",
              "MENDOZA",
              "RUIZ",
              "HUGHES",
              "PRICE",
              "ALVAREZ",
              "CASTILLO",
              "SANDERS",
              "PATEL",
              "MYERS",
              "LONG",
              "ROSS",
              "FOSTER",
              "JIMENEZ",
              "POWELL",
              "JENKINS",
              "PERRY",
              "RUSSELL",
              "SULLIVAN",
              "BELL",
              "COLEMAN",
              "BUTLER",
              "HENDERSON",
              "BARNES",
              "GONZALES",
              "FISHER",
              "VASQUEZ",
              "SIMMONS",
              "ROMERO",
              "JORDAN",
              "PATTERSON",
              "ALEXANDER",
              "HAMILTON",
              "GRAHAM",
              "REYNOLDS",
              "GRIFFIN",
              "WALLACE",
              "MORENO",
              "WEST",
              "COLE",
              "HAYES",
              "BRYANT",
              "HERRERA",
              "GIBSON",
              "ELLIS",
              "TRAN",
              "MEDINA",
              "AGUILAR",
              "STEVENS",
              "MURRAY",
              "FORD",
              "CASTRO",
              "MARSHALL",
              "OWENS",
              "HARRISON",
              "FERNANDEZ",
              "MCDONALD",
              "WOODS",
              "WASHINGTON",
              "KENNEDY",
              "WELLS",
              "VARGAS",
              "HENRY",
              "CHEN",
              "FREEMAN",
              "WEBB",
              "TUCKER",
              "GUZMAN",
              "BURNS",
              "CRAWFORD",
              "OLSON",
              "SIMPSON",
              "PORTER",
              "HUNTER",
              "GORDON",
              "MENDEZ",
              "SILVA",
              "SHAW",
              "SNYDER",
              "MASON",
              "DIXON",
              "MUNOZ",
              "HUNT",
              "HICKS",
              "HOLMES",
              "PALMER",
              "WAGNER",
              "BLACK",
              "ROBERTSON",
              "BOYD",
              "ROSE",
              "STONE",
              "SALAZAR",
              "FOX",
              "WARREN",
              "MILLS",
              "MEYER",
              "RICE",
              "SCHMIDT",
              "GARZA",
              "DANIELS",
              "FERGUSON",
              "NICHOLS",
              "STEPHENS",
              "SOTO",
              "WEAVER",
              "RYAN",
              "GARDNER",
              "PAYNE",
              "GRANT",
              "DUNN",
              "KELLEY",
              "SPENCER",
              "HAWKINS",
              "ARNOLD",
              "PIERCE",
              "VAZQUEZ",
              "HANSEN",
              "PETERS",
              "SANTOS",
              "HART",
              "BRADLEY",
              "KNIGHT",
              "ELLIOTT",
              "CUNNINGHAM",
              "DUNCAN",
              "ARMSTRONG",
              "HUDSON",
              "CARROLL",
              "LANE",
              "RILEY",
              "ANDREWS",
              "ALVARADO",
              "RAY",
              "DELGADO",
              "BERRY",
              "PERKINS",
              "HOFFMAN",
              "JOHNSTON",
              "MATTHEWS",
              "PENA",
              "RICHARDS",
              "CONTRERAS",
              "WILLIS",
              "CARPENTER",
              "LAWRENCE",
              "SANDOVAL",
              "GUERRERO",
              "GEORGE",
              "CHAPMAN",
              "RIOS",
              "ESTRADA",
              "ORTEGA",
              "WATKINS",
              "GREENE",
              "NUNEZ",
              "WHEELER",
              "VALDEZ",
              "HARPER",
              "BURKE",
              "LARSON",
              "SANTIAGO",
              "MALDONADO",
              "MORRISON",
              "FRANKLIN",
              "CARLSON",
              "AUSTIN",
              "DOMINGUEZ",
              "CARR",
              "LAWSON",
              "JACOBS",
              "OBRIEN",
              "LYNCH",
              "SINGH",
              "VEGA",
              "BISHOP",
              "MONTGOMERY",
              "OLIVER",
              "JENSEN",
              "HARVEY",
              "WILLIAMSON",
              "GILBERT",
              "DEAN",
              "SIMS",
              "ESPINOZA",
              "HOWELL",
              "LI",
              "WONG",
              "REID",
              "HANSON",
              "LE",
              "MCCOY",
              "GARRETT",
              "BURTON",
              "FULLER",
              "WANG",
              "WEBER",
              "WELCH",
              "ROJAS",
              "LUCAS",
              "MARQUEZ",
              "FIELDS",
              "PARK",
              "YANG",
              "LITTLE",
              "BANKS",
              "PADILLA",
              "DAY",
              "WALSH",
              "BOWMAN",
              "SCHULTZ",
              "LUNA",
              "FOWLER",
              "MEJIA",
              "DAVIDSON",
              "ACOSTA",
              "BREWER",
              "MAY",
              "HOLLAND",
              "JUAREZ",
              "NEWMAN",
              "PEARSON",
              "CURTIS",
              "CORTEZ",
              "DOUGLAS",
              "SCHNEIDER",
              "JOSEPH",
              "BARRETT",
              "NAVARRO",
              "FIGUEROA",
              "KELLER",
              "AVILA",
              "WADE",
              "MOLINA",
              "STANLEY",
              "HOPKINS",
              "CAMPOS",
              "BARNETT",
              "BATES",
              "CHAMBERS",
              "CALDWELL",
              "BECK",
              "LAMBERT",
              "MIRANDA",
              "BYRD",
              "CRAIG",
              "AYALA",
              "LOWE",
              "FRAZIER",
              "POWERS",
              "NEAL",
              "LEONARD",
              "GREGORY",
              "CARRILLO",
              "SUTTON",
              "FLEMING",
              "RHODES",
              "SHELTON",
              "SCHWARTZ",
              "NORRIS",
              "JENNINGS",
              "WATTS",
              "DURAN",
              "WALTERS",
              "COHEN",
              "MCDANIEL",
              "MORAN",
              "PARKS",
              "STEELE",
              "VAUGHN",
              "BECKER",
              "HOLT",
              "DELEON",
              "BARKER",
              "TERRY",
              "HALE",
              "LEON",
              "HAIL",
              "BENSON",
              "HAYNES",
              "HORTON",
              "MILES",
              "LYONS",
              "PHAM",
              "GRAVES",
              "BUSH",
              "THORNTON",
              "WOLFE",
              "WARNER",
              "CABRERA",
              "MCKINNEY",
              "MANN",
              "ZIMMERMAN",
              "DAWSON",
              "LARA",
              "FLETCHER",
              "PAGE",
              "MCCARTHY",
              "LOVE",
              "ROBLES",
              "CERVANTES",
              "SOLIS",
              "ERICKSON",
              "REEVES",
              "CHANG",
              "KLEIN",
              "SALINAS",
              "FUENTES",
              "BALDWIN",
              "DANIEL",
              "SIMON",
              "VELASQUEZ",
              "HARDY",
              "HIGGINS",
              "AGUIRRE",
              "LIN",
              "CUMMINGS",
              "CHANDLER",
              "SHARP",
              "BARBER",
              "BOWEN",
              "OCHOA",
              "DENNIS",
              "ROBBINS",
              "LIU",
              "RAMSEY",
              "FRANCIS",
              "GRIFFITH",
              "PAUL",
              "BLAIR",
              "OCONNOR",
              "CARDENAS",
              "PACHECO",
              "CROSS",
              "CALDERON",
              "QUINN",
              "MOSS",
              "SWANSON",
              "CHAN",
              "RIVAS",
              "KHAN",
              "RODGERS",
              "SERRANO",
              "FITZGERALD",
              "ROSALES",
              "STEVENSON",
              "CHRISTENSEN",
              "MANNING",
              "GILL",
              "CURRY",
              "MCLAUGHLIN",
              "HARMON",
              "MCGEE",
              "GROSS",
              "DOYLE",
              "GARNER",
              "NEWTON",
              "BURGESS",
              "REESE",
              "WALTON",
              "BLAKE",
              "TRUJILLO",
              "ADKINS",
              "BRADY",
              "GOODMAN",
              "ROMAN",
              "WEBSTER",
              "GOODWIN",
              "FISCHER",
              "HUANG",
              "POTTER",
              "DELACRUZ",
              "MONTOYA",
              "TODD",
              "WU",
              "HINES",
              "MULLINS",
              "CASTANEDA",
              "MALONE",
              "CANNON",
              "TATE",
              "MACK",
              "SHERMAN",
              "HUBBARD",
              "HODGES",
              "ZHANG",
              "GUERRA",
              "WOLF",
              "VALENCIA",
              "SAUNDERS",
              "FRANCO",
              "ROWE",
              "GALLAGHER",
              "FARMER",
              "HAMMOND",
              "HAMPTON",
              "TOWNSEND",
              "INGRAM",
              "WISE",
              "GALLEGOS",
              "CLARKE",
              "BARTON",
              "SCHROEDER",
              "MAXWELL",
              "WATERS",
              "LOGAN",
              "CAMACHO",
              "STRICKLAND",
              "NORMAN",
              "PERSON",
              "COLON",
              "PARSONS",
              "FRANK",
              "HARRINGTON",
              "GLOVER",
              "OSBORNE",
              "BUCHANAN",
              "CASEY",
              "FLOYD",
              "PATTON",
              "IBARRA",
              "BALL",
              "TYLER",
              "SUAREZ",
              "BOWERS",
              "OROZCO",
              "SALAS",
              "COBB",
              "GIBBS",
              "ANDRADE",
              "BAUER",
              "CONNER",
              "MOODY",
              "ESCOBAR",
              "MCGUIRE",
              "LLOYD",
              "MUELLER",
              "HARTMAN",
              "FRENCH",
              "KRAMER",
              "MCBRIDE",
              "POPE",
              "LINDSEY",
              "VELAZQUEZ",
              "NORTON",
              "MCCORMICK",
              "SPARKS",
              "FLYNN",
              "YATES",
              "HOGAN",
              "MARSH",
              "MACIAS",
              "VILLANUEVA",
              "ZAMORA",
              "PRATT",
              "STOKES",
              "OWEN",
              "BALLARD",
              "LANG",
              "BROCK",
              "VILLARREAL",
              "CHARLES",
              "DRAKE",
              "BARRERA",
              "CAIN",
              "PATRICK",
              "PINEDA",
              "BURNETT",
              "MERCADO",
              "SANTANA",
              "SHEPHERD",
              "BAUTISTA",
              "ALI",
              "SHAFFER",
              "LAMB",
              "TREVINO",
              "MCKENZIE",
              "HESS",
              "BEIL",
              "OLSEN",
              "COCHRAN",
              "MORTON",
              "NASH",
              "WILKINS",
              "PETERSEN",
              "BRIGGS",
              "SHAH",
              "ROTH",
              "NICHOLSON",
              "HOLLOWAY",
              "LOZANO",
              "RANGEL",
              "FLOWERS",
              "HOOVER",
              "SHORT",
              "ARIAS",
              "MORA",
              "VALENZUELA",
              "BRYAN",
              "MEYERS",
              "WEISS",
              "UNDERWOOD",
              "BASS",
              "GREER",
              "SUMMERS",
              "HOUSTON",
              "CARSON",
              "MORROW",
              "CLAYTON",
              "WHITAKER",
              "DECKER",
              "YODER",
              "COLLIER"]

counter_males=0
new_list_males = []
while(counter_males<100):
    first_name = random.choice(male_first_names)
    last_name = random.choice(last_names)
    last_name_lower = last_name.lower()
    last_name_capitalized = last_name_lower.capitalize()
    name = first_name + " " + last_name_capitalized
    new_list_males.append(name)
    counter_males=counter_males+1

counter_females=0
new_list_females = []
while(counter_females<100):
    first_name = random.choice(female_first_names)
    last_name = random.choice(last_names)
    last_name_lower = last_name.lower()
    last_name_capitalized = last_name_lower.capitalize()
    name = first_name + " " + last_name_capitalized
    new_list_females.append(name)
    counter_females=counter_females+1

print(new_list_males)
print(new_list_females)