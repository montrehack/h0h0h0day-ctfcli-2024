###############################################################################
# Welcome message and initialization of the progressionNumber and checkWire 
# variables.

print(
"__________              .__                         \n"+
"\\______   \\ ____   ____ |  |   ____ _____    ____   \n"+
" |    |  _//  _ \\ /  _ \\|  | _/ __ \\\\__  \\  /    \\  \n"+
" |    |   (  <_> |  <_> )  |_\\  ___/ / __ \\|   |  \\ \n"+
" |______  /\\____/ \\____/|____/\\___  >____  /___|  / \n"+
"        \\/                        \\/     \\/     \\/  \n\n")

print(
" __      __                  .___           .__                     " +
".___\n" +
"/  \\    /  \\____   ____    __| _/___________|  | _____    ____    " +
"__| _/\n" +
"\\   \\/\\/   /  _ \\ /    \\  / __ |/ __ \\_  __ \\  | \\__  \\  / " +
"\\  / __ | \n" +
" \\        (  <_> )   |  \\/ /_/ \\  ___/|  | \\/  |__/ __ \\|   |  " +
"\\/ /_/ | \n" +
"  \\__/\\  / \\____/|___|  /\\____ |\\___  >__|  |____(____  /___|  " +
"/\\____ | \n" +
"       \\/             \\/      \\/    \\/                \\/     \\" +
"/      \\/ \n\n")

print("Welcome to Boolean Wonderland! I am struggling to solve some " 
+ "boolean circuits... I hope you can help me! Type \"help\" for more " + 
"information.\n")

progressionNumber=0
checkWire=0

###############################################################################
# Main function that prints the right output based on the command input of the
# user and the progressionNumber.

