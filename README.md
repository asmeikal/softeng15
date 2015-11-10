
Questo file non è un readme.

# Struttura del file

Propongo di utilizzare sintassi [Markdown](https://daringfireball.net/projects/markdown/syntax) in questo file.
Propongo inoltre di documentare scoperte e proposte e pensieri.

Propongo di salvare in fondo al file i link interessanti o utili che troviamo.
Propongo di documentare le idee che ci vengono usando un log LIFO in cui ogni entry viene messa in cima (quindi prima 2015-11-10 poi 2015-11-09 e via così).

# Problematiche interessanti

- Notifiche via SMS/email per eventi di vario tipo, come: login, bonifici ricevuti, etc. *(espandere)*
- Gestione centralizzata dei pagamenti (prelievi? **come si dice?**) ricorrenti autorizzati

# Log

### 2015-11-10

[Qui][project_example] quello che sembra essere un esempio di progetto di ingegneria del software che riguarda software bancario.

Bozza di progetto da Michele: il progetto potrebbe riguardare un sito di home banking che si interfaccia con quello che pare si chiami [core banking][core_banking], ossia database etc che contengono tutti i dati della banca.
Potremmo astrarre completamente il core banking, illustrando un insieme di funzionalità per interfacciarsi con il core banking.
Queste funzionalità sono da creare a mano al momento della realizzazione.
Sono comunque poco importanti perché il centro del progetto deve essere il sito di home banking e le funzionalità che questo propone.


<!-- Raccolta link utili -->

[totp_rfc]:			https://tools.ietf.org/html/rfc6238			"Time-based One-Time Passwords"
[core_banking]:		https://en.wikipedia.org/wiki/Core_banking	"Core Banking"
[project_example]:	http://www.slideshare.net/nancs/54024405-projectreportbankingmanagementsystem
