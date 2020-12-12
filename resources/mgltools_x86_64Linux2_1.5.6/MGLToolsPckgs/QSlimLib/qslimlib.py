# This file was automatically generated by SWIG (http://www.swig.org).
# Version 1.3.31
#
# Don't modify this file, modify the SWIG interface instead.
# This file is compatible with both classic and new-style classes.

import _qslimlib
import new
new_instancemethod = new.instancemethod
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'PySwigObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError,name

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

import types
try:
    _object = types.ObjectType
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0
del types


init_slim = _qslimlib.init_slim
cleanup_for_output = _qslimlib.cleanup_for_output
class MxSMFReader(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MxSMFReader, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MxSMFReader, name)
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        this = _qslimlib.new_MxSMFReader(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _qslimlib.delete_MxSMFReader
    __del__ = lambda self : None;
    __swig_setmethods__["unparsed_hook"] = _qslimlib.MxSMFReader_unparsed_hook_set
    __swig_getmethods__["unparsed_hook"] = _qslimlib.MxSMFReader_unparsed_hook_get
    if _newclass:unparsed_hook = _swig_property(_qslimlib.MxSMFReader_unparsed_hook_get, _qslimlib.MxSMFReader_unparsed_hook_set)
    def asp_store(*args, **kwargs): return _qslimlib.MxSMFReader_asp_store(*args, **kwargs)
    def read(*args, **kwargs): return _qslimlib.MxSMFReader_read(*args, **kwargs)
    def parse_line(*args, **kwargs): return _qslimlib.MxSMFReader_parse_line(*args, **kwargs)
    def createModel(*args, **kwargs): return _qslimlib.MxSMFReader_createModel(*args, **kwargs)
    def bind_normals(*args, **kwargs): return _qslimlib.MxSMFReader_bind_normals(*args, **kwargs)
    def bind_colors(*args, **kwargs): return _qslimlib.MxSMFReader_bind_colors(*args, **kwargs)
    def bind_texcoord(*args, **kwargs): return _qslimlib.MxSMFReader_bind_texcoord(*args, **kwargs)
MxSMFReader_swigregister = _qslimlib.MxSMFReader_swigregister
MxSMFReader_swigregister(MxSMFReader)

class MxSMFWriter(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, MxSMFWriter, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, MxSMFWriter, name)
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        this = _qslimlib.new_MxSMFWriter(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["vertex_annotate"] = _qslimlib.MxSMFWriter_vertex_annotate_set
    __swig_getmethods__["vertex_annotate"] = _qslimlib.MxSMFWriter_vertex_annotate_get
    if _newclass:vertex_annotate = _swig_property(_qslimlib.MxSMFWriter_vertex_annotate_get, _qslimlib.MxSMFWriter_vertex_annotate_set)
    __swig_setmethods__["face_annotate"] = _qslimlib.MxSMFWriter_face_annotate_set
    __swig_getmethods__["face_annotate"] = _qslimlib.MxSMFWriter_face_annotate_get
    if _newclass:face_annotate = _swig_property(_qslimlib.MxSMFWriter_face_annotate_get, _qslimlib.MxSMFWriter_face_annotate_set)
    def write(*args, **kwargs): return _qslimlib.MxSMFWriter_write(*args, **kwargs)
    def writeSMF(*args, **kwargs): return _qslimlib.MxSMFWriter_writeSMF(*args, **kwargs)
    __swig_destroy__ = _qslimlib.delete_MxSMFWriter
    __del__ = lambda self : None;
MxSMFWriter_swigregister = _qslimlib.MxSMFWriter_swigregister
MxSMFWriter_swigregister(MxSMFWriter)

class ContractionCallback(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ContractionCallback, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ContractionCallback, name)
    __repr__ = _swig_repr
    def __init__(self, *args, **kwargs): 
        this = _qslimlib.new_ContractionCallback(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _qslimlib.delete_ContractionCallback
    __del__ = lambda self : None;
ContractionCallback_swigregister = _qslimlib.ContractionCallback_swigregister
ContractionCallback_swigregister(ContractionCallback)

class QSlimModel(ContractionCallback):
    __swig_setmethods__ = {}
    for _s in [ContractionCallback]: __swig_setmethods__.update(getattr(_s,'__swig_setmethods__',{}))
    __setattr__ = lambda self, name, value: _swig_setattr(self, QSlimModel, name, value)
    __swig_getmethods__ = {}
    for _s in [ContractionCallback]: __swig_getmethods__.update(getattr(_s,'__swig_getmethods__',{}))
    __getattr__ = lambda self, name: _swig_getattr(self, QSlimModel, name)
    __repr__ = _swig_repr
    __swig_setmethods__["history"] = _qslimlib.QSlimModel_history_set
    __swig_getmethods__["history"] = _qslimlib.QSlimModel_history_get
    if _newclass:history = _swig_property(_qslimlib.QSlimModel_history_get, _qslimlib.QSlimModel_history_set)
    __swig_setmethods__["smfReader"] = _qslimlib.QSlimModel_smfReader_set
    __swig_getmethods__["smfReader"] = _qslimlib.QSlimModel_smfReader_get
    if _newclass:smfReader = _swig_property(_qslimlib.QSlimModel_smfReader_get, _qslimlib.QSlimModel_smfReader_set)
    __swig_setmethods__["model"] = _qslimlib.QSlimModel_model_set
    __swig_getmethods__["model"] = _qslimlib.QSlimModel_model_get
    if _newclass:model = _swig_property(_qslimlib.QSlimModel_model_get, _qslimlib.QSlimModel_model_set)
    __swig_setmethods__["slim"] = _qslimlib.QSlimModel_slim_set
    __swig_getmethods__["slim"] = _qslimlib.QSlimModel_slim_get
    if _newclass:slim = _swig_property(_qslimlib.QSlimModel_slim_get, _qslimlib.QSlimModel_slim_set)
    def __init__(self, *args, **kwargs): 
        this = _qslimlib.new_QSlimModel(*args, **kwargs)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _qslimlib.delete_QSlimModel
    __del__ = lambda self : None;
    def clean_history(*args, **kwargs): return _qslimlib.QSlimModel_clean_history(*args, **kwargs)
    def bind_normals(*args, **kwargs): return _qslimlib.QSlimModel_bind_normals(*args, **kwargs)
    def bind_colors(*args, **kwargs): return _qslimlib.QSlimModel_bind_colors(*args, **kwargs)
    def bind_texcoord(*args, **kwargs): return _qslimlib.QSlimModel_bind_texcoord(*args, **kwargs)
    def get_color_binding(*args, **kwargs): return _qslimlib.QSlimModel_get_color_binding(*args, **kwargs)
    def get_texcoord_binding(*args, **kwargs): return _qslimlib.QSlimModel_get_texcoord_binding(*args, **kwargs)
    def get_normal_binding(*args, **kwargs): return _qslimlib.QSlimModel_get_normal_binding(*args, **kwargs)
    def get_vert_count(*args, **kwargs): return _qslimlib.QSlimModel_get_vert_count(*args, **kwargs)
    def get_face_count(*args, **kwargs): return _qslimlib.QSlimModel_get_face_count(*args, **kwargs)
    def num_valid_faces(*args, **kwargs): return _qslimlib.QSlimModel_num_valid_faces(*args, **kwargs)
    def num_valid_verts(*args, **kwargs): return _qslimlib.QSlimModel_num_valid_verts(*args, **kwargs)
    def slim_to_target(*args, **kwargs): return _qslimlib.QSlimModel_slim_to_target(*args, **kwargs)
    def contraction_callback(*args, **kwargs): return _qslimlib.QSlimModel_contraction_callback(*args, **kwargs)
    def cleanup_for_output(*args, **kwargs): return _qslimlib.QSlimModel_cleanup_for_output(*args, **kwargs)
    def outmodel(*args, **kwargs): return _qslimlib.QSlimModel_outmodel(*args, **kwargs)
    def writeSMF(*args, **kwargs): return _qslimlib.QSlimModel_writeSMF(*args, **kwargs)
QSlimModel_swigregister = _qslimlib.QSlimModel_swigregister
QSlimModel_swigregister(QSlimModel)



