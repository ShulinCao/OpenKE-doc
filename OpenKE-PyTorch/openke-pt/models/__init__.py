"""
This package implements the knowledge embedding models. :mod:`Model` is the base model. We have implemented seven classic knowledge embedding models.

* :class:`models.TransE`
* :class:`models.TransH`
* :class:`models.TransR`
* :class:`models.TransD`
* :class:`models.RESCAL`
* :class:`models.DistMult`
* :class:`models.ComplEx`

"""
from . import Model
from Model import *
from . import TransE
from TransE import *
from . import TransH
from TransH import *
from . import TransR
from TransR import *
from . import TransD
from TransD import *
from . import RESCAL
from RESCAL import *
from . import DistMult
from DistMult import *
from . import ComplEx
from ComplEx import *