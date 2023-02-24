#!/usr/bin/env python
# coding: utf-8

# In[58]:


#ibraries
from chemdataextractor import Document
from chemdataextractor.model import BaseModel, Compound, StringType, ModelType
from chemdataextractor.model.units import TemperatureModel, LengthModel
from chemdataextractor.parse import R, I, W, Optional, merge, join, AutoSentenceParser
from chemdataextractor.doc import Paragraph, Heading, Sentence
from pprint import pprint


# In[59]:


#reading the document
with open('html_files (2).html', 'rb') as f:
    doc = Document.from_file(f)
print(doc)


# In[60]:


#Document Metadata
doc.metadata


# In[61]:


class WorkingTemperature(TemperatureModel):
    """ A working temperature property"""
    specifier_expr = ((I('heat-sink') + I('temperature'))|(I('operating')+I('temperature'))|(I('operation')+I('temperature'))|(I('maximum')+I('temperature'))|(I('working')+I('temperature'))|(I('pulsed')+('mode'))|(I('continous')+I('wave')+I('mode'))).add_action(join)
    specifier = StringType(parse_expression=specifier_expr,required=False, contextual=True)
    compound = ModelType(Compound,required=False,contextual=True)
    compound.model_class.fields['names'].required = True
    parsers = [AutoSentenceParser()]


# In[62]:


doc.models = [WorkingTemperature]
results = doc.records.serialize()
pprint(results)


# In[ ]:




