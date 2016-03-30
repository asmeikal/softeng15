﻿
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
- `xcolor`
- `pgfgantt`

La struttura dei documenti &egrave; la seguente:
```
\documentclass[10pt]{softeng}

\Phase{<fase> - <iterazione>}
\DocumentTitle{<titolo documento>}

\begin{document}

\startofdocument

<testo>

\end{document}
```
La classe `softeng` è costruita sulla classe `article`, quindi permette il sezionamento da `section` in giù.

Per creare tabelle carine e colorate c'&egrave; un environment apposito:
```
\begin{ptable}{<n-colonne>}
\ptitlerow{\bf <titolo tabella>}
\pcells{<cella1> & <cella2> & ... & <cellan>}
\pline
\ptitlerow{<titolo riga lunga>}
\prow{<riga lunga>}
\end{ptable}
```

Visual Paradigm permette di esportare i file in formato `svg`.
LaTeX vuole immagini in formato `eps`.
Lo script `svg2eps.sh` installa due malware e converte il file `svg` dato come primo parametro in un file `eps`.
Ha bisogno di `inkscape`.

Il `Makefile` compila usando `latexmk`.

**Per il futuro:** vorrei provare a scrivere uno scriptino per "finalizzare" i documenti.
Lo scriptino dovrebbe prendere tutti i file `tex` nella cartella, cambiare `\date{\today}` alla data odierna, e schiaffarli tutti in una cartella `Iterations/N` incrementando `N` a ogni botta.

# Log

### 2016-03-30

Ristrutturazione documenti Inception.
Produrremo:

1. Analisi del contesto e studio di fattibilit&agrave;
   - Analisi del contesto (con questioni legali)
   - Fattibilit&agrave;
2. Documento dei requisiti
   - Definizione dei requisiti (requisiti utente)
   - Specifica dei requisiti (requisiti sistema - funzionali, non funzionali, di dominio)
   - Glossario
   - Tracciabilit&agrave; requisiti
   - Convalida dei requisiti
3. Piano di progetto
   - *Milestone* fasi e iterazioni
   - Analisi dei rischi
   - Stime costi
   - Gruppi di lavoro
   - Diagramma di GANTT

### 2016-03-24

Gigi produce glossario, Michele rischi.

### 2016-03-22

Distribuzione compiti: Gigi ai requisiti, Michele ai rischi, Artemio all'allungamento del brodo sull'analisi del contesto.

### 2016-02-25

Iniziata stesura del documento di analisi del contesto.

- Riguardo il **portafoglio fondi** Gigi propone di non consentire l'acquisto di nuovi titoli, argomento complesso e che pertiene pi&ugrave; al trading, ma solo di visionare i titoli che si posseggono, di conoscerne l'andamento (ottenuto da dati che assumiamo la banca abbia), ed eventualmente di venderli.
- Artemio propone di permettere agli utenti di effettuare **bidding** dei conti e delle carte, ossia di richiedere alla banca di aprire un conto o di ottenere una carta a certe condizioni, che la banca pu&ograve; valutare ed eventualmente accettare.
- &Egrave; bene che il sistema sia personalizzabile: gli addetti della banca devono poter inserire nuove offerte di conti o carte, magari indirizzandole a utenti che rispecchiano certe caratteristiche.
- L'audit di sicurezza riguarda la possibilit&agrave; dell'utente di controllare gli ultimi accessi e le ultime operazioni.
- La Banca d'Italia deve avere un accesso preferenziale ai dati della banca e degli utenti.

### 2016-02-15

Abbiamo individuato i documenti che nasceranno dall'inception e che probabilmente ci porteremo dietro durante il progetto:

- Piano di progetto
- Rischi
- Requisiti

Gli altri documenti della fase di Inception non verranno aggiornati al termine della prima fase.

I documenti da produrre durante l'inception sono:

1. Analisi del contesto e studio di fattibilità. L'idea è quella di documentarci approfonditamente sul dominio applicativo, concentrandoci su quanto scritto nella proposta di progetto (audit di sicurezza, portafogli fondi, azioni, etc.). Servirà da riferimento nelle fasi future, è bene che sia un documento completo.
2. Modello di business, con diagrammi di business. Va scritto partendo dall'analisi del contesto.
3. Requisiti e Rischi:
   - glossario dei requisiti chiave.
   - i rischi maggiori sembrano essere sicurezza del sistema e correttezza del software. Individuare anche rischi minori.
4. Piano di progetto: analisi dei costi e pianificazione temporale.

L'ordine dei documenti indica le dipendenze che pensiamo ci siano.

Proponiamo di iniziare dall'Analisi del contesto, seguendo quanto scritto nella proposta di progetto.
In particolare, dobbiamo chiarire i concetti nel punto 3 della sezione 1 (visione del sistema).

Il prossimo incontro è per martedì 23 alle 16 e qualcosa, per condividere quello che abbiamo scoperto sull'Analisi del contesto.

Link utili:

- [Esempi diagrammi visual paradigm][vpgallery].
- [Documentazione da presentare][documentazione_progetto].

### 2015-12-03

L'1 dicembre inviamo a Bottoni la proposta, il 2 dicembre chiede chiarimenti riguardo la figura 1, il 3 dicembre scriviamo i chiarimenti e inviamo la nuova proposta.
Bottoni risponde "bene così".

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
[vp_gallery]:    http://www.visual-paradigm.com/VPGallery/index.html
[documentazione_progetto]: http://wwwusers.di.uniroma1.it/~ingsoft1/Lezioni2008-2009/versioniPDF/DocumentazioneProgetto.pdf
