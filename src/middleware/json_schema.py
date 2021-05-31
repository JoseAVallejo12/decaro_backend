from kanpai import Kanpai


schema = Kanpai.Object({
    'primer_nombre': Kanpai.String().trim().required("primer_nombre is required"),
    'segundo_nombre': Kanpai.String().trim(),
    'primer_apellido': Kanpai.String().trim().required("primer_apellido is required"),
    'segundo_apellido': Kanpai.String().trim(),
    'cedula': Kanpai.String().trim().required("cedula is required"),
    'area_a_ingresar': Kanpai.String().trim(),
    'telefono': Kanpai.String().trim().required("telefono is required"),
    'direccion_residencia': Kanpai.String().trim(),
})

