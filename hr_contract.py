from openerp import models, fields, api, tools

class tk_hr_contract(models.Model):
	_inherit = 'hr.contract'

	de_minimis = fields.Float(string="De Minimis")
	allowance = fields.Float(string="Allowance")