def printCommandOutput(commandInput, progressionNumber,checkWire):
    if commandInput=="help":
        if progressionNumber==0:
            print("Here is a list of commands you can use:\n")
            print("help: prints a description of the different commands you " 
            + "can use.")
            print("showCircuit1: prints the first boolean circuit to solve.")
            print("solveCircuit1 \"y0y1y2y3y4y5y6y7\": verifies if the " +
            "argument is the right output for the first circuit.\n")
        elif progressionNumber==1:
            print("Here is a list of commands you can use:\n")
            print("help: prints a description of the different commands you " 
            + "can use.")
            print("showCircuit1: prints the first boolean circuit to solve.")
            print("solveCircuit1 \"y0y1y2y3y4y5y6y7\": verifies if the " +
            "argument is the right output for the first circuit.")
            print("showCircuit2: prints the second boolean circuit to solve." +
            " With the right argument given to this command, " +
            "the wires should appear.")
            print("solveCircuit2 \"y0y1y2y3y4y5y6y7\": verifies if the " +
            "argument is the right output for the second circuit.\n")
        else:
            print("Here is a list of commands you can use:\n")
            print("help: prints a description of the different commands you " 
            + "can use.")
            print("showCircuit1: prints the first boolean circuit to solve.")
            print("solveCircuit1 \"y0y1y2y3y4y5y6y7\": verifies if the " +
            "argument is the right output for the first circuit.")
            print("showCircuit2: prints the second boolean circuit to solve." + 
            " With the right argument given to this command, " +
            "the wires should appear.")
            print("solveCircuit2 \"y0y1y2y3y4y5y6y7\": verifies if the " +
            "argument is the right output for the second circuit.")
            print("showCircuit3: prints the third boolean circuit to solve." +
            " With the right argument given to this command, " +
            "the wires should appear. You should take a look at this website" +
            ": https://open.kattis.com/problems/leapfrogencryption.")
            print("solveCircuit3 \"y0y1y2y3y4y5y6y7\": verifies if the " +
            "argument is the right output for the third circuit.\n")
        return progressionNumber,checkWire
    elif commandInput=="showCircuit1":
        for _ in firstCircuit:
            print(_)
        print()
        print("Here is the first circuit. Consider the inputs from top to " +
        "bottom to " + "be the following: x0x1x2x3x4x5x6x7 = 10011101. " +
        "With y0y1y2y3y4y5y6y7 being the " +
        "outputs from top to bottom, solve the circuit by calling " +
        "solveCircuit1 with the right " +
        "output as the argument.\n")
        return progressionNumber,checkWire
    elif commandInput[0:12] =="showCircuit2" and progressionNumber>=1:
        if commandInput[12:]=="":
            for _ in secondCircuitNoWires:
                print(_)
            print()
            print("Here is the second circuit to solve. I seem to have lost " +
            "the wires somehow... I'd try typing \"help\" if I were you!\n")
        elif commandInput[13:]=="cesarsalad":
            for _ in secondCircuit:
                print(_)
            print()
            print("I found the wires!\n\n")
            print("Here is the second circuit. Consider the inputs from top " +
            "to bottom to " +
            "be the following: x0x1x2x3x4x5x6x7 = 10111001. " +
            "With y0y1y2y3y4y5y6y7 being the " +
            "outputs from top to bottom, solve the circuit by calling " +
            "solveCircuit2 with the right " +
            "output as the argument.\n")
            if checkWire==0:
                checkWire=1
        else:
            for _ in secondCircuitNoWires:
                print(_)
            print()
            print("I couldn't find the wires... Try again!\n")
        return progressionNumber,checkWire
    elif commandInput[0:12] =="showCircuit3" and progressionNumber>=2:
        if commandInput[12:]=="":
            for _ in thirdCircuitNoWires:
                print(_)
            print()
            print("Here is the third circuit to solve. I seem to have lost " +
            "the wires again... I'd try typing \"help\" if I were you!\n")
        elif commandInput[13:]=="cbaiieglleoiolokn":
            for _ in thirdCircuit:
                print(_)
            print()
            print("I found the wires!\n\n")
            print("Here is the third circuit. Consider the inputs from top " +
            "to bottom to " +
            "be the following: x0x1x2x3x4x5x6x7 = 00111000. " +
            "With y0y1y2y3y4y5y6y7 being the " +
            "outputs from top to bottom, solve the circuit by calling " +
            "solveCircuit3 with the right " +
            "output as the argument.\n")
            if checkWire==1:
                checkWire=2
        else:
            for _ in thirdCircuitNoWires:
                print(_)
            print()
            print("I couldn't find the wires... Try again!\n")
        return progressionNumber,checkWire
    elif commandInput[0:13]=="solveCircuit1":
        if commandInput[14:]=="11000011":
            print("wymulmufux\n")
            for _ in lightningBolt:
                print(_)
            print()
            print("This is the right output! Type \"showCircuit2\" to show " +
            "the second circuit.\n")
            if progressionNumber==0:
                progressionNumber=1
        else:
            print("Wrong output, try again!\n")
        return progressionNumber,checkWire
    elif commandInput[0:13]=="solveCircuit2" and progressionNumber>=1:
        if checkWire>=1:
            if commandInput[14:]=="00110011":
                print("ilikebooleanlogic cesar\n")
                for _ in lightningBolt:
                    print(_)
                print()
                print("This is the right output! Type \"showCircuit3\" to " +
                "show the third circuit.\n")
                if progressionNumber==1:
                    progressionNumber=2
            else:
                print("Wrong output, try again!\n")
        else:
            print("How can you solve a circuit without wires? Help me find " +
            "the wires first!\n")
        return progressionNumber,checkWire
    elif commandInput[0:13]=="solveCircuit3" and progressionNumber>=2:
        if checkWire>=2:
            
            if commandInput[14:]=="00000001":
                for _ in lightningBolt:
                    print(_)
                print()
                print("This is the right output!\n")
                if progressionNumber==2:
                    progressionNumber=3
            else:
                print("Wrong output, try again!\n")
        else:
            print("How can you solve a circuit without wires? Help me find " +
            "the wires first!\n")
        return progressionNumber,checkWire
    else:
        print("This command isn't recognized.\n")
        return progressionNumber,checkWire
    
