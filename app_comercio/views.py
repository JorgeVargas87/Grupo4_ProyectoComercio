from django.contrib.messages.views import SuccessMessageMixin
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, CreateView

from .forms import ClienteForm, MonitorForm, ComputadorForm, MouseForm
from .models import Cliente, Monitor, Mouse, Computador, Producto
from django.http import JsonResponse
from django.apps import apps


class HomePageView(TemplateView):
    template_name = "home.html"


class CompraPageView(TemplateView):
    template_name = "Compra.html"

    def post(self, request):
        product_id = request.POST.get('product')
        client_id = request.POST.get('client')
        selected_product = request.POST.get('selected_product')
        if selected_product == 'monitor':
            monitor = Monitor.objects.get(pk=product_id)
            cliente = Cliente.objects.get(pk=client_id)
            cliente.compraMonitor.add(monitor)
            cliente.save()
        elif selected_product == 'mouse':
            mouse = Mouse.objects.get(pk=product_id)
            cliente = Cliente.objects.get(pk=client_id)
            cliente.compraMouse.add(mouse)
            cliente.save()
        elif selected_product == 'computer':
            computer = Computador.objects.get(pk=product_id)
            cliente = Cliente.objects.get(pk=client_id)
            cliente.compraComputador.add(computer)
            cliente.save()
        else:
            return JsonResponse({'error': 'Producto seleccionado invalido.'}, status=400)

        return JsonResponse({'message': 'Compra existosa.'})


class AboutPageView(TemplateView):
    template_name = "about.html"


class ClientePageView(ListView):
    model = Cliente
    template_name = "cliente.html"
    context_object_name = 'data'
    http_method_names = ['get', 'post']


class MonitorPageView(ListView):
    model = Monitor
    template_name = "monitor.html"
    context_object_name = 'data'


class MousePageView(ListView):
    model = Mouse
    template_name = "mouse.html"
    context_object_name = 'data'


class ComputadorPageView(ListView):
    model = Computador
    template_name = "computador.html"
    context_object_name = 'data'


class AddClientePageView(SuccessMessageMixin, CreateView):
    form_class = ClienteForm
    template_name = 'IngresarCliente.html'
    success_message = 'Cliente Ingresado'
    error_message = "Error en ingresar a un cliente"
    success_url = reverse_lazy("ingresar-cliente")

    def get_success_url(self):
        return reverse('ingresar-cliente')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AddMonitorPageView(SuccessMessageMixin, CreateView):
    form_class = MonitorForm
    template_name = 'IngresarMonitor.html'
    success_message = 'Monitor Ingresado'
    error_message = "Error en ingresar a un monitor"
    success_url = reverse_lazy("ingresar-monitor")

    def get_success_url(self):
        return reverse('ingresar-monitor')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AddComputadorPageView(SuccessMessageMixin, CreateView):
    form_class = ComputadorForm
    template_name = 'IngresarComputador.html'
    success_message = 'Computador Ingresado'
    error_message = "Error en ingresar a un computador"
    success_url = reverse_lazy("ingresar-computador")

    def get_success_url(self):
        return reverse('ingresar-computador')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class AddMousePageView(SuccessMessageMixin, CreateView):
    form_class = MouseForm
    template_name = 'IngresarMouse.html'
    success_message = 'Mouse Ingresado'
    error_message = "Error en ingresar a un mouse"
    success_url = reverse_lazy("ingresar-mouse")

    def get_success_url(self):
        return reverse('ingresar-mouse')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class DeleteClientView(View):
    template_name = 'cliente.html'
    success_url = 'cliente'

    def post(self, request):
        selected_items = request.POST.getlist('selected_items')

        # Validate and sanitize the selected_items
        try:
            selected_items = list(map(int, selected_items))  # Convert to a list of integers
        except ValueError:
            raise Http404("Invalid input for selected_items")

        # Perform the deletion
        Cliente.objects.filter(rut__in=selected_items).delete()

        return redirect(self.success_url)  # Redirect to a success page or another view

    def get(self, request):
        return render(request, self.template_name)


class ProductOptionsView(View):
    def get(self, request):
        selected_product = request.GET.get('selected_product')

        product_model = apps.get_model('app_comercio', selected_product.capitalize())
        if product_model is None or not issubclass(product_model, Producto):
            return JsonResponse({'error': 'Invalid product selected.'}, status=400)

        # Query the database to get the appropriate product options based on the selected_product
        product_options = product_model.objects.all()
        options = [{'id': option.idProducto, 'name': option.marca + " " + str(option.precioUnitario)} for option in
                   product_options]
        return JsonResponse({'options': options})


class ClientOptionsView(View):
    def get(self, request):
        # Query the database to get the client options
        client_options = Cliente.objects.all()
        options = [{'rut': option.rut, 'name': option.nombre} for option in client_options]
        return JsonResponse({'options': options})


class DeleteMouseView(View):
    template_name = 'mouse.html'
    success_url = 'mouse'

    def post(self, request, pk):
        mouse = Mouse.objects.get(pk=pk)
        mouse.delete()

        return redirect(self.success_url)

    def get(self, request):
        return render(request, self.template_name)


class DeleteComputadorView(View):
    template_name = 'computador.html'
    success_url = 'computador'

    def post(self, request, pk):
        computador = Computador.objects.get(pk=pk)
        computador.delete()

        return redirect(self.success_url)

    def get(self, request):
        return render(request, self.template_name)


class DeleteMonitorView(View):
    template_name = 'monitor.html'
    success_url = 'monitor'

    def post(self, request, pk):
        monitor = Monitor.objects.get(pk=pk)
        monitor.delete()

        return redirect(self.success_url)

    def get(self, request):
        return render(request, self.template_name)
