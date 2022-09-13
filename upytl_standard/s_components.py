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
        h.Nav(Class='navbar is-primary', Role='navigation'): {
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
                                h.A(For = 'b in buttons',Class={'b.get("class", "button is-link")'}, Href={'b.get("href", "index")'}):'[[ b["name"] ]]',
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
        error = None
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
        error = None
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
        error = None
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
        error = None
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
        error = None,
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
        error = None
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
        error = None
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
        error = None
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
        name = None,
        type = None,
        value = None,
        error = None,
        placeholder=None,
        options=[]
    )
    
    template = {
        h.Div(): {
            h.Template(If='type =="textarea"'):{
                TextAreaField(
                    name = {'name'},
                    value = {'value'},
                    errror = {'error'},
                    placeholder = {'placeholder'}
        
                ): '',
            },
            h.Template(Elif='type=="select"'):{
                SelectField(
                    name = {'name'},
                    value = {'value'},
                    error = {'error'},
                    options= {'options'}
        
                ): '',
            },
            
            h.Template(Elif='type=="checkbox"'):{
                CheckBoxField(
                    name = {'name'},
                    value = {'value'},
                    error = {'error'}
                ): '',    
            },
            h.Template(Elif='type == "radio"'):{
                RadioField(
                    name = {'name'},
                    value = {'value'},
                    error = {'error'}
                ): '',    
            },
            
            h.Template(Elif='type =="text"'):{
                StringField(
                    name={'name'},
                    value = {'value'},
                    error = {'error'},
                    placeholder = {'placeholder'}
                ): '',
            },
            
            h.Template(Elif='type=="file"'):{
                FileField(
                    name={'name'},
                    value = {'value'},
                    error = {'error'}
                ): ''        
            },
            h.Template(Elif='type=="email"'):{
                EmailField(
                    name={'name'},
                    value = {'value'},
                    error = {'error'},
                    placeholder = {'placeholder'}
                ): ''        
            },

            h.Template(Elif='type == "password"'):{
                PasswordField(
                    name={'name'},
                    value = {'value'},
                    error = {'error'}

                ): ''        
            },
        }
    }

class Form(Component):
    props = dict(
        fields=None
    )
    template = {
        h.Div(Class='box'):{

            h.Form(If='fields', action='#'):{
                h.Div(For='fld in fields', Style={'margin':'15px'}):{
                    StandardField(
                        name='{fld[name]}',  
                        type={'fld.get("type", "text")'},
                        value={'fld.get("value", "")'},
                        error={'fld.get("error", "")'},
                        options={'fld.get("options", "")'},
                        placeholder={'fld.get("placeholder", "What the Fuck")'}
                    ):'',
                },
                h.Button(type='submit'): 'Submit'
            },
            h.Div(Else=''): 'Sorry, no fields were passed to this form'
        }    
    }
