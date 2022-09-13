from upytl import (
    Component, Slot, html as h
)

class HTMLPage(Component):
    props = dict(
        footer_class='page-footer',
        page_title="This is the page_title placeholder",
        nav = "This is our navbar placeholder"
    )
    template = {
        h.Html(): {
            h.Head():{
                h.Title(): '[[page_title]]',
                h.Meta(charset=b'utf-8'):'',
                },
            h.Body():{
                
                h.Link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.4/css/bulma.min.css'):None, 

                h.Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css", integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==", crossorigin="anonymous"):None,
                
                Slot(SlotName=b'nav'):{
                    h.Div():'No NavBar passed to the form'
                },
                Slot(SlotName=b'content'):{h.Div(): '[there is no default content]'},
                Slot(SlotName=b'footer'):{h.Div(): 'This is the footer placeholder'},
            }
        }
    }

class NavBarItem(Component):
    props = dict(
        item = dict(label = 'No Item'),
    )
    template = {
        h.Template(If='not item.get("child")'):{
            h.A(Class='navbar-item has-text-primary is-size-5', Href={'item.get("href")'}): "[[ item['label'] ]]",
        },
        h.Template(Else=''):{
            h.Div(Class='navbar-item has-dropdown is-hoverable'): {
                h.A(Class='navbar-link has-text-primary is-size-5 has-text-weight-semibold is-arrowless'): "[[ item['label'] ]]",
                h.Div(Class='navbar-dropdown is-boxed'): {
                    h.Template(For='ch in item.get("child")'): {
                        h.Template(If='not ch.get("child")'):{
                            h.A(Class='navbar-item', Href={'ch.get("href", "index")'}): "[[ ch['label'] ]]",
                        },
                        h.Template(Else=''): {
                            h.Div(Class='navbar-item has-dropdown'): {
                                h.A(Class='navbar-link'): "[[ ch['label'] ]]",
                                h.Div(Class='navbar-dropdown'): {
                                    h.Template(For='c in ch.get("child")'): {
                                        h.A(Class='navbar-item', Href={'c.get("href", "index")'}): "[[ c['label'] ]]",
                                    }
                                }
                            }
                        }    
                    }
                }
            }
        }
    }


class NavBar(Component):
    props = dict(
        menu = [],
    )
    template = {
        h.Nav(Class='navbar is-light', Role='navigation'): {
            h.Div(Class='navbar-brand'): {
                h.A(Class='navbar-item', href="https://bulma.io"): '',   
            },
            h.Div(Id="navbarBasicExample", Class="navbar-menu"):{
                h.Div(Class='navbar-start'):{
                    h.Template(For='item in menu'):{
                        NavBarItem(
                            item = {'item'},
                        ):'',
                    },
                },
            }
        }    
    }
   
class TextAreaField(Component):
    props = dict(
        field = None,
        val = None,
        err = None
    )
    template = {
        h.Label(Class='label'):{
            h.Text():'[[field.label]]',
        },
        h.Div(Class='control'): {
            h.Textarea(Class='textarea', name={'field.name'}):'[[val]]',
        },
        h.P(If='err', Class='help has-text-danger'): '[[ err ]]'    
    } 

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
    def template_factory():
        return {
            h.Div(For='it in tree', Style={'margin-left': {'f"{depth * 4}px"'} }): {
                h.Div(): '[[ it["name"] ]]',
                TreeView(If='"nodes" in it', depth={'depth+1'}, tree={'it["nodes"]'}): ''
            },
        }


class StringField(Component):
    props = dict(
        field = None,
        val = None,
        err = None
    )
    template = {
        h.Template():{
            h.Label(Class='label'):{
                h.Text():'[[field.label ]]',
                h.Div(Class='control'): {
                h.Input(Class='input', type='text', name={'field.name'}, value={'val'}):'',
            },
            h.P(Class='help has-text-danger'): '[[ err ]]'    
        
            },
        }    
    }

class PasswordField(Component):
    props = dict(
        field = None,
        val = None,
        err = None
    )
    template = {
        h.Label(Class='label required'):{
            h.Text():'[[field.label ]]',
            },
            h.Div(Class='control'): {
                h.Input(Class='input', type='password', name={'field.name'}, value={'val'}):'',
            },
            h.P(If='err', Class='help has-text-danger'): '[[ err ]]'
    }

class SelectField(Component):
    props = dict(
        field = None,
    )
    template = {
        h.Label(Class='label'):{
        h.Text():'[[field.get("name") ]]',
        },
        h.Div(Class='control'): {
            h.Select(name={'field.get("name")'}):{
                h.Option(For='opt in field.get("options")', Class="js-states form-control", value={'opt.get("value")'}): 
                    '[[ opt.get("name", opt["value"]) ]]'
            },    
        }
    }    
class FileField(Component):
    props = dict(
        field = None,
        val = {},
        err = {}
    )
    template = {
        h.Label(Class='label'):{
            h.Text():'[[field.name]]',
        },
        h.Input(type='file', name={'field.name'}, accept="image/*"):'',
    }

class CheckBoxField(Component):
    props = dict(
        field = None,
        val = None,
        err = None
    )
    template = {
        h.Label(Class='checkbox'):{
            h.Template(If='val'):{
                h.Input(type='checkbox', name={'field.name'},checked=''):'[[field.name]]',
            },
            h.Template(Else=''):{
                h.Input(type='checkbox', name={'field.name'}):'[[field.name]]',
                
            }
            
        },
        h.P(If='err', Class='help has-text-danger'): '[[ err ]]'
            
    }

class RadioField(Component):
    props = dict(
        field = None,
        val = None,
        err = None
    )
    template = {
        h.Div(Class='control'): {
            h.Label(Class="radio"):None,
            
            h.Template(If='val'):{
                h.Input(If='val', checked='', Type='radio', name={'field.name'}):'[[field.name]]',
            },
            h.Template(Else=''):{
                h.Input(If='val', Type='radio', name={'field.name'}):'[[field.name]]',
                
            },
                
        },
        h.P(If='err', Class='help has-text-danger'): '[[ err ]]'
        
    }


class Field(Component):
    props = dict(
        name='[no name]',
        value='',
        type='text',
        # for select
        options=[],
    )
    template = {
        
        h.Div(Class='field'):{
            h.Label(If='type=="text"'):{
                h.Text():'[[name]]',
                h.Div(Class='control'):{
                    h.Input(name='{name}', value='{value}'):'',        
                },
            },
            h.Label(Elif='type=="select"'):{
                h.Text():'[[name]]',
                h.Select(name='{name}'):{
                    h.Option(For='opt in options', value='{opt[value]}', selected={'opt["value"]==value'}):
                         '[[ opt.get("name", opt["value"]) ]]'
                },
            },
        }            
        
    }
class Form(Component):
    props = dict(
        fields=None
    )
    template = {
        h.Form(If='fields', action='#'):{
            h.Div(For='fld in fields', Style={'margin':'15px'}):{
                Field(
                    name='{fld[name]}',  type={'fld.get("type", "text")'},
                    value={'fld.get("value", "")'},
                    options={'fld.get("options", None)'},
                ):'',
            },
            h.Button(type='submit'): 'Submit'
        },
        h.Div(Else=''): 'Sorry, no fields were passed to this form'
    }
