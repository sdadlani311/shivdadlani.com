# -*- coding: utf-8 -*-
from application import db

from datetime import datetime


class Base(db.Document):

    created = db.DateTimeField(
        verbose_name=u'Criado em',
        required=True
    )
    updated = db.DateTimeField(
        verbose_name=u'Atualizado em',
        required=True
    )

    meta = {'abstract': True}

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(BaseDocument, self).save(*args, **kwargs)
