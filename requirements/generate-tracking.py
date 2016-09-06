
output_name = "generated/func_tracking_table.tex"

prefix_user_req = "itm:utente:funzionali:"
prefix_system_req = "sec:sistema:funzionali:"

user_req = [
	"iscrizione",
	"gestione-conto",
	"gestione-conto:verifica-saldo",
	"gestione-conto:verifica-andamento",
	# "gestione-conto:revisione",
	"gestione-conto:operazioni",
	"gestione-conto:operazioni-veloci",
	"storico",
	# "resoconto",
	"dipendenti:accesso",
	"dipendenti:operazioni-veloci",
	"management:bidding:approvazione",
	"management:bidding:creazione",
	"bidding:utente",
	"management:pacchetti-investimento:creazione",
	"management:pubblicita",
	"notifiche",
	"storico-dettagliato",
]

system_req = {
	"ISCRCORR" : [ "iscrizione" ],
	"CROPVEL" : [ "dipendenti:operazioni-veloci" ],
	"DISOPVEL" : [ "gestione-conto", "gestione-conto:operazioni-veloci", "dipendenti:operazioni-veloci" ],
	"DISPAG" : [ "gestione-conto", "gestione-conto:operazioni" ],
	"VERTIT" : [ "gestione-conto", "gestione-conto:verifica-andamento" ],
	"VERSAL" : [ "gestione-conto", "gestione-conto:verifica-saldo" ],
    "VERSTOR" : [ "storico" ],
    "DIPACC" : [ "dipendenti:accesso" ],
    "APPBID" : [ "management:bidding:approvazione" ],
    "CREABID" : [ "management:bidding:creazione" ],
    "USRBID" : ["bidding:utente" ],
}

system_reqs = system_req.keys()

if __name__ == "__main__":
    res = ""

    cols = len(system_req.keys()) + 1

    res += """
\\begin{table}[h]
\\resizebox{1\\textwidth}{!}{\\begin{minipage}{\\textwidth}
\\begin{center}
"""

    res += "\\begin{tabular}{r*{" + str(cols-1) + "}{|c}}\n"

    for k in system_reqs:
        res += "\t& \\vertical{\hyperref[" + prefix_system_req + k + "]{\\id" + k + "}}\n"
    res += "\t\\\\ \\hline\n"

    for u in user_req:
        res += "\t\\ref{" + prefix_user_req + u + "} "
        for k in system_reqs:
            res += "& "
            if u in system_req[k]:
                res += "\V "
        res += "\\\\\n"

    res += """
\\end{tabular}
\\end{center}
\\caption{Corrispondenza fra requisiti utente e requisiti sistema per i requisiti funzionali.}
\\label{table:tracking:funzionali}
\\end{minipage} }
\\end{table}
"""

    with open(output_name, "w") as f:
        f.write(res)

