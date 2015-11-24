
Questo file non è un readme.

# Struttura del file

Propongo di utilizzare sintassi [Markdown](https://daringfireball.net/projects/markdown/syntax) in questo file.
Propongo inoltre di documentare scoperte e proposte e pensieri.

Propongo di salvare in fondo al file i link interessanti o utili che troviamo.
Propongo di documentare le idee che ci vengono usando un log LIFO in cui ogni entry viene messa in cima (quindi prima 2015-11-10 poi 2015-11-09 e via così).
Ogni entry inizia con tre asterischi (\#\#\#) seguiti dalla data in formato AAAA-MM-GG.

# Problematiche interessanti

- Notifiche via SMS/email per eventi di vario tipo, come: login, bonifici ricevuti, etc. *(espandere)*
- Gestione centralizzata dei pagamenti (prelievi? **come si dice?**) ricorrenti autorizzati

# Glossarietto

- **Backend**: il database originale della banca, scritto in COBOL, che è costante e immutabile.

# Scrittura dei documenti

Requisiti per compilare LaTeX sono: LaTeX (`texlive`), `latexmk`, e probabilmente i seguenti package:
- `babel-italian`
- `fullpage`
- `parskip`
- `hyperref`
- `nameref`
- `fancyhdr`
- `graphicx`

La struttura dei documenti deve essere una cosa simile:
```
\documentclass[utf8]{softeng}
\begin{document}
Chiacchiere.
\begin{figure}
\includegraphics{ClassDiagram}
\caption{Un diagramma di classe}
\end{figure}
\end{document}
```
La classe `softeng` è costruita sulla classe `article`, quindi permette il sezionamento da `section` in giù.
L'opzione `utf8` permette di inserire direttamente lettere accentate nel testo, e non obbligatoriamente cose come `\'e`.

Visual Paradigm permette di esportare i file in formato `svg`.
LaTeX vuole immagini in formato `eps`.
Lo script `svg2eps.sh` installa due malware e converte il file `svg` dato come primo parametro in un file `eps`.
Ha bisogno di `inkscape`.

Il `Makefile` compila usando `latexmk`.

**Per il futuro:** vorrei provare a scrivere uno scriptino per "finalizzare" i documenti.
Lo scriptino dovrebbe prendere tutti i file `tex` nella cartella, cambiare `\date{\today}` alla data odierna, e schiaffarli tutti in una cartella `Iterations/N` incrementando `N` a ogni botta.

# Log

### 2015-11-24

Proposta di progetto quasi ultimata nel buco lasciato da Korner nel nostro tempo e nei nostri cuori.

### 2015-11-19

Improvvisa realizzazione del gruppo che quanto scritto durante il precedente incontro sia di fatto il documento dei requisiti, e non quello di visione del sistema.
Il gruppo inizia quindi la stesura del documento di visione del sistema consultando documento simile del progetto **Curator Assistant**.
Il gruppo constata che Artemio parla italiano meglio di Luigi e Michele, e trae le dovute conclusioni.
Urge divisione del lavoro e successivo lavoro individuale per ultimare la stesura entro il 23/11 e presentarla quindi al professor Bottoni.

### 2015-11-17

Appassionato inizio di stesura della proposta di progetto nel secondo laboratorio di Matematica.
La sorpresa di Gigi regna indiscussa.

### 2015-11-12

Risultato di oggi: insicurezza su cosa voglia Bottoni, se un sistema di Home Banking o una banca vera e propria per scappare con i soldi di tutti.

Il progetto potrebbe riguardare la creazione di un interfaccia web per l'home banking.
In questo caso probabilmente si dovrà considerare come dato il database della banca contenente i dati sui conti e sulle operazioni fatte dagli utenti, e il progetto dovrà interfacciarsi con questo database (che d'ora in poi chiameremo *backend*).
Quindi, possiamo scegliere:
- Supponiamo che il backend offra un insieme di primitive (da trovare) che sono sufficienti a svolgere tutte le operazioni che vogliamo fare.
- Non supponiamo niente sul backend, elenchiamo un insieme di primitive sufficienti a svolgere le operazioni che vogliamo fare, e diciamo che *incapsuleremo* il backend opportunamente per rendere possibile la chiamata a queste primitive.
- Supponiamo che il backend sia mascherato da [Open Bank Project][open_bank_project] (se non lo è, noi si chiama gli amici di OBP e gli si chiede di installare il loro sistema), e l'interfaccia per home banking la sviluppiamo usando le primitive di OBP.

Michele ritiene interessante la possibilità di ricreare un sottoinsieme di [Open Bank Project][open_bank_project] adattandolo alle necessità delle banche *retail* italiane.
Necessario discutere ancora questa opzione.

### 2015-11-10

[Qui][project_example] quello che sembra essere un esempio di progetto di ingegneria del software che riguarda software bancario.

Bozza di progetto da Michele: il progetto potrebbe riguardare un sito di home banking che si interfaccia con quello che pare si chiami [core banking][core_banking], ossia database etc che contengono tutti i dati della banca.
Potremmo astrarre completamente il core banking, illustrando un insieme di funzionalità per interfacciarsi con il core banking.
Queste funzionalità sono da creare a mano al momento della realizzazione.
Sono comunque poco importanti perché il centro del progetto deve essere il sito di home banking e le funzionalità che questo propone.

[Qui][fondi_intro] un'introduzione ai fondi (nella slide dei progetti Bottoni nomina un misterioso "portafoglio fondi").

<!-- Raccolta link utili -->

[totp_rfc]:			https://tools.ietf.org/html/rfc6238			"Time-based One-Time Passwords"
[core_banking]:		https://en.wikipedia.org/wiki/Core_banking	"Core Banking"
[project_example]:	http://www.slideshare.net/nancs/54024405-projectreportbankingmanagementsystem
[fondi_intro]:		http://www.borsainside.com/finanzainside/fondi-di-investimento/
[firma_digitale_pdf]: http://www.agid.gov.it/sites/default/files/linee_guida/firme_multiple.pdf
[open_banking_uk_article]: http://opensource.com/business/15/4/open-standard-api-banking
[teller_io]:		http://teller.io/
[open_bank_project]: https://openbankproject.com/
[ibm_business_modeling_practices]: http://www.ibm.com/developerworks/rational/library/content/RationalEdge/aug04/5634.html
[ibm_business_modeling_uml]: http://www.ibm.com/developerworks/rational/library/360.html

