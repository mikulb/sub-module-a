{
    'name': 'Custom HR',
    'category': 'none',
    'summary': 'A module the enhances the Odoo HR Module with the basic 201 fields in the Philippines.',
    'version': '0.1',
    'description': """
Custom HR
====================================
Custom HR Customizations
        """,
    'author': 'Toolkt Inc',
    'depends': ['base','base_setup','basic','l10n_ph','pentaho_reports', 'hr', 'hr_holidays','attendance_monitor',
                'mail',
                ],
    'demo': [
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_view.xml',
        'views/hr_view_employee.xml',
        'views/hr_contract_view.xml',
        'security/menu_security.xml',
    ],
    'qweb': [

    ],
    'installable': True,
}