###############################################################################
# Circuits and images to print.
firstCircuit=[
".                                                                              .",
".        '.........                                                            .",
".        '         ...                                                         .",
".   ....''           .'                                                        .",
".        '            ..                   ........                            .",
".        '             ^.........'         .'      ....              .....     .",
".       .'            `           '.........`.         .'.           '         .",
".    ....'          .'                       `           ..         ..         .",
".        `...........                        `            `........'`          .",
".                                            `           '.         ..         .",
".                                 '.........^          .'            '         .",
".       .......                  ..        '`..........              '....     .",
".       `      .....             ..                                            .",
".   ....'`         .'.           ..                                            .",
".        `           .'          '.                                            .",
".        `            .'..........         .'..                                .",
".        `           .'                    ..  ....                 '....      .",
".   ....'`          '.                     ..      ....             `          .",
".       `      .....               ........`.          ..``''.....'`           .",
".       .......                   '        ..        .... ..       .'          .",
".                                ..        ..    ....               `          .",
".                                ..        ......                     ...      .",
".        `...........            ..         .                                  .",
".       .'          .'           ..                                            .",
".    ....'            `          ..                                            .",
".        '             ^........'`                                             .",
".        '            ..         `         .`...                   '..         .",
".   ....''           .'          ..        ..   ....              '            .",
".        '         ...           .'        ..       ....          '            .",
".        '.........               .........'.           '`^`......^            .",
".                                          ..       ....           '           .",
".       .                                  ..   ....               `           .",
".       `....                              .'...                   ....        .",
".       `    ....                                                              .",
".       `        ....  .                                                       .",
".   ....`           .`^.`........'                                             .",
".       `       ....             ..        .........                           .",
".       `   ....                 ..         '       ....          ...          .",
".       ^...                      ..........`.          '.        `            .",
".                                            `           .'       `            .",
".                                            `            `......`.            .",
".       `..                                  `           '.       `            .",
".       `  ....                   '.........\"          ..         `..          .",
".       `      ....              ..        ''..........                        .",
".   ....`          ...'.'........'                                             .",
".       `         .......                                                      .",
".       `     ....                                                             .",
".       ` ....                                                                 .",
".       '.                                                                     ."
]

secondCircuitNoWires=[
".                                                                              .",
".                                                                              .",
".     .                                                                        .",
".     `....                                                                    .",
".     `    ....                                                                .",
".     `        ....                                                            .",
". ....`            '`^'`...                                                    .",
".     `        ....   .                    `.........                          .",
".     `    ....                            ..        ..'              '.....   .",
".     `....                            .....^           .'            '        .",
".     '                                     ..            `          '.        .",
".                                            '            .`........``         .",
".     '.                                    '            ..          .'        .",
".     ` ....                           .....^          .'             '        .",
".     `     ....                           `       ....               '.....   .",
".     `         ....  .                    ........                            .",
". ....^            '`\".`...                                                    .",
".     `        ....                                                            .",
".     `    ....                            `.........                 ....     .",
".     `....                                ..        ...             `         .",
".     .                                .....^           .'          ..         .",
".                                           ..            `         `          .",
".                                            '            .`.......`'          .",
".      `...........                         '            ..         `          .",
".      `           .'                  .....^          .'           `          .",
". .....`             `                     `      .....              ....      .",
".      `              ^....                .......                             .",
".      `             .'                                                        .",
". .....`             `                                                         .",
".      `           ''                      .                                   .",
".      `...........                        `....                    '..        .",
".                                          `    ....               `           .",
".                                          `        ....           `           .",
".     ........                         ....^            .`\".`.....'`           .",
".     `       ....                         `         ....  .       '.          .",
". .....`          .'                       `     ....              .'          .",
".      `            ..                     ` ....                   '...       .",
".      `             ''....                ..                                  .",
".      `            .`                                                         .",
". .....`           '.                                                          .",
".     '         ...                                                            .",
".     '.........                            `...........                       .",
".                                           `           .'          ...        .",
".                                      .....`             `        `           .",
".     `..........                           `              ^.......`           .",
".     ..         .'.                        `              `      .'           .",
". .....`           .'                  .....`             `        `           .",
".      `             `                      `           .'         `..         .",
".      `             ''....                 `...........                       .",
". .....`            '.                                                         .",
".     .'         .'.                                                           .",
".     ^...........                                                             .",
".                                                                              .",
".                                                                              ."
]

