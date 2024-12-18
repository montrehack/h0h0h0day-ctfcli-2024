# README

## CTFd / CTFCli Automation

To generate ctfcli commands to add all challenges to a CTFd instance :

    find . -mindepth 2 -maxdepth 2 | grep -v "./venv"| grep -v "./.ctf/" | awk '{print substr($1,3); }' | sed -e "s/^/python -m ctfcli challenge add /"

    python -m ctfcli challenge add jail/ChriSHmaSH
    python -m ctfcli challenge add forensics/atos-eviden-montrehack
    python -m ctfcli challenge add forensics/DZ_Ghostware
    python -m ctfcli challenge add forensics/irs_little_helper
    python -m ctfcli challenge add forensics/exfiltration_pro_max
    python -m ctfcli challenge add forensics/repas_de_noel
    python -m ctfcli challenge add crypto/9x9_cipher_machine
    python -m ctfcli challenge add crypto/booleanWonderland
    python -m ctfcli challenge add crypto/A_needle_in_a_christmas_log
    python -m ctfcli challenge add steg/santas_text
    python -m ctfcli challenge add steg/dialing_to_merry_festivities
    python -m ctfcli challenge add reverse/unlock_some_binary
    python -m ctfcli challenge add reverse/la_gare_pole_nord
    python -m ctfcli challenge add misc/visa_or_mastercard
    python -m ctfcli challenge add misc/gift_delivery
    python -m ctfcli challenge add pwn/sleigh_ride
    python -m ctfcli challenge add pwn/gift_wrapper
    python -m ctfcli challenge add osint/osint-5
    python -m ctfcli challenge add osint/osint-4
    python -m ctfcli challenge add osint/osint-2
    python -m ctfcli challenge add osint/osint-1
    python -m ctfcli challenge add web/elves_packing_factory_2
    python -m ctfcli challenge add web/WinterBoot
    python -m ctfcli challenge add web/opain
    python -m ctfcli challenge add web/SantaVision
    python -m ctfcli challenge add web/santa_recipe_processor
    python -m ctfcli challenge add web/jardin_de_givre
    python -m ctfcli challenge add web/this_is_a_flask_app
    python -m ctfcli challenge add web/custom_tshirts
    python -m ctfcli challenge add web/succ
    python -m ctfcli challenge add web/elves_packing_factory_1
    python -m ctfcli challenge add web/christmas_RESTored
    python -m ctfcli challenge add web/i_want_a_mojito_oh_oh
    python -m ctfcli challenge add web/santas_whereabouts
    python -m ctfcli challenge add web/FENtastic

To install all challenges (AKA publish state in CTF) : 

    find . -mindepth 2 -maxdepth 2 | grep -v "./venv"| grep -v "./.ctf/" | awk '{print substr($1,3); }' | sed -e "s/^/python -m ctfcli challenge install /"

    python -m ctfcli challenge install jail/ChriSHmaSH
    python -m ctfcli challenge install forensics/atos-eviden-montrehack
    python -m ctfcli challenge install forensics/DZ_Ghostware
    python -m ctfcli challenge install forensics/irs_little_helper
    python -m ctfcli challenge install forensics/exfiltration_pro_max
    python -m ctfcli challenge install forensics/repas_de_noel
    python -m ctfcli challenge install crypto/9x9_cipher_machine
    python -m ctfcli challenge install crypto/booleanWonderland
    python -m ctfcli challenge install crypto/A_needle_in_a_christmas_log
    python -m ctfcli challenge install steg/santas_text
    python -m ctfcli challenge install steg/dialing_to_merry_festivities
    python -m ctfcli challenge install reverse/unlock_some_binary
    python -m ctfcli challenge install reverse/la_gare_pole_nord
    python -m ctfcli challenge install misc/visa_or_mastercard
    python -m ctfcli challenge install misc/gift_delivery
    python -m ctfcli challenge install pwn/sleigh_ride
    python -m ctfcli challenge install pwn/gift_wrapper
    python -m ctfcli challenge install osint/osint-5
    python -m ctfcli challenge install osint/osint-4
    python -m ctfcli challenge install osint/osint-2
    python -m ctfcli challenge install osint/osint-1
    python -m ctfcli challenge install web/elves_packing_factory_2
    python -m ctfcli challenge install web/WinterBoot
    python -m ctfcli challenge install web/opain
    python -m ctfcli challenge install web/SantaVision
    python -m ctfcli challenge install web/santa_recipe_processor
    python -m ctfcli challenge install web/jardin_de_givre
    python -m ctfcli challenge install web/this_is_a_flask_app
    python -m ctfcli challenge install web/custom_tshirts
    python -m ctfcli challenge install web/succ
    python -m ctfcli challenge install web/elves_packing_factory_1
    python -m ctfcli challenge install web/christmas_RESTored
    python -m ctfcli challenge install web/i_want_a_mojito_oh_oh
    python -m ctfcli challenge install web/santas_whereabouts
    python -m ctfcli challenge install web/FENtastic



To change a challenge's description, points, etc, modify it's `challenge.yml` and re-sync it:

    python -m ctfcli challenge sync jail/ChriSHmaSH

Installing and syncing will trigger Montrehack's CTFd Webhook and publish to discord, spoiling the challenges ahead of time. Make the channel private or delete the bot's messages to avoid leaks.