import random

opere = [

    # =========================
    # VERGA / VERISMO
    # =========================

    {
        "titolo": "Cavalleria rusticana",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "La lupa",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "La roba",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "Prefazione a I Malavoglia",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "La famiglia Malavoglia",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "Il ritorno e l'addio di 'Ntoni",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "L'addio alla roba",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "La morte di Gesualdo",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "I Malavoglia",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "Mastro-don Gesualdo",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "Vita dei campi",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    {
        "titolo": "Novelle rusticane",
        "autore": "Giovanni Verga",
        "epoca": "Verismo"
    },

    # =========================
    # BAUDELAIRE / SIMBOLISMO
    # =========================

    {
        "titolo": "L'albatro",
        "autore": "Charles Baudelaire",
        "epoca": "Simbolismo"
    },

    {
        "titolo": "Spleen",
        "autore": "Charles Baudelaire",
        "epoca": "Simbolismo"
    },

    {
        "titolo": "Corrispondenze",
        "autore": "Charles Baudelaire",
        "epoca": "Simbolismo"
    },

    {
        "titolo": "I fiori del male",
        "autore": "Charles Baudelaire",
        "epoca": "Simbolismo"
    },

    # =========================
    # PASCOLI
    # =========================

    {
        "titolo": "X Agosto",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Il lampo",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Il tuono",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Novembre",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Lavandare",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Il gelsomino notturno",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "La mia sera",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Italy",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "La grande proletaria si è mossa",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Myricae",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Canti di Castelvecchio",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Primi poemetti",
        "autore": "Giovanni Pascoli",
        "epoca": "Decadentismo"
    },

    # =========================
    # D'ANNUNZIO
    # =========================

    {
        "titolo": "Il ritratto di un esteta",
        "autore": "Gabriele D'Annunzio",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Il verso è tutto",
        "autore": "Gabriele D'Annunzio",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "La pioggia nel pineto",
        "autore": "Gabriele D'Annunzio",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "La città è piena di fantasmi",
        "autore": "Gabriele D'Annunzio",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Il piacere",
        "autore": "Gabriele D'Annunzio",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Alcyone",
        "autore": "Gabriele D'Annunzio",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Le Laudi",
        "autore": "Gabriele D'Annunzio",
        "epoca": "Decadentismo"
    },

    {
        "titolo": "Notturno",
        "autore": "Gabriele D'Annunzio",
        "epoca": "Decadentismo"
    },

    # =========================
    # FUTURISMO / DADAISMO
    # =========================

    {
        "titolo": "Manifesto del Futurismo",
        "autore": "Filippo Tommaso Marinetti",
        "epoca": "Futurismo"
    },

    {
        "titolo": "Il bombardamento di Adrianopoli",
        "autore": "Filippo Tommaso Marinetti",
        "epoca": "Futurismo"
    },

    {
        "titolo": "Zang Tumb Tumb",
        "autore": "Filippo Tommaso Marinetti",
        "epoca": "Futurismo"
    },

    {
        "titolo": "Per fare una poesia dadaista",
        "autore": "Tristan Tzara",
        "epoca": "Dadaismo"
    },

    {
        "titolo": "Manifesto del Dadaismo",
        "autore": "Tristan Tzara",
        "epoca": "Dadaismo"
    },

    # =========================
    # SVEVO
    # =========================

    {
        "titolo": "Una vita",
        "autore": "Italo Svevo",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "Senilità",
        "autore": "Italo Svevo",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "Prefazione e Preambolo",
        "autore": "Italo Svevo",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "L'ultima sigaretta",
        "autore": "Italo Svevo",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "Una catastrofe inaudita",
        "autore": "Italo Svevo",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "La coscienza di Zeno",
        "autore": "Italo Svevo",
        "epoca": "Romanzo della crisi"
    },

    # =========================
    # PIRANDELLO
    # =========================

    {
        "titolo": "Il sentimento del contrario",
        "autore": "Luigi Pirandello",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "La patente",
        "autore": "Luigi Pirandello",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "Il treno ha fischiato",
        "autore": "Luigi Pirandello",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "Il fu Mattia Pascal",
        "autore": "Luigi Pirandello",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "Uno, nessuno e centomila",
        "autore": "Luigi Pirandello",
        "epoca": "Romanzo della crisi"
    },

    {
        "titolo": "La condizione di personaggi",
        "autore": "Luigi Pirandello",
        "epoca": "Teatro nel teatro"
    },

    {
        "titolo": "Sei personaggi in cerca d'autore",
        "autore": "Luigi Pirandello",
        "epoca": "Teatro nel teatro"
    },

    {
        "titolo": "L'umorismo",
        "autore": "Luigi Pirandello",
        "epoca": "Romanzo della crisi"
    },

    # =========================
    # UNGARETTI
    # =========================

    {
        "titolo": "Veglia",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Fratelli",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "I fiumi",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "San Martino del Carso",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Allegria di naufragi",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Sono una creatura",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Soldati",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Mattina",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "L'Allegria",
        "autore": "Giuseppe Ungaretti",
        "epoca": "Ermetismo"
    },

    # =========================
    # QUASIMODO
    # =========================

    {
        "titolo": "Ed è subito sera",
        "autore": "Salvatore Quasimodo",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Alle fronde dei salici",
        "autore": "Salvatore Quasimodo",
        "epoca": "Ermetismo"
    },

    # =========================
    # MONTALE
    # =========================

    {
        "titolo": "Non chiederci la parola",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Meriggiare pallido e assorto",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Spesso il male di vivere",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Non recidere, forbice, quel volto",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "La casa dei doganieri",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Ho sceso, dandoti il braccio, almeno un milione di scale",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Ossi di seppia",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Le occasioni",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    {
        "titolo": "Satura",
        "autore": "Eugenio Montale",
        "epoca": "Ermetismo"
    },

    # =========================
    # NEOREALISMO
    # =========================

    {
        "titolo": "Considerate se questo è un uomo",
        "autore": "Primo Levi",
        "epoca": "Neorealismo"
    },

    {
        "titolo": "Se questo è un uomo",
        "autore": "Primo Levi",
        "epoca": "Neorealismo"
    },

    {
        "titolo": "I partigiani costretti alla ritirata",
        "autore": "Beppe Fenoglio",
        "epoca": "Neorealismo"
    },

    {
        "titolo": "I ventitré giorni della città di Alba",
        "autore": "Beppe Fenoglio",
        "epoca": "Neorealismo"
    },

    {
        "titolo": "La pistola",
        "autore": "Italo Calvino",
        "epoca": "Neorealismo"
    },

    {
        "titolo": "Ultimo viene il corvo",
        "autore": "Italo Calvino",
        "epoca": "Neorealismo"
    },

    {
        "titolo": "La giornata di uno scrutatore",
        "autore": "Italo Calvino",
        "epoca": "Neorealismo"
    },

    {
        "titolo": "Tutto in un punto",
        "autore": "Italo Calvino",
        "epoca": "Narrativa fantastica"
    },

    {
        "titolo": "Ottavia, una città sottile",
        "autore": "Italo Calvino",
        "epoca": "Narrativa fantastica"
    },

    {
        "titolo": "Ersilia, la città itinerante",
        "autore": "Italo Calvino",
        "epoca": "Narrativa fantastica"
    },

    {
        "titolo": "Il sentiero dei nidi di ragno",
        "autore": "Italo Calvino",
        "epoca": "Neorealismo"
    },

    {
        "titolo": "Le Cosmicomiche",
        "autore": "Italo Calvino",
        "epoca": "Narrativa fantastica"
    },

    {
        "titolo": "Le città invisibili",
        "autore": "Italo Calvino",
        "epoca": "Narrativa fantastica"
    }

]

random.shuffle(opere)

totale = len(opere)

corrette = 0
errori = 0
completate = 0

print("=== QUIZ LETTERATURA ===")

for opera in opere:

    titolo = opera["titolo"]
    autore_corretto = opera["autore"].lower().strip()
    epoca_corretta = opera["epoca"].lower().strip()

    while True:

        print(f"\n📚 Progresso: {completate}/{totale} opere completate")
        print(f"🎯 Titolo: {titolo}")

        autore = input("Inserisci autore: ").lower().strip()
        epoca = input("Inserisci epoca: ").lower().strip()

        if autore == autore_corretto and epoca == epoca_corretta:

            print("✅ Corretto!")
            corrette += 1
            completate += 1
            break

        else:

            errori += 1

            print("\n❌ Sbagliato!")
            print(f"✔ Autore corretto: {opera['autore']}")
            print(f"✔ Epoca corretta: {opera['epoca']}")

            print("\nRiprova per continuare.")

            while True:

                autore_retry = input("Autore: ").lower().strip()
                epoca_retry = input("Epoca: ").lower().strip()

                if autore_retry == autore_corretto and epoca_retry == epoca_corretta:
                    print("✅ Ok, passiamo alla prossima!")
                    completate += 1
                    break
                else:
                    print("❌ Ancora sbagliato, riprova.")

            break

print("\n🎉 FINITO!")

print("\n===== RISULTATI =====")
print(f"Opere completate: {completate}/{totale}")
print(f"Corrette al primo tentativo: {corrette}")
print(f"Errori: {errori}")
