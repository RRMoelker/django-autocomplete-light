import autocomplete_light


class AutocompleteModel(autocomplete_light.AutocompleteModel):
    def __init__(self, request=None, values=None):
        if request and getattr(self.choices.model.objects, 'language', False):
            self.choices = self.choices.model.objects.language(request.LANGUAGE_CODE)
        super(AutocompleteModel, self).__init__(request, values)


class AutocompleteModelBase(AutocompleteModel, autocomplete_light.AutocompleteBase):
    pass


class AutocompleteModelTemplate(AutocompleteModel, autocomplete_light.AutocompleteTemplate):
    pass