
import calendar
from datetime import date
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def accueil():

    calendrier = None
    erreur = None

    mois = date.today().month
    annee = date.today().year

    if request.method == "POST":

        try:
            mois = int(request.form["mois"])
            annee = int(request.form["annee"])

            if 1 <= mois <= 12 and 1 <= annee <= 9999:

                cal = calendar.Calendar(firstweekday=0)
                calendrier = cal.monthdayscalendar(annee, mois)

            else:
                erreur = "Mois ou année invalide."

        except ValueError:
            erreur = "Veuillez entrer une année valide."

    noms_mois = [
        "Janvier", "Février", "Mars", "Avril",
        "Mai", "Juin", "Juillet", "Août",
        "Septembre", "Octobre", "Novembre", "Décembre"
    ]

    return render_template(
        "index.html",
        calendrier=calendrier,
        mois=mois,
        annee=annee,
        noms_mois=noms_mois,
        erreur=erreur
    )


if __name__ == "__main__":
    app.run(debug=True)
