#!/usr/bin/env python
# coding: utf-8

# In[1]:


from chemdataextractor import Document
from chemdataextractor.model import BaseModel, Compound, StringType, ModelType
from chemdataextractor.model.units import TemperatureModel, LengthModel
from chemdataextractor.parse import R, I, W, Optional, merge, join, AutoSentenceParser
from chemdataextractor.doc import Paragraph, Heading, Sentence
from pprint import pprint
from lxml import etree


# In[2]:


class WorkingTemperature(TemperatureModel):#inherits the temperature model to handle the units
    """ A working temperature property"""
    specifier_expr = ((I('heat')+I('-')+I('sink')+I('temperature')+I('of'))|(I('operating')+I('temperature'))|(I('operation')+I('temperature'))|(I('maximum')+I('temperature'))|(I('working')+I('temperature'))|(I('pulsed')+('mode'))|(I('continous')+I('wave')+I('mode'))|(I('maximum')+I('heat')+I('-')+I('sink')+I('temperature'))).add_action(join)
    specifier = StringType(parse_expression=specifier_expr,required=True, contextual=True)
    compound = ModelType(Compound,required=False,contextual=True)
    compound.model_class.fields['names'].required = False
    parsers = [AutoSentenceParser()]


# In[3]:


# two sentences from the abstract, numbers changed a bit to better view the source of records
s1 = Sentence('The laser operated up to a heat-sink temperature of 110K in pulsed mode, 95K in continuous wave (cw) mode, and the threshold current density at 5K was ∼140A∕cm2.')
s2 = Sentence('In pulsed operation, the device lased up to a maximum heat-sink temperature (Tmax) of 111K. The threshold current density (Jth) at 6K was 142A∕cm2. ')
s1.models = [WorkingTemperature]
s2.models = [WorkingTemperature]


# In[4]:


sentence_parser = AutoSentenceParser(lenient=True)
sentence_parser.model = WorkingTemperature


# In[5]:


for result in sentence_parser.root.scan(s1.tagged_tokens):
    print(etree.tostring(result[0]), '\n')
pprint(s1.records.serialize())


# In[6]:


for result in sentence_parser.root.scan(s2.tagged_tokens):
    print(etree.tostring(result[0]), '\n')
pprint(s2.records.serialize())

