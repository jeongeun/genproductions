#!/bin/bash


cd /afs/cern.ch/user/j/jelee/workspace/genproductions/bin/MadGraph5_aMCatNLO/cards/production/13TeV/WprimeToLNu_NLO 
masses=(1000 2000 3000 4000 5000 6000)
postfix=(_run_card.dat _customizecards.dat _proc_card.dat _extramodels.dat)
name=WprimeToMuNu_NLO
sample=WprimeToMuNu
#MuNusample=WprimeToMuNu_M

## output WprimeToENu_M-<MASS>_NLO_NNPDF31nnlo  -nojpeg


echo ${masses[*]}

for mass in ${masses[*]}; do
    echo generating cards for M = $mass GeV
    dirname=${sample}_M-${mass}_NLO_NNPDF31nnlo
    cd $name ; mkdir $dirname

    for i in {0..3}; do
        sed "s/<MASS>/${mass}/g" ${sample}${postfix[$i]} > ${sample}_M-${mass}${postfix[$i]}

        if [ ${mass} == 1000 ]; then
           sed "s/<WIDTH>/35.5045/g" ${sample}_M-${mass}${postfix[$i]} > ${dirname}/${dirname}${postfix[$i]} ; rm ${sample}_M-${mass}${postfix[$i]};
        elif [ ${mass} == 2000 ]; then
           sed "s/<WIDTH>/71.0090/g" ${sample}_M-${mass}${postfix[$i]} > ${dirname}/${dirname}${postfix[$i]} ; rm ${sample}_M-${mass}${postfix[$i]};
        elif [ ${mass} == 3000 ]; then
           sed "s/<WIDTH>/106.513/g" ${sample}_M-${mass}${postfix[$i]} > ${dirname}/${dirname}${postfix[$i]} ; rm ${sample}_M-${mass}${postfix[$i]};
        elif [ ${mass} == 4000 ]; then
           sed "s/<WIDTH>/142.018/g" ${sample}_M-${mass}${postfix[$i]} > ${dirname}/${dirname}${postfix[$i]} ; rm ${sample}_M-${mass}${postfix[$i]};
        elif [ ${mass} == 5000 ]; then
           sed "s/<WIDTH>/177.522/g" ${sample}_M-${mass}${postfix[$i]} > ${dirname}/${dirname}${postfix[$i]} ; rm ${sample}_M-${mass}${postfix[$i]};
        else
           sed "s/<WIDTH>/213.027/g" ${sample}_M-${mass}${postfix[$i]} > ${dirname}/${dirname}${postfix[$i]} ; rm ${sample}_M-${mass}${postfix[$i]};
        fi
    done

    
done


