
def menu(context, variables):
    return [
       {   'name' : 'News',
           'class' : 'news_menu_item',
           'url' : reverse('news'),
           'match' : r'^'+ reverse('news') + r'$',
           'sub' : None,
       },

    ]
