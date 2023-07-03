from django.urls import path
from .views import AboutPageView, ClientePageView, HomePageView, AddClientePageView, MonitorPageView, \
    AddComputadorPageView, MousePageView, ComputadorPageView, AddMonitorPageView, AddMousePageView, DeleteClientView, \
    ProductOptionsView, ClientOptionsView, CompraPageView, DeleteMouseView, DeleteComputadorView, DeleteMonitorView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path("about", AboutPageView.as_view(), name="about"),
    path("cliente", ClientePageView.as_view(), name="cliente"),
    path("monitor", MonitorPageView.as_view(), name="monitor"),
    path("mouse", MousePageView.as_view(), name="mouse"),
    path("computador", ComputadorPageView.as_view(), name="computador"),
    path("IngresarCliente", AddClientePageView.as_view(), name='ingresar-cliente'),
    path("IngresarComputador", AddComputadorPageView.as_view(), name='ingresar-computador'),
    path("IngresarMonitor", AddMonitorPageView.as_view(), name='ingresar-monitor'),
    path("IngresarMouse", AddMousePageView.as_view(), name='ingresar-mouse'),
    path('get_product_options/', ProductOptionsView.as_view(), name='get_product_options'),
    path('get_client_options/', ClientOptionsView.as_view(), name='get_client_options'),
    path('Compra/', CompraPageView.as_view(), name='compra'),
    path('cliente/', DeleteClientView.as_view(), name='delete_data'),
    path('monitor/<int:pk>/eliminar/', DeleteMonitorView.as_view(), name='eliminar-monitor'),  # Nueva URL para eliminar monitor
    path('computador/<int:pk>/eliminar/', DeleteComputadorView.as_view(), name='eliminar-computador'),  # Nueva URL para eliminar computador
    path('mouse/<int:pk>/eliminar/', DeleteMouseView.as_view(), name='eliminar-mouse'),  # Nueva URL para eliminar mouse
]