#!/usr/bin/env python
# coding: utf-8

# In[9]:


#future imports
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


# In[10]:


#libraries
from chemdataextractor import Document
from chemdataextractor.model import BaseModel, Compound, StringType, ModelType
from chemdataextractor.model.units import TemperatureModel, LengthModel
from chemdataextractor.parse import R, I, W, Optional, merge, join, AutoSentenceParser
from chemdataextractor.parse.elements import W, I, R, Optional, Any, OneOrMore, Not, ZeroOrMore
from chemdataextractor.doc import Paragraph, Heading, Sentence
from lxml import etree
from pprint import pprint


# In[11]:


#Units and models definition for power in mW
#extend the powerModel with the milliwatt class in order to capture power measurements in milliwatts.
from chemdataextractor.model.units.dimension import Dimension
from chemdataextractor.model.units.quantity_model import QuantityModel
from chemdataextractor.model.units.unit import Unit
from chemdataextractor.model.units.charge import Charge
from chemdataextractor.model.units.energy import Energy
from chemdataextractor.model.units.electric_potential import ElectricPotential
from chemdataextractor.model.units.current import ElectricalCurrent
import logging
log = logging.getLogger(__name__)

class Power(Dimension):
    constituent_dimensions = ElectricPotential() * ElectricalCurrent()


class PowerModel(QuantityModel):
    dimensions = Power()


class PowerUnit(Unit):

    def __init__(self, magnitude=0.0, powers=None):
        super(PowerUnit, self).__init__(Power(), magnitude, powers)


class Watt(PowerUnit):

    def convert_value_to_standard(self, value):
        return value

    def convert_value_from_standard(self, value):
        return value

    def convert_error_to_standard(self, error):
        return error

    def convert_error_from_standard(self, error):
        return error
    
class milliwatt(PowerUnit):
    """
    Class for power in milliwatt
    """

    def convert_value_to_standard(self, value):
        return value/1000

    def convert_value_from_standard(self, value):
        return value*1000
    def convert_error_to_standard(self, error):
        return error

    def convert_error_from_standard(self, error):
        return error

units_dict = {R('(W|w)(att(s)?)?', group=0): Watt, R('(mW|(milli(W|w)watt(s)?))\.?', group=0): milliwatt}
Power.units_dict.update(units_dict)
Power.standard_units = Watt()


# In[18]:


#working temperature property model
class OpticalPower(PowerModel):#inherits the temperature model to handle the units
    """ A working temperature property"""
    specifier_expr = ((I('peak')+I('power')|I('peak')+I('-')+I('power'))|(I('peak')+I('power')+I('is')+I('approximately'))).add_action(join)
    specifier = StringType(parse_expression=specifier_expr,required=True, contextual=True)
    compound = ModelType(Compound,required=False,contextual=True)
    compound.model_class.fields['names'].required = True
    parsers = [AutoSentenceParser()]


# In[19]:


#reading the document
with open('345.html', 'rb') as f:
    doc = Document.from_file(f)
print(doc)


# In[20]:


doc.models = [OpticalPower]
results=doc.records.serialize()
pprint(results)


# In[ ]:




