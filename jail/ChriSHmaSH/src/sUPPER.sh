#!/bin/bash
export PATH=/usr/local/bin:/usr/bin:/usr/games:/bin/another_sh
export USER=$(whoami)
# Custom shell prompt loop
echo "WELCOME TO SANTA SHELL!"
while true; do
    # Display a custom prompt
    echo -n "Santa-shell> "

    # Read user input
    read command

    # Uppercase the input and execute the command
    uppercase_command=$(echo "$command" | tr '[:lower:]' '[:upper:]')

    if [[ "$command" =~ \$[0-9] ]]; then
        echo "No you don't touch that"
        continue
    fi

    # Execute the uppercased command
    /bin/sh -c "$uppercase_command" 
done