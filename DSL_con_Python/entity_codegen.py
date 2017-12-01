"""
An example how to generate angularjs code from textX model using jinja2
template engine (http://jinja.pocoo.org/docs/dev/)
"""
from os import mkdir
from os.path import exists, dirname, join
import jinja2
from entity_test import get_categoria_mm


def main(debug=False):

    this_folder = dirname(__file__)

    categoria_mm = get_categoria_mm(debug)

    # Build Person model from person.ent file
    modelo_tienda = categoria_mm.model_from_file(join(this_folder, 'tienda.ent'))

    def javatype(s):
        return {
                'letra': 'char',
                'letras': 'String',
		'numero': 'int'
        }.get(s.name, s.name)

    # Create output folder
    vistaHTML_folder = join(this_folder, 'vistaHTML')
    if not exists(vistaHTML_folder):
        mkdir(vistaHTML_folder)

    # Initialize template engine.
    jinja_env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(this_folder),
        trim_blocks=True,
        lstrip_blocks=True)

    # Register filter for mapping Entity type names to Java type names.
    #jinja_env.filters['javatype'] = javatype

     # Load template
    template = jinja_env.get_template('vista.template')

    for categoria in modelo_tienda.categorias:
        # For each entity generate java file
        with open(join(vistaHTML_folder,
                       "%s.html" % categoria.name), 'w') as f:
            f.write(template.render(categoria=categoria))

    template = jinja_env.get_template('estilos.template')

    for categoria in modelo_tienda.categorias:
        # For each entity generate java file
        with open(join(vistaHTML_folder,
                       "%s_estilo.css" % categoria.name), 'w') as f:
            f.write(template.render(categoria=categoria))		

 

if __name__ == "__main__":
    main()
