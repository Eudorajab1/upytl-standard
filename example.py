from upytl import (
    Component, Slot, SlotTemplate, UPYTL, html as h
)

from upytl_standard import (
    StandardField,
    StandardForm,
    StandardNavBar,
    DTGrid,
    HTMLPage,
    HTMLGrid,
    TreeView,

)


# Now define a specific page template

t = {
    HTMLPage(footer_class='custom-footer'):{
        SlotTemplate(Slot='nav'):{
            StandardNavBar(menu={'menu'}, user={'user_name'}, buttons={'buttons'}): '',
        },
        SlotTemplate(Slot='flash'):{
            h.Div(Class="notification is-success has-text-centered"):'Hello and Welcome to the Standard UPYTL components. I am a simulated FLASH message',
        },
        SlotTemplate(Slot='content'):{
            h.Template():{
                h.Div(Class='box'):{
                    h.Div(Class='title is-5'):'Standard Form Component with Sample Fields',
                    
                    h.Div():{
                        StandardForm(fields={'fields'}):'',
                    }
                },
                
                h.Div(Class='box'):{
                    h.Div(Class='title is-5'):'DataTables Grid',
                    DTGrid(
                        title={'grid.get("title")'}, 
                        name={'grid.get("name")'},
                        grid_buttons={'grid.get("grid_buttons")'},
                        columns={'grid.get("columns")'},
                        labels={'grid.get("labels")'}, 
                        data={'grid.get("data")'}
                    ): {},
                },
                h.Div(Class='box'):{
                    h.Div(Class='title is-5'):'HTML Grid',
                    HTMLGrid(
                        title={'grid.get("title")'}, 
                        name={'grid.get("name")'},
                        grid_buttons={'grid.get("grid_buttons")'},
                        columns={'grid.get("columns")'},
                        labels={'grid.get("labels")'}, 
                        data={'grid.get("data")'}
                    ): {},
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

cfg = dict(href_prefix = 'app_name')

def URL(rel_href):
    return f'{cfg["href_prefix"]}/{rel_href}'

u = UPYTL(global_ctx=dict(CFG=cfg, URL=URL))

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
        {'name':'string', 'label': 'Text Field with value', 'value': 'Tom is the man','placeholder': 'Tom'},
        {'name':'email', 'label':'Email field with Placeholder', 'type':'email', 'placeholder': 'Email field placeholder'},
        {
            'name':'select', 'label': 'Select Field', 'type': 'select', 'value': '#888888',
            'options': [
                dict(name='Choose red', value='#FF0000'),
                dict(name='Choose geen', value='#00FF00'),
                dict(name='Choose blue', value='#0000FF'),
                dict(name='Choose gray', value='#888888'),
            ],
        },
        {'name':'password','label': 'Password Field', 'type': 'password'},
        {'name':'textarea', 'label': 'Text Area Field', 'type': 'textarea', 'placeholder':'This is a textarea placeholder'},
        {'name': 'Radio Field', 'type': 'radio', 'value': False },
        {'name': 'Checkbox Field', 'type': 'checkbox', 'value': True },
        {'name': 'upload', 'label':'File Upload Field', 'type': 'file' },
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
    ],
    grid={
        'title': 'Standard Grid Components',
        'name': "standard_grid", 
        'grid_buttons':[],
        'columns': [{'data':'id'}, {'data':'first_name'}, {'data':'last_name'}, {'data':'age'}, {'data':'status'}],
            #
        #],
        'labels':['Id', 'First Name', 'Last Name', 'Age', 'Status'],
        'data': [
            {'id':'1', 'first_name': 'Peter', 'last_name': 'Parker', 'age':'12', 'status':'Undertmined'},
            {'id':'2', 'first_name': 'Joe', 'last_name': 'Bloggs', 'age':'89', 'status':'Somewhere'},
            {'id':'3', 'first_name': 'Valery', 'last_name': 'Elliot', 'age':'22', 'status':'Busy'},
            {'id':'4', 'first_name': 'Joan', 'last_name': 'Bayez', 'age':'19', 'status':'Chilling'},
            {'id':'5', 'first_name': 'Emma', 'last_name': 'Clapton', 'age':'24', 'status':'Working'},
            {'id':'6', 'first_name': 'Jolene', 'last_name': 'Jolene', 'age':'26', 'status':'Sleeping'},
            {'id':'7', 'first_name': 'Kevin', 'last_name': 'Kostner', 'age':'33', 'status':'Eating'},
            {'id':'8', 'first_name': 'Peter', 'last_name': 'Parker', 'age':'12', 'status':'Undertmined'},
            {'id':'9', 'first_name': 'Joe', 'last_name': 'Bloggs', 'age':'89', 'status':'Somewhere'},
            {'id':'10', 'first_name': 'Valery', 'last_name': 'Elliot', 'age':'22', 'status':'Busy'},
            {'id':'11', 'first_name': 'Joan', 'last_name': 'Bayez', 'age':'19', 'status':'Chilling'},
            {'id':'12', 'first_name': 'Emma', 'last_name': 'Clapton', 'age':'24', 'status':'Working'},
            {'id':'13', 'first_name': 'Jolene', 'last_name': 'Jolene', 'age':'26', 'status':'Sleeping'},
            {'id':'14', 'first_name': 'Kevin', 'last_name': 'Kostner', 'age':'33', 'status':'Eating'},
        ],
    }
)

rendered = upytl.render(t, ctx, indent=2)

print(rendered)

with open('example.html', 'w', encoding='utf8') as out:
    out.write(rendered)

print('\n'*2, '****** rendered with metatags ************')
print(upytl.render(t, ctx, indent=2, debug=True))