from upytl import (
    Component, Slot, SlotTemplate, UPYTL, html as h
)

from upytl_standard import * 

class TreeView(Component):
    """
    This class demonstrates the use of the `template_factory` method
    which allows to recursively use the component in its template.
    """
    props = dict(
        tree=[],
        depth=0
    )

    @staticmethod
    def template_factory(cls):
        TreeView = cls
        return {
            h.Div(For='it in tree', Style={'margin-left': {'f"{depth * 4}px"'} }): {
                h.Div(): '[[ it["name"] ]]',
                TreeView(If='"nodes" in it', depth={'depth+1'}, tree={'it["nodes"]'}): ''
            },
        }



# Now define a specific page template

t = {
    HTMLPage(footer_class='custom-footer'):{
        SlotTemplate(Slot='nav'):{
            StandardNavBar(menu={'menu'}, user={'user_name'}, buttons={'buttons'}): '',
        },
        SlotTemplate(Slot='content'):{
            h.Template():{
                h.Div(Class='box'):{
                    h.Div():{
                        Form(fields={'fields'}):'',
                    },
                },
                h.Div(Class='box'):{
                    h.H4(Class='title is-4'):'Tree-view example using template_factory():',
                    TreeView(tree={'tree'}):{}
                }
            },
        }
    }
}


# Define context

def URL():
    return 'https://github.com/valq7711/upytl'


# Keep in mind, that context (ctx) passed to render upytl.render
# is inaccessible in custom components, since components are similar to imported functions
# and component props and slots are similar to function arguments.
# So there is an optional `global_ctx` argument, which can be passed to UPYTL
# to provide access to desired stuff from anywhere including custom components

upytl = UPYTL(global_ctx=dict(URL=URL))

ctx = dict(
    page_title='UPYTL example',
    user_name = 'john',
    fields=[
        {'name': 'Text Field with value', 'value': 'Tom is the man','placeholder': 'Tom'},
        {'name': 'Email field with Placeholder', 'type':'email', 'placeholder': 'Email field placeholder'},
        {
            'name': 'Select Field', 'type': 'select', 'value': '#888888',
            'options': [
                dict(name='Choose red', value='#FF0000'),
                dict(name='Choose geen', value='#00FF00'),
                dict(name='Choose blue', value='#0000FF'),
                dict(name='Choose gray', value='#888888'),
            ],
        },
        {'name': 'Password Field', 'type': 'password'},
        {'name': 'Text Area Field', 'type': 'textarea', 'placeholder':'This is a textarea placeholder'},
        {'name': 'Radio Field', 'type': 'radio', 'value': False },
        {'name': 'Checkbox Field', 'type': 'checkbox', 'value': True },
        {'name': 'File Upload Field', 'type': 'file' },
    ],
    tree=[
        {
            'name': 'Top',
            'nodes': [
                {'name': 'child-1'},
                {
                    'name': 'child-2',
                    'nodes': [
                        {'name': '2-child-1'},
                        {'name': '2-child-2'},
                        {
                            'name': '2-child-3',
                            'nodes': [
                                {'name': '2-child-3/#1'},
                                {'name': '2-child-3/#2'},
                            ]
                        },
                    ]
                },
                {'name': 'child-3'},
            ]
        },
    ],
    menu = [
        {
            'label':'Home', 
            'href': 'Home'
        },
        {
            'label':'UPYTL',
            'child': [
                {
                    'label': 'About',
                },
                {
                    'label': 'Using',
                    'href' : 'using'
                },
                {
                    'label': 'Customising',
                    'href': 'customisng'
                },
            ]
        },
        {
            'label':'Components',
            'child': [
                {
                    'label': 'About',
                    'href': 'comp_about'
                },
                {
                    'label': 'Using',
                    'href' : 'comp_using'
                },
                {
                    'label': 'Customising',
                    'href': 'customisng'
                },
            ]
        },    
        {'label':'Another Menu'},
        {'label':'And one More'},
    ],
    buttons=[
        {'name':'Log In', 'href':'#'},
        {'name':'Profile', 'href':'#'},
        {'name':'Log Out', 'href':'#'},
    ]
)

rendered = upytl.render(t, ctx, indent=2)

print(rendered)

with open('example.html', 'w', encoding='utf8') as out:
    out.write(rendered)

print('\n'*2, '****** rendered with metatags ************')
print(upytl.render(t, ctx, indent=2, debug=True))