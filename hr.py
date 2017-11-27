from openerp import models, fields, api, _
from datetime import datetime
#from openerp import toolsdefefewfc

class lsgh_hr_academics(models.Model):
	_name = "lsgh.hr.academics"
	acad_level = fields.Selection([
		('elementary','Elementary'),
			('high_school','High School'),
			('college','College'),
			('post_grad_studies','Post Graduate Studies'),
		],'Academic Level',track_visibility='onchange')
	school = fields.Char('School',size=254)
	degree_obtained = fields.Char('Degree Obtained',size=254)
	honors = fields.Char('Honors Received',size=254)
	academics_id = fields.Many2one('hr.employee','Academic Level')
	start_date = fields.Date(string="Start Date")
	end_date = fields.Date(string="End Date")
	units = fields.Integer(string="Units Earned")
	major = fields.Char(string="Major")
	minor = fields.Char(string="Minor")
	degree_type = fields.Selection([
		('bs','BS'),
			('ab','AB'),
		],'Degree Type',track_visibility='onchange')

class dlsz_seminars(models.Model):
	_name = 'dlsz.seminars'
	
	seminar_title = fields.Char(string="Seminar Title")
	venue = fields.Char(string="Venue")
	speaker = fields.Char(string="Speaker")
	start_date = fields.Date(string="Start Date")
	end_date = fields.Date(string="End Date")
	hr_employee = fields.Many2one('hr.employee')

class dlsz_hr_children(models.Model):
	_name = "dlsz.hr.children"

	first_name = fields.Char('First Name',size=254)
	last_name = fields.Char('Last Name',size=254)
	date_of_birth = fields.Date('Date of Birth')
	school = fields.Char('Level/School',size=254)
	children_id = fields.Many2one('hr.employee','Children')
	relationship = fields.Char(string="Relationship")

