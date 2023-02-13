from bpy.props import StringProperty
from ..swivelmeta_component import SwivelMetaComponent
from ..types import Category, PanelType, NodeType


class MixerVisible(SwivelMetaComponent):
    '''Mixer Visible Component'''
    _definition = {
        'name': 'mixer-visible',  # name of the A-Frame component
        'display_name': 'Mixer Visible',  # name displayed in Blender
        'category': Category.EXPERIMENTAL,  # category in Blender
        'node_type': NodeType.NODE,
        # panel in Blender where the component will be displayed
        'panel_type': [PanelType.OBJECT],
        # icon in Blender that will be displayed next to the component name
        'icon': 'IMAGE_ALPHA'
    }
