from upytl import (
    Component, Slot, SlotTemplate, UPYTL, html as h
)

from upytl_standard import * 

# Now define a specific page template

t = {
    HTMLPage(footer_class='custom-footer'):{
        
        SlotTemplate(Slot='content'):{
            h.Div(Class='box'):(
                'Hey [[ user_name.title() ]]! How are you?'
            ),
            h.Div(Class='box'):{
                Form(fields={'fields'}):''
            },
#            h.H4():'Tree-view example:',
#            TreeView(tree={'tree'}):{}
        },
        
    
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
        {'name': 'Friend Name', 'value': 'Tom?'},
        {'name': 'Email'},
        {
            'name': 'Favorite Color', 'type': 'select', 'value': '#888888',
            'options': [
                dict(name='red', value='#FF0000'),
                dict(name='geen', value='#00FF00'),
                dict(name='blue', value='#0000FF'),
                dict(name='gray', value='#888888'),
            ],
        }
    ],
)

rendered = upytl.render(t, ctx, indent=2)

print(rendered)

with open('example.html', 'w', encoding='utf8') as out:
    out.write(rendered)

print('\n'*2, '****** rendered with metatags ************')
print(upytl.render(t, ctx, indent=2, debug=True))