secondCircuit=[
"'                                                                              .",
"'     ..                                                                       .",
"'     ` ....                                                                   .",
"'     `     ....                                                               .",
"'     `         ....  ..                                                       .",
"'  ...^            .'\".`..........                                             .",
"'     `        ....              `         .`..........                        .",
"'     `    ....                  `.         '.         .'             ......   .",
"'     `....                      `...........`           .'           `        .",
"'                                `           `             `         .`        .",
"'                                `           `             `.........''        .",
"'      `.                        .'..........`           .'           `        .",
"'     .' ....                               ..         .'.            `        .",
"'     .'     ....                          .^..........                '....   .",
"'     .'         .... ..                                                       .",
"'  ...''           ..`''.........'                                             .",
"'     .'       ....              `                                             .",
"'     .'   ....                  '         .`..........               ....     .",
"'     .^...                      .'         '.         .'            `         .",
"'                                  ..........`           .'          `         .",
"'                                            `             `        .'         .",
"'       .........                            `             `........'.         .",
"'      `         ....              ..........`           .'          `         .",
"'  ....\"            .'           .'         ..         .'.           `         .",
"'      `              `          `         .`..........               ....     .",
"'      `              `...........                                             .",
"'      `              `                                                        .",
"'  ....\"             '.                                                        .",
"'      `           .'                       '.                                 .",
"'      ............                         `.....                  '...       .",
"'                                           `    .....              `          .",
"'                                           `         ....  .       `          .",
"'     ..........                  ..........`            '`^'`.....`'          .",
"'      `        ....             '.         `        ....           `          .",
"'  ....''          .'            '          `    ....               `          .",
"'       `            '.          '          `....                    '..       .",
"'       `             ^..........\"          .                                  .",
"'       `            '           `                                             .",
"'  ....`.          ''            `.                                            .",
"'     .'       ....              `.                                            .",
"'     .........                  `.         .'............                     .",
"'                                '`.........'.           .'         ....       .",
"'                                '    `     ..             `        `          .",
"'     '`..........               '    `     ..             ''......'.          .",
"'      `          .'.            '    `     ..             `       '           .",
"'  .....`           .'           '    ......'.            .'       ..          .",
"'       `             `..........'          ..          .'.         `..        .",
"'       `            .'                      '..........                       .",
"'  .....`           '.                                                         .",
"'      `         ..'                                                           .",
"'     ''.........                                                              .",
"'                                                                              ."
]

thirdCircuitNoWires=[
"'                                                                                        '",
"'                                                                                        '",
"'                                                                                        '",
"'                                                      '..                               '",
"'                                                      `  ....                           '",
"'        `'..........                                  `      ....                       '",
"'         `          .'.                               `          .... ..                '",
"'    .....''           .'                          ....^            .'``''...            '",
"'          `             `                             `        .....                    '",
"'          `             `.....                        `    ....                         '",
"'          `            '                              `....                             '",
"'     ....\"           ''                               .                                 '",
"'        ''...........                                                                   '",
"'                                                                                        '",
"'                                                      ''...                             '",
"'                                                      '    ....                         '",
"'                                                      '        ....            `..      '",
"'                                                   ...^            ..'`.'.....'.        '",
"'         `............                                '           .......               '",
"'         `            ''                              '       ....                      '",
"'    .....^              `                             '   ....                          '",
"'         `              '.                            ''..                              '",
"'         `              .`....                                                          '",
"'         `              `                                                               '",
"'     ....^            .'                               ...........                      '",
"'         `.............                                `          ..'       '....       '",
"'                                                  .....^             '.     `           '",
"'                                                       `              `     `           '",
"'                                                       `              .`....\"....       '",
"'       .'..........                                    `              '     `           '",
"'        `         .''                             .....^             .'     `           '",
"'    .....`           .'                                `           .'.      '....       '",
"'         `             `                               '...........                     '",
"'         `             .`....                                                           '",
"'         `            .'                                                                '",
"'    ....`.          .'.                                '............                    '",
"'        '       ....                                   `            '.      ......      '",
"'       .........                                  .....^             .'     `           '",
"'                                                       `              '.    `           '",
"'                                                       `              .`....`           '",
"'        ...........                                    `              `     `           '",
"'        `          ..'                            .....^             '       .....      '",
"'    ....\"             ..                               `         ....                   '",
"'        `              ..                               .........                       '",
"'        `               ^....                                                           '",
"'        `              .'                                                               '",
"'    ....\"             .'                              `'..........                      '",
"'        `           .'.                                `          .'.                   '",
"'        ............                              ......'           .`                  '",
"'                                                        `             `                 '",
"'                                                        `             `...........      '",
"'                                                   .....'           .'                  '",
"'                                                       `          .'.                   '",
"'                                                      `'..........                      '",
"'                                                                                        '",
"'                                                                                        '"
]

