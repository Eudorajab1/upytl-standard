class SimpleForm:
    def __init__(
        self,
        fields = {},
        validation=None,
    ):
        self.fields = fields
        self.validation = validation
        self.vars = {}
        self.errors = {}
        self.files = None
        print('Fields are', self.fields)
        
    @staticmethod
    def _get_value(payload, key):
        is_omitted = key not in payload
        multidict = True
        getter = getattr(payload, 'getall', '')
        if not getter:
            multidict = False
            getter = payload.get
        v = getter(key)
        if multidict and isinstance(v, list):
            if v:
                if len(v) == 1:
                    v = v[0]
            else:
                v = None
        return v, is_omitted
    
    def get_options(self):
        # not implemented
        ...
    
    def process(self):
        
        """ here is we we will render the form and ouptut to html file"""
        print('Inside process')
        if self.__call__(self.fields).accepted:   
            return self
        
    def __call__(self, payload):
        print('Payload is ', payload)
        self.accepted = True
        return self
        validated_vars = {}
        self.files = []
        for field in self.fields:
            if not field.writable:  
                continue
            if payload:
                raw_value, is_omitted = self._get_value(payload, field.name)
            else:
                raw_value = ''
                is_omitted = False
            
                    
            self.vars[field.name]  = raw_value
            if is_omitted:
                continue
        if self.errors:
            print('about to return erros')
            return self
        self.vars.update(validated_vars)
        print('SELF VARS', self.vars)
        if self.validation:
            self.validation(self)
        if self.errors:
            print('About to return errors again ')
            return self
        self.accepted = True
        return self
    """
    def upload(self, default_folder = None, forced_folder = None):
        if not self.accepted:
            raise RuntimeError('payload is not accepted')
        uploaded = []
        for field, storage in self.files:
            if hasattr(storage, 'file'):
                value = field.store(
                    storage.file, storage.filename, forced_folder or field.uploadfolder or default_folder
                )
            else: # suppose it is `string`
                value = storage
                if value and value[0] != ':':
                    value = ''
            uploaded.append(value)
        self.vars[field.name] = uploaded if len(uploaded)>1 else uploaded[0]

    def update(self, table = None, record = None, record_id = None, query = None, del_files = False):
        if not self.accepted:
            raise RuntimeError('payload is not accepted')
        record = record or self.record
        print('Record in update is ', record)
        if not table and record:
            rec_op = getattr(record or self.record, 'update_record', None)
            if rec_op:
                table = rec_op.db[rec_op.tablename]
                record_id = rec_op.id
        if not (table and (record_id or query)):
            raise RuntimeError('too few arguments')

        vars = table._filter_fields(self.vars)
        print('Vars are ', vars)
        if not vars:
            return
        db = table._db
        if record_id:
            q = table._id == record_id
        elif query:
            q = query

        print('Query in update is ', q)
        upload_fields_to_del = []
        for k in list(vars.keys()):
            if table[k].type == 'upload':
                if not vars[k]:
                    del vars[k]
                else:
                    upload_fields_to_del.append(table[k])
                    if vars[k] == ':delete':
                        self.vars[k] = vars[k] = ''

        if not vars:
            return
        if del_files and upload_fields_to_del:
            rows = db(q).select(*upload_fields_to_del)
            for r in rows:
                for fld in upload_fields_to_del:
                    fname = r[fld.name]
                    if fname != vars[fld.name]:
                        fp = os.path.join(fld.uploadfolder, fname)
                        if os.path.isfile(fp):
                            os.remove(fp)
        db(q).update(**vars)
        if record:
            record.update(**vars)
            return record.id

    def insert(self, table):
        if not self.accepted:
            raise RuntimeError('payload is not accepted')
        vars = {
            k: v for k, v in table._filter_fields(self.vars).items()
            if table[k].type != 'upload' or v and v[0] != ':'
        }
        print(f' Vars: {vars}' )
    
        id = self.vars["id"] = table.insert(**vars)
        print ('Id is ', id)
        db = self.db
        db.commit()
        return id

        """