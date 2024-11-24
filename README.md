**Phylogenetic Insights into _MIZ1_ Gene Evolution and Workflow**


**Introduction**

This project provides a detailed analysis of the _MIZ1_ gene's phylogenetic evolution across land plants, focusing on gene duplication events, evolutionary conservation, and gene expression patterns. The _MIZ1_ gene is implicated in the adaptation of plants to terrestrial environments, particularly in response to abiotic stresses such as drought, salt, and cold. By constructing a phylogenetic tree of the _MIZ1_ gene, this analysis identifies key evolutionary relationships, paralog distribution, and expression patterns across different plant species.

This workflow details the bioinformatics tools and methods used for sequence processing, alignment, phylogenetic tree construction, and visualization of gene expression patterns.

**Prerequisites**

Before starting the analysis, ensure that you have an account on an HPC (High Performance Computing) system with the following bioinformatics tools available:

BLAST
HMMER
Muscle or MAFFT (for sequence alignment)
TrimAl (for sequence trimming)
IQ-TREE (for phylogenetic tree construction)
Data and File Details
Annotated Protein Sequences:

The list of selected plant species is provided in list_of_plant_species.docx .
The dataset folder contains annonated genome sequence files, which have been preprocessed, renamed, and cleaned of any special characters (e.g., "*", "."). These files are ready for further analysis.
The dataset folder can be downloaded from https://drive.google.com/file/d/1rVISvE7stg3GD3AuuYBL4ddQl_SLDk7-/view?usp=drive_link
Genome Sequence File:
The concatenated genome sequences for the selected plant species are cleaned of unwanted special characters and stored in all_genome_cleaned.fa.

BLAST Database:
A BLAST database is constructed from the cleaned genome sequences in all_genome_cleaned.fa and stored in the BLAST_database_folder.

Query Sequences:
The query sequences for the functional _MIZ1_ gene and its 11 paralogs from _Arabidopsis thaliana_ are provided in MIZ1_sequence.fasta.

HMMER Profile:
A profile for the MIZ1 domain is created using the query sequences and stored in MIZ1_profile.hmm for further HMMER searches.
BLAST and HMMER Search:

BLAST and HMMER searches are performed on the genome database, using an E-value threshold of 10^5 for BLAST and default settings for HMMER.
The homologs identified from both searches are combined, with duplicates removed. The final homolog sequences are stored in result/hb_nodubli_extracted_seq.fas.

Sequence Alignment:
The homolog sequences are aligned using Muscle with the following command:
"bash
Copy code
muscle -in hb_nodubli_extracted_seq.fas -out align_hb.fas"

Sequence Trimming:
The aligned sequences are trimmed using TrimAl to improve alignment quality:
"bash
Copy code
trimal -in align_hb.fas -out trim_hb.fas -automated1"

Phylogenetic Tree Construction:
The phylogenetic tree is constructed from the trimmed sequences using IQ-TREE:
"bash
Copy code
iqtree2 -s trim_hb.fas -m MFP -B 1000 -nt 6"
The phylogenetic tree file is saved as trim_hb.fas.iqtree

Visualization:
The phylogenetic tree is visualized using FigTree.

Gene expression data are processed and visualized using Python code in the visualization_of_gene_expression_and_python_code folder.

**Findings:**

**The output of the Thesis is in outputs.docx which can be referred to understand the Findings** 

**Phylogenetic Insights into MIZ1 Evolution**:


The phylogenetic analysis of _MIZ1_ homologs revealed distinct evolutionary patterns across land plants. Homologs from closely related species exhibited similar alignment patterns, underscoring the evolutionary conservation of this gene. The phylogenetic tree, focusing on embryophytes, suggests that the _MIZ1_ gene is specific to land plants, with a significant role in their adaptation to terrestrial environments. The analysis identified three major paralogs, suggesting two gene duplication events, with the first duplication occurring early in land plant evolution, followed by variations in gene presence across plant groups (Figure 2, Figure 3).

