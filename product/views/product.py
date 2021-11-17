from django.views.generic.edit import CreateView, UpdateView, DeleteView


class ProductCreateView(CreateView):
    model = Product


class ProductUpdateView(UpdateView):
    model = Product


class ProductDeleteView(DeleteView):
    model = Product
