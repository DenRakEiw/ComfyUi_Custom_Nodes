class PrintHelloWorld:

    @classmethod
    def INPUT_TYPES(cls):

               return {"required": {
                    "text": ("STRING", {"multiline": False, "default": "Hello World"}),
                    }
                }

    RETURN_TYPES = ()
    FUNCTION = "print_text"
    OUTPUT_NODE = True
    CATEGORY = "Tutorial Nodes"

    def print_text(self, text):

        print(f"Tutorial Text : {text}")
       
        return {}
    
    class ConcatenateHelloWorld:

    @classmethod
    def INPUT_TYPES(cls):

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "Tutorial Nodes"

    def concatenate_text(self, text1, text2):
       
        return {}

class ConcatenateHelloWorld:

    @classmethod
    def INPUT_TYPES(cls):

    RETURN_TYPES = ("STRING",)
    FUNCTION = "concatenate_text"
    CATEGORY = "Tutorial Nodes"

    def concatenate_text(self, text1, text2):
       
        return {}