A notable aspect of the analysis is the increased gene expression observed in roots under abiotic stress, particularly around the functional _MIZ1_ gene of Arabidopsis thaliana (Figure 4). This highlights the gene’s involvement in stress response, especially under conditions like drought and salt stress. Interestingly, non-seeded species, such as some basal plants, showed homologs of the MIZ1 gene near its functional form in Arabidopsis, with notable expression in the roots. These results suggest a conserved role of MIZ1 in stress response across various plant lineages.

Additionally, the synteny analysis identified conserved genes across species, such as those involved in stress response (e.g., Glycosyltransferase family 61, Heat stress transcription factor B-3) (Figure 5), indicating that the _MIZ1_ gene's function is integrated with other vital processes, such as stress tolerance and root development.

**Gene Duplication and Evolutionary Significance**

The gene duplication events, particularly in the second and third paralogs, provide insight into the evolutionary history of the _MIZ1_ gene. The first duplication appears to have occurred in the common ancestor of land plants, reflecting the progression from bryophytes through to angiosperms (Figure 6-9). The second duplication event, however, remains unclear due to missing phyla in the second and third paralogs. One possible explanation is the loss of the gene copy in specific plant groups, such as hornworts, lycophytes, and mosses, possibly due to the selective pressure favoring the retention of functional copies in more adapted plant lineages.

This analysis suggests that the _MIZ1_ gene has been crucial for plant adaptation to land by playing a key role in hydrotropism and water management. Its conservation across diverse land plant groups emphasizes its essential function in plant survival under terrestrial conditions, especially in water-limited environments.

**Comparative Gene Expression Across Land Plants**

Gene expression data further elucidates the functional diversification of _MIZ1_ paralogs across plant species. The expression of _MIZ1_ paralogs was analyzed in various plant regions, with a focus on their role under abiotic stress. The data showed that while all three paralogs are expressed across multiple plant tissues, the roots consistently exhibited higher expression levels under drought, salt, and cold stress conditions. This supports the hypothesis that the _MIZ1_ gene evolved to help plants cope with environmental stresses, particularly those affecting water uptake and retention.

In basal lineages such as _Marchantia polymorpha_ (liverworts), which lacks true roots, _MIZ1_ expression was highest in reproductive tissues, suggesting that the gene may have initially evolved to support desiccation tolerance in these plants. Over time, as plants evolved vascular tissues and roots, _MIZ1_ gene function may have adapted to support water management and stress resilience in more complex plant systems.

Species-specific expression patterns were also noted. For example, in _Vitis vinifera_, _MIZ1_ expression was highest in the pericarp, leaves, and seeds, with minimal expression in the roots (data not shown). 

**Conclusion**

The findings of this study suggest that the _MIZ1_ gene is integral to land plant evolution, with its role in water management and abiotic stress tolerance being conserved across plant lineages. The gene’s expression patterns, particularly in the roots during stress conditions, emphasize its ongoing relevance in plant survival. The evolutionary dynamics of MIZ1, shaped by gene duplication events, reflect the gene's adaptation to different environmental challenges as plants transitioned from aquatic to terrestrial habitats. These results not only provide a deeper understanding of _MIZ1_'s functional evolution but also contribute to the broader context of plant adaptation to land.

