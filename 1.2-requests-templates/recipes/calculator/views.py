from django.shortcuts import render, reverse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    template_name = 'calculator/home.html'
    return render(request, template_name)
# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def dish_recipe(request, dish):
    servings =  request.GET.get('servings')
    print(servings)
    template_name = 'calculator/index.html'
    context = {'recipe': {}}
    cont1 = {'recipe': {}}
    if dish in DATA:
        if servings:
            for ingredient, amount in DATA[dish].items():
                context['recipe'][ingredient] = amount * int(servings)
        else:
            context['recipe'] = DATA[dish]
    return render(request, 'calculator/index.html', context)