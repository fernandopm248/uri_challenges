for i in range(int(input(""))):
    pedra = 'pedra'
    papel = 'papel'
    tesoura = 'tesoura'
    spock = 'Spock'
    lagarto = 'lagarto'

    sheldon, raj = input("").split()
    if sheldon == pedra and raj == papel:
        vencedor = "Raj trapaceou!"
    elif raj == pedra and sheldon == papel:
        vencedor = "Bazinga!"
    elif sheldon == tesoura and raj == papel:
        vencedor = "Bazinga!"
    elif raj == tesoura and sheldon == papel:
        vencedor = "Raj trapaceou!"
    elif sheldon == pedra and raj == lagarto:
        vencedor = "Bazinga!"
    elif raj == pedra and sheldon == lagarto:
        vencedor = "Raj trapaceou!"
    elif sheldon == lagarto and raj == spock:
        vencedor = "Bazinga!"
    elif raj == lagarto and sheldon == spock:
        vencedor = "Raj trapaceou!"
    elif sheldon == spock and raj == tesoura:
        vencedor = "Bazinga!"
    elif raj == spock and sheldon == tesoura:
        vencedor = "Raj trapaceou!"
    elif sheldon == tesoura and raj == lagarto:
        vencedor = "Bazinga!"
    elif raj == tesoura and sheldon == lagarto:
        vencedor = "Raj trapaceou!"
    elif sheldon == lagarto and raj == papel:
        vencedor = "Bazinga!"
    elif raj == lagarto and sheldon == papel:
        vencedor = "Raj trapaceou!"
    elif sheldon == papel and raj == spock:
        vencedor = "Bazinga!"
    elif raj == papel and sheldon == spock:
        vencedor = "Raj trapaceou!"
    elif sheldon == spock and raj == pedra:
        vencedor = "Bazinga!"
    elif raj == spock and sheldon == pedra:
        vencedor = "Raj trapaceou!"
    elif sheldon == pedra and raj == tesoura:
        vencedor = "Bazinga!"
    elif raj == pedra and sheldon == tesoura:
        vencedor = "Raj trapaceou!"
    elif raj == sheldon:
        vencedor = "De novo!"
    print("Caso #%i:" % (i + 1), vencedor)




