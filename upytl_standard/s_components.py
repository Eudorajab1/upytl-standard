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
                h.Link(rel="stylesheet", href="https://cdn.datatables.net/1.10.24/css/jquery.dataTables.min.css"):None,
                h.Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.14.0/css/all.min.css", integrity="sha512-1PKOgIY59xJ8Co8+NE6FZ+LOAZKjy+KY8iq0G4B3CyeY6wYHN3yt9PW0XpSriVlkMXe40PTKnXrLnZ9+fkDaog==", crossorigin="anonymous"):None,
                h.Script(src="https://code.jquery.com/jquery-3.5.1.js"):None,
                h.Script(src="https://cdn.datatables.net/1.10.24/js/jquery.dataTables.min.js"):None,
                    
                Slot(SlotName=b'nav'):{
                    h.Div():'No NavBar passed to the form'
                },
                Slot(SlotName=b'content'):{h.Div(): '[there is no default content]'},
                Slot(SlotName=b'footer'):{
                    h.Footer(Class="footer is-small"):{
                        h.Div(Class= "content has-text-centered"):{
                            h.Template():{
                                h.P(): 'Powered by UPYTL Standard Components (c) 2022',
                            }    
                        }
                    }
                }
            }
        }
    }

class NavBarItem(Component):
    props = dict(
        item = dict(label = 'No Item'),
    )
    template = {
        h.Template(If='not item.get("child")'):{
            h.A(Class='navbar-item', Href={'item.get("href")'}): "[[ item['label'] ]]",
        },
        h.Template(Else=''):{
            h.Div(Class='navbar-item has-dropdown is-hoverable'): {
                h.A(Class='navbar-link'): "[[ item['label'] ]]",
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

class StandardNavBar(Component):
    props = dict(
        menu = [],
        user = '',
        buttons=[]
    )
    template = {
        h.Nav(Class='navbar', Role='navigation'): {
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
                h.Div(Class='navbar-end'): {
                    h.Div(Class='navbar-item'): {
                        h.Div(): 'Welcome [[ user.title() ]]',
                    },
                    h.Div(Class='navbar-item'): {
                        h.Template(If = 'not buttons'):{
                            h.Div(): '',
                        },
                        h.Template(Else = ''):{
                            h.Div(Class='buttons'):{
                                h.A(For = 'b in buttons',Class={'b.get("class", "button")'}, Href={'b.get("href", "index")'}):'[[ b["name"] ]]',
                            },
                        }        
                    }
                }
            }
        }    
    }
   
class TextAreaField(Component):
    props = dict(
        name='[no name]',
        value=None,
        type='textarea',
        placeholder = None,
        error = ''
    )
    template = {
        h.Label(Class='label'):{
            h.Text():'[[name]]',
        },
        h.Div(Class='control'): {
            h.Textarea(Class='textarea', placeholder='placeholder'):'[[value]]',
        },
        h.P(If='error', Class='help has-text-danger'): '[[ error ]]'    
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
    def template_factory(cls):
        TreeView = cls
        return {
            h.Div(For='it in tree', Style={'margin-left': {'f"{depth * 4}px"'} }): {
                h.Div(): '[[ it["name"] ]]',
                TreeView(If='"nodes" in it', depth={'depth+1'}, tree={'it["nodes"]'}): ''
            },
        }

class StringField(Component):
    props = dict(
        name='[no name]',
        value='',
        type='string',
        placeholder= '',
        error = ''
    )
    template = {
        h.Template():{
            h.Label(Class='label'):{
                h.Text():'[[ name ]]',
            },
            h.Div(Class='control'): {
                h.Input(Class='input', type='text', name={'name'}, value={'value'}, placeholder={'placeholder'}):'',
            },
            h.P(Class='help has-text-danger'): '[[ error ]]'    
        
        }    
    }

class EmailField(Component):
    props = dict(
        name='[no name]',
        value='',
        type='email',
        placeholder='',
        error = ''
    )
    template = {
        h.Template():{
            h.Label(Class='label'):{
                h.Text():'[[ name ]]',
                h.Div(Class='control'): {
                h.Input(Class='input', type='email', name={'name'}, value={'value'}, placeholder={'placeholder'}):'',
            },
            h.P(Class='help has-text-danger'): '[[ error ]]'    
        
            },
        }    
    }

class PasswordField(Component):
    props = dict(
        name='[no name]',
        value='',
        type='password',
        error = ''
    )
    template = {
        h.Label(Class='label required'):{
            h.Text():'[[ name ]]',
            },
            h.Div(Class='control'): {
                h.Input(Class='input', type='password', name={'name'}, value='value'):'',
            },
            h.P(If='error', Class='help has-text-danger'): '[[ error ]]'
    }

class SelectField(Component):
    props = dict(
        name='[no name]',
        value='',
        type='select',
        error = '',
        options = []
    )
    template = {
        h.Label(Class='label'):{
        h.Text():'[[ name ]]',
        },
        h.Div(Class='control'): {
            h.Select(name={'name'}):{
                h.Option(For='opt in options', Class="js-states form-control", value={'opt.get("value")'}): 
                    '[[ opt.get("name", opt["value"]) ]]'
            },    
        }
    }    
class FileField(Component):
    props = dict(
        name='[no name]',
        value='',
        type='file',
        error = ''
    )
    template = {
        h.Label(Class='label'):{
            h.Text():'[[name]]',
        },
        h.Input(type='file', name={'name'}, accept="image/*"):'',
    }

class CheckBoxField(Component):
    props = dict(
        name='[no name]',
        value='',
        type='checkbox',
        error = ''
    )
    template = {
        h.Label(Class='checkbox'):{
            h.Template(If='value'):{
                h.Input(type='checkbox', name='name',checked=''):'[[name]]',
            },
            h.Template(Else=''):{
                h.Input(type='checkbox', name='name'):'[[name]]',
            }
        },
        h.P(If='error', Class='help has-text-danger'): '[[ error ]]'
    }

class RadioField(Component):
    props = dict(
        name='[no name]',
        value='',
        type='radio',
        error = ''
    )
    template = {
        h.Div(Class='control'): {
            h.Label(Class="radio"):None,
            
            h.Template(If='value'):{
                h.Input(If='value', checked='', Type='radio', name='name'):'[[name]]',
            },
            h.Template( Else=''):{
                h.Input(Type='radio', name='name'):'[[name]]',
            },
        },
        h.P(If='error', Class='help has-text-danger'): '[[ error ]]'
    }

class StandardField(Component):
    props = dict(
        field = None,
    )
    
    template = {
        h.Div(): {
            h.Template(If='field.get("type") =="textarea"'):{
                TextAreaField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    placeholder = {'field.get("placeholder", "")'}
        
                ): '',
            },
            h.Template(Elif='field.get("type") =="select"'):{
                SelectField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    options= {'field.get("options", [])'}
        
                ): '',
            },
            
            h.Template(Elif='field.get("type")=="checkbox"'):{
                CheckBoxField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    
                ): '',    
            },
            h.Template(Elif='field.get("type") == "radio"'):{
                RadioField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    
                ): '',    
            },
            
            h.Template(Elif='field.get("type") =="text"'):{
                StringField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    placeholder = {'field.get("placeholder", "")'}
                ): '',
            },
            
            h.Template(Elif='field.get("type")=="file"'):{
                FileField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    
                ): ''        
            },
            h.Template(Elif='field.get("type")=="email"'):{
                EmailField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    placeholder = {'field.get("placeholder", "")'}
                ): ''        
            },

            h.Template(Elif='field.get("type") == "password"'):{
                PasswordField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    

                ): ''        
            },
            h.Template(Else=''):{
                
                ## we default to String field 
                
                StringField(
                    name = {'field.get("name", "")'},
                    value = {'field.get("value", "")'},
                    errror = {'field.get("error", "")'},
                    placeholder = {'field.get("placeholder", "")'}
                ): ''        
            },
        }
    }

