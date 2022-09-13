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


class Navbar(Component):
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
        field = None,
        val = None,
        err = None,
    )
    
    template = {
        h.Div(): {
            h.Template(If='field.type =="text"'):{
                TextAreaField(
                    field = {'field'},
                    val = {'val'},
                    err = {'err'}
        
                ): '',
            },
            h.Template(Elif='field.type=="select"'):{
                SelectField(
                    field = {'field'},
                    val = {'val'},
                    err = {'err'}
        
                ): '',
            },
            
            h.Template(Elif='field.type=="boolean"'):{
                h.Template(If='field.widget == "Checkbox"'):{
                    CheckBoxField(
                        field = {'field'},
                        val = {'val'},
                        err = {'err'}
        
                    ): '',    
                },
                h.Template(Elif='field.widget == "Radio"'):{
                    RadioField(
                        field = {'field'},
                        val = {'val'},
                        err = {'err'}
        
                    ): '',    
                },
                h.Template(Else=''):{
                    StringField(
                        field = {'field'},
                        val = {'val'},
                        err = {'err'}
                    ): '',
                },    
            },
            
            h.Template(Elif='field.type =="string"'):{
                StringField(
                    field={'field'},
                    val = {'val'},
                    err = {'err'}
                ): '',
            },
            
            h.Template(Elif='field.type=="upload"'):{
                FileField(
                    field={'field'},
                    val = {'val'},
                    err = {'err'}
                ): ''        
            },
            h.Template(Elif='field.type == "password"'):{
                PasswordField(
                    field={'field'},
                    val = {'val'},
                    err = {'err'}

                ): ''        
            },
        }
        
    }

class Form(Component):
    props = dict(
        fields=None,
        vals = {},
        errs = {},
        flash = None
    )
    template = {
        h.Form(If='fields', method='POST', Class='box', enctype='multipart/form-data'):{
            h.Template(For='fld in fields'):{
                h.Div(Class='field'):{
                    Field(
                    field = {'fld'},
                    val = {'vals.get(fld.name, None)'},
                    err = {'errs.get(fld.name, None)'},
                    ):{},
                },
            },
            h.Div(Class='field'):{
                h.Input(Class='button is-success is-light is-small', type='submit', value='Submit'): '',
                h.Input(Class='button is-danger is-light is-small', type='reset', value='Cancel'): '',
            }
        },
        h.Div(Else=''): 'Sorry, no fields were passed to this form'
    }
