# -*- coding: utf-8 -*-

from openerp import api, models


class Task(models.Model):
    _name = "project.task"
    _inherit = ['project.task']

    @api.multi
    def get_access_action(self):
        """ Override method that generated the link to access the document. Instead
        of the classic form view, redirect to the post on the website directly """
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': '/my/tasks/%s' % self.id,
            'target': 'self',
            'res_id': self.id,
        }

    @api.multi
    def _notification_get_recipient_groups(self, message, recipients):
        """ Override to set the access button: everyone can see an access button
        on their notification email. It will lead on the website view of the
        post. """
        res = super(Task, self)._notification_get_recipient_groups(message, recipients)
        access_action = self._notification_link_helper('view', model=message.model, res_id=message.res_id)
        for category, data in res.iteritems():
            res[category]['button_access'] = {'url': access_action, 'title': _('View Task')}
        return res