class StandardForm(Component):
    props = dict(
        fields=None
    )
    template = {
        h.Div(Class='box'):{

            h.Form(If='fields', action='#'):{
                h.Div(For='fld in fields', Style={'margin':'15px'}):{
                    StandardField(field = {'fld'}):{},
                },
                h.Button(type='submit'): 'Submit Button'
            },
            h.Div(Else=''): 'Sorry, no fields were passed to this form'
        }    
    }

class HTMLGrid(Component):
    props = dict(
        title = '',
        name = '',
        columns = [],
        data = []
    )
    template = {
        h.Div(Class='box'):{
            h.Table(id={'title'}, Class="table is-bordered is-striped", Style="width:100%"):{
                h.THead():{
                    h.TR():{
                        h.TH(For='col in columns'): '[[ col.title() ]]',
                    },
                },
                h.TBody():{
                    h.TR(For='dat in data'):{
                        h.Template(For='d in dat'):{
                            h.TD(If='d in columns'): '[[ dat[d] ]]'    
                        },
                    },
                }
            }
        }                
    }

class DTGrid(Component):
    props = dict(
        title='',
        name = '',
        columns = [],
        data = []
    )
    template = {
        h.Div(Class='box'):{
            h.Table(Id={'name'}, Class="table is-bordered is-striped", Style="width:100%"):{
            
            #h.Table(id={'name'}, Class="table is-bordered is-striped", Style="width:100%"):{
                h.THead():{
                    h.TR():{
                        h.TH(For='col in columns'): '[[ col.title() ]]',
                    },
                },
                h.TBody():{
                    h.TR(For='dat in data'):{
                        h.Template(For='d in dat'):{
                            h.TD(If='d in columns'): '[[ dat[d] ]]'    
                        },
                    },
                }
            },
            h.Script():"""$(document).ready( function () {
            $('#%s').DataTable()
            });""" % '[[ name ]]'
        }
    }
    
