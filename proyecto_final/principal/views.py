from tracemalloc import get_object_traceback
from urllib import request
from django.db.models import Q # Required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import redirect_to_login
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.template import RequestContext
from django.views.generic import View,ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.urls import reverse_lazy

from principal.forms import *
from principal.models import *




class AccesoUsuarioColaborador(PermissionRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if(not self.request.user.is_authenticated):
            return redirect_to_login(self.request.get_full_path(),
                                    self.get_login_url(),self.get_redirect_field_name())
        if not self.has_permission():
            return redirect('/no_posee_permisos/')
        return super(AccesoUsuarioColaborador, self).dispatch(request, *args, **kwargs)


# Vistas inicio
def index(request):
    return render(request, 'principal/index.html')

def no_permisos(request):
    return render(request, 'principal/no_posee_permisos.html')
# Vista resumen
class VistaInicio(AccesoUsuarioColaborador,View):
    permission_required = ('principal.view_cliente')
    template_name = "principal/resumen.html"
    def get(self, request):        
        labels = []
        labels2 = []
        data = []
        data2 = []        
        stockqueryset = Inventario.objects.filter(borrado=False).order_by('-cantidad')
        for item in stockqueryset:
            labels.append(item.nombre)
            data.append(item.cantidad)
            data2.append(item.cantidadmin)
        # sales = SaleBill.objects.order_by('-fecha')[:3]
        purchases = ComprobanteCompra.objects.order_by('-fecha')[:5]
        sales = ComprobanteServicio.objects.order_by('-fechav')[:5]
        context = {
            'labels'    : labels,
            'data'      : data,
            'data2'     : data2,
            'sales'     : sales,
            'purchases' : purchases
        }
        return render(request, self.template_name, context)

# ClassBaseViews Colaborador Crear/Modificar/Eliminar/Leer
#Crear

class CrearColaborador(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_colaborador')
    model = Colaborador
    form_class = ColaboradorForm
    # fields = '__all__'
    success_url = reverse_lazy('lista_colaborador')
#Modificar
class ModificarColaborador(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_colaborador')
    model = Colaborador
    form_class = ColaboradorForm
    # fields = '__all__'
    success_url = reverse_lazy('lista_colaborador')
#Eliminar
class EliminarColaborador(AccesoUsuarioColaborador,View):
    permission_required = ('principal.change_colaborador')
    template_name = 'principal/colaborador_confirm_delete.html'
    success_message = "Colaborador Eliminado Exitosamente"

    def get(self, request, pk):
        colaborador = get_object_or_404(Colaborador, pk=pk)
        return render(request, self.template_name, {'object' : colaborador})

    def post(self, request, pk):  
        colaborador = get_object_or_404(Colaborador, pk=pk)
        colaborador.borrado = True
        colaborador.save()                                               
        return redirect('lista_colaborador')
#Leer
class LeerColaborador(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_colaborador')
    model = Colaborador
    queryset = Colaborador.objects.filter(borrado=False)
    
    
# ClassBaseViews Credito Crear/Modificar/Eliminar/Leer
#Crear
class CrearCredito(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_credito')
    model = Credito
    fields = '__all__'
    success_url = reverse_lazy('lista_credito')
#Modificar
class ModificarCredito(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_credito')
    model = Credito
    fields = '__all__'
    success_url = reverse_lazy('lista_credito')
#Eliminar
class EliminarCredito(AccesoUsuarioColaborador,DeleteView):
    permission_required = ('principal.delete_credito')
    queryset = Credito.objects.all()
    success_url = reverse_lazy('lista_credito')
#Leer
class LeerCredito(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_credito')
    model = Credito
    queryset = Credito.objects.all()
# ClassBaseViews Clientes Crear/Modificar/Eliminar/Leer
#Crear
class CrearCliente(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_cliente')
    model = Cliente
    # fields = '__all__'
    form_class = ClienteForm
    success_url = reverse_lazy('lista_cliente')
    

#Modificar
class ModificarCliente(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_cliente')
    model = Cliente
    # fields = '__all__'
    form_class = ClienteForm
    success_url = reverse_lazy('lista_cliente')

#Eliminar
class EliminarCliente(AccesoUsuarioColaborador,View):
    permission_required = ('principal.change_cliente')
    template_name = 'principal/cliente_confirm_delete.html'
    success_message = "Cliente Eliminado Exitosamente"

    def get(self, request, pk):
        cliente = get_object_or_404(Cliente, pk=pk)
        return render(request, self.template_name, {'object' : cliente})

    def post(self, request, pk):  
        cliente = get_object_or_404(Cliente, pk=pk)
        cliente.borrado = True
        cliente.save()                                               
        return redirect('lista_cliente')
    
#Leer
class LeerCliente(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_cliente')
    model = Cliente
    queryset = Cliente.objects.filter(borrado=False)


################################################################################################
# Muestra todos los proveedore
class LeerProveedor(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_proveedor')
    model = Proveedor
    queryset = Proveedor.objects.filter(borrado=False)


# used to add a new supplier
class CrearProveedor(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_proveedor')
    model = Proveedor
    form_class = ProveedorForm
    success_url = reverse_lazy('lista_proveedor')
    

# Utilizado para actualizar la información del proveedor
class ModificarProveedor(AccesoUsuarioColaborador,SuccessMessageMixin, UpdateView):
    permission_required = ('principal.change_proveedor')
    model = Proveedor
    form_class = ProveedorForm
    success_url = 'lista_proveedor'
    success_message = "Proveedor actualizado correctamente"



# # Utilizado para eliminar Proveedor
class EliminarProveedor(AccesoUsuarioColaborador,View):
    permission_required = ('principal.change_proveedor')
    template_name = 'principal/proveedor_confirm_delete.html'
    success_message = "Proveedor eliminado correctamente"

    def get(self, request, pk):
        proveedor = get_object_or_404(Proveedor, pk=pk)
        return render(request, self.template_name, {'object' : proveedor})

    def post(self, request, pk):  
        proveedor = get_object_or_404(Proveedor, pk=pk)
        proveedor.borrado = True
        proveedor.save()                                               
        return redirect('lista_proveedor')


# # Utilizado para ver la información del proveedor
class ProveedorVista(AccesoUsuarioColaborador,View):
    permission_required = ('principal.view_proveedor')
    def get(self, request, nombre):
        supplierobj = get_object_or_404(Proveedor, nombre=nombre)
        bill_list = ComprobanteCompra.objects.filter(proveedor=supplierobj)
        page = request.GET.get('page', 1)
        paginator = Paginator(bill_list, 10)
        try:
            bills = paginator.page(page)
        except PageNotAnInteger:
            bills = paginator.page(1)
        except EmptyPage:
            bills = paginator.page(paginator.num_pages)
        context = {
            'proveedor'  : supplierobj,
            'bills'     : bills
        }
        return render(request, 'principal/proveedor.html', context)
################################################################################################

# Muestra la lista de comprobantes de compras
class LeerCompra(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.add_comprobantecompra')
    model = ComprobanteCompra
    template_name = "principal/comprobantecompra_list.html"
    context_object_name = 'bills'
    ordering = ['-fecha']
    paginate_by = 10

# Selecciona al proveedor para la compra
class SeleccionarProveedorView(AccesoUsuarioColaborador,View):
    permission_required = ('principal.add_comprobantecompra')
    form_class = SeleccionarProveedor
    template_name = 'principal/select_proveedor.html'

    def get(self, request, *args, **kwargs):                                    # carga la pagina dle formulario
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):                                   # redirecciona del proveedor seleccionado a la pagina de compra
        form = self.form_class(request.POST)
        if form.is_valid():
            supplierid = request.POST.get("proveedor")
            proveedor = get_object_or_404(Proveedor, id=supplierid)
            return redirect('nueva_compra', proveedor.pk)
        return render(request, self.template_name, {'form': form})


# Utilizado para generar el comprabante y actulizar el invetario 
class CrearCompraView(AccesoUsuarioColaborador,View):                                                 
    permission_required = ('principal.add_detallecomprobanteCompra')
    template_name = 'principal/nueva_compra.html'

    def get(self, request, pk):
        formset = UnidadCompraFormset(request.GET or None)                      # Crea un formset vacio
        supplierobj = get_object_or_404(Proveedor, pk=pk)                        # Guarda al proveedor como objeto
        context = {
            'formset'   : formset,
            'proveedor'  : supplierobj,
        }                                                                       # Envia el proveedor y formset como objetos
        return render(request, self.template_name, context)

    def post(self, request, pk):
        formset = UnidadCompraFormset(request.POST)                             # obteine el formset de unidad compra
        supplierobj = get_object_or_404(Proveedor, pk=pk)                        # Obteine el objeto de proveedor
        if formset.is_valid():
            # Guarda el comprobante
            billobj = ComprobanteCompra(proveedor=supplierobj)                        # crea el objeto 'comprobnatecompra' y vincula el proveedor como  'supplierobj'
            billobj.save()                                                      # Guarda el comprobantecompra
            # Crea un objeto de detalle de comprobante
            billdetailsobj = DetalleComprobanteCompra(nocomp=billobj)
            billdetailsobj.save()
            for form in formset:                                                # for para ciclar cada unidad en su respectivo inventario
                # Guarda sin commit la unidad y vincuala el comprobante con la unidad
                billitem = form.save(commit=False)
                billitem.nocomp = billobj                                       # Vincula el comprobante a el inventario
                # Obtiene el inventario seguna el nombre de la unidad
                stock = get_object_or_404(Inventario, nombre=billitem.inventario.nombre)       # Obtiene la unidad del inventario
                # Calcula el precio total
                billitem.totalprecio = billitem.preciouni * billitem.cantidad
                # Actualiza la cantidad en el invetario
                stock.cantidad += billitem.cantidad                              # Actualiza cantidadad en inventario
                # Guarda el invetario y comprobante
                stock.save()
                billitem.save()
            messages.success(request, "Inventario actualizado correctamente")
            return redirect('compra_comprobante', nocomp=billobj.nocomp)
        formset = UnidadCompraFormset(request.GET or None)
        context = {
            'formset'   : formset,
            'proveedor'  : supplierobj
        }
        return render(request, self.template_name, context)


# Eliminar el comprobante en caso de inserciones erroenes
class EliminarCompra(AccesoUsuarioColaborador,SuccessMessageMixin, DeleteView):
    permission_required = ('principal.delete_comprobantecompra')
    model = ComprobanteCompra
    success_url = '/lista_compras/'
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = UnidadCompra.objects.filter(nocomp=self.object.nocomp)
        for item in items:
            stock = get_object_or_404(Inventario, nombre=item.inventario.nombre)
            if stock.borrado == False:
                stock.cantidad -= item.cantidad
                stock.save()
        return super(EliminarCompra, self).delete(*args, **kwargs)

class ComprobanteCompraView(View):
    permission_required = ('principal.view_comprobantecompra')
    model = ComprobanteCompra
    template_name = "principal/comprobante_compra.html"
    bill_base = "principal/base.html"

    def get(self, request, nocomp):
        context = {
            'bill'          : ComprobanteCompra.objects.get(nocomp=nocomp),
            'items'         : UnidadCompra.objects.filter(nocomp=nocomp),
            'billdetails'   : DetalleComprobanteCompra.objects.get(nocomp=nocomp),
            'bill_base'     : self.bill_base,
        }
        return render(request, self.template_name, context)

    def post(self, request, nocomp):
        form = DetalleCompraForm(request.POST)
        if form.is_valid():
            billdetailsobj = DetalleComprobanteCompra.objects.get(nocomp=nocomp)
            
            billdetailsobj.destino = request.POST.get("destino")
            billdetailsobj.total = request.POST.get("total")

            billdetailsobj.save()
            messages.success(request, "Detalle de comprobante actualizado correctamente")
        context = {
            'bill'          : ComprobanteCompra.objects.get(nocomp=nocomp),
            'items'         : UnidadCompra.objects.filter(nocomp=nocomp),
            'billdetails'   : DetalleComprobanteCompra.objects.get(nocomp=nocomp),
            'bill_base'     : self.bill_base,
        }
        return render(request, self.template_name, context)
################################################################################################
# shows the list of bills of all sales 
class LeerServicio(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.add_comprobanteservicio')
    model = ComprobanteServicio
    template_name = "principal/comprobanteservicio_list.html"
    context_object_name = 'bills'
    ordering = ['-fechav']

# used to generate a bill object and save items
class CrearServicioVista(AccesoUsuarioColaborador,View):    
    permission_required = ('principal.add_comprobanteservicio')                                                  
    template_name = 'principal/nuevo_servicio.html'

    def get(self, request):
        form = ServicioForm(request.GET or None)
        formset = VentaUnidadFormset(request.GET or None)                          # Crea un formset vacio
        stocks = Inventario.objects.filter(borrado=False)
        context = {
            'form'      : form,
            'formset'   : formset,
            'stocks'    : stocks
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = ServicioForm(request.POST)
        formset = VentaUnidadFormset(request.POST)                                 # Obtiene el metodo post del formset
        if form.is_valid() and formset.is_valid():
            # Guarda el comprobante
            billobj = form.save(commit=False)
            billobj.save()     
            # Crea un objeto detallecomprobanteservcio
            billdetailsobj = DetalleComprobanteServicio(nocomp=billobj)
            billdetailsobj.save()
            for form in formset:                                                # for que cicla cada elemento de servicios individualmete en su propio objeto
                # guarda sin commit para vincular el producto con el comprobante
                billitem = form.save(commit=False)
                billitem.nocomp = billobj                                       # vincula el comprobante con la unidad vendida
                # Obtine la unidad del invetario
                stock = get_object_or_404(Inventario, nombre=billitem.inventario.nombre)      
                # Calcula el precio total
                billitem.totalprecio = billitem.preciouni * billitem.cantidad
                # Actualiza la cantidad en el inventario
                stock.cantidad -= billitem.cantidad   
                # Guarda el comprobante y el inventario
                stock.save()
                billitem.save()
            messages.success(request, "Unidad Vendida ha sido registrada exitosamente")
            return redirect('comprobante_servicio', nocomp=billobj.nocomp)
        form = ServicioForm(request.GET or None)
        formset = VentaUnidadFormset(request.GET or None)
        context = {
            'form'      : form,
            'formset'   : formset,
        }
        return render(request, self.template_name, context)


# used to delete a bill object
class EliminarServicioView(AccesoUsuarioColaborador,SuccessMessageMixin, DeleteView):
    permission_required = ('principal.delete_comprobanteservicio')
    model = ComprobanteServicio
    success_url = '/lista_servicio/'
    
    def delete(self, *args, **kwargs):
        self.object = self.get_object()
        items = UnidadVendida.objects.filter(nocomp=self.object.nocomp)
        for item in items:
            stock = get_object_or_404(Inventario, nombre=item.inventario.nombre)
            if stock.borrado == False:
                stock.cantidad += item.cantidad
                stock.save()
        messages.success(self.request, "Comprobante de servicio eliminado correctamente")
        return super(EliminarServicioView, self).delete(*args, **kwargs)


class ComprobanteServicioView(AccesoUsuarioColaborador,View):
    permission_required = ('principal.view_comprobanteservicio')
    model = ComprobanteServicio
    template_name = "principal/comprobante_servicio.html"
    bill_base = "principal/base.html"
    
    def get(self, request, nocomp):
        context = {
            'bill'          : ComprobanteServicio.objects.get(nocomp=nocomp),
            'items'         : UnidadVendida.objects.filter(nocomp=nocomp),
            'billdetails'   : DetalleComprobanteServicio.objects.get(nocomp=nocomp),
            'bill_base'     : self.bill_base,
        }
        return render(request, self.template_name, context)

    def post(self, request, nocomp):
        form = DetalleServicioForm(request.POST)
        if form.is_valid():
            billdetailsobj = DetalleComprobanteServicio.objects.get(nocomp=nocomp)
            
            billdetailsobj.tiposervicio = request.POST.get("tiposervicio")
            billdetailsobj.descripcion = request.POST.get("descripcion")
            billdetailsobj.total = request.POST.get("total")

            billdetailsobj.save()
            messages.success(request, "Detalle de comprobante actualizado correctamente")
        context = {
            'bill'          : ComprobanteServicio.objects.get(nocomp=nocomp),
            'items'         : UnidadVendida.objects.filter(nocomp=nocomp),
            'billdetails'   : DetalleComprobanteServicio.objects.get(nocomp=nocomp),
            'bill_base'     : self.bill_base,
        }
        return render(request, self.template_name, context)

################################################################################################
# ClassBaseViews Inventario Crear/Modificar/Eliminar/Leer
#Crear
class CrearInventario(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_inventario')
    model = Inventario
    form_class = InventarioForm
    # fields = ('categoria', 'nombre', 'cantidad', 'medida','cantidadmin')
    success_url = reverse_lazy('lista_inventario')
#Modificar
class ModificarInventario(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_inventario')
    model = Inventario
    form_class = InventarioForm
    # fields = ('categoria', 'nombre_p', 'cantidad','cantidadmin')
    success_url = reverse_lazy('lista_inventario')
#Eliminar
class EliminarInventario(AccesoUsuarioColaborador,View):
    permission_required = ('principal.change_inventario')
    template_name = 'principal/inventario_confirm_delete.html'
    
    def get(self, request, pk):
        inventario = get_object_or_404(Inventario, pk=pk)
        return render(request, self.template_name,{'object':inventario})
    
    def post(self, request, pk):  
        inventario = get_object_or_404(Inventario, pk=pk)
        inventario.borrado = True
        inventario.save()                                               
        return redirect('lista_inventario')
        
#Leer
class LeerInventario(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_inventario')
    model = Inventario
    queryset = Inventario.objects.filter(borrado=False)

# ClassBaseViews Inventario Crear/Modificar/Eliminar/Leer
#Crear
class CrearCategorias(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_categorias')
    model = Categorias
    fields = '__all__'
    success_url = reverse_lazy('lista_categorias')
#Modificar
class ModificarCategorias(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_categorias')
    model = Categorias
    fields = '__all__'
    success_url = reverse_lazy('lista_categorias')
#Eliminar
class EliminarCategorias(AccesoUsuarioColaborador,View):
    permission_required = ('principal.change_inventario')
    template_name = 'principal/categorias_confirm_delete.html'
    
    def get(self, request, pk):
        categoria = get_object_or_404(Categorias, pk=pk)
        return render(request, self.template_name,{'object':categoria})
    
    def post(self, request, pk):  
        categoria = get_object_or_404(Categorias, pk=pk)
        categoria.borrado = True
        categoria.save()                                               
        return redirect('lista_categorias')
    
#Leer
class LeerCategorias(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_categorias')
    model = Categorias
    queryset = Categorias.objects.filter(borrado=False)

# ClassBaseViews Solicitud Crear/Modificar/Eliminar/Leer
#Crear
class CrearSolicitud(AccesoUsuarioColaborador,CreateView):
    permission_required = ('principal.add_solicitud')
    model = Solicitud
    form_class = SolicitudForm
    # fields = '__all__'
    success_url = reverse_lazy('lista_solicitud')
#Modificar
class ModificarSolicitud(AccesoUsuarioColaborador,UpdateView):
    permission_required = ('principal.change_solicitud')
    model = Solicitud
    fields = '__all__'
    success_url = reverse_lazy('lista_solicitud')
#Eliminar
class EliminarSolicitud(AccesoUsuarioColaborador,DeleteView):
    permission_required = ('principal.delete_solicitud')
    queryset = Solicitud.objects.all()
    success_url = reverse_lazy('lista_solicitud')
#Leer
class LeerSolicitud(AccesoUsuarioColaborador,ListView):
    permission_required = ('principal.view_solicitud')
    model = Solicitud
    queryset = Solicitud.objects.all()
    paginate_by = 10
    def get_queryset(self):
        q = self.request.GET.get('q')
        if q:
            object_list = self.model.objects.filter(
                Q(cliente__nombre__icontains=q) | Q(colaborador__nombre__icontains=q) | Q(descripcion__icontains=q) 
                | Q(fecha__icontains=q) | Q(pago__icontains=q)
            )
        else:
            object_list = self.model.objects.all()
        return object_list

@login_required
def special(request):
    return HttpResponse('Iniciaste sesión!')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registrado = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registrado = True
        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'principal/register.html',
                            {'user_form':user_form,
                            'profile_form':profile_form,
                            'registrado':registrado})

def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('resumen'))
            else:
                HttpResponse('La Cuenta no esta activa')
        else:
            print('Alguien intento entrar')
            print('Username:{} and password {}'.format(username, password))
            return HttpResponse('datos de inicio de sesion invalidos')
    else:
        return render(request,'principal/login.html',{})


def error_404_view(request, exception):
    return render(request, 'principal/404.html')