# Text Mining Pipeline for Mining the Quantum Cascade Laser properties Based on ChemDataExtractor2
## Introduction
* We propose a text mining pipeline for mining the qcl properties(thickness,heterostructre, temperature,power and lasing frequency) from a corpus of scienitific articles documenting the developmemnt of quantum cascade lasers. The pipleine is based on ChemDataExtractor2, a chemistry aware software toolkit [[1]](https://pubs.acs.org/doi/full/10.1021/acs.jcim.6b00207).
* The grammar-based parsing rules used in AutoSentenceParser in chemDataExtractor become less efficient when generalized from chemistry to the wider materials science.The tool can therefore not be readily used to mine the parameters of qcls without adptation/modification). One of the ways to overcome this is by extending the property models defined in chemDataExtractor[[2]](https://pubs.acs.org/doi/full/10.1021/acs.jcim.1c00446),[[3]](https://www.nature.com/articles/s41597-022-01752-1).
* We extend the parsing capabilties of chemDataExtractor by defining new proerty models and parsers for each of the qcl properties, which we utilise to extract the properties from the scientific publications. 
## References
1. Swain, M. C., & Cole, J. M. (2016). ChemDataExtractor: a toolkit for automated extraction of chemical information from the scientific literature. Journal of chemical information and modeling, 56(10), 1894-1904. DOI: 10.1021/acs.jcim.6b00207
2.  Mavracic, J., Court, C. J., Isazawa, T., Elliott, S. R., & Cole, J. M. (2021). ChemDataExtractor 2.0: Autopopulated Ontologies for Materials Science. Journal of Chemical Information and Modeling, 61(9), 4280-4289. doi.org/10.1021/acs.jcim.1c00446
3.  Sierepeklis, O., & Cole, J. M. (2022). A thermoelectric materials database auto-generated from the scientific literature using ChemDataExtractor. Scientific data, 9(1), 1-12. doi.org/10.1038/s41597-022-01752-1

