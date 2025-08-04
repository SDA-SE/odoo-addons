from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    first_name = fields.Char(string='First Name', help='First name of the contact')
    middle_name = fields.Char(string='Middle Name', help='Middle name of the contact')
    last_name = fields.Char(string='Last Name', help='Last name of the contact')

    @api.depends('first_name', 'middle_name', 'last_name')
    def _compute_name(self):
        """Compute the name field from first_name, middle_name and last_name"""
        for partner in self:
            name_parts = []
            if partner.first_name:
                name_parts.append(partner.first_name)
            if partner.middle_name:
                name_parts.append(partner.middle_name)
            if partner.last_name:
                name_parts.append(partner.last_name)
            
            partner.name = ' '.join(name_parts) if name_parts else ""

    def _inverse_name(self):
        """Split the name field into first_name, middle_name and last_name when name is changed"""
        for partner in self:
            if partner.name:
                name_parts = partner.name.strip().split()
                if len(name_parts) >= 3:
                    partner.first_name = name_parts[0]
                    partner.middle_name = ' '.join(name_parts[1:-1])
                    partner.last_name = name_parts[-1]
                elif len(name_parts) == 2:
                    partner.first_name = name_parts[0]
                    partner.middle_name = ""
                    partner.last_name = name_parts[1]
                elif len(name_parts) == 1:
                    partner.first_name = name_parts[0]
                    partner.middle_name = ""
                    partner.last_name = ""
                else:
                    partner.first_name = ""
                    partner.middle_name = ""
                    partner.last_name = ""
            else:
                partner.first_name = ""
                partner.middle_name = ""
                partner.last_name = ""

    # Override the name field to add compute and inverse methods
    name = fields.Char(
        compute='_compute_name',
        inverse='_inverse_name',
        store=True,
        index=True
    )
