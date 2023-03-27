#!/usr/bin/env python
# coding: utf-8

# In[1]:


#libraries
from chemdataextractor import Document
from chemdataextractor.model import BaseModel, Compound, StringType, ModelType
from chemdataextractor.model.units import TemperatureModel, LengthModel
from chemdataextractor.parse import R, I, W, Optional, merge, join, AutoSentenceParser
from chemdataextractor.doc import Paragraph, Heading, Sentence
from lxml import etree
from pprint import pprint


# In[2]:


#reading the document
with open('p1.html', 'rb') as f:
    doc = Document.from_file(f)
print(doc)


# In[3]:


#Document Metadata
doc.metadata


# In[4]:


#The qcl Heterostructure(material) property model
class QCLHeterostructure(BaseModel):#inherits the compound model to parse material names
    """ A QCL Heterostructure(Material) property model"""
    specifier_expr =((I('laser')+I('structure'))|(I('design')+I('based')+I('on'))|(W('QW')+I('structure')+I('based')+I('on'))|I('growth')|I('system')|(I('material')+I('of')+I('choice')+I('is'))|(I('was')+I('grown')+I('in'))|(I('module')+I('grown')+I('in'))|(I('material')+I('system'))|(I('material')+I('systems'))|(I('material')+I('combination'))|I('wafer')|I('MBE')).add_action(join)
    specifier = StringType(parse_expression=specifier_expr,required=True, contextual=True)
    compound = ModelType(Compound,required=False,contextual=True)
    #compound.model_class.fields['names'].required = False
    parsers = [AutoSentenceParser()]


# In[5]:


#analyzing the whole document at once
doc.models = [QCLHeterostructure]
results=doc.records.serialize()
pprint(results)


# In[6]:


#setting the Sentence parsers
sentence_parser = AutoSentenceParser(lenient=True)
sentence_parser.model = QCLHeterostructure


# In[7]:


#analyzing the individual tokens
for p in doc.paragraphs:
    for s in p.sentences:
        x=s.tagged_tokens
        for result in sentence_parser.root.scan(x):
            #print(etree.tostring(result[0]), '\n')
            pprint(s.records.serialize())

