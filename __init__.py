"""
@author: Dennis
@title: ComfyUI_Guide_To_Making_Custom_Nodes
@description: Akatsuzi's TutorialAkatsuzi's Tutorial
"""

from .nodes.nodes import *

NODE_CLASS_MAPPINGS = {
    "Print Hello World": PrintHelloWorld,
    "Concatenate Hello World": ConcatenateHelloWorld,
    "Hello World Overlay Text": HelloWorldOverlayText,
    }
    
print("\033[34mComfyUI Tutorial Nodes: \033[92mLoaded\033[0m")    