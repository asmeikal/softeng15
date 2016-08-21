
### Dipendenze

La generazione delle tabelle dei requisiti richiede i seguenti moduli python:

- `pyaml`

### Istruzioni

Per creare un requisito:

1. entrare nella cartella `generated/yaml`;
2. copiare il file `example.yaml` in un nuovo file `[nome-requisito].yaml`;
3. modificare il file `[nome-requisito.yaml]`;
4. dalla directory corrente (`requirements` rispetto alla root del progetto) eseguire il comando:
   ```
   python generate-templates.py
   ```
5. ricompilare il file `requirements.tex` nella root del progetto per vedere i risultati.

I file contenuti nella cartella `generated/yaml` sono in formato [YAML](https://en.wikipedia.org/wiki/YAML).

Le stringhe in YAML sono racchiuse da apostrofi (`'`).
Per inserire un apostrofo in una stringa YAML vanno inseriti due apostrofi consecutivi (`''`), ad es.:
```
nome_campo: 'iscrizione del''utente'
```

