# As seen on http://tex.stackexchange.com/questions/40738/how-to-properly-make-a-latex-project

.PHONY: all clean

CURR_DIR = .

OUT_DIR = $(CURR_DIR)

TARGETS = $(CURR_DIR)/proposal.pdf

#IMAGES = $(CURR_DIR)/Prova.eps

all: $(TARGETS) $(IMAGES)

# Regola per compilare i singoli file .tex
$(TARGETS): $(TARGETS:.pdf=.tex)
	latexmk -bibtex -pdf -pdflatex="pdflatex -interaction=nonstopmode" -use-make $(CURR_DIR)/$(@F:.pdf=.tex)

# Regola per convertire svg in eps
$(IMAGES): $(IMAGES:.eps=.svg)
	./svg2eps.sh $(CURR_DIR)/$(@F:.eps=.svg)

# Rimuove tutti i file non .tex
clean:
	latexmk -C

# Rimuove tutti i file non .tex o .pdf
neat:
	latexmk -c