References: 
1.	Iino M. Toward understanding the ecological functions of tropisms: interactions among and effects of light on tropisms. Curr Opin Plant Biol. 2006;9(1):89-93.
2.	Gilroy ES, Masson PH. PLANI IR0 PISMS.
3.	Jaffe MJ, Takahashi H, Biro RL. A pea mutant for the study of hydrotropism in roots. Science. 1985 Oct 25;230(4724):445-7.
4.	Galvan-Ampudia CS, Julkowska MM, Darwish E, Gandullo J, Korver RA, Brunoud G, Haring MA, Munnik T, Vernoux T, Testerink C. Halotropism is a response of plant roots to avoid a saline environment. Current Biology. 2013 Oct 21;23(20):2044-50.
5.	 Eysholdt-Derzsó E, Sauter M. Root bending is antagonistically affected by hypoxia and ERF-mediated transcription via auxin signaling. Plant Physiology. 2017 Sep 1;175(1):412-23.
6.	Su et al., 2017
7.	Kobayashi A, Takahashi A, Kakimoto Y, Miyazawa Y, Fujii N, Higashitani A, Takahashi H. A gene essential for hydrotropism in roots. Proceedings of the National Academy of Sciences. 2007 Mar 13;104(11):4724-9.
8.	Takahashi H. Hydrotropism: the current state of our knowledge. Journal of plant research. 1997 Jun;110:163-9.
9.	 Takahashi H, Mizuno H, Kamada M, Fujii N, Higashitani A, Kamigaichi S, Aizawa S, Mukai C, Shimazu T, Fukui K, Yamashita M. A spaceflight experiment for the study of gravimorphogenesis and hydrotropism in cucumber seedlings. Journal of Plant Research. 1999 Dec;112:497-505.
10.	 Takahashi N, Goto N, Okada K, Takahashi H. Hydrotropism in abscisic acid, wavy, and gravitropic mutants of Arabidopsis thaliana. Planta. 2002 Dec;216:203-11.
11.	Eapen D, Barroso ML, Campos ME, Ponce G, Corkidi G, Dubrovsky JG, Cassab GI. A no hydrotropic response root mutant that responds positively to gravitropism in Arabidopsis. Plant physiology. 2003 Feb 1;131(2):536-46.
12.	 Saucedo M, Ponce G, Campos ME, Eapen D, García E, Lujan R, Sanchez Y, Cassab GI. An altered hydrotropic response (ahr1) mutant of Arabidopsis recovers root hydrotropism with cytokinin. Journal of experimental botany. 2012 Jun 13;63(10):3587-601.
13.	Miyazawa Y, Takahashi A, Kobayashi A, Kaneyasu T, Fujii N, Takahashi H. GNOM-mediated vesicular trafficking plays an essential role in hydrotropism of Arabidopsis roots. Plant physiology. 2009 Feb 1;149(2):835-40.
14.	Miyazawa Y, Moriwaki T, Uchida M, Kobayashi A, Fujii N, Takahashi H. Overexpression of MIZU-KUSSEI1 enhances the root hydrotropic response by retaining cell viability under hydrostimulated conditions in Arabidopsis thaliana. Plant and Cell Physiology. 2012 Nov 1;53(11):1926-33.
15.	Yamazaki T, Miyazawa Y, Kobayashi A, Moriwaki T, Fujii N, Takahashi H. MIZ1, an essential protein for root hydrotropism, is associated with the cytoplasmic face of the endoplasmic reticulum membrane in Arabidopsis root cells. FEBS letters. 2012 Feb 17;586(4):398-402.
16.	Moriwaki T, Miyazawa Y, Fujii N, Takahashi H. Light and abscisic acid signalling are integrated by MIZ1 gene expression and regulate hydrotropic response in roots of Arabidopsis thaliana. Plant, Cell & Environment. 2012 Aug;35(8):1359-68.
17.	Moriwaki T, Miyazawa Y, Kobayashi A, Uchida M, Watanabe C, Fujii N, Takahashi H. Hormonal regulation of lateral root development in Arabidopsis modulated by MIZ1 and requirement of GNOM activity for MIZ1 function. Plant physiology. 2011 Nov 1;157(3):1209-20.
18.	Moriwaki T, Miyazawa Y, Kobayashi A, Takahashi H. Molecular mechanisms of hydrotropism in seedling roots of Arabidopsis thaliana (Brassicaceae). American journal of botany. 2013 Jan;100(1):25-34.
19.	Dietrich D, Pang L, Kobayashi A, Fozard JA, Boudolf V, Bhosale R, Antoni R, Nguyen T, Hiratsuka S, Fujii N, Miyazawa Y. Root hydrotropism is controlled via a cortex-specific growth mechanism, 2017. Nat Plants 3: 17057.
20.	Nakajima Y, Nara Y, Kobayashi A, Sugita T, Miyazawa Y, Fujii N, Takahashi H. Auxin transport and response requirements for root hydrotropism differ between plant species. Journal of experimental botany. 2017 Jun 15;68(13):3441-56.
21.	Oyanagi A, Takahashi H, Suge H. Interactions between Hydrotropism and Gravitropism in the Primary Seminal Roots of Triticum eastivum L. Annals of Botany. 1995 Mar 1;75(3):229-35.
22.	Takahashi H, Scott TK. Hydrotropism and its interaction with gravitropism in maize roots. Plant Physiology. 1991 Jun 1;96(2):558-64.
23.	Water UN. World Water Assessment Programme. Water in a changing world: facts and figures. Paris: Unesco. 2012.
24.	Rockstrom J. Balancing water for humans and nature: the new approach in ecohydrology. Routledge; 2013 Jun 17.
25.	Sadigov R. Rapid growth of the world population and its socioeconomic results. The Scientific World Journal. 2022;2022(1):8110229.
26.	Grigorieva E, Livenets A, Stelmakh E. Adaptation of agriculture to climate change: A scoping review. Climate. 2023 Oct 6;11(10):202.
27.	Koncagül E, Connor R. The United Nations World Water Development Report 2023: partnerships and cooperation for water; facts, figures and action examples.
28.	Oguz MC, Aycan M, Oguz E, Poyraz I, Yildiz M. Drought stress tolerance in plants: Interplay of molecular, biochemical and physiological responses in important development stages. Physiologia. 2022 Dec 9;2(4):180-97.
29.	Henry A, Gowda VR, Torres RO, McNally KL, Serraj R. Variation in root system architecture and drought response in rice (Oryza sativa): phenotyping of the OryzaSNP panel in rainfed lowland fields. Field Crops Research. 2011 Jan 31;120(2):205-14.
30.	Lynch JP. Steep, cheap and deep: an ideotype to optimize water and N acquisition by maize root systems. Annals of botany. 2013 Jul 1;112(2):347-57.
31.	Uga Y, Sugimoto K, Ogawa S, Rane J, Ishitani M, Hara N, Kitomi Y, Inukai Y, Ono K, Kanno N, Inoue H. Control of root system architecture by DEEPER ROOTING 1 increases rice yield under drought conditions. Nature genetics. 2013 Sep;45(9):1097-102.
32.	Rogers ED, Benfey PN. Regulation of plant root system architecture: implications for crop advancement. Current Opinion in Biotechnology. 2015 Apr 1;32:93-8.
33.	Gao Y, Lynch JP. Reduced crown root number improves water acquisition under water deficit stress in maize (Zea mays L.). Journal of experimental botany. 2016 Aug 1;67(15):4545-57.
34.	Iwata S, Miyazawa Y, Fujii N, Takahashi H. MIZ1-regulated hydrotropism functions in the growth and survival of Arabidopsis thaliana under natural conditions. Annals of Botany. 2013 Jul 1;112(1):103-14.
35.	Bowles AM, Paps J, Bechtold U. Water‐related innovations in land plants evolved by different patterns of gene cooption and novelty. New Phytologist. 2022 Jul;235(2):732-42.
36.	Liu GQ, Lian L, Wang W. The molecular phylogeny of land plants: progress and future prospects. Diversity. 2022 Sep 21;14(10):782.
37.	Su, D.; Yang, L.; Shi, X.; Ma, X.; Zhou, X.; Hedges, S.B.; Zhong, B. Large-scale phylogenomic analyses reveal the monophyly of bryophytes and neoproterozoic origin of land plants. Mol. Biol. Evol. 2021, 38, 3332–3344.
38.	Cox, C.J.; Li, B.; Foster, P.G.; Embley, T.M.; Civan, P. Conflicting phylogenies for early land plants are caused by composition biases among synonymous substitutions. Syst. Biol. 2014, 63, 272–279.
39.	Zhang, J.; Fu, X.X.; Li, R.Q.; Zhao, X.; Liu, Y.; Li, M.H.; Zwaenepoel, A.; Ma, H.; Goffinet, B.; Guan, Y.L.; et al. The hornwort genome and early land plant evolution. Nat. Plants 2020, 6, 107–118.
40.	Wickett, N.J.; Mirarab, S.; Nguyen, N.; Warnow, T.; Carpenter, E.; Matasci, N.; Ayyampalayam, S.; Barker, M.S.; Burleigh, J.G.; Gitzendanner, M.A.; et al. Phylotranscriptomic analysis of the origin and early diversification of land plants. Proc. Natl. Acad. Sci. USA 2014, 111, E4859–E4868.
41.	One Thousand Plant Transcriptomes Initiative. One thousand plant transcriptomes and the phylogenomics of green plants. Nature 2019, 574, 679–685
42.	Kranz, H.D.; Huss, V.A.R. Molecular evolution of pteridophytes and their relationship to seed plants: Evidence from complete 18S rRNA gene sequences. Plant Syst. Evol. 1996, 202, 1–11
43.	Pryer, K.M.; Schneider, H.; Smith, A.R.; Cranfill, R.; Wolf, P.G.; Hunt, J.S.; Sipes, S.D. Horsetails and ferns are a monophyletic group and the closest living relatives to seed plants. Nature 2001, 409, 618–622.
44.	Rai, H.S.; Graham, S.W. Utility of a large, multigene plastid data set in inferring higher-order relationships in ferns and relatives (monilophytes). Am. J. Bot. 2010, 97, 1444–1456
45.	Ran, J.H.; Shen, T.T.; Wang, M.M.; Wang, X.Q. Phylogenomic resolves the deep phylogeny of seed plants and indicates partial convergent or homoplastic evolution between Gnetales and angiosperms. Proc. R. Soc. B 2018, 285, 20181012.
46.	Bowe, L.M.; Coat, G.; DePamphilis, C.W. Phylogeny of seed plants based on all three genomic compartments: Extant gymnosperms are monophyletic and Gnetales’ closest relatives are conifers. Proc. Natl. Acad. Sci. USA 2000, 97, 4092–4097.
47.	Chaw, S.M.; Parkinson, C.L.; Cheng, Y.C.; Vincent, T.M.; Palmer, J.D. Seed plant phylogeny inferred from all three plant genomes: Monophyly of extant gymnosperms and origin of Gnetales from conifers. Proc. Natl. Acad. Sci. USA 2000, 97, 4086–4091.
48.	Liu, Y.; Wang, S.; Li, L.; Yang, T.; Dong, S.; Wei, T.; Wu, S.; Liu, Y.; Gong, Y.; Feng, X.; et al. The Cycas genome and the early evolution of seed plants. Nat. Plants 2022, 8, 389–401.
49.	Wan, T.; Liu, Z.M.; Li, L.F.; Leitch, A.R.; Leitch, I.J.; Lohaus, R.; Liu, Z.J.; Xin, H.P.; Gong, Y.B.; Liu, Y.; et al. A genome for gnetophytes and early evolution of seed plants. Nat. Plants 2018, 4, 82–89.
50.	Parkinson, C.L.; Adams, K.L.; Palmer, J.D. Multigene analyses identify the three earliest lineages of extant flowering plants. Curr. Biol. 1999, 9, 1485–1491.
51.	Saarela, J.M.; Rai, H.S.; Doyle, J.A.; Endress, P.K.; Mathews, S.; Marchant, A.D.; Briggs, B.G.; Graham, S.W. Hydatellaceae identified as a new branch near the base of the angiosperm phylogenetic tree. Nature 2007, 446, 312–315.
52.	Qiu, Y.L.; Dombrovska, O.; Lee, J.; Li, L.; Whitlock, B.A.; Bernasconi-Quadroni, F.; Rest, J.S.; Davis, C.C.; Borsch, T.; Hilu, K.W.; et al. Phylogenetic analyses of basal angiosperms based on nine plastid, mitochondrial, and nuclear genes. Int. J. Plant Sci. 2005, 166, 815–842.
53.	Amborella Genome Project; Albert, V.A.; Barbazuk, W.B.; Depamphilis, C.W.; Der, J.P.; Leebens-Mack, J.; Ma, H.; Palmer, J.D.; Rounsley, S.; Sankoff, D.; et al. The Amborella genome and the evolution of flowering plants. Science 2013, 342, 1241089.
54.	Zhang, L.; Chen, F.; Zhang, X.; Li, Z.; Zhao, Y.; Lohaus, R.; Chang, X.; Dong, W.; Ho, S.Y.W.; Liu, X.; et al. The water lily genome and the early evolution of flowering plants. Nature 2020, 577, 79–84.
55.	Moore, M.J.; Bell, C.D.; Soltis, P.S.; Soltis, D.E. Using plastid genome-scale data to resolve enigmatic relationships among basal angiosperms. Proc. Natl. Acad. Sci. USA 2007, 104, 19363–19368.
56.	Ma, J.; Sun, P.; Wang, D.; Wang, Z.; Yang, J.; Li, Y.; Mu, W.; Xu, R.; Wu, Y.; Dong, C.; et al. The Chloranthus sessilifolius genome provides insight into early diversification of angiosperms. Nat. Commun. 2021, 12, 6929.
57.	Guo, X.; Fang, D.; Sahu, S.K.; Yang, S.; Guang, X.; Folk, R.; Smith, S.A.; Chanderbali, A.S.; Chen, S.; Liu, M.; et al. Chloranthus genome provides insights into the early diversification of angiosperms. Nat. Commun. 2021, 12, 6930.
58.	Fürst-Jansen JM, de Vries S, de Vries J. Evo-physio: on stress responses and the earliest land plants. Journal of Experimental Botany. 2020 Jun 11;71(11):3254-69.
59.	Hetherington AJ, Dolan L. Stepwise and independent origins of roots among land plants. Nature. 2018 Sep 13;561(7722):235-8.
60.	Léran S, Varala K, Boyer J-C, Chiurazzi M, Crawford N, Daniel-Vedele F, David L, Dickstein R, Fernandez E, Forde B et al. 2014. A unified nomenclature of nitrate transporter 1/peptide transporter family members in plants. Trends in Plant Science 19: 5–9.
61.	Kien Huu Nguyen KH, Chien Van Ha CV, Nishiyama R, Watanabe Y, Leyva-González MA, Fujita Y, Uven Thi Tran UT, Li WeiQiang LW, Tanaka M, Seki M, Schaller GE. Arabidopsis type B cytokinin response regulators ARR1, ARR10, and ARR12 negatively regulate plant responses to drought.
62.	Altschul, S. F., Gish, W., Miller, W., Myers, E. W., & Lipman, D. J. (1990). "Basic local alignment search tool." Journal of Molecular Biology, 215(3), 403-410.
63.	Eddy, S. R. (1998). "Profile hidden Markov models." Bioinformatics, 14(9), 755-763.
64.	 Li, W., & Godzik, A. (2006). "Cd-hit: A fast program for clustering and comparing large sets of protein or nucleotide sequences." Bioinformatics, 22(13), 1658-1659.
65.	Edgar, R. C. (2004). "MUSCLE: multiple sequence alignment with high accuracy and high throughput." Nucleic Acids Research, 32(5), 1792-1797.
66.	Capella-Gutiérrez, S., Silla-Martínez, J. M., & Gabaldón, T. (2009). "trimAl: a tool for automated alignment trimming in large-scale phylogenetic analyses." Bioinformatics, 25(15), 1972-1973.
67.	Nguyen, L. T., Schmidt, H. A., Von Haeseler, A., & Minh, B. Q. (2015). "IQ-TREE: A fast and effective stochastic algorithm for estimating maximum-likelihood phylogenies." Molecular Biology and Evolution, 32(1), 268-274.
68.	Rambaut, A. (2010) FigTree v1.3.1. Institute of Evolutionary Biology, University of Edinburgh, Edinburgh.
69.	Reference: Louis, A., Nguyen, N. T. T., & Muffato, M. (2012). "GenomicusPlants: an online portal for plant comparative genomics." Bioinformatics, 28(21), 2871-2873.
70.	Conekt: Co-expression Network Toolkit for Plants.
71.	Marchantia.info: A resource for Marchantia polymorpha gene expression data.
72.	Winter, D., Vinegar, B., Nahal, H., Ammar, R., Wilson, G. V., & Provart, N. J. (2007). "An 'Electronic Fluorescent Pictograph' browser for exploring and analyzing large-scale biological data sets." PLoS One, 2(8), e718.
73.	Zuckerkandl E, Pauling L. Evolutionary divergence and convergence in proteins. InEvolving genes and proteins 1965 Jan 1 (pp. 97-166). Academic press.
74.	Lynch M, Conery JS. The evolutionary fate and consequences of duplicate genes. science. 2000 Nov 10;290(5494):1151-5.
75.	Kondrashov FA, Kondrashov AS. Role of selection in fixation of gene duplications. Journal of Theoretical Biology. 2006 Mar 21;239(2):141-51.
76.	Pires ND, Dolan L. Morphological evolution in land plants: new designs with old genes. Philosophical Transactions of the Royal Society B: Biological Sciences. 2012 Feb 19;367(1588):508-18.
77.	Menand B, Yi K, Jouannic S, Hoffmann L, Ryan E, Linstead P, Schaefer DG, Dolan L. An ancient mechanism controls the development of cells with a rooting function in land plants. Science. 2007 Jun 8;316(5830):1477-80.
78.	Cao JG, Dai XL, Zou HM, Wang QX. Formation and development of rhizoids of the liverwort Marchantia polymorpha. The Journal of the Torrey Botanical Society. 2014 Apr 1:126-34.
79.	Kaur V, Yadav SK, Wankhede DP, Pulivendula P, Kumar A, Chinnusamy V. Cloning and characterization of a gene encoding MIZ1, a domain of unknown function protein and its role in salt and drought stress in rice. Protoplasma. 2020 Mar;257(2):475-87.
80.	Xiang DL, Li GS. Control of leaf development in the water fern Ceratopteris richardii by the auxin efflux transporter CrPINMa in the CRISPR/Cas9 analysis. BMC Plant Biology. 2024 Apr 24;24(1):322.
81.	Singh NK, Anand S, Jain A, Das S. Comparative genomics and synteny analysis of KCS17-KCS18 cluster across different genomes and sub-genomes of brassicaceae for analysis of its evolutionary history. Plant molecular biology reporter. 2017 Apr;35:237-51.
82.	Devos KM, Beales J, Nagamura Y, Sasaki T. Arabidopsis–rice: will colinearity allow gene prediction across the eudicot–monocot divide?. Genome Research. 1999 Sep 1;9(9):825-9.
83.	Salse J, Piégu B, Cooke R, Delseny M. Synteny between Arabidopsis thaliana and rice at the genome level: a tool to identify conservation in the ongoing rice genome sequencing project. Nucleic Acids Research. 2002 Jun 1;30(11):2316-28.

