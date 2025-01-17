import json
import os

class IntegerApiNode:
    CATEGORY = "api"
    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("output",)
    FUNCTION = "forward_number"

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "name": ("STRING", {"default": "name"}),
                "default_value": ("INT", {"default": 0}),
            },
        }

    def forward_number(self, name, default_value):
      return (default_value, )