thirdCircuit=[
"'                                                                                        '",
"'                                                                                        '",
"'                                                                                        '",
"'                                                       `..                              '",
"'                                                       `  ....                          '",
"'        .\"...........                                  `      ....                      '",
"'         .'          ''                                `          .... ..               '",
"'     .....^            '.          '...................`            .'\".`....           '",
"'          '.            .'         `                   `        ....                    '",
"'          '.            .`.........\"....`              `    ....                        '",
"'          `            .'          `    ..             `....                            '",
"'     .....`          .'            `    ..             .                                '",
"'        .,...........              `    ..                                              '",
"'                                   `    ..                                              '",
"'                                   `    ..             ^....                            '",
"'                                   `    ..             `    ....                        '",
"'                                   `    ..             `        ....           .'..     '",
"'                                   `   .``.............^            ..`'''.....`        '",
"'          ^............            ` '. ..    ..       `          .... ..               '",
"'          `            '.          ` `  ..    ..       `      ....                      '",
"'     .....`             '.         ` `  ..    ..       `  ....                          '",
"'          `              `        '. `  ..    ..       `..                              '",
"'          `              ^........   `  ..    ..                                        '",
"'     .....`             ..           `  ..    ..                                        '",
"'          `            '.            `  ..    ..        ...........                     '",
"'          ^............              `  .'    ..        `          .'.       `....      '",
"'                                     `   '....`'........`            .`     `           '",
"'                                     `        ..        `              `    `           '",
"'                                     `        ..        `              `....\".....      '",
"'        `..........                  `        .'        `              `    `           '",
"'        .'         .'.               `         '........`             '.    `           '",
"'    .....,            '.             `                  `           .'       '....      '",
"'          `            .'            `                  `...........                    '",
"'          `             `...........`....                                               '",
"'         ..            `                `                                               '",
"'    .....,           ''                 `               `...........                    '",
"'        `.       ....                   `               `           .'.      ......     '",
"'        .........                    '..\"...............`             '.    '.          '",
"'                                    `   `               `              `    `           '",
"'                                    `   `               `              `....\"           '",
"'         ...........                `   '.              `              `    '.          '",
"'         `          ...             `     .....^........`            .'      ......     '",
"'    .....^             `            `          `        `         ..'                   '",
"'         `              `           `          `        ..........                      '",
"'         `              `.......`....          `                                        '",
"'         `              `       `              `                                        '",
"'    .....^             '.       `              `       \"...........                     '",
"'         `           .'         .'             `       .'          ''                   '",
"'         '...........             .............\"........^            ''                 '",
"'                                               `        ..             `                '",
"'                                               `        ..             `...........     '",
"'                                               '........`            .'                 '",
"'                                                       .`          .'.                  '",
"'                                                       \"...........                     '",
"'                                                                                        '",
"'                                                                                        '"
]

lightningBolt=[
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                        .'..........'.                          ",
"                                       .,:::::::::::\".                          ",
"                                      .,:::::::::::^                            ",
"                                     .,:::::::::::`                             ",
"                                    .,::::::::::,'                              ",
"                                   .,::::::::::,.                               ",
"                                  ',::::::::::\".                                ",
"                                 ':::::::::::^                                  ",
"                                ':::::::::::`                                   ",
"                               '::::::::::,'                                    ",
"                              `::::::::::,.                                     ",
"                             `:::::::::::^```````                               ",
"                            `::::::::::::::::::`.                               ",
"                           ^:::::::::::::::::\".                                 ",
"                          .``````\":::::::::,`                                    ",
"                                 \"::::::::^.                                     ",
"                                ':::::::,'                                       ",
"                               .,:::::,`                                         ",
"                               ^:::::\".                                          ",
"                              '::::,'                                            ",
"                              ,:::`                                              ",
"                             ^::\".                                               ",
"                            ':,'                                                 ",
"                           .,^                                                   ",
"                           `.                                                    ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                ",
"                                                                                "
]

###############################################################################
# Cleans the end and the start of each line of the circuits so it is a dot.

for _ in range(len(firstCircuit)):
    firstCircuit[_]="."+firstCircuit[_][1:-1]+"."
for _ in range(len(secondCircuit)):
    secondCircuitNoWires[_]="."+secondCircuitNoWires[_][1:-1]+"."
for _ in range(len(secondCircuit)):
    secondCircuit[_]="."+secondCircuit[_][1:-1]+"."
for _ in range(len(thirdCircuitNoWires)):
    thirdCircuitNoWires[_]="."+thirdCircuitNoWires[_][1:-1]+"."
for _ in range(len(thirdCircuit)):
    thirdCircuit[_]="."+thirdCircuit[_][1:-1]+"."

###############################################################################
# Main loop of the program, takes the user's input and passes it to 
# printCommandOuput. If progressionNumber is at 3, the user solved the three
# circuits and the program prints the flag.

while True:        
    commandInput=input()
    print()
    progressionNumber,checkWire=printCommandOutput(commandInput,
    progressionNumber,checkWire)
    if progressionNumber==3:
        print("Congratulations! Here is a token of my appreciation for your " +
        "hard work: flag{Y0u_kNoW_8ool3An_a1G3Bra}")
        break
