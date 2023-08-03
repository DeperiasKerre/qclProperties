# Text Mining Pipeline for Mining the Quantum Cascade Laser properties 
## Introduction
* We propose a text mining pipeline for mining the qcl properties(heterostructre, temperature,power, barrier thickness and lasing frequency) from a corpus of scienitific articles documenting the development of quantum cascade lasers. The pipleine is based on ChemDataExtractor, a chemistry aware software toolkit [[1]](https://pubs.acs.org/doi/full/10.1021/acs.jcim.6b00207).
* The grammar-based parsing rules used in AutoSentenceParser in chemDataExtractor become less efficient when generalized from chemistry to the wider materials science.The tool can therefore not be readily used to mine the parameters of qcls without adptation/modification). One of the ways to overcome this is by extending the property models defined in chemDataExtractor[[2]](https://pubs.acs.org/doi/full/10.1021/acs.jcim.1c00446),[[3]](https://www.nature.com/articles/s41597-022-01752-1).
* We improve  the parsing capabilties of chemDataExtractor on qcl properties by extending the property models and define new grammar parsing rules  for each of the qcl properties, which we utilise to extract the properties from the scientific publications.
* We evalaute our pipeline on open access journals from AIP,IOP and OPTICA publishers.
## Citation
TBD
## Usage
* To run the scripts, you need to install chemdataextractor2.
* For this work, version 2.0.2 has been used. 
* This can be installed using pip on the command line as: pip install chemdataextractor2==2.0.2
* The documentation for chemdataextractor2 can be found [here](https://cambridgemolecularengineering-chemdataextractor-development.readthedocs-hosted.com/en/latest/)
* ChemDataExtractor v2 is licensed under the MIT license_, a permissive, business-friendly license for open source software.
* MIT license: https://github.com/CambridgeMolecularEngineering/ChemDataExtractor/blob/master/LICENSE
## References
1. Swain, M. C., & Cole, J. M. (2016). ChemDataExtractor: a toolkit for automated extraction of chemical information from the scientific literature. Journal of chemical information and modeling, 56(10), 1894-1904. DOI: 10.1021/acs.jcim.6b00207
2.  Mavracic, J., Court, C. J., Isazawa, T., Elliott, S. R., & Cole, J. M. (2021). ChemDataExtractor 2.0: Autopopulated Ontologies for Materials Science. Journal of Chemical Information and Modeling, 61(9), 4280-4289. doi.org/10.1021/acs.jcim.1c00446
3.  Sierepeklis, O., & Cole, J. M. (2022). A thermoelectric materials database auto-generated from the scientific literature using ChemDataExtractor. Scientific data, 9(1), 1-12. doi.org/10.1038/s41597-022-01752-1

