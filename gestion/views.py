from django.shortcuts import render
from .models import Departamento




def index(request):
   return render(request, "gestion/index.html")




def departamentos(request):
    dept = Departamento()
    mensaje = None
    listado = []


    # lee de POST o GET indistintamente
    accion = request.POST.get('accion') or request.GET.get('accion')
    dept_no = request.POST.get('dept_no') or request.GET.get('dept_no')
    dnombre = request.POST.get('dnombre') or request.GET.get('dnombre')
    loc = request.POST.get('loc') or request.GET.get('loc')


    if accion == 'insertar':
        mensaje = dept.insert_dept(dept_no, dnombre, loc)
    elif accion == 'actualizar':
        mensaje = dept.update_dept(dept_no, dnombre, loc)
    elif accion == 'borrar':
        mensaje = dept.delete_dept(dept_no)
    elif accion == 'visualizar':
        mensaje = "Mostrando listado de departamentos"


    listado = dept.get_all()


    contexto = {
        "mensaje": mensaje,
        "listado": listado,
        "dept_no": dept_no or "",
        "dnombre": dnombre or "",
        "loc": loc or "",
    }


    return render(request, "gestion/insertar.html", contexto)




# Create your views here.





