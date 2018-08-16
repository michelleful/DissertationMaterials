Data from Michelle A. Fullwood and Timothy J. O'Donnell (2013). Learning Non-concatenative Morphology. In Proceedings of the Fourth Annual Workshop on Cognitive Modeling and Computational Linguistics (CMCL).

Also Chapter 2 of Fullwood (2018). If you use this dataset, please cite the paper above.


File: quran.verbs.data
----------------------
Source: Qu'ranic Arabic Corpus (Dukes, 2011) and Buckwalter Arabic Morphological Analyzer version 1.0 (Buckwalter, 2002) 
Format: Tab-separated data
Record count: 1563

- Column 1: Full verb in Buckwalter transliteration
- Column 2: Root/residue bitmask. 1 = root, 0 = residue
- Column 3: Root in Buckwalter transliteration
- Column 4: Residue (everything apart from the root) in Buckwalter transliteration

Note, design decision: o and ~ (null vowel and geminate consonant marker respectively) were included as-is and went into residue.


File: english.verbs.data
-----------------------
Source: Penn Treebank (Marcus et al 1999) and CELEX (Baayen et al 1995)
Format: Tab-separated data
Record count: 1549

- Column 1: Full verb in regular English orthography
- Column 2: Full verb in DISC transliteration
- Column 3: Root/residue bitmask. 1 = root, 0 = residue
- Column 4: "Root", or English stem, minus the ablaut vowel
- Column 5: Residue, everything besides the stem -- usually a suffix, but sometimes ablaut vowel (+ suffix), etc

Note: See paper for more detail on design decisions made in determining root and residue.
