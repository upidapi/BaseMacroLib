class BaseVk:
    """ 
    exposes the attributes of a vk enum 
    also uses those attributes to a few helper funcs 
    """
    def __init_subclass__(cls, *_, **__):
        """
        some trickery to get the (sub) class __dict__
        then find all manually added attributes (vk(s))
        and add them to a dict
        """
        cls._keyname_to_v_code_map = {
            key: val for key, val in cls.__dict__.items()
            if not (key.startswith("__") and key.endswith("__"))
        }

        cls._v_code_to_keyname_map = {
            val: key for key, val in cls._keyname_to_v_code_map.items()
        }

    @classmethod
    def keyname_to_v_code(cls, keyname):
        """ convert a keyname to a vk """
        return cls._keyname_to_v_code_map[keyname]


    @classmethod
    def v_code_to_keyname(cls, v_code):
        """ convert a vk to a keyname """
        return cls._v_code_to_keyname_map[v_code]
