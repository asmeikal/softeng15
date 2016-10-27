#!/bin/bash

declare -A image_folders

image_folders[0]="Images"
image_folders[1]="Images/activity"
image_folders[2]="Images/sequence"
image_folders[3]="Images/use-cases"

for f in ${image_folders[@]}
do
	./make-eps.sh $f
done

declare -A targets

targets[0]="proposal"
targets[1]="analisi-contesto"
targets[2]="piano-progetto"
targets[3]="requirements"
targets[4]="use-case-model"
targets[5]="analisi-sistema"
targets[6]="design-sistema"
targets[7]="test-plan"

for t in ${targets[@]}
do
	latexmk -pdf $t
done

for i in `seq 0 7`
do
	echo "cp \"${targets[$i]}.pdf\" \"documents/${i}-${targets[$i]}.pdf\""
	cp "${targets[$i]}.pdf" "documents/HBS-${i}-${targets[$i]}.pdf"
done

