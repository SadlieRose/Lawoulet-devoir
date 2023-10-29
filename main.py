from random import randrange
import random
import pickle
import keyboard

def main():
    epsedo = input("Byenvini nan jwet la.\n Rantre nonw an miniskil pou kòmanse jwet la :\n")

    while ' ' in epsedo or not epsedo.islower() ==False:
        epsedo = input("Rantre yon epsedo en miniskil ki pa gen espas svp! : \n")
    print(f" {epsedo}  Byenvini nan jwet la.\n")

    data = None
    try:
        with open('jeux.pkl', 'rb') as s:
            data = pickle.load(s)
        if data['epsedo'] == epsedo:
            print(f"Byenveni, {epsedo}! Eskò ou se {data['esko']}")
        else:
            print(f"Ou se yon nouvo itilizate, {epsedo}. Eskò ou an se 0")
            data = {'epsedo': epsedo, 'esko': 0}
    except (FileNotFoundError, TypeError):
        print(f"Ou se yon nouvo itilizate, {epsedo}. Eskò ou an se 0")
        data = {'epsedo': epsedo, 'esko': 0}

    while True:
        nombre_ordi = randrange(1, 10)
        print(f"nonb kache a se {nombre_ordi}")
        
        chans = 5
        print("BYENVINI NAN JWET SA KI SE LAWOULET!")
        while chans > 0:
            choix = input("Devine nonm ki te chwazi an: \n")

            # if keyboard.is_pressed('k') or keyboard.is_pressed('K'):
            #     print("Jwet la ap kanpe")
            #     break

            try:
                choix = int(choix)
            except ValueError:
                print("Rantre yon nonb valab nan entèval 1 ak 9. \n")
                continue

            if choix < 1 or choix > 9:
                print("Rantre yon nonb ki nan entèval la. \n")
                continue

            if choix == nombre_ordi:
                print("Ou reyisi \n")
                data['esko'] += 1
                break
            else:
                chans -= 1
                if choix < nombre_ordi:
                    print("vre nonb lan pi piti ke sa ou sot chwazi an \n")
                elif choix > nombre_ordi:
                    print("vre nonb lan pi gro ke sa ou sot chwazi an \n")
                if chans == 0:
                    print("Ou pa genyen chans anko \n")

        print(f"Eskò ou an se {data['esko']}. BRAVO! \n")

        Jwe_anko = input("Ou vle jwe anko? (Wi/Non): \n")
        if Jwe_anko.lower() != "Wi":
            break

    with open('jeux.pkl', 'wb') as s:
        pickle.dump(data, s)

if __name__ == "__main__":
    main()
