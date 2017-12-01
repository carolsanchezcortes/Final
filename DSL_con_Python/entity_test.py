from __future__ import unicode_literals
import os
from os.path import dirname, join
from textx.metamodel import metamodel_from_file
from textx.export import metamodel_export, model_export


this_folder = dirname(__file__)


class TipoSimple(object):
    """
    We are registering user SimpleType class to support
    simple types (integer, string) in our entity models
    Thus, user doesn't need to provide integer and string
    types in the model but can reference them in attribute types nevertheless.
    """
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name

    def __str__(self):
        return self.name


def get_categoria_mm(debug=False):
    """
    Builds and returns a meta-model for Entity language.
    """
    # Built-in simple types
    # Each model will have this simple types during reference resolving but
    # these will not be a part of `types` list of EntityModel.
    type_builtins = {
            'letra': TipoSimple(None, 'letra'),
            'letras': TipoSimple(None, 'letras'),
	    'numero': TipoSimple(None, 'numero')
    }
    categoria_mm = metamodel_from_file(join(this_folder, 'categoria.tx'),
                                    classes=[TipoSimple],
                                    builtins=type_builtins,
                                    debug=debug)

    return categoria_mm


def main(debug=False):

    categoria_mm = get_categoria_mm(debug)

    # Export to .dot file for visualization
    dot_folder = join(this_folder, 'dotexport')
    if not os.path.exists(dot_folder):
        os.mkdir(dot_folder)
    metamodel_export(categoria_mm, join(dot_folder, 'categoria_meta.dot'))

    # Build Person model from person.ent file
    modelo_categoria = categoria_mm.model_from_file(join(this_folder, 'tienda.ent'))

    # Export to .dot file for visualization
    model_export(modelo_categoria, join(dot_folder, 'tienda.dot'))


if __name__ == "__main__":
    main()
