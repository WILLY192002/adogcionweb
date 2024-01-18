import os
import jinja2
import pdfkit

def generar_reporte(animal, operaciones, enfermedades, vacunas, razayespecie):
    context = {
        'animal_name': animal.name,
        'animal_photo': animal.photo,
        'animal_age': animal.age,
        'animal_sex': animal.sex,
        'animal_size': animal.size,
        'animal_specie': razayespecie[1].name,
        'animal_breed': razayespecie[0].name,
        'animal_weight': animal.weight,
        'animal_observation': animal.observation,
        'operaciones': [f"{op.name}: {op.description}" for op in operaciones],
        'enfermedades': [f"{enf.name}: {enf.description}" for enf in enfermedades],
        'vacunas': [f"{vac.name}: {vac.description}" for vac in vacunas]
    }
    
    template_loader = jinja2.FileSystemLoader('./')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'src/templates/reporte.html'
    template = template_env.get_template(html_template)
    output_text = template.render(context)

    config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

    # Obtén la ruta a la carpeta de descargas
    descargas = os.path.join(os.path.expanduser('~'), 'Downloads')

    output_pdf = os.path.join(descargas, f'reporte_{animal.name}.pdf')
    pdfkit.from_string(output_text, output_pdf, configuration=config)