class custom_hr(models.Model):
	_inherit = "hr.employee"

	active = fields.Boolean('Active', default=True)

	fname = fields.Char(string='First Name',size=254, select=1,track_visibility='onchange')
	mname = fields.Char(string='Middle Name',size=254,track_visibility='onchange')
	lname =  fields.Char(string='Last Name',size=254,track_visibility='onchange')
	card_no = fields.Char(string="Card No.",size=254,track_visibility='onchange')
	mi = fields.Char(string='MI',size=254)

	birth_month = fields.Selection([('January', 'January'),('February','February'),('March', 'March'),('April','April'),('May', 'May'),('June','June'),('July','July'),('August', 'August'),('September','September'),('October','October'),('November', 'November'),('December','December')],track_visibility='onchange')
	
	academics_ids = fields.One2many('lsgh.hr.academics','academics_id','Academic Level',track_visibility='onchange')
	seminar_ids = fields.One2many('dlsz.seminars','hr_employee','Seminars Level',track_visibility='onchange')

	employee_id = fields.Char(string='Employee ID', size=254,track_visibility='onchange')
	personal_email = fields.Char(string='Personal Email:', size=254,track_visibility='onchange')
	birth_place = fields.Char(string="Birth Place", size=254,track_visibility='onchange')
	marriage_date = fields.Date(string='Marriage Date',track_visibility='onchange')
	height = fields.Char(string="Height",track_visibility='onchange')
	weight = fields.Char(string="Weight",track_visibility='onchange')
	citizenship_of_father = fields.Char(string="Citizenship Of Father",track_visibility='onchange')
	citizenship_of_mother = fields.Char(string="Citizenship Of Mother",track_visibility='onchange')
	occupation_of_father = fields.Char(string="Occupation of Father",track_visibility='onchange')
	occupation_of_mother = fields.Char(string="Occupation of Mother",track_visibility='onchange')
	citizenship_of_spouse = fields.Char(string="Citizenship of Spouse",track_visibility='onchange')
	occupation_of_spouse = fields.Char(string="Occupation of Spouse",track_visibility='onchange')
	professional_membership = fields.Char(string="Professional Membership",track_visibility='onchange')
	special_skills = fields.Char(string="Special Skills",track_visibility='onchange')
	interest = fields.Char(string="Interest",track_visibility='onchange')
	languages = fields.Char(string="Languages",track_visibility='onchange')
	hobbies = fields.Char(string= "Hobbies",track_visibility='onchange')
	talents = fields.Char(string="Talents",track_visibility='onchange')
	custom_marital_status = fields.Char(string="Marital Status", size=254,track_visibility='onchange')

	nickname = fields.Char('Nickname',size=254,track_visibility='onchange')
	id_no = fields.Char('ID Number',size=254,track_visibility='onchange')
	position = fields.Char('Position',size=254,track_visibility='onchange')
	city_address = fields.Char('City Address',size=254,track_visibility='onchange')
	city_tel_no = fields.Char('Tel No.',size=254,track_visibility='onchange')
	provincial_address = fields.Char('Provincial Address',size=254,track_visibility='onchange')
	prov_tel_no = fields.Char('Tel No.',size=254,track_visibility='onchange')
	sss_no = fields.Char('SSS Number',size=254,track_visibility='onchange')
	ph_no = fields.Char('Philhealth Number',size=254,track_visibility='onchange')
	prc_no = fields.Char('PRC License Number',size=254,track_visibility='onchange')
	prc_date_issued = fields.Date('PRC Date Issued',track_visibility='onchange')
	valid_until = fields.Date('Valid Until',track_visibility='onchange')
	date_started = fields.Date('Date Started',track_visibility='onchange')
	perm_appoint = fields.Char('Permanent Appointment',size=254,track_visibility='onchange')
	hdmf_no = fields.Char('HDMF ID Number', size=254,track_visibility='onchange')
	tin = fields.Char('TIN',size=254,track_visibility='onchange')
	date_resigned = fields.Date('Date Resigned/Retired',track_visibility='onchange')
	maiden_name = fields.Char('Maiden Name (if married)',size=254,track_visibility='onchange')
	religion = fields.Char('Religion',size=254,track_visibility='onchange')
	citizenship = fields.Char(string = 'Citizenship',size=254,track_visibility='onchange')
	subject = fields.Char('Subject',size=254,track_visibility='onchange')
	level = fields.Char('Level',size=254,track_visibility='onchange')
	tin_num = fields.Char('TIN',size=254,track_visibility='onchange')
	bir_certified_dependent = fields.Selection([('0', 'None'),('1','One Dependent'),('2', 'Two Dependent'),('3', 'Three Dependent'),('4', 'Four or More Dependent')],string="BIR Certified Number of Dependents", default='0' ,track_visibility='onchange')

	# Family data
	name_of_spouse = fields.Char('Name of Spouse',size=254,track_visibility='onchange')
	employer_of_spouse = fields.Char("Employer of Spouse", size=254,track_visibility='onchange')
	office_address = fields.Char('Office Address',size=254,track_visibility='onchange')
	office_tel_no = fields.Char('Tel No',size=254,track_visibility='onchange')
	date_marriage = fields.Date('Date of Marriage',track_visibility='onchange')
	marriage_place = fields.Char('Place',size=254,track_visibility='onchange')

	children_ids = fields.One2many('dlsz.hr.children','children_id','Children',track_visibility='onchange')

	mother_name = fields.Char('Mother\'s Name',size=254,track_visibility='onchange')
	father_name = fields.Char('Father\'s Name',size=254,track_visibility='onchange')
	parent_address = fields.Char('Address',size=254,track_visibility='onchange')
	emer_contact_person = fields.Char('Emergency Contact Person',size=254,track_visibility='onchange')
	emer_contact_no = fields.Char('Contact Number',size=254,track_visibility='onchange')
	emer_contact_address = fields.Char('Address',size=254,track_visibility='onchange')
	#employee_internal_category = fields.Selection([('admin-asp', 'ADMIN-ASP'),('admin-asf','ADMIN-ASF'),('admin-faculty', 'ADMIN-FACULTY'),('gs-faculty', 'GS-FACULTY'),('hs-faculty', 'HS-FACULTY'),('brafenhs-faculty','BRAFENHS-FACULTY'),('gs-asf','GS-ASF'),('hs-asf','HS-ASF'),('brafenhs-asf','BRAFENHS-ASF'),('staff','STAFF'),('asp','ASP')])

	employee_internal_category = fields.Many2one('employee.internal.category',string='Employee Internal Category')

	@api.onchange('birthday')
	def  _onchange_birthday(self):
	#print '_onchange_birthday'
		if self.birthday:
			self.birth_month = datetime.strptime(self.birthday, '%Y-%m-%d').strftime("%B")
class config_late(models.Model):
	_inherit = 'config.late'

	employee_internal_category = fields.Many2one('employee.internal.category',string='Employee Internal Category')


class employee_internal_category(models.Model):
	_name = 'employee.internal.category'

	name = fields.Char(string="Category" )
