# Analysis of CpG Islands in Human Sex Chromosomes using Hidden Markov Models

**Authors:** Martí Díez Macià, Ainhoa López Carrasco, Maria López Moriana  
**Course / Project:** Clustering Methods and Algorithms in Genomics and Evolution / Algorithms for Sequence Analysis in Bioinformatics

---

## 📖 Introduction

**What are CpG islands?**  
- DNA regions with a high concentration of 'CG' dinucleotides.  
- Rare in the genome but biologically significant:  
  - Located near gene promoters, involved in transcription and gene expression.  
  - Crucial in gene regulation and DNA methylation.  
  - Abnormal methylation linked to various diseases.

**Project Outline:**  
1. Obtain FASTA sequences (Chromosomes X, Y, 21)  
2. Compare CpG island detection criteria  
3. Count and map CpG islands  
4. Identify CpG regions and store positions  
5. Apply Hidden Markov Model (HMM) to find hidden states and calculate probabilities  
6. Perform comparative analysis

**Hypothesis:**  
The detection and distribution of CpG islands across human chromosomes X and Y are influenced by chromosome size and threshold percentage, affecting their identification and biological implications.

---

## 🧪 Methodology

### CpG Island Detection
- **10% Threshold:** ≥50 'CG' dinucleotides in blocks of 500 bps.  
- **20% Threshold:** ≥100 'CG' dinucleotides, identifying larger CpG regions.  
- Functions used:  
  - `contar_cpg_islands()`  
  - `obtener_posiciones_nucleotidos_cpg()`  
  - `obtener_posiciones_nucleotidos_no_cpg()`  
  - `etiquetar()`

### Hidden Markov Model (HMM)
- **States:** CpG, No CpG  
- **Transition Probabilities:** Likelihood of moving from one state to another  
- **Emission Probabilities:** Likelihood of observing a nucleotide in a given state  
- **Normalization:** Probabilities divided by sequence length  

### Comparative Data Visualization
- Comparison among chromosomes at **10% and 20% thresholds**.  
- Observations:  
  - Chromosome 21: Higher proportion of CpG islands  
  - Chromosome X: Moderate CpG island presence  
  - Chromosome Y: Barely any CpG regions  

- Localization: CpG islands compared with overlapping coding genes, suggesting conserved regulatory regions.

---

## 💬 Discussion

**Model Assumptions:**  
- Independence between observations and states.  
- Constant transition probability between states.  

**Limitations:**  
- Computationally intensive  
- Current state depends only on the previous state  
- Potential deviations from actual biological patterns  

**Comparison with Literature:**  
1. *Prediction of CpG Islands with HMMs* – Thierry Grimm  
   - Similar probabilities, algorithmic differences  
2. *Using Hidden Markov Models to Infer CpG Islands and Promoter Regions* – Karthik Mittal  
   - Different definitions of CpG islands  
3. *Correlating CpG islands, motifs, and sequence variants in chromosome 21* – Nick Cercone  
   - Functional focus, divergence in CpG island size  

---

## ✅ Conclusion

- **CpG prediction:** HMM successfully predicted CpG islands in selected chromosomes.  
- **Analytical approach:** Model explains distribution and appearance of CpG islands.  
- **Gene regulation:** CpG islands near promoters affect DNA methylation and expression.  
- **Future research:** Explore complex interactions, evolutionary significance, and variability across chromosomes.  
- **Challenges:** Computational limitations and model assumptions may affect accuracy.

---

## 📂 Project Pipeline

1. Sequence retrieval (FASTA)  
2. CpG island counting and mapping  
3. Threshold-based region analysis  
4. HMM application for hidden states  
5. Probability matrix calculation  
6. Comparative visualization and discussion

---

