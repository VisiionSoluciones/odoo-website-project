# -*- coding: utf-8 -*-

from openerp import http
from openerp.addons.website_portal.controllers.main import website_account


class WebsiteAccount(website_account):
    @http.route(['/my', '/my/home'], type='http', auth="user", website=True)
    def account(self):
        response = super(WebsiteAccount, self).account()
        project_tasks = http.request.env['project.task'].search([])
        response.qcontext.update({'tasks': project_tasks})
        return response


class WebsiteProjectTask(http.Controller):
    @http.route(['/my/tasks/<int:task_id>'], type='http', auth="user", website=True)
    def tasks_followup(self, task_id=None):
        task = http.request.env['project.task'].browse(task_id)
        return http.request.website.render("website_project_task.tasks_followup", {'task': task